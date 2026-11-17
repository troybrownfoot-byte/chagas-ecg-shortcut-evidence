# PRECHECK_NEX2 result - normal-ECG routed expert head on the frozen CG-Net: FAIL (test read 26 not run)

Written 2026-11-04 10:50 Beijing time. Lock 01:22:59 (the status line of PRECHECK_NEX2.md says "~02:00"; the lock line is authoritative); amendment 1
(stage 1 re-run on the workstation because the AutoDL 4090 ran out of balance and stopped with its stage-1 outputs, never read by stage 2).
Stage 1 (train rows only): gate accuracy on the hold-out .751, routing rate .43; the hold-out BCE chose the strongest L2 (lambda 1, grid edge) for
every seed: .07951 -> .07946 (seed 1234); bias-only .07946. Val read (analysis/nex2_eval.py; G1 passed):
NEX2 - BASE: S -.0002 [-.0005, +.0001], V2 +.0001 [-.0005, +.0005], V2_norm -.0024 [-.0041, -.0008], V2_abn +.0008 [+.0004, +.0011],
N_sami +.0000 [-.0013, +.0016] -> PASS false; TEST_NEX2_SKIPPED.
Reading: a head on the frozen pooled features cannot move the normal-ECG weakness; together with PRECHECK_NEX (within the normal stratum CG-Net
ranks well, N_sami .892) the weakness is the ranking of abnormal-ECG negatives above infected people with a normal ECG. It is a limitation to report
(the indeterminate form), not a head-level problem.
