# PROTOCOL_TEST_ANCC - one-shot test read of the negative-control device calibration (written 2026-11-02 ~18:28 Beijing; locked before any test label is read)

Approval: the user wrote "批准" at ~18:22 Beijing to the proposal of a test confirmation of the calibration for every model family. Test read 14 of the project (after TEST_H, read 13).

## What is tested
The calibration (ANCC) subtracts a fixed per-device logit offset, estimated on CODE-15% train hold-out negatives with age/sex adjustment (analysis/results/ancc/ancc.json; nothing is fitted on test), from device-A exams. Exam-level stratified V1 cannot change (its strata are the devices). On val (PROTOCOL_ANCC, amendment 1) it raised external AUROC for every family, kept pooled stratified V1 (+.0001 [-.0004, +.0006]) and raised V2 (+.0036 pooled).

## Inputs (analysis/test_ancc.py on the 3090)
- CGN: ref9 EPCDSE, 3 seeds, re-scored on the test crop memmap. Gate: equal to the TEST_H FULL 12-lead scores of the same seed (collected/test_h/runs/AGADSE_s*, the paper's CG-Net) on every row, max |diff| < 1e-3. The final method is CGN pooled (CGN_P: mean logit over a patient's test exams, calibration before pooling).
- BASE, DEM: stored test_scores_tb.csv (crop); gate: 1,024 re-scored rows of seed 1234 equal the stored scores (< 1e-3).
- LSO_BASE, LSO_DEM, LSO_CGN (never saw SaMi-Trop): re-scored on test; their V2 has SaMi-Trop test positives never seen in training.
- Device: CODE-15% from the test record length (analysis/results/test_a_test/lengths.csv), SaMi-Trop from the signal span (< 3,400). Labels (chagas_step2_20261013/exam_id_split.csv) are read only after every gate.
Metrics as analysis/test_h_abl_eval.py: stratified V1 (S), V2, challenge (top 5% of all test exams); plus P (pooled CODE-15% AUROC). Paired patient-cluster bootstrap 2,000x, seed 1234.

## Hypotheses (fixed now)
- TA1 (primary): the final method CGN_P: V2(C+O) - V2(C) CI above 0, and pooled S(C+O) - pooled S(C) lower bound above -.002.
- TA2: LSO_CGN: V2(C+O) - V2(C) CI above 0 (external-like positives).
- TA3: BASE and DEM: V2(C+O) - V2(C) CI above 0, each.
- TA4: the family ranking holds after the calibration: CGN_P(C+O) - BASE_P(C+O) and CGN_P(C+O) - DEM_P(C+O) on S and V2 (reported with CIs; supported where the CI is above 0).
- Reported without a hypothesis: P (expected to fall: inside CODE-15% the device carries the label-recording period), challenge, the LSO family contrasts, the number of CODE-15% test patients with exams on both devices.
Multiplicity: four new hypotheses on top of the 43 tests counted in TEST_H; CIs are reported unadjusted and the count is stated.

## Use
If TA1 holds, the calibration enters the method as its sixth component (inference only, no labels, no training) and the paper reports test V2 / P / challenge with and without it. If it does not, the calibration is reported as a val/external finding (W1, W2) only.
