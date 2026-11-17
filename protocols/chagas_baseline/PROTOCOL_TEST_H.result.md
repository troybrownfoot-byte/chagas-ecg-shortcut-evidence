# PROTOCOL_TEST_H result - one-shot test read 13: the integrated CG-Net and its leave-one-module-out ablation on test

Written 2026-10-28 15:45 Beijing time. Protocol locked 01:52:11 (re-locked 02:09:09, header time only); amendments 1-3 locked 02:14:22,
03:49:47, 07:57:10. Test scoring on this PC (analysis/test_h_score.py v2; val1024 checks of all fetched checkpoints PASS, worst 4.2e-4;
34,603 test rows per file) finished 15:05:21. analysis/test_h_abl_eval.py (sha256 f289dba9..., equal to the lock) run once with --split
test, 15:06:07-15:37:57; output analysis/results/test_h/test_h_abl_test.json and .log. Bonferroni m = 43 (alpha/m = 0.00116).
Engineering checks (every seed): FULL 12-lead == NOAGA 12-lead exactly; NOEMA 12-lead == EPCD 12-lead exactly.

## Hypotheses (whole network FULL_P = crop + EPC-D + EMA + AGA + longitudinal pooling, vs the manuscript CG-Net MS = crop + EPC (DEME) + AGA)
| | contrast | point [95% CI] | p | Bonferroni (m = 43) | result |
|---|---|---|---|---|---|
| TH1 | FULL_P - MS, 12-lead stratified V1 | +0.0096 [+0.0023, +0.0169] | 0.011 | p_adj 0.48, not passed | SUPPORTED |
| TH2 | FULL_P - MS, reduced stratified V1 | +0.0129 [+0.0050, +0.0206] | 0.00105 | p_adj 0.045, passed | SUPPORTED |
Secondary (FULL_P - MS): 12-lead V2 +0.0110 [+0.0014, +0.0207]; reduced V2 +0.0092 [+0.0021, +0.0160]; 12-lead challenge -0.0037
[-0.0211, +0.0119].

## Does each module improve the whole network on test? (FULL_P - variant_P, primary contrast, lower bound > 0)
| module | variant | primary | point [95% CI] | p | Bonferroni | contributes |
|---|---|---|---|---|---|---|
| EPC-D | NOEPCD (AGA on BASE + EMA) | 12-lead strat V1 | +0.0149 [+0.0051, +0.0246] | 0.0030 | not passed | yes |
| EMA | NOEMA (AGA on EPCDSR) | 12-lead strat V1 | +0.0056 [+0.0017, +0.0091] | 0.0030 | not passed | yes |
| AGA | NOAGA (EPCDSE base) | reduced strat V1 | +0.0191 [+0.0120, +0.0267] | 2.7e-7 | passed | yes |
| pooling | FULL (no pooling) | 12-lead strat V1 | +0.0086 [+0.0031, +0.0142] | 0.0019 | not passed | yes |
| crop | NOCROP (orig format) | 12-lead strat V1 | +0.0014 [-0.0015, +0.0050] | 0.40 | - | no (primary) |
Crop on its designed metric: 12-lead V2 +0.0367 [+0.0213, +0.0522] (p < 1e-4), as on val (+0.0414): it removes the record-length
shortcut against SaMi-Trop; the locked primary (stratified V1) was misspecified for it (stated in PROTOCOL_ABL.result.md before this read).
Cumulative chain (12-lead strat V1): BASE -> +EPC-D +0.0145 [+0.0047, +0.0240] -> +EMA +0.0050 [+0.0011, +0.0084] -> +AGA (reduced
+0.0202 [+0.0134, +0.0275]) -> +pooling +0.0086 [+0.0031, +0.0142].
Overall FULL_P - BASE: 12-lead strat V1 +0.0280 [+0.0152, +0.0404], V2 +0.0399 [+0.0249, +0.0545], challenge +0.0282 [+0.0012, +0.0558];
reduced strat V1 +0.0495 [+0.0326, +0.0657], reduced V2 +0.0837 [+0.0635, +0.1040] (both strat V1 pass Bonferroni).

## Test metrics (3-seed ensembles; _P = pooled)
| arm | 12-lead strat V1 | 12-lead V2 | 12-lead challenge | reduced strat V1 | reduced V2 |
|---|---|---|---|---|---|
| BASE (ECGFounder + de-shortcut pipeline) | .7957 | .8373 | .3971 | .7555 | .7811 |
| MS (manuscript CG-Net) | .8142 | .8662 | .4289 | .7921 | .8557 |
| FULL (new, single exam) | .8152 | .8742 | .4265 | .7983 | .8607 |
| FULL_P (new, pooled) | .8237 | .8772 | .4252 | .8050 | .8648 |
BASE and MS reproduce the manuscript's Table 2 rows (.796/.837/.397 and .814/.866/.429).

## Reading
The integrated network improves on the manuscript model on test at 12 leads (+0.96 points, 95% CI > 0) and at reduced leads (+1.29,
also under Bonferroni), and every module except crop (on its misspecified primary) contributes within the whole network on test, as on
val and on the second host. Caveat for the paper: at 12 leads the single-exam model is only +0.10 above MS (.8152 vs .8142, descriptive);
the 12-lead gain over the manuscript comes mainly from longitudinal pooling (MS was not pooled in this read). EPC-D's test contribution is
against no demographics (+0.0149); against the manuscript's EPC it was not non-inferior in read 10 (-0.0040 [-0.0091, +0.0018]).
