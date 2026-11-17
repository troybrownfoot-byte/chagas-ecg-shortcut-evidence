#!/usr/bin/env python3
"""Check the locked protocols of this evidence package against their lock files.

For every file under protocols/, the script computes its SHA-256 and looks for that hash in the lock files of the package
(*.lock, *.sha256 and *.lock.json). It prints one row per file: the lock files that record the current hash, or a note when
none does (result notes written after a read are not locked). Lock files also list evaluation scripts and result files that
are not part of this package; their hashes can be checked once the code is released.

Usage: python verify_locks.py [--markdown]
Standard library only; tested with Python 3.8 or later.
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "protocols")
HEX64 = re.compile(r"\b[0-9a-f]{64}\b")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 16), b""):
            h.update(block)
    return h.hexdigest()


def is_lock(name):
    return name.endswith(".lock") or name.endswith(".sha256") or name.endswith(".lock.json")


def lock_entries(path):
    """(hash, recorded name or '', timestamp comment or '') for every hash written in a lock file"""
    text = open(path, encoding="utf-8", errors="replace").read()
    out = []
    if path.endswith(".json"):
        def walk(obj, key=""):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    walk(v, k)
            elif isinstance(obj, list):
                for v in obj:
                    walk(v, key)
            elif isinstance(obj, str):
                for h in HEX64.findall(obj):
                    out.append((h, key, ""))
        try:
            walk(json.loads(text))
        except ValueError:
            out += [(h, "", "") for h in HEX64.findall(text)]
        return out
    stamp = ""
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("#"):
            stamp = s.lstrip("# ")[:25]
            continue
        m = re.match(r"^([0-9a-f]{64})\s+\*?(.+)$", s)
        if m:
            out.append((m.group(1), m.group(2).strip(), stamp))
        else:
            out += [(h, "", stamp) for h in HEX64.findall(s)]
    return out


def locked_prefix(path, locks):
    """Longest leading part of the file, ending at a line break, whose SHA-256 is recorded in a lock file:
    (number of lines, total lines, lock file) or None. Detects text appended after locking."""
    known = {}
    for lk, ents in locks.items():
        for e in ents:
            known.setdefault(e[0], lk)
    lines = open(path, "rb").read().splitlines(keepends=True)
    h, best = hashlib.sha256(), None
    for i, line in enumerate(lines, 1):
        if line.endswith(b"\n"):          # also try the prefix without its final line break
            h2 = h.copy()
            h2.update(line.rstrip(b"\r\n"))
            if h2.hexdigest() in known:
                best = (i, len(lines), known[h2.hexdigest()])
        h.update(line)
        if h.hexdigest() in known:
            best = (i, len(lines), known[h.hexdigest()])
    return best if best and best[0] < len(lines) else None


def main():
    files, locks = [], {}
    for dp, _, fs in os.walk(ROOT):
        for f in sorted(fs):
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
            files.append((rel, p))
            if is_lock(f):
                locks[rel] = lock_entries(p)
    rows, n_ok, n_prefix = [], 0, 0
    for rel, p in sorted(files):
        if is_lock(os.path.basename(rel)):
            continue
        h = sha256(p)
        hits = [lk for lk, ents in locks.items() if any(e[0] == h for e in ents)]
        if hits:
            n_ok += 1
            status = "recorded in " + ", ".join(sorted(hits))
        elif rel.endswith(".result.md"):
            status = "result note written after the read (not locked)"
        else:
            pref = locked_prefix(p, locks)
            if pref:
                n_prefix += 1
                lines, total, lk = pref
                status = (f"first {lines} of {total} lines match the hash recorded in {lk}; "
                          f"the remaining lines were appended later")
            else:
                status = "current hash not recorded in any lock file"
        rows.append((rel, h, status))
    md = "--markdown" in sys.argv
    if md:
        print("| File | SHA-256 (first 16) | Status |")
        print("|---|---|---|")
    for rel, h, status in rows:
        print(f"| {rel} | `{h[:16]}` | {status} |" if md else f"{rel:60s} {h[:16]}  {status}")
    print(("\n" if md else "") + f"{n_ok} of {len(rows)} non-lock files have their current hash recorded in a lock file; "
          f"{n_prefix} more start with a locked version followed by appended lines.")


if __name__ == "__main__":
    main()
