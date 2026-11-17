# Test protocol for F4 (12-lead) and F5 (lead II) heterogeneous fusion

Written and hash-locked 2026-10-21, while F4 and F5 are still running and before any F4/F5 validation result is seen. The user authorised test use on 2026-10-21 provided there is no leakage. Project-level test history: reduced-lead/dose (1st), tricks (2nd), SR-KD (authorised 3rd, not executed because Stage A stopped); this is the next test read and will be disclosed as such.

## Leakage rules
- Every model and every fusion parameter is fixed using training and validation data only. The test split is used once, for inference and evaluation, after this file is locked.
- All analyses below are run and reported regardless of the F4/F5 validation outcomes; no method, seed, threshold or subset is selected using test data.
- Test labels are read only by the final evaluation script, after all test scores are written to disk and hashed.

## Models (fixed checkpoints)
- R_s: `chagas_tricks/runs/agesex_s{1234,1235,1236}` — test scores reused from `chagas_tricks/test_eval_tricks/test_scores.csv` (columns agesex_s1234…s1236).
- P_s: plain 12-lead ResNet (s1234 = step-6 `mix_best.pt`; s1235/s1236 = `chagas_reduced_lead/runs_s2/lead12_*`) — reused from `chagas_reduced_lead/test_eval/test_scores.csv` (lead12_s0, s1, s2 = seeds 1234, 1235, 1236; uncropped columns).
- R-II_s: lead-II ResNet — reused from the same file (single_II_s0, s1, s2; uncropped).
- F_s: ECGFounder 12-lead (`runs/F1/best.pt`, `runs_F4/F_s{1235,1236}/best.pt`) — new test inference.
- F-II_s: ECGFounder single-lead on lead II (`runs_F5/FII_s{1234,1235,1236}/best.pt`) — new test inference.
Before reuse, each reused column is checked for 34,603 rows, alignment by (dataset, exam_id) with the frozen test rows, and values in [0, 1].

## Test preprocessing for ECGFounder inputs
Identical to the train/validation pipeline (PREREGISTRATION_F1.md plus the registered clarifications): non-zero span, official `filter_bandpass` at 400 Hz, resample to 500 Hz, centre/crop to 5,000 samples, per-record z-score, float16; all-zero records and records with non-zero span < 200 samples become all-zero inputs. Counts of such records are reported. Lead-II inputs = channel 1 re-standardised per record, as in F5.

## Fusion
For each seed and each pair, LS, DCGF-s and DCGF-s-homo are refitted once on the full validation split with exactly the F4 procedure (float64 L-BFGS, same initialisation and penalty), and the fitted parameters are saved before any test inference. They are then applied to test logits. RA = mean of within-test ranks of the two members (label-free); LA = sigmoid of the mean test logits. 3-seed aggregation as in F4/F5.
Pairs: 12-lead (R_s, F_s), homogeneous (R_s, P_s); lead II (R-II_s, F-II_s), homogeneous (R-II_s, R-II_next), next = 1234→1235→1236→1234.

## Endpoints and statistics
V1, V3, overall AUROC, top-5% recall overall / SaMi-Trop / CODE-15% positives; per seed and 3-seed. Paired patient-cluster bootstrap on test patients, 2,000×, seed 1234, percentile 95% CI.

## Test hypotheses (mirroring the validation hypotheses; all reported)
12-lead: T1 DCGF-s − R ensemble and DCGF-s − 6-ResNet (both lower bounds > 0); T2 DCGF-s − LS; T3 DCGF-s − DCGF-s-homo.
Lead II: T4 DCGF-s − R-II ensemble (V1 lower bound > 0); T5 |V3(DCGF-s) − 0.5| < |V3(R-II ensemble) − 0.5| with the V3 difference CI excluding 0; T6 DCGF-s − DCGF-s-homo.
Also reported: RA, LA, LS, single backbones, R ensemble, 6-ResNet.
