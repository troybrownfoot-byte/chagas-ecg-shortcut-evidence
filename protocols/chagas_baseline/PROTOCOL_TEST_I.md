# PROTOCOL_TEST_I - final Table 2 with the full metric set (descriptive; one test read)

Status: written 2026-10-31 12:05 Beijing time (clock), before any computation of the metrics below on the test split for the two 2026
methods and before any F1 / AUPRC / ECE / Brier / alert-point metric was computed on the test split for any method; locked by sha256 in
PROTOCOL_TEST_I.lock. User authorisation: "允许使用测试集" (2026-10-30 ~17:55) and "执行" (2026-10-31 ~11:40) for the Table 2 update.
This read is logged as one descriptive read in TEST_USE_LOG.md. No hypothesis; the Bonferroni family (m = 43) is unchanged; no model is
trained, selected or tuned on the test split, and no row is added or dropped after seeing results.

## Metric set (user decision 2026-10-30, after the literature survey of recent papers)
Literature basis: CODE-II (npj Digit Med 2026; AUROC, AUPRC, F1 / precision / recall / specificity / NPV at the F1 threshold, ECE,
bootstrap CIs), the 2026 CMR-aligned Chagas paper (AUROC, top-5% TPR = challenge score), Ahus (CinC 2025; challenge score, AUROC),
the 2026 holistic ECG foundation-model benchmark (calibration via ECE), TRIPOD+AI (discrimination and calibration). User adds F1.
Table 2 (performance):
- length-stratified AUROC within CODE-15% (primary; definition of analysis/test_d_eval.py),
- cross-cohort AUROC V2 (SaMi-Trop positives vs CODE-15% negatives),
- challenge score (fraction of all positives in the top 5% of all records),
- AUPRC (average precision over all records, CODE-15% + SaMi-Trop, as the official PhysioNet 2025 scorer),
- F1 at the 5% alert operating point (top 5% flagged; the challenge's triage setting). Note: at a fixed alert rate F1 is a monotone
  function of the challenge score; reported because reviewers expect it.
Shortcut diagnostics table: pooled CODE-15% AUROC V1, source AUROC V3 (SaMi-Trop vs CODE-15% positives; closer to 0.5 is better),
pooled minus stratified AUROC.
Calibration (supplement): ECE (15 equal-width bins over all records) and Brier score. Methods trained with focal loss or reweighting are
miscalibrated by design; calibration is descriptive and not ranked.
Alert point (supplement): sensitivity, specificity, PPV, NPV at the 5% alert rate over all records.
CIs: paired patient-cluster bootstrap 2,000x (seed 1234), CG-Net (pooled) minus each method, for every Table-2 metric.

## Rows (3-seed mean-probability ensembles unless stated; every source file listed in the analysis script)
ResNet (2020) and ResNet + age/sex (2020): chagas_tricks/test_eval_tricks/test_scores.csv (baseline_s*, agesex_s*).
InceptionTime, xresnet1d101, MERL, ST-MEM (1 seed), HuBERT-ECG, Stenhede and Ranjbar, 1D ConvNeXt (1 seed):
  baselines_e/runs_local and runs_4090, <method>_s*/test_scores.csv (row order = test_rows_F45.csv).
ECG-CPC (2026) and xECG (2026): collected/test_e2/{cpc,xecg}_s*/test_scores.csv (TEST_E2; row order = test_rows_F45.csv).
CinCo (2025) official pipeline: analysis/results/test_a_test/cinco_scores.csv base_s*_final_orig;
CinCo (2025) + de-shortcut pipeline: base_s*_stage1_crop.
ECGFounder (2025) full fine-tuning: analysis/results/test_a_test/a0_scores.csv a0_s*_orig.
ECGFounder + de-shortcut pipeline (baseline): collected/test_h/runs/BASEER_s*/test_scores_leads_th.csv score_12.
+ FiLM-Demo: collected/rent4090/runs/DEM_s*/test_scores_tb.csv score_crop.
CG-Net (single exam) and CG-Net (full = + pooling): collected/test_h/runs/AGADSE_s*/test_scores_leads_th.csv score_12; pooling = mean
logit over the patient's test exams. The CG-Net row must reproduce Table 2 (strat .8237, V2 .8772, challenge .4253) and the baseline
row (.7957 / .8373 / .3971); TEST_E2 rows are new.
Analysis: analysis/test_i_eval.py (sha in the lock). Dry run first on the validation split (rows with val scores) to check the code;
then one test run.
