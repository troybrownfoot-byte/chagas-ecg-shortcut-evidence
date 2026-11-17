# One-shot TEST evaluation protocol

Written 2026-10-18 before the test split was loaded for any model. Script: `evaluate_test.py` (hash in `test_lock.sha256`).
The test split (patient-level, from `/media/hyhz/GZR/chagas_step2_20261013/exam_id_split.csv`) has not been read by any training, model selection or analysis so far.

## Models (all frozen; no retraining, no threshold tuning on test)
- Reduced-lead study, 3 seeds each (1234, 1235, 1236): lead12, single_II, single_I, limb6. lead12 seed 1234 = step-6 `mix_best.pt`.
- Route-1 dose study, seed 1234: w1 (= step-6 `mix_best.pt`), w5, w20, w80.

## Primary endpoints (reduced-lead, 3-seed mean ensembles, patient-cluster bootstrap 2000x)
- H1 source shortcut: V3 = AUROC(SaMi-Trop test vs CODE-15% test positives). Confirmed for an arm if ensemble V3 CI lower bound > 0.5 AND >= 2 of 3 seeds have V3 > 0.5.
- H2 diagnostic non-inferiority: within-CODE-15% AUROC (reduced − lead12), paired bootstrap; non-inferior if CI lower bound >= −0.02.

## Secondary endpoints
- Overall test AUROC and within-CODE AUROC per arm (ensemble and per seed).
- Top-5% recall overall / SaMi-Trop / CODE-15% positives.
- V3 within recording-length strata (7.3 s and 10.2 s, from the non-zero span of each test record).
- V3 after the length-equalising crop (central 7.335 s, as in `crop_intervention.py`).
- Route 1: T1 (within-CODE), T2 (SaMi-Trop vs CODE-15% negatives), T3 (SaMi-Trop vs CODE-15% positives) for w1, w5, w20, w80.

## Rules
- Run once. A rerun is allowed only if the script crashes before `test_results.json` is written; any rerun is logged.
- Results are reported as they come out; no model, threshold, endpoint or stratum is changed after seeing them.
