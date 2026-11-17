# PROTOCOL_TEST_ADH - one-shot test read 17: the acquisition-disentangled head (ADH) at 12 leads (written 2026-11-03 ~01:22 Beijing; locked before the stage B1 result and before any test label)

Approval: the user approved test use on 2026-11-02 ~20:25 Beijing ("批准使用测试集") together with the request for network-structure modules; each read gets its own lock. Read 16 was PROTOCOL_TEST_ANCC (11-02 19:02; its protocol and result call it read 14 by mistake; TEST_USE_LOG corrected at this lock). This read runs only if PROTOCOL_ADH stage B1 passed (adh_stageB1.json B1_PASS true; the script refuses otherwise).

## What is tested
ADH (PROTOCOL_ADH, amendments 1-3) trains CG-Net's 12-lead network (EPCDSE) with the frozen acquisition-period offset of the CODE-15% labels in the likelihood and a negative-control device discriminator through gradient reversal; both are training-only, so the deployed network is architecturally EPCDSE. Evidence so far: hold-out device AUROC among negatives .79-.81 -> .49 (native), external WM +.0042 [+.0015, +.0069] over the calibrated reference without any post-processing (EXT_PASS), stage A S -.0054 (fail), stage B1 (val) pending at this lock.

## Inputs (analysis/test_adh.py on the 3090 workstation; sha in the lock)
- ADH: EPCDSEA seeds 1234, 1235 (stage A runs; sha d2609cc3, 1d8016bf) and 1236 (stage B1 run; sha as logged at its pull), trained with SaMi-Trop.
- CGN: ref9 EPCDSE seeds 1234-1236 (the paper's CG-Net 12-lead network); gate: re-scored test logits equal the TEST_H FULL 12-lead scores on every row (max |diff| < 1e-3).
- LSO_ADH: SaMi-Trop-naive EPCDSEA seeds 1234-1236 (sha 5a4803e9, 0a7b993a, 0586ef00); LSO_CGN: lso2 LSO_EPCDSE seeds 1234-1236 (as read 16). Their V2 uses SaMi-Trop test records neither model saw.
- Test crop memmap, 3-seed mean probability, longitudinal pooling (mean logit over a patient's test exams). Offsets (only for the _O scores) fixed before the read from CODE-15% train hold-out negatives: CGN / LSO_CGN from ancc.json (as read 16), ADH from adh_stageB1.json, LSO_ADH from adh_ext.json.
- Device: CODE-15% from the test record length, SaMi-Trop from the signal span (< 3,400). Labels (exam_id_split.csv) are read only after every gate; after the labels, CGN_P, CGN_P_O, LSO_CGN and LSO_CGN_O must reproduce read 16 (< 1e-4).
Metrics as read 16: S (stratified V1), V2, P, challenge; device AUROC of the score among CODE-15% test negatives. Paired patient-cluster bootstrap 2,000x, seed 1234.

## Hypotheses (fixed now)
- TD1 (primary; module effect, both without post-processing): ADH_P - CGN_P: V2 CI lower bound above 0 and S CI lower bound above -.005 (the EPC-D non-inferiority margin).
- TD2 (the module replaces the post-processing): ADH_P (no post-processing) - CGN_P_O (the current deployment, with ANCC): V2 and S CI lower bounds above -.005 (non-inferiority on both).
- TD3 (external-like, as EXT_PASS): LSO_ADH (no post-processing) - LSO_CGN_O: V2 CI lower bound above 0.
- Reported without a hypothesis: P and challenge (expected to fall, as for ANCC: inside CODE-15% the device carries the label-recording period), exam-level contrasts, ADH with its own offset, device AUROC among test negatives (mechanism), mean p on CODE-15% test.
Multiplicity: three new hypotheses; the project count goes from 47 to 50. CIs are reported unadjusted and the count is stated.

## Use
- TD1 and TD2 hold: ADH enters CG-Net as a network module (seventh component): the deployed pipeline is crop -> CG-Net trained with ADH -> pooling, no post-processing; ANCC stays in the paper as the post-hoc finding that motivated it and as the comparison.
- TD1 only: ADH is a module that improves the network, and ANCC is still reported as the deployment's post-processing option.
- Neither: ADH is reported with its val, hold-out and external results only.
Whatever the outcome, the numbers are reported; no other test read of ADH models follows without a new lock.
