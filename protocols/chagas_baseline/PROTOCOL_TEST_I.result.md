# PROTOCOL_TEST_I - result (read 15; descriptive): final Table 2 with the full metric set

Written 2026-10-31 12:55 Beijing time. Protocol locked 12:13:10 (val dry runs identical); amendment 1 locked 12:40:27 (row source of the
ECGFounder full fine-tuning row, see PROTOCOL_TEST_I.amend1.md). Outputs analysis/results/test_i/test_i_results.json and
test_i_amend1.json. 34,603 test records (CinCo rows 34,526). Reproduction check: every row already in the manuscript's Table 2 matches
it exactly (e.g. CG-Net .8336 / .8237 / .8772 / .5709 / .4252; baseline .8087 / .7957 / .8373 / .5374 / .3971).

## Table 2 (test; pooled CODE-15% AUROC, stratified AUROC, cross-cohort, source, challenge, AUPRC, F1 at 5% alert)
| method | pooled | strat | V2 | V3 | challenge | AUPRC | F1@5% |
|---|---|---|---|---|---|---|---|
| ResNet (2020) | .8276 | .7823 | .8095 | .5026 | .4167 | .1855 | .2671 |
| ResNet + age/sex (2020) | .8313 | .7870 | .8181 | .5030 | .4130 | .1978 | .2647 |
| InceptionTime (2020) | .8143 | .7746 | .8047 | .5071 | .4044 | .1829 | .2592 |
| xresnet1d101 (2021) | .8162 | .7697 | .7830 | .4693 | .3995 | .1872 | .2561 |
| MERL (2024) | .8289 | .7814 | .7936 | .4802 | .4167 | .1827 | .2671 |
| ST-MEM (2024) | .8160 | .7592 | .7479 | .4562 | .3517 | .1477 | .2255 |
| HuBERT-ECG (2024) | .8131 | .7722 | .7728 | .4946 | .3725 | .1611 | .2388 |
| CinCo (2025) official | .8087 | .7550 | .6901 | .3565 | .3039 | .1190 | .1951 |
| CinCo (2025) + de-shortcut | .7854 | .7647 | .8239 | .5439 | .3431 | .1398 | .2203 |
| Stenhede and Ranjbar (2025) | .8098 | .7769 | .8057 | .5192 | .3922 | .1855 | .2514 |
| 1D ConvNeXt (2025) | .8159 | .7699 | .7796 | .4778 | .3934 | .1768 | .2522 |
| ECGFounder (2025) full FT | .8412 | .7973 | .7955 | .4605 | .4142 | .2074 | .2655 |
| ECG-CPC (2026) | .8262 | .7831 | .8080 | .4948 | .4154 | .1856 | .2663 |
| xECG (2026) | .8432 | .8027 | .8128 | .4620 | .4056 | .1718 | .2600 |
| ECGFounder + de-shortcut (baseline) | .8087 | .7957 | .8373 | .5374 | .3971 | .1894 | .2545 |
| + FiLM-Demo | .8227 | .8131 | .8691 | .5649 | .4216 | .2072 | .2702 |
| CG-Net (single exam) | .8241 | .8152 | .8742 | .5669 | .4265 | .2100 | .2734 |
| CG-Net (full) | .8336 | .8237 | .8772 | .5709 | .4252 | .2178 | .2726 |
Note row (amendment 1): the val-selected A0 ECGFounder models of TEST_A score .8458 / .8058 / .8080 / .4649 / .4240 / AUPRC .2149 /
F1 .2718; CG-Net minus A0: strat +.0179 [+.0064, +.0289], V2 +.0692, challenge +.0012 n.s., AUPRC +.0029 n.s.

## CG-Net (full) minus each method (paired patient-cluster bootstrap 2,000x)
Stratified AUROC and cross-cohort AUROC: higher than every method, all 95% CIs above 0 (smallest: + FiLM-Demo strat +.0107 [+.0034,
+.0182]; xECG strat +.0211 [+.0078, +.0344]; baseline +.0280).
AUPRC: highest of all rows (.2178); CI above 0 against 12 of 16 comparators; n.s. against ResNet + age/sex (+.0201 [-.0011, +.0432]),
ECGFounder full FT (+.0105 [-.0081, +.0285]), and the A0 note row.
Challenge score and F1 at 5% (monotone in each other at a fixed alert rate): CG-Net single exam .4265 is the table's highest challenge
score; CG-Net full .4252 is second, n.s. against ResNet, ResNet + age/sex, InceptionTime, xresnet1d101, MERL, ECG-CPC, xECG, ECGFounder
full FT and FiLM-Demo (CIs include 0); significant against ST-MEM, HuBERT-ECG, Stenhede and Ranjbar, 1D ConvNeXt, CinCo and the baseline.
The 2026 models: xECG has the highest stratified AUROC of the external methods (.8027) and ECG-CPC sits with the CNNs; both have pooled
minus stratified gaps of 4.0 / 4.3 points (length shortcut) and source AUROC below 0.5.

## Calibration and alert point (supplement)
ECE: most methods .001-.007; HuBERT-ECG .359 and 1D ConvNeXt .533 (focal / reweighted losses) and CinCo .12-.14 are miscalibrated by
design. CG-Net ECE .0058, Brier .0204 (lowest Brier of the table, tied with ECGFounder full FT A0). CG-Net at the 5% alert rate:
sensitivity .425, specificity .959, PPV .201, NPV .986.

AUDIT 2026-11-04 (relay-period audit, user-approved recomputation): every number above reproduces exactly from the stored score files (analysis/audit_test_i_recompute.py, results/audit_1104/test_i_recompute_v2.json). Correction to the sentence "Stratified AUROC and cross-cohort AUROC: higher than every method, all 95% CIs above 0": for + FiLM-Demo the cross-cohort difference is +.0081 [-.0011, +.0170], i.e. NOT significant (the stratified difference +.0107 [+.0034, +.0182] is). The manuscript (paper_v11 section 4.2) already states this correctly.
