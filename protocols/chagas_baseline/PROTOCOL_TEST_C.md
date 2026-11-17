# TEST_C: one-shot test-split confirmation of the lead component AGA (written 2026-10-25; test not read)

## Question
Does AGA (availability-gated adapters on the frozen DEME; PROTOCOL_LEAD amendment 1) improve screening with missing leads on the held-out test split, as on val (reduced-mean stratified V1 +.0146 [+.0085, +.0208], V2 +.0207 [+.0123, +.0293]), while leaving 12-lead outputs unchanged?

## Models (trained; inference only)
DEME (seeds 1234-1236; PROTOCOL_MOD) and AGA (seeds 1234-1236; collected/rent4090/runs/AGA_s*). 3-seed mean-probability ensembles. Crop format (the direction-A pipeline). Configurations: 12 leads; limb 6; I+II; II; I (absent leads zeroed, window re-standardised, as in PROTOCOL_LEAD). Reduced mean = mean over the four reduced configurations.

## Hypotheses: fixed-sequence testing at alpha = 0.05 (95% CI), stop at the first failure
- Engineering check (precondition, not a statistical test): AGA 12-lead test scores equal DEME's exactly for every seed; otherwise stop and report.
- TC1 (first): AGA - DEME reduced-mean stratified V1 lower bound > 0.
- TC2 (only if TC1 holds): AGA - DEME reduced-mean V2 lower bound > 0.
Order rationale: robustness of within-CODE discrimination is the primary purpose of the lead component; V2 second (FDA, Multiple Endpoints in Clinical Trials, 2022).

## Statistics
Metrics and paired patient-cluster bootstrap (2,000x, seed 1234, clusters = (dataset, patient_id)) as in analysis/aga_eval.py; length rule as in TEST_A. Sensitivity (reported, no decision): Bonferroni over every primary contrast on this split (TEST_USE_LOG m = 29, plus TC1 and TC2 -> 31; alpha/m = .0016). Descriptive: per-configuration stratified V1, V2, pooled V1.

## Procedure
1. Score with train_module.py --score-only --lead-subsets --score-split SPLIT --split-root DIR (split rows, crop memmap, no labels; same masking code as PROTOCOL_LEAD).
2. Dry run on val: the scores must equal the val_scores_leads.csv used by analysis/aga_eval.py exactly, and analysis/test_c_eval.py --split val must reproduce the amendment-1 AGA - DEME result; results reported to the user.
3. Lock the scripts (PROTOCOL_TEST_C.lock).
4. Only after explicit user approval: score test (test memmaps built for TEST_B, sha256 296e547e... / 51b0ab1e...), evaluate once; labels read once from chagas_step2_20261013/exam_id_split.csv; all results reported and added to TEST_USE_LOG.md (read 7).

## Disclosures
- Internal held-out split of the same cohorts (not external validation).
- AGA was designed after the val screen of lead masking (PROTOCOL_LEAD) showed a 12-lead cost, and retained on val; val gains are therefore optimistic.
- No reduced-lead model has been evaluated on this test split before; reduced-lead ResNet models were (read 1, 10-18, different models and endpoints).

## Result (test split, one shot; read started 2026-10-25 15:43; analysis/results/test_c/test_c_results.json)
- Engineering check: AGA 12-lead test scores identical to DEME for all three seeds.
- TC1: AGA - DEME reduced-mean stratified V1 +.0216 [+.0156, +.0275] -> SUPPORTED. TC2: reduced-mean V2 +.0279 [+.0192, +.0378] -> SUPPORTED. Bonferroni sensitivity (m = 31): p(TC1) 6.1e-13, p(TC2) 2.4e-9 -> both pass.
- Per configuration (stratified V1 / V2): limb6 +.026 / +.037; I+II +.017 / +.028; II +.019 / +.020; I +.024 / +.027 (all CIs > 0).
- Arms: DEME 12-lead stratified V1 .814 / V2 .866; reduced mean .771 / .828. AGA 12-lead identical; reduced mean .792 / .856.
