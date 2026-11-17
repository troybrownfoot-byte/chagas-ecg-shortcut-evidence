# PROTOCOL_TEST_G — result (test read 12): TH1 SUPPORTED — longitudinal patient-level score pooling improves EPCDSE on the test split

Written 2026-10-27 22:28 Beijing time. Protocol locked 22:24:36 after an exact val dry run (reproduced EXP11). No new model
scoring: the read-11 test scores of the EPCDSE / EPCDSR models were pooled (sigmoid of the mean logit over the patient's test exams).
analysis/test_g_eval.py --split test -> analysis/results/exp11/test_g_test.json.

Test split, pooled - single, point [95% CI]:
| models | stratified V1 | V2 | challenge |
| EPCDSE seeds 1237-1239 (TH1, primary) | +0.0063 [+0.0005, +0.0118] | +0.0030 [+0.0023, +0.0037] | -0.0074 [-0.0226, +0.0119] |
| EPCDSE seeds 1234-1236 | +0.0086 [+0.0029, +0.0148] | +0.0029 [+0.0022, +0.0036] | +0.0000 |
| EPCDSE six seeds | +0.0073 [+0.0016, +0.0129] | +0.0029 | -0.0049 |
| EPCDSR six seeds (raw weights) | +0.0067 [+0.0012, +0.0125] | +0.0023 | -0.0037 |
| EPCDSE seeds 1237-1239, patient-harmonised test labels (356 labels changed; point) | +0.0111 | +0.0030 | -0.0137 |
TH1 SUPPORTED (stratified V1 lower bound > 0, V2 lower bound > -0.010). Bonferroni sensitivity (m = 36): approximate p 0.014 > 0.05/36 ->
not passed; reported as such. Val (EXP11): +0.0059 [+0.0007, +0.0106] (EXP2 seeds), +0.0070 [+0.0020, +0.0116] (EXP6 seeds).
Interpretation: averaging the model's evidence over a patient's serial ECGs gives a consistent +0.006 to +0.009 stratified AUROC on
val and test; it does not improve the top-5% challenge score. Candidate contribution: inference method for longitudinal tele-ECG
screening, together with the label harmonisation of EXP10 (both exploit the chronicity of the infection).
