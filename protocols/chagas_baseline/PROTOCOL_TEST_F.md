# PROTOCOL_TEST_F — one-shot test confirmation of weight EMA on EPCDS

Status: written 2026-10-27 ~18:55 Beijing time, after the val confirmation (PROTOCOL_EXP6: CONFIRMED) and before any test score of
these models exists; locked by sha256 in PROTOCOL_TEST_F.lock. User approval (2026-10-27 ~16:10): "批准使用测试集" for the one-shot test
confirmation of anything that passes its val rule. This is test read 11 (TEST_USE_LOG.md).

## Hypothesis and evidence
Weight EMA (decay 0.999, EMA-based checkpoint selection; PROTOCOL_EXP2 code) improves EPCDS. Val: EXP2 (seeds 1234-1236) stratified V1
+0.0041 [+0.0003, +0.0079], V2 +0.0068; EXP6 (new seeds 1237-1239, confirmatory) stratified V1 +0.0066 [+0.0018, +0.0112], V2 +0.0072
[-0.0011, +0.0152], challenge +0.0165; six seeds +0.0052 [+0.0014, +0.0086].

## Models (all A6000, code train_module.exp2.py sha256 da1edbd3...; checkpoints fetched sha256-verified)
EPCDSE = EMA weights (best.pt), EPCDSR = raw weights of the same runs (raw_best.pt), seeds 1237-1239 (collected/exp6/runs, primary)
and 1234-1236 (collected/exp2/runs, descriptive). Descriptive references: EPCDS (original RTX 4090 runs, test read 10 scores) and DEME
(TEST_B scores).

## Scoring (local GTX 1650; analysis/test_f_score.py)
epcd_score.py with two changes only: classes read from train_module.exp2.py (defines EPCDSE / EPCDSR); crop format only. Test memmap
/home/hyhz/tb_build/test/test_crop.f16.dat (the test path of read 10), test_rows_F45.csv (no label column). Output
<RUN>/test_scores_tf.csv. Val dry run before the lock: EPCDSE_s1237 scored locally on val must match the A6000 val scores (max |diff|
<= 5e-4, all metric differences < 0.0005), and analysis/test_f_eval.py --split val must reproduce the EXP6 confirmation contrast.

## Decision (analysis/test_f_eval.py; crop format; 3-seed mean-probability ensembles; paired patient-cluster bootstrap 2,000x, seed 1234)
TG1 (primary, single hypothesis): EPCDSE - EPCDSR (seeds 1237-1239): stratified V1 95% CI lower bound > 0 AND V2 95% CI lower bound >
-0.010 -> SUPPORTED. Bonferroni sensitivity across all test hypotheses (m = 35): approximate one-sided p of TG1 <= 0.05/35.
Descriptive: the same contrast for seeds 1234-1236 and six-seed ensembles; EPCDSE6 - EPCDS(4090), EPCDSE6 - DEME, EPCDSR6 - EPCDS.
If TG1 is supported, EMA becomes part of the CG-Net training recipe for the EPCDS variant (the EPC vs EPCDS choice remains the user's).
