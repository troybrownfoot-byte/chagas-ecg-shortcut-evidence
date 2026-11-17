# PROTOCOL_TEST_F — result (test read 11): TG1 SUPPORTED — weight EMA improves EPCDS on the test split

Written 2026-10-27 20:36 Beijing time. Protocol locked 18:58:03 after exact val dry runs. 12 checkpoints scored locally with the
locked scorer (crop format; EPCDSR_s1237 crashed once without a traceback right after the previous model and was re-run alone, log
in the scratchpad); analysis/test_f_eval.py --split test -> analysis/results/test_f/test_eval.json.

Test split, point [95% CI] (3-seed mean-probability ensembles; paired patient-cluster bootstrap 2,000x):
| contrast | stratified V1 | V2 | challenge |
| EPCDSE - EPCDSR, seeds 1237-1239 (TG1, primary) | +0.0084 [+0.0034, +0.0135] | +0.0018 [-0.0070, +0.0101] | +0.0135 [-0.0036, +0.0307] |
| EPCDSE - EPCDSR, seeds 1234-1236 | +0.0051 [+0.0016, +0.0087] | +0.0049 [-0.0005, +0.0106] | +0.0086 |
| EPCDSE6 - EPCDSR6 (six seeds) | +0.0063 [+0.0028, +0.0099] | +0.0024 [-0.0037, +0.0084] | +0.0147 [+0.0000, +0.0255] |
| EPCDSE6 - EPCDS (original RTX 4090 runs) | +0.0061 [+0.0021, +0.0100] | +0.0062 [+0.0008, +0.0118] | +0.0086 |
| EPCDSE6 - DEME (paper's EPC) | +0.0021 [-0.0028, +0.0073] | +0.0061 [-0.0032, +0.0149] | +0.0025 |
| EPCDSR6 - EPCDS (hardware replicate) | -0.0002 [-0.0030, +0.0026] | +0.0038 | -0.0061 |
TG1: stratified V1 lower bound > 0 and V2 lower bound > -0.010 -> SUPPORTED. Bonferroni sensitivity (m = 35): approximate p 0.0034 >
0.05/35 -> does not pass the family-wise threshold; reported as such.
Interpretation: weight EMA (decay 0.999, EMA-based checkpoint selection) gives a consistent gain of about +0.005 to +0.008 stratified
V1 on val and test, in two independent seed sets. It is adopted as part of the CG-Net training recipe for the EPCDS variant (candidate
contribution: training strategy against early memorisation of noisy self-reported labels). With EMA, EPCDS is no longer below EPC on
test (+0.0021 vs DEME).
