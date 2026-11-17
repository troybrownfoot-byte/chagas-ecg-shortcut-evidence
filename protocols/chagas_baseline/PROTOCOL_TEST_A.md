# TEST_A: one-shot test-split confirmation for paper direction A (drafted 2026-10-23; test labels not read before user approval)

Direction A (user decision 2026-10-23): a source-robust screening pipeline = (1) length-consistent input (crop-then-preprocess: each raw record cut to its first 2,934 samples at 400 Hz before the model's own preprocessing), (2) no source-confounded fine-tuning stage (CinCo stage 3 trains SaMi-Trop positives against non-Brazilian negatives only), (3) shortcut-free evaluation (length-stratified V1, V2). Validation evidence: PROTOCOL_LEN amendments 4-5, PROTOCOL_ALIGN amendment 8 (exploratory).

## Models (all already trained; inference only)
- A0: ECGFounder 12-lead fine-tuned, seeds 1234-1236 (chagas_founder runs/F1, runs_F4/F_s1235, runs_F4/F_s1236).
- CinCo faithful baseline (cinco_run): base_s1234-36; final = mean sigmoid of the 5 stage-3 fold models (run_model.py default path); stage1 = pretrain_model.pth.
- 3-seed mean-probability ensembles; records scored by both pipelines (CinCo WFDB conversion misses all-zero records) are analysed.

## Hypotheses (primary; decision rule fixed now)
- T1 (length fix on the strong model): A0 crop vs A0 orig.
- T2 (pipeline A on the public baseline): CinCo stage1 + crop vs CinCo final (released pipeline).
- Each is SUPPORTED iff V2 difference 95% CI lower bound > 0 AND length-stratified V1 difference 95% CI lower bound > -0.01 (non-inferiority margin).
Paired patient-cluster bootstrap 2,000x (seed 1234), clusters = (dataset, patient_id).

## Secondary (descriptive, no decision rule)
Pooled V1, V3, challenge score (TPR in top 5%), V1 per length stratum, CinCo stage1 vs final and stage1 + crop vs stage1, and the test-split prevalence by record length (does the length-prevalence association replicate on test?).

## Procedure (analysis/test_a.py)
1. Dry run on val (--split val): every stage must reproduce the locked val results (lengths = analysis/val_lengths.csv, i.e. WFDB header lengths; A0 orig = saved val scores, A0 crop = amendment-5 scores; CinCo final/stage1/crop = saved val scores); dry-run results reported to the user.
2. Lock this file + script (PROTOCOL_TEST_A.lock).
3. Only after user approval: lengths, a0, cinco on --split test (no labels), then evaluate (reads exam_id_split.csv test labels once).

## Result (test split, one shot; 2026-10-24 13:35; analysis/results/test_a_test/results.json; n = 34,526 records scored by both pipelines)
- T1 A0 crop - orig: V2 +.038 [+.021, +.055]; length-stratified V1 -.0015 [-.0028, -.0001] -> SUPPORTED. Pooled V1 -.030 [-.038, -.023] (length shortcut removed), V3 +.074, challenge -.015 [-.033, +.001].
- T2 CinCo stage1 + crop - CinCo final (released): V2 +.134 [+.102, +.166]; stratified V1 +.010 [-.001, +.021] -> SUPPORTED. Challenge +.039 [+.010, +.068], pooled V1 -.023, V3 +.187.
- Secondary: CinCo stage1 - final: V2 +.058 [+.031, +.085], stratified V1 +.012 [+.001, +.023]; stage1 + crop - stage1: V2 +.076 [+.061, +.090], stratified V1 -.0023 [-.0034, -.0014].
- Arms: A0 orig V1 .845 / strat .805 / V2 .808 / chal .424; A0 crop .815 / .804 / .846 / .409; CinCo final .809 / .755 / .690 / .304; CinCo stage1 + crop .785 / .765 / .824 / .343.
- Length-prevalence association replicates on test: CODE-15% 7.3-s records 2.88% positive (n 21,354) vs 10.2-s records 0.28% (n 13,008), about 10x (val 17x).
