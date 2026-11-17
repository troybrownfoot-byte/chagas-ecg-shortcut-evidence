# TEST_D: additional baselines for the paper's comparison table (written 2026-10-26 before any new test metric; user approved test use 2026-10-26)

## Purpose (descriptive, no hypothesis test, no decision rule)
Add published-architecture baselines to Table 2 of the manuscript. Models are fixed checkpoints trained earlier on the same frozen patient split; no model, seed, threshold or format is chosen with test data.

## Models (existing scores, inference already done; 3-seed mean-probability ensembles)
- ResNet (Ribeiro et al. 2020 architecture, plain 12-lead): chagas_tricks baseline_s1234-1236 (= chagas_reduced_lead lead12_s0-s2), native input.
- ResNet + age/sex: chagas_tricks agesex_s1234-1236, native input.
- Reference: CG-Net at 12 leads = EPC (DEME) crop format, collected/rent4090/runs/DEME_s*/<split>_scores_tb.csv score_crop (scores already used in TEST_B).
Val: chagas_tricks/stage2/ensemble_scores/{baseline,agesex}_val_scores.csv; DEME val_scores_tb.csv.

## Metrics / statistics
As analysis/mod_eval.py: pooled V1, length-stratified V1 (TEST_A length rule), V2, V3, challenge (top-5% recall). Paired patient-cluster bootstrap 2,000x (seed 1234): 95% CI of each arm and of CG-Net minus each baseline. Reported in full, no claims beyond description.

## Procedure
1. Dry run on val (analysis/test_d_eval.py --split val), reported. 2. Lock (PROTOCOL_TEST_D.lock). 3. Test run once; labels read once from chagas_step2_20261013/exam_id_split.csv; added to TEST_USE_LOG.md as read 8 (descriptive, adds no primary contrast to the Bonferroni family).

## Disclosures
These ResNet test scores were evaluated before on this split (read 1-2, pooled V1/V3 only); length-stratified V1, V2 and challenge for them are new.
2026-10-26 TEST_D done (descriptive, read 8): ResNet V1 .828/strat .782/V2 .809/V3 .503/chal .417; ResNet+agesex .831/.787/.818/.503/.413; CG-Net .824/.814/.866/.559/.429. analysis/results/test_d/test_d_results.json
