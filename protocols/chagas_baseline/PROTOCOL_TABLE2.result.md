# PROTOCOL_TABLE2 result (descriptive test read 14) - Table 2 rows of the integrated CG-Net

Written 2026-10-28 16:06 Beijing time; analysis/table2_update.py run once 15:59:15-16:03:58 (output analysis/results/test_h/table2_update.json).
Check passed: BASE .809/.796/.837/.537/.397 and MS .824/.814/.866/.559/.429 reproduce the manuscript's Table 2 rows (ECGFounder +
de-shortcut pipeline; CG-Net) exactly.
| row | pooled AUROC | stratified AUROC | cross-cohort AUROC (V2) | source AUROC (V3) | challenge |
|---|---|---|---|---|---|
| CG-Net (manuscript, MS) | .8245 | .8142 | .8662 | .5593 | .4289 |
| new integrated CG-Net, single exam (FULL) | .8241 | .8152 | .8742 | .5669 | .4265 |
| new integrated CG-Net + longitudinal pooling (FULL_P) | .8336 | .8237 | .8772 | .5709 | .4252 |
FULL - MS: pooled -.0004 [-.0053,+.0046], strat +.0010 [-.0040,+.0063], V2 +.0080 [-.0014,+.0176], V3 +.0076 [-.0014,+.0172], challenge
-.0025 [-.0180,+.0113]. FULL_P - MS: pooled +.0091 [+.0023,+.0165], strat +.0096 [+.0023,+.0169], V2 +.0110 [+.0014,+.0207], V3 +.0116
[+.0012,+.0225], challenge -.0037 [-.0211,+.0119]. FULL_P - BASE: pooled +.0250, strat +.0280, V2 +.0399, V3 +.0335, challenge +.0282
(all CI > 0). Reading: at 12 leads the single-exam integrated model equals the manuscript model; the 12-lead gain comes from pooling.
