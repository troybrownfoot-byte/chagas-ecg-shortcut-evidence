# PROTOCOL_TEST_G — one-shot test confirmation of longitudinal patient-level score pooling (EXP11)

Status: written 2026-10-27 22:20 Beijing time, after the EXP11 val result (GAIN: stratified V1 +0.0059 [+0.0007, +0.0106], V2
+0.0031 [+0.0024, +0.0039]) and before any pooled test score; locked by sha256 in PROTOCOL_TEST_G.lock. User approval (2026-10-27):
"允许使用测试集". Test read 12 (TEST_USE_LOG.md); Bonferroni family m = 36.

## Hypothesis
TH1 (single): on the test split, pooling the EPCDSE scores over each patient's exams (sigmoid of the mean logit within (dataset,
patient_id)) improves stratified V1 (95% CI lower bound > 0) without loss of V2 (95% lower bound > -0.010); EPCDSE = EMA weights of the
EXP6 runs, seeds 1237-1239 (the TEST_F primary models; their test scores already exist, test_scores_tf.csv, scored by the locked scorer
in read 11 - no new model scoring). Descriptive: seeds 1234-1236, six seeds, EPCDSR, patient-harmonised test labels.

## Analysis (analysis/test_g_eval.py; crop format; paired patient-cluster bootstrap 2,000x, seed 1234; metric code as TEST_F)
Labels joined only inside the script. Val dry run before the lock must reproduce EXP11 (EPCDSE_POOL - EPCDSE on the EXP2 seeds).
