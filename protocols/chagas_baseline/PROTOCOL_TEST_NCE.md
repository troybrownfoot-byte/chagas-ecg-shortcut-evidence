# PROTOCOL_TEST_NCE - one-shot test read 20: negative-control concept erasure (NCE) at 12 leads (written 2026-11-03 ~02:51 Beijing; locked before any NCE result and before any test label)

Approval: the user approved test use on 2026-11-02 ~20:25 Beijing ("批准使用测试集"); each read gets its own lock. Runs only if PROTOCOL_NCE stage B1 passed on val (nce_stageB1.json B1_PASS, amendment 1) AND its external endpoint passed (nce_ext.json EXT_PASS_M); the runner and the script check both, otherwise nothing is scored.

## What is tested
NCE (EPCDSEN) = the CG-Net 12-lead network trained with the fixed acquisition-period offset in the likelihood and a rank-1 erasure of the device mean-difference among CODE-15% negatives before the head (no adversary). The erasure folds into the head, so the deployed network is an EPCDSE network with a changed head and no post-processing. The question: can this layer replace the post-hoc calibration (ANCC) of the current deployment?

## Inputs (analysis/test_nce.py on the 3090 workstation; sha in the lock)
- NCE: EPCDSEN seeds 1234-1236 (peft_ws/nce; stage A seeds and the amendment-1 seed; config and training fold self-check verified, sha recorded), scored with the erasure folded into the head.
- CGN: ref9 EPCDSE seeds 1234-1236 (gate: equal to the TEST_H FULL 12-lead scores on every row, max |diff| < 1e-3).
- LSO_NCE: SaMi-Trop-naive EPCDSEN seeds 1234-1236 (rental; sha equal to its PULLED line); LSO_CGN: lso2 LSO_EPCDSE (as read 16).
- Offsets (only for the _O scores) fixed before the read from CODE-15% train hold-out negatives: CGN / LSO_CGN ancc.json, NCE nce_stageB1.json, LSO_NCE nce_ext.json.
- Test crop memmap, 3-seed mean probability, pooling = mean logit over a patient's test exams. Labels read only after every gate; after the labels CGN_P, CGN_P_O, LSO_CGN, LSO_CGN_O must reproduce read 16 (< 1e-4). Metrics as read 16; device AUROC among CODE-15% test negatives. Paired patient-cluster bootstrap 2,000x, seed 1234.

## Hypotheses (fixed now)
- TN1 (primary; the layer replaces the post-processing): NCE_P (no post-processing) - CGN_P_O (current deployment with ANCC): S and V2 CI lower bounds above -.005.
- TN2 (module effect, both without post-processing): NCE_P - CGN_P: V2 CI lower bound above 0 and S CI lower bound above -.005.
- TN3 (unseen-cohort positives): LSO_NCE (no post-processing) - LSO_CGN_O: V2 CI lower bound above 0.
Reported: exam level, NCE with its own ANCC, P and challenge, device AUROC, mean p. Multiplicity: three new hypotheses; project count 49 -> 52. CIs unadjusted, count stated.

## Use
TN1 holds: NCE enters CG-Net as a network-structure module that replaces the post-hoc calibration (deployment: crop -> CG-Net with NCE -> pooling); TN2/TN3 qualify how much it adds. TN1 fails: reported as a val/external finding; ANCC stays.
