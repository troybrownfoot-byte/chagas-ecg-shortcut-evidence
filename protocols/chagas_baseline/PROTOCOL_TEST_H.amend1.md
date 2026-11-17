# PROTOCOL_TEST_H amendment 1 — the whole-network ablation (PROTOCOL_ABL) added to the one-shot test read

Status: written 2026-10-28 02:10-02:14 Beijing time (clock), before any INT1, EXP12 or ABL val result and before any TEST_H test score;
locked by sha256 in PROTOCOL_TEST_H.amend1.lock. Reason: user 2026-10-28 "继续推进实验，不过要测试加上模块后，整个网络性能是否有提升" -
the test read must show whether each module improves the whole network, not only the full model against the manuscript.

## Changes (TH1, TH2, the conditions of the read and the bootstrap are unchanged)
1. Same-host ablation arms (PROTOCOL_ABL; gpushare RTX 4090) are scored on the test split: FULL = AGADSE; NOAGA = EPCDSE (--base-only from
   AGADSE); NOEMA = AGADSR (AGA on EPCDSR); EPCD = EPCDSR (--base-only from AGADSR); NOEPCD = AGABE (AGA on BASE + EMA); BASE = BASEER (raw
   weights of the BASEE runs); NOCROP = AGADSE in the A0 (orig) format, 12 leads. The original NOEMA arm of TEST_H (AGADS on EPCDS from the
   compshare host) is replaced by the same-host AGADSR, because GPU numerics differ between hosts by 0.002-0.004, which is the size of the
   EMA effect; the cross-host arm is not scored.
2. Analysis: analysis/test_h_abl_eval.py (definitions identical to analysis/abl_eval.py): leave-one-module-out FULL_P - variant_P for EPC-D,
   EMA, AGA (reduced), pooling and crop; cumulative chain BASE -> +EPC-D -> +EMA -> +AGA -> +pooling; overall FULL_P - BASE and FULL_P - MS.
   A module "contributes within the whole network on test" iff its primary contrast (12-lead stratified V1; reduced for AGA) has 95% lower
   bound > 0; Bonferroni m = 43 (36 earlier reads + TH1 + TH2 + 5 module tests), adjusted p reported. TH1/TH2 are read from the same
   script ('overall FULL_P-MS': 12_V1_strat and red_V1_strat lower bounds), with the identical bootstrap draws and the identical FULL and
   MS inputs as analysis/test_h_eval.py; test_h_eval.py itself (which would need the dropped cross-host arm) is therefore not run.
3. Scoring: analysis/test_h_score.py v1 (adds --fmt orig and --configs; with the defaults it reproduces the locked v0 bit for bit on
   1,024 val rows; the orig path equals the earlier local EPCDS orig scores exactly; v0 kept as analysis/test_h_score.v0.py, sha256 39ca3b2b).
   Order and files: remote/test_h_local.sh (val1024 check of every fetched checkpoint vs the host lead scores, max |diff| < 1e-3 required;
   abl_val = the -crop val scores of PROTOCOL_ABL; test = the one-shot test scoring). Checkpoints fetched sha256-verified with
   remote/fetch_ckpts_th.sh into collected/ckpt.
4. Order of the read: INT1 val decision -> ABL val analysis (abl_eval.py) -> val dry run of test_h_abl_eval.py (real val files) -> test
   scoring -> test_h_abl_eval.py --split test once -> TEST_USE_LOG read 13.
