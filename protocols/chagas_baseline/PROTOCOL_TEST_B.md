# TEST_B: one-shot test-split confirmation of the retained demographic module (2026-10-24; test not read)

## Question
Does the retained demographic module improve the A0 screening model on the held-out test split, as DEM did on val (crop format: stratified V1 +.018 [+.006, +.031], V2 +.027 [+.014, +.041])? The module tested (call it M) is fixed by PROTOCOL_MOD amendment 1 before any test read: M = DEME (epidemiology-informed design) if its val adoption rule holds, otherwise M = DEM.

## Models (trained; inference only)
BASE and M, seeds 1234-1236, PROTOCOL_MOD runs (collected/rent4090/runs; best.pt sha256 prefixes BASE c2ee11ff / af6e9d60 / ab6eb76f, DEM c3944ed5 / e0b1dcf7 / 243b5e01; DEME hashes added when fetched). 3-seed mean-probability ensembles. Primary inference format = crop-then-preprocess (the direction-A pipeline); A0 format secondary.

## Hypotheses: fixed-sequence (hierarchical) testing, each at alpha = 0.05 two-sided (95% CI), stop at the first failure
- TB1 (tested first): V2(M) - V2(BASE) 95% CI lower bound > 0 AND length-stratified V1 difference lower bound > -0.005 (an intersection-union test, no alpha split).
- TB2 (tested only if TB1 holds): length-stratified V1 difference lower bound > 0.
Order rationale (fixed before the test read): the module was motivated by the cross-source V2 gap and its V2 effect had the larger margin on val (z about 4 vs 2.8). Under fixed-sequence testing the family-wise error stays at 0.05 without splitting alpha (FDA, Multiple Endpoints in Clinical Trials, final guidance, Oct 2022).
Non-inferiority margin -0.005 (stratified V1): fixed in PROTOCOL_MOD Tier 2 before any training; it is half of the smallest effect detectable on val (about .01) and much stricter than the common 0.05 AUC convention. Justification is given here because literature reviews find NI margins often unjustified (Radiology 2013, doi 10.1148/radiol.13130967).

## Statistics
- Metrics as in analysis/mod_eval.py (V1, length-stratified V1 with the TEST_A length rule, V2, V3, challenge).
- Paired patient-cluster bootstrap, 2,000x, seed 1234, clusters = (dataset, patient_id). Clustering because several records come from the same patient; the cluster-adjusted analysis of ROC data follows Obuchowski (Biometrics 1997).
- Sensitivity analysis (reported, not a decision rule): Bonferroni over every primary contrast ever evaluated on this test split (TEST_USE_LOG.md m = 27, plus TB1 and TB2 -> 29; alpha/m = .0017).
- Secondary, descriptive: pooled V1, V3, challenge, per-length V1, A0-format contrasts.

## Procedure
1. Build test memmaps for test_rows_F45.csv in both formats with the exact builder code used for train/val (regen_memmap.py transform; make_val_crop.py transform). Builder check: rebuilding the val memmaps with the same script must reproduce val.f16.dat and val_crop.f16.dat bitwise.
2. Score test rows with train_module.py --score-only (new option --score-split test: test rows and demographics only, no labels; dummy zero labels in the loader).
3. Dry run: steps 1-2 plus the evaluation on --split val must reproduce analysis/results/mod/mod_eval.json exactly; results reported to the user.
4. Lock the scripts (PROTOCOL_TEST_B.lock). PROTOCOL_LSO results and the PROTOCOL_MOD amendment-1 decision (val) are completed first, so that every decision precedes the test read.
5. Only after user approval: score test, then evaluate once; labels read once from chagas_step2_20261013/exam_id_split.csv; all results reported and added to TEST_USE_LOG.md.

## Disclosures (TEST_USE_LOG.md; TRIPOD+AI)
- The test split is an internal held-out patient split of the same cohorts (CODE-15%, SaMi-Trop), not external validation. External ECG-Chagas validation typically shows much lower performance (e.g. AUROC .68 REDS-II, .59 ELSA-Brasil; PLoS NTD 2023, PMC10361500).
- Age/sex added to a ResNet was already evaluated on this test split (10-19, V1 +.004, replicated), and length effects were seen on test on 10-18; this test read is therefore not the first look at demographic inputs on this split.
- DEM entered the screen through a val pre-check and was retained on val, and DEME was chosen on val by a pre-specified rule, so val gains are optimistic; the test result is the claim-bearing evidence.

Locked after user approval of the plan (2026-10-24, 'execute your recommendation'); the test read itself still needs explicit user approval after the val dry run.

## Amendment 1 (2026-10-24 19:36; before any DEME val score and before any test read)
M is now fixed by PROTOCOL_MOD amendment 2 (M = DEME, our design, iff DEME - BASE meets Tier 1 or Tier 2 on val; else DEM). Primary hypotheses TB1/TB2 unchanged, on M. Pre-specified descriptive ablation without claims when M = DEME: DEM - BASE and DEME - DEM on test (generic vs our design). All are reported.

## Result (test split, one shot; read started 2026-10-24T20:20:46+08:00; analysis/results/test_b/test_b_results.json)
M = DEME (val rule). Pre-read checks: DEME TEST_B scoring path reproduced its val scores (max |diff| 0.0); the rebuilt test A0-format memmap equals the historical test memmap (sha256 296e547e...73cb).
- TB1: DEME - BASE (crop) V2 +.0289 [+.0154, +.0432]; stratified V1 +.0185 [+.0079, +.0286] -> SUPPORTED. TB2: stratified V1 lower bound > 0 -> SUPPORTED. Bonferroni sensitivity (m = 29): p(TB1) 2.3e-5, p(TB2) 2.3e-4 < .0017 -> both pass.
- Secondary: pooled V1 +.016 [+.006, +.026]; V3 +.022 [+.004, +.039]; challenge +.032 [+.009, +.057]; A0 format: stratified V1 +.019 [+.008, +.029], V2 +.027 [+.015, +.038].
- Arms (crop): BASE V1 .809 / strat .796 / V2 .837 / challenge .397; DEME .825 / .814 / .866 / .429.
- Descriptive ablation (no claims): DEM - BASE stratified V1 +.017 [+.006, +.028], V2 +.032 [+.017, +.047]; DEME - DEM stratified V1 +.001 [-.002, +.005], V2 -.003 [-.010, +.003] (equivalent).
