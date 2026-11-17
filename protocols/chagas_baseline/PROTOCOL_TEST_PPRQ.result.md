# PROTOCOL_TEST_PPRQ result - test read 19 (run 02:19-02:35 Beijing 2026-11-03 on the 3090; analysis/test_pprq.py 246e1e0e; analysis/results/test_pprq/test_pprq.json)

Gates passed before any label: ref9 EPCDSE equals the TEST_H FULL 12-lead scores (max |diff| 2.8e-4, 2.1e-4, 1.4e-4); all six PPR-Q checkpoints match their locked sha256; after the labels CGN_P, CGN_P_O, LSO_CGN, LSO_CGN_O reproduce read 16 exactly (max |diff| 0). Offsets (fixed, train hold-out): CGN .2466, LSO_CGN .2640, Q .3161, LSO_Q .2325.

| test (n = 34,603) | S | V2 | P | challenge | device AUROC among CODE-15% negatives |
|---|---|---|---|---|---|
| CGN_P / CGN_P_O (current deployment) | .8237 / .8239 | .8772 / .8824 | .8336 / .8245 | .4252 / .4105 | exam .563 / .506 |
| Q_P / Q_P_O | .8224 / .8227 | .8731 / .8805 | .8347 / .8228 | .4191 / .4105 | exam .579 / .503 |
| LSO_CGN / LSO_CGN_O | .8113 / .8113 | .8451 / .8514 | .8230 / .8113 | .4020 / .3922 | .574 / .508 |
| LSO_Q / LSO_Q_O | .8093 / .8093 | .8528 / .8581 | .8196 / .8086 | .4142 / .4020 | .563 / .503 |

## Hypotheses
- TQ1 (primary) NOT SUPPORTED: Q_P_O - CGN_P_O S -.0012 [-.0038, +.0013] (non-inferior), V2 -.0019 [-.0078, +.0034] (lower bound below -.005, non-inferiority not shown).
- TQ2 formally SUPPORTED, borderline: LSO_Q_O - LSO_CGN_O V2 +.0067 [+.0000, +.0151] (lower bound just above 0); uncalibrated LSO_Q - LSO_CGN V2 +.0077 [+.0012, +.0160]; P falls (-.0027 [-.0052, -.0002]).
- Multiplicity: two new hypotheses (project count 49); TQ2 would not survive any correction.

## Consequence (locked use rule)
TQ1 failed, so PPR-Q does not enter the method ("otherwise: val and external findings only"). Reported as a finding: a learned period offset in the likelihood leaves in-distribution test discrimination about unchanged (S -.0012, V2 -.0019, CIs include 0) and moves the score of unseen-cohort positives up by about .007 V2 (W1/W2 on val: WM +.0073), with the caveat that the learned offset drifted to about -3.2. Together with ADH (stage B1 fail) this closes the training-time route for the acquisition-period problem as a method component; the post-hoc ANCC (read 16) remains the confirmed device correction.
