# PROTOCOL_TEST_ADH2 - one-shot test read 18: ADH with the AGA lead adapters at reduced leads (written 2026-11-03 ~01:50 Beijing; locked before the B2 result, before read 17 and before any test label)

Approval: the user approved test use on 2026-11-02 ~20:25 Beijing ("批准使用测试集"); each read gets its own lock. Order: read 18 runs only if PROTOCOL_ADH stage B2 passed on val (adh_stageB2.json B2_PASS) AND read 17 supported ADH at 12 leads (test_adh.json TD1 or TD2). Both conditions are checked by the runner and again by the script; otherwise nothing is scored.

## What is tested
The full CG-Net with ADH: the AGA lead adapters of CG-Net trained on the frozen ADH bases (AGADSEA, stage B2; 12-lead output identical to the ADH base) against the paper's CG-Net (AGADSE, read 13 lead scores), at reduced lead sets, both without post-processing.

## Inputs (remote/test_adh2_ws.sh, analysis/test_adh2.py on the 3090 workstation; shas in the lock)
- AGADSEA seeds 1234-1236 (peft_ws/adh3), scored on the test crop memmap under 12, limb6, I_II, II and I by train_module.agaadh.py --score-only --lead-subsets --score-split test. Gates before the labels: result.json base_unchanged for each run; the 12-lead scores equal the EPCDSEA base scores computed by the script (max |diff| < 1e-3).
- AGADSE seeds 1234-1236: stored read-13 lead scores (collected/test_h/runs). After the labels, its pooled reduced-lead S and V2 and pooled 12-lead S must reproduce read 13 (< 1e-4).
- 3-seed mean probability; pooled = mean logit over a patient's test exams. Metrics S (stratified V1 by device) and V2 per configuration, exam level and pooled; reduced = mean over limb6, I_II, II, I. Paired patient-cluster bootstrap 2,000x, seed 1234.

## Hypotheses (fixed now)
- TE1 (primary): pooled reduced-lead S, AGADSEA - AGADSE: CI lower bound above -.005 (non-inferiority, EPC-D margin).
- TE2: pooled reduced-lead V2, AGADSEA - AGADSE: CI lower bound above 0.
Reported without a hypothesis: every configuration, exam level, 12 leads. Multiplicity: two new hypotheses; project count 50 -> 52 (if read 17 ran). CIs unadjusted, count stated.

## Use
TE1 (and TE2) hold: the paper reports ADH for the whole CG-Net (12 and reduced leads) on test. Otherwise the reduced-lead path keeps the paper's CG-Net adapters on the old base and ADH is reported for 12 leads only.
