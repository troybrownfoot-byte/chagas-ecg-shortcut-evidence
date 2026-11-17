# PROTOCOL_TEST_SP validation amendment 1 - seal attempt 1 failed on a stale expected hash of the validation original-format cache (G7)

Written on 2026-11-10 (Beijing time) after seal attempt 1 failed. It is locked in PROTOCOL_TEST_SP.validation_amend1.lock before the sp_core.py correction is applied and before the seal is run again. At this point no seal lock, no validation scoring and no test read exist. It follows protocol line 139 (operator archive and relock procedure); the protocol text itself (d3fb2695...) is not changed.

## What happened
- 19:21:14 remote/b1_seal_val_ws_v2.sh (9ac464cf...) started with the expected analysis/sp_v4.py hash 967514ea...; ARMED, GPU_APPS 0, INSPECT_OK (selected epochs 9, 9, 8).
- 19:33:02 "analysis/sp_core.py seal" stopped with "RuntimeError: G7/original cache mismatch at seal val_orig" (sp_core.py line 358; collected/b1v2_seal.out sha256 86029a88b8deeb3d899be025c76308ac24b1b32c2ca8448b253b306dd10292ab; collected/b1v2_event.txt sha256 8c3174f41fc97fe8ac3e97dccdf0f5de27fbfcef1086e54b09d92dc1058a290e).
- No PROTOCOL_TEST_SP.lock.json was written. test_sp_eval.py never started, and no validation or test score, session marker or witness exists.
- Before the failing check, prepare_seal() had created analysis/results/test_sp with two files. Neither reads validation or test data:
  - cinco_missing_native.csv (sha256 49d4ee4d0e0e98189e5c0e6f570033fb2280f8bd0c7cd6d161a487be684e42ae), the 16 training hold-out negatives without native records;
  - self_test.json (sha256 93be88593be4dee19f77c8da2208199819c0c8b92c4635215a2123d8df5fc097), synthetic arrays only.

## Cause
- sp_core.py fixes ORIG_SHA['val'] = 0b9b9589b7da72358eecf700aeb194d768a2847de53dff71423e6a69e8f9d9bb. That is the value in chagas_founder/memmap_manifest.json (a715b140...) for the original A0 build. The file with that hash no longer exists.
- On 2026-10-23 the A0 memmaps were regenerated with unchanged preprocessing code and library versions:
  - chagas_founder/regen_memmap.log (71f01fb3...) and /home/hyhz/chagas_founder_memmap/regen_report.json (cf7f7a3a...) record val 98167af3651e674e19cc2d286d85794ed60581827bdb003c08d8c6af5a135663, "match": false.
  - PROTOCOL_TMP.md (0c0f745d...) and PROTOCOL_MOD.md (1004639c...) record it before any TMP/MOD result, in the memmap note of 2026-10-23 15:39: "float-rounding level, original files no longer available. Numerical equivalence check: A0 seeds 1234/1236 scored on the regenerated val memmap reproduce their saved val scores with max |diff| 9.6e-5 / 9.5e-5, mean 2.3e-6 / 1.7e-6, 0 records > 1e-3. Every arm (incl. BASE) uses the regenerated memmaps."
  - analysis/results/tb_build_val.log (d1b93771..., 2026-10-24) rebuilt the validation caches and found 98167af3... and 4c485a4f... "equals_existing": true.
- /home/hyhz/chagas_founder_memmap/val.f16.dat has hashed 98167af3... since 2026-10-23 (mtime 2026-10-23 00:37:39 US Pacific) and did not change.
- The runs compared in TEST_SP were trained or scored on this file after 2026-10-23:
  - the BASE checkpoints of the controlled baseline (collected/rent4090/runs/BASE_s1234-1236, written 2026-10-24; the MOD screen arm named in the memmap note);
  - the CG-Net checkpoints (collected/ckpt/AGADSE_s1234-1236, from the AGA and EPC-D line developed after the regeneration);
  - the November comparator training and scoring.
  At validation, G1 checks that each frozen checkpoint reproduces its stored validation scores on this file.
- The other three caches match their fixed hashes at seal attempt 1: val_crop 4c485a4f..., test 296e547e..., test_crop 51b0ab1e....
- The 0b9b9589... value was a transcription of the superseded manifest when sp_core.py was written. It is not the historical hash that protocol lines 56 and 123 require.

## Correction
- analysis/sp_core.py line 21: ORIG_SHA['val'] changes from 0b9b9589b7da72358eecf700aeb194d768a2847de53dff71423e6a69e8f9d9bb to 98167af3651e674e19cc2d286d85794ed60581827bdb003c08d8c6af5a135663. No other byte changes.
- sp_core.py sha256 before ce2b3d4c59b1dedce21ae91e6b20435ee270fecc4e6c0a484f8283505f074c05, after 43741803e077c23969499981a5d8c05916016c950793b86d622195f3a9db076f. The old file is kept as collected/sp_core.ce2b3d4c.py.
- Diff:
  ```
  21c21
  < ORIG_SHA = {'val':'0b9b9589b7da72358eecf700aeb194d768a2847de53dff71423e6a69e8f9d9bb','test':'296e547e8ddd6d6ee0d707f7cc7df43eefd4abcff158ecfa7bc588dd473d73cb'}
  ---
  > ORIG_SHA = {'val':'98167af3651e674e19cc2d286d85794ed60581827bdb003c08d8c6af5a135663','test':'296e547e8ddd6d6ee0d707f7cc7df43eefd4abcff158ecfa7bc588dd473d73cb'}
  ```
- Unchanged by this amendment:
  - G7: all four caches must match their fixed hashes at seal and are rehashed by verify();
  - G1: rescoring the frozen checkpoints on validation must reproduce their stored validation scores;
  - every tolerance and gate, the decision family and the decision rules;
  - PROTOCOL_TEST_SP.md (d3fb2695...), analysis/sp_v4.py (967514ea...), analysis/test_sp_eval.py (f50fe268...), remote/b1_seal_val_ws_v2.sh (9ac464cf...) and remote/test_sp_ws.sh (319f30fa...);
  - the reporting lock PRELOCK_REPORT_SP.lock (8012ca5d..., 19:20:46), which hashes neither analysis/sp_core.py nor any cache;
  - the S14 pre-check log (collected/S14_PRECHECK.log, 19:20:46).

## Archive of attempt 1 (nothing deleted)
- analysis/results/test_sp is renamed to /media/hyhz/GZR/chagas_baseline/analysis/results/test_sp_failed_20261110_193302 and holds the two files above.
- Previous lock SHA256: none. The seal failed before PROTOCOL_TEST_SP.lock.json existed, so no lock is moved into the archive.
- The attempt-1 logs are renamed, so that the rerun cannot overwrite them:
  - collected/b1v2_seal.out to collected/b1v2_seal.attempt1.out;
  - collected/b1v2_event.txt to collected/b1v2_event.attempt1.txt;
  - collected/b1v2_nohup.out (empty) to collected/b1v2_nohup.attempt1.out.
  collected/b1v2_auto.log stays in place; the rerun appends to it.
- The rerun is the same locked remote/b1_seal_val_ws_v2.sh with the same expected sp_v4.py hash. Its seal() freezes this supplement and its lock.
- The failed attempt is reported with the TEST_SP results.
