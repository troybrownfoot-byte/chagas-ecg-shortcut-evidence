# PROTOCOL_TEST_NNRG - one-shot test read 22: the noisy-negative filter (NNR amendment-1 module EPCDSEG) inside the integrated CG-Net, 12 and reduced leads

Status: written 2026-11-03 ~13:42 Beijing time, before the PROTOCOL_NNR stage B2 result and before any test label of an EPCDSEG model; locked by sha256 in PROTOCOL_TEST_NNRG.lock. Runs only if stage B2 passes (checked by the runner and by both scripts).

Approval: the user approved test use on 2026-11-02 ~20:25 Beijing ("批准使用测试集"); a module that passes its preregistered val rule gets its one-shot test confirmation without asking again (user, 10-27); each read has its own lock.

## What is tested
EPCDSEG trains CG-Net's 12-lead network with small-loss filtering of CODE-15% negatives (from epoch 2 the highest-BCE CODE-15% negative of every 64-row micro-batch gets loss weight 0; checkpoint chosen among epochs >= 2); the deployed network is architecturally EPCDSE. Mechanism: the dropped negatives are about 12x enriched for known noisy negatives. Val (each model with its own ANCC, pooled) vs the deployment: S -.0004 [-.0029, +.0022], V2 +.0002 [-.0029, +.0034] (B1 PASS); external (SaMi-Trop-naive, W1/W2) WM +.0022 [+.0002, +.0041] (EXT_PASS); adopted under the locked PROTOCOL_NNR amendment-1 rule. Stage B2 re-trains the AGA adapters on the EPCDSEG bases (whole-model rule).

## Inputs (scripts on the 3090 workstation; shas in the lock)
- analysis/test_nnrg.py (from analysis/test_pprq.py): G = EPCDSEG seeds 1234-1236 (peft_ws/nnr; sha 559ce374, 8ecfac64, 1cc1b651); LSO_G = SaMi-Trop-naive EPCDSEG (f7c93de4, c0f2a565, ced5b114); CGN = ref9 EPCDSE (gate: equal to the TEST_H FULL 12-lead scores on every row, max |diff| < 1e-3); LSO_CGN = lso2 LSO_EPCDSE (as read 16). Offsets fixed before the read (CODE-15% train hold-out negatives): CGN .2466 / LSO_CGN .2640 (ancc.json), G .2540 (nnr2_B1_EPCDSEG.json), LSO_G .2923 (nnr2_ext_nnrg.json). Labels read only after every gate; after the labels CGN_P, CGN_P_O, LSO_CGN, LSO_CGN_O must reproduce read 16 (< 1e-4).
- analysis/test_nnrg2.py (from analysis/test_adh2.py): AGADSEG (stage B2 runs) scored on the test crop under 12, limb6, I_II, II, I by train_module.nnrb2.py --score-only --lead-subsets --score-split test (remote/test_nnrg_ws.sh); gates: base_unchanged in every result.json, 12-lead identity with the EPCDSEG bases (< 1e-3); AGADSE = read-13 lead scores; after the labels AGADSE must reproduce read 13 (< 1e-4). No post-processing for either at reduced leads (as stage B2).
Metrics as reads 16 and 18: S, V2 (P, challenge at 12 leads); pooled = mean logit over a patient's test exams; paired patient-cluster bootstrap 2,000x, seed 1234.

## Hypotheses (fixed now)
- TG1 (primary; the deployment with the module vs without, both calibrated, pooled, 12 leads): G_P_O - CGN_P_O: S and V2 CI lower bounds above -.005 (non-inferiority, EPC-D margin).
- TG2 (unseen-cohort positives): LSO_G_O - LSO_CGN_O: V2 CI lower bound above 0.
- TG3 (integrated network at reduced leads): AGADSEG - AGADSE, pooled, mean over the four reduced configurations: S and V2 CI lower bounds above -.005.
Reported without a hypothesis: the uncalibrated contrasts, exam level, P and challenge, device AUROC, mean p, every lead configuration. Multiplicity: three new hypotheses; project count 51 -> 54. CIs unadjusted, count stated.

## Use
TG1 and TG3 hold: EPCDSEG enters CG-Net as the training-time module for the label problem (non-inferior in-distribution at 12 and reduced leads); with TG2 also the unseen-cohort claim, worded against the PROTOCOL_TVC null band. TG1 only: reported as non-inferior at 12 leads. Otherwise: val and external findings only.
