# PROTOCOL_TEST_ANCC result - one-shot test read 14 (run 19:02-19:2x Beijing on the 3090; analysis/test_ancc.py f76c256f; analysis/results/test_ancc/test_ancc.json)

Gates passed before any label was read: ref9 EPCDSE re-scored on test equals the TEST_H FULL 12-lead scores of the paper's CG-Net on every row (max |diff| 2.8e-4, 2.1e-4, 1.4e-4); stored BASE / DEM test scores equal re-scoring on 1,024 rows (3e-8, 5e-8). 835 CODE-15% test patients have exams on both devices. Offsets fixed from the train hold-out (ancc.json).

| test (n = 34,603) | S | V2 | P | challenge |
|---|---|---|---|---|
| CGN_P (final, pooled) C | .8237 | .8772 | .8336 | .4252 |
| CGN_P C+O | .8239 | .8824 | .8245 | .4105 |
| CGN exam C / C+O | .8152 / .8152 | .8742 / .8791 | .8241 / .8139 | .4265 / .4105 |
| DEM_P C / C+O | .8185 / .8187 | .8720 / .8775 | .8291 / .8191 | .4277 / .4118 |
| BASE_P C / C+O | .8022 / .8026 | .8410 / .8474 | .8167 / .8039 | .4056 / .3946 |
| LSO_CGN C / C+O | .8113 / .8113 | .8451 / .8514 | .8230 / .8113 | .4020 / .3922 |
| LSO_DEM C / C+O | .8105 / .8105 | .8436 / .8516 | .8241 / .8102 | .4105 / .3934 |
| LSO_BASE C / C+O | .7951 / .7951 | .7996 / .8066 | .8114 / .7988 | .4020 / .3909 |

## Hypotheses
- TA1 (primary) SUPPORTED: CGN_P V2 +.0053 [+.0016, +.0088]; pooled S +.0002 [-.0004, +.0008] (non-inferior).
- TA2 SUPPORTED: LSO_CGN V2 (SaMi-Trop test positives never seen) +.0063 [+.0020, +.0104].
- TA3 SUPPORTED: BASE V2 +.0061 [+.0011, +.0106]; DEM V2 +.0054 [+.0014, +.0091] (also LSO_BASE +.0070, LSO_DEM +.0080, CIs above 0).
- TA4 PARTLY: CGN_P - BASE_P after calibration S +.0214 [+.0103, +.0323], V2 +.0351 [+.0203, +.0501] (supported); CGN_P - DEM_P S +.0052 [-.0002, +.0109], V2 +.0049 [-.0043, +.0141] (not supported; the calibration does not change this gap, the gap itself is small on test). Exam level CGN - DEM S +.0021 [-.0035, +.0080].

## Reported without a hypothesis
- P falls for every family (-.009 to -.014, CIs below 0), as on val.
- challenge falls for every family: CGN_P -.0147 [-.0272, -.0012], CGN exam -.0159, BASE -.0147, DEM -.0098, LSO -.010 to -.017. The challenge score counts CODE-15% self-reported positives in the top 5% of all test exams; CODE-15% labels are recorded far more often in the device-A period (3.00% vs 0.24% on fit rows), so the device shortcut raises it. Removing the shortcut costs this label-period gain on CODE-15% labels while raising AUROC against serology-confirmed positives (V2 here; W1 and W2 on the external cohorts).
- Multiplicity: four new hypotheses (47 tests in the project count); the TA1-TA3 lower bounds are +.0011 to +.0020, so they would not survive a Bonferroni correction at m = 47; they are consistent in direction with val, W1 and W2.

## Consequence
The negative-control device calibration enters the method as its sixth component (inference only; offsets from CODE-15% hold-out negatives; no labels of any target cohort; placed before longitudinal pooling). The paper reports test S unchanged, V2 up, and P / challenge down with the label-period explanation, plus W1 / W2 external gains (+.012 to +.015 WM for every family).
