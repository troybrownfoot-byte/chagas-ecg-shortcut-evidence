# PROTOCOL_TEST_ADHX - one-shot test read 21: does ADH improve discrimination for positives of a cohort the model never saw? (written 2026-11-03 ~09:04 Beijing; locked before any test label of these models)

Approval: the user approved test use on 2026-11-02 ~20:25 Beijing ("批准使用测试集"); each read gets its own lock. This read asks a new, narrower question than read 17 (which did not run because ADH failed its in-distribution val read): ADH is not adopted, but its external result (W1 / W2, SaMi-Trop-naive models: WM +.0042 [+.0015, +.0069] over the calibrated reference without post-processing) suggests a robustness property. Test has its own unseen-cohort comparison: SaMi-Trop test positives against CODE-15% test negatives, scored by models trained without SaMi-Trop.

## Inputs (analysis/test_adhx.py on the 3090 workstation; sha in the lock)
LSO_ADH = SaMi-Trop-naive EPCDSEA seeds 1234-1236 (sha 5a4803e9, 0a7b993a, 0586ef00); LSO_CGN = lso2 LSO_EPCDSE seeds 1234-1236 (as read 16). Offsets for the _O scores fixed before the read (CODE-15% train hold-out negatives): LSO_CGN .2640 (ancc.json), LSO_ADH .1656 (adh_ext.json). Pipeline gate before the labels: ref9 EPCDSE seed 1234 equals its TEST_H 12-lead scores; after the labels LSO_CGN / LSO_CGN_O reproduce read 16 (< 1e-4). No in-distribution ADH score is read.

## Hypotheses (fixed now)
- TX1 (primary): LSO_ADH (no post-processing) - LSO_CGN_O (with ANCC): V2 CI lower bound above 0.
- TX2: LSO_ADH - LSO_CGN (both without post-processing): V2 CI lower bound above 0.
Reported: S, P, challenge, device AUROC among CODE-15% test negatives, LSO_ADH with its own offset. Multiplicity: two new hypotheses; project count 49 -> 51. CIs unadjusted, count stated.

## Use
TX1 holds: the paper reports ADH as a network module with a test-confirmed gain on an unseen cohort and a val-measured in-distribution cost (stage B1, PRECHECK_V2DEC), i.e. a robustness configuration, not the default model. TX1 fails: ADH is reported with its val and external numbers only.
