# PROTOCOL_TEST_ADHX result - test read 21 (run 09:05-09:10 Beijing 2026-11-03; workstation; analysis/test_adhx.py 5878e096; analysis/results/test_adhx/test_adhx.json)

Gates passed: ref9 EPCDSE seed 1234 equals its TEST_H scores (2.8e-4); LSO_ADH checkpoints match their sha; LSO_CGN / LSO_CGN_O reproduce read 16 exactly. Offsets: LSO_CGN .2640, LSO_ADH .1656.

| test, SaMi-Trop-naive models | S | V2 | P | challenge | device AUROC CODE-15% negatives |
|---|---|---|---|---|---|
| LSO_CGN / LSO_CGN_O | .8113 / .8113 | .8451 / .8514 | .8230 / .8113 | .4020 / .3922 | .574 / .508 |
| LSO_ADH / LSO_ADH_O | .8099 / .8099 | .8567 / .8605 | .8172 / .8091 | .4142 / .4056 | .545 / .501 |

- TX1 (primary) NOT SUPPORTED: LSO_ADH (no post-processing) - LSO_CGN_O V2 +.0052 [-.0042, +.0164] (S -.0014, P +.0059, challenge +.0221 [+.0081, +.0335]).
- TX2 SUPPORTED: LSO_ADH - LSO_CGN (both raw) V2 +.0116 [+.0019, +.0219].
- With each its own calibration: V2 +.0090 [-.0003, +.0195], challenge +.0135 [+.0023, +.0256].
- Multiplicity: two new hypotheses (project count 51); TX2 would not survive a correction.

## Reading
On test, as on val and W1 / W2, ADH's unseen-cohort benefit is of the size of the post-hoc calibration: it beats the uncalibrated CG-Net but not the calibrated one. ADH stays a reported robustness analysis (network-internal device invariance about equivalent to ANCC on unseen cohorts, with an in-distribution cost), not a method component.
