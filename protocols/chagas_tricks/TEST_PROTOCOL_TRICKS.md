# One-shot TEST evaluation of the published-tricks arms

Written 2026-10-19 before any tricks model was scored on the test split. All design choices were made on validation only.

## Disclosure
The test split was read once before (2026-10-18, `chagas_reduced_lead/test_eval/`) for the reduced-lead study. That evaluation did not include any tricks model and no tricks setting was chosen from it. This is the second and last use of the test split for the 12-lead models.

## Models (frozen; no retraining, no threshold tuning)
- Baseline: 12-lead seeds 1234/1235/1236. Test scores are REUSED from `/media/hyhz/GZR/chagas_reduced_lead/test_eval/test_scores.csv` (columns lead12_s0, lead12_s1, lead12_s2); these models are not re-scored.
- Primary arms, 3 seeds each (`runs/<arm>_s{1234,1235,1236}/best.pt`): agesex, rank, combo (agesex+rank).
- Descriptive arms, seed 1234 only: aug, soft, consist, posw.

## Primary endpoint
Within-CODE-15% AUROC (V1) of each primary arm's 3-seed mean ensemble minus the baseline ensemble, paired patient-cluster bootstrap (2,000 replicates, seed 1234).
Replicated on test if the 95% CI lower bound > 0. Also report combo − agesex and combo − rank.

## Secondary endpoints
Overall AUROC; Top-5% recall overall / SaMi-Trop / CODE-15% positives; V3 (SaMi-Trop vs CODE-15% positives) with bootstrap CI; per-seed V1 and V3. Descriptive arms: same metrics, single seed, no inference.

## Rules
Run once; the script refuses to run if `test_eval_tricks/test_results.json` exists. Rerun only if it crashes before writing that file (logged). No model, endpoint or threshold changes after seeing results.
