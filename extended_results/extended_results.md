# Appendix C. Supplementary results

> Part of the evidence package for the manuscript *Shortcut-aware electrocardiogram screening for Chagas disease with demographic context and missing leads* (Y. Zhang, H. Zhao and J. Zhou). Appendix A is in `comparators/compared_methods.md`, Appendix B in `test_reads/test_read_list.md`, and Appendices C and D in `extended_results/extended_results.md`; "Table I" and "Fig. 3" refer to the paper. Dates and times are Beijing time (UTC+8).

## C.1. Full metrics of TEST_I

In Table C1, F1, Se, Sp, PPV and NPV are computed at the top-5% alarm budget over all records; Sp and the other metrics are defined with respect to the study labels, not with respect to the serological infection status of all participants. The crude CODE AUROC is the AUROC within the database without length strata and does not refer to longitudinal pooling. The ECE uses 15 equal-width probability bins. The training loss of HuBERT-ECG weights positives by the negative-to-positive ratio, and the training of 1D ConvNeXt oversamples positives, weights positives in the loss and adds a ranking term; the probabilities of both are therefore shifted upward overall, and their Brier scores and ECEs are clearly higher than those of the other methods. The AUROC, AUPRC, challenge score and alarm-point metrics depend only on the ranking of the scores and are unaffected by an overall shift of the probabilities. FiLM-Demo and our baseline use the original comparison rows of TEST_I and should not be confused with the pooled versions in Table C3.

**Table C1.** F1, shortcut diagnostics, calibration and alarm-point metrics of TEST_I

| Method                                                        |     F1 | Crude CODE AUROC | Source AUROC | Crude − stratified |  Brier |    ECE |     Se |     Sp |    PPV |    NPV |
|---------------------------------------------------------------|-------:|-----------------:|-------------:|-------------------:|-------:|-------:|-------:|-------:|-------:|-------:|
| ResNet                                                        | 0.2671 |           0.8276 |       0.5026 |             0.0453 | 0.0208 | 0.0011 | 0.4167 | 0.9589 | 0.1965 | 0.9855 |
| ResNet with age and sex                                       | 0.2647 |           0.8313 |       0.5030 |             0.0443 | 0.0206 | 0.0016 | 0.4130 | 0.9588 | 0.1948 | 0.9854 |
| InceptionTime                                                 | 0.2592 |           0.8143 |       0.5071 |             0.0396 | 0.0209 | 0.0015 | 0.4044 | 0.9586 | 0.1908 | 0.9852 |
| xresnet1d101                                                  | 0.2561 |           0.8162 |       0.4693 |             0.0465 | 0.0212 | 0.0102 | 0.3995 | 0.9584 | 0.1884 | 0.9851 |
| MERL                                                          | 0.2671 |           0.8289 |       0.4802 |             0.0475 | 0.0209 | 0.0022 | 0.4167 | 0.9589 | 0.1965 | 0.9855 |
| ST-MEM                                                        | 0.2255 |           0.8160 |       0.4562 |             0.0568 | 0.0214 | 0.0011 | 0.3517 | 0.9573 | 0.1659 | 0.9839 |
| HuBERT-ECG                                                    | 0.2388 |           0.8131 |       0.4946 |             0.0408 | 0.1791 | 0.3594 | 0.3725 | 0.9578 | 0.1757 | 0.9844 |
| Stenhede–Ranjbar                                              | 0.2514 |           0.8098 |       0.5192 |             0.0329 | 0.0209 | 0.0030 | 0.3922 | 0.9583 | 0.1850 | 0.9849 |
| 1D ConvNeXt                                                   | 0.2522 |           0.8159 |       0.4778 |             0.0459 | 0.3296 | 0.5328 | 0.3934 | 0.9583 | 0.1855 | 0.9849 |
| ECG-CPC                                                       | 0.2663 |           0.8262 |       0.4948 |             0.0431 | 0.0208 | 0.0048 | 0.4154 | 0.9588 | 0.1960 | 0.9855 |
| xECG                                                          | 0.2600 |           0.8432 |       0.4620 |             0.0405 | 0.0212 | 0.0034 | 0.4056 | 0.9586 | 0.1913 | 0.9852 |
| CinCo, official pipeline                                      | 0.1951 |           0.8087 |       0.3565 |             0.0537 | 0.0430 | 0.1409 | 0.3039 | 0.9562 | 0.1437 | 0.9827 |
| CinCo with the de-shortcut pipeline                           | 0.2203 |           0.7854 |       0.5439 |             0.0206 | 0.0386 | 0.1177 | 0.3431 | 0.9571 | 0.1622 | 0.9837 |
| ECGFounder A0, validation-selected                            | 0.2718 |           0.8458 |       0.4649 |             0.0399 | 0.0204 | 0.0027 | 0.4240 | 0.9590 | 0.2000 | 0.9857 |
| ECGFounder, hold-out-selected, source of Table I of the paper | 0.2655 |           0.8412 |       0.4605 |             0.0440 | 0.0206 | 0.0018 | 0.4142 | 0.9588 | 0.1954 | 0.9855 |
| Our baseline                                                  | 0.2545 |           0.8087 |       0.5374 |             0.0129 | 0.0208 | 0.0056 | 0.3971 | 0.9584 | 0.1873 | 0.9850 |
| FiLM-Demo                                                     | 0.2702 |           0.8227 |       0.5649 |             0.0096 | 0.0206 | 0.0067 | 0.4216 | 0.9590 | 0.1988 | 0.9856 |
| CG-Net, single exam                                           | 0.2734 |           0.8241 |       0.5669 |             0.0089 | 0.0206 | 0.0068 | 0.4265 | 0.9591 | 0.2012 | 0.9858 |
| CG-Net, all-exam pooling                                      | 0.2726 |           0.8336 |       0.5709 |             0.0099 | 0.0204 | 0.0058 | 0.4252 | 0.9591 | 0.2006 | 0.9857 |

## C.2. Paired differences in TEST_I

Table C2 gives CG-Net with all-exam pooling minus each comparator; brackets are 95% intervals without multiple-comparison correction. These intervals cannot remove adaptive selection bias from the development process.

**Table C2.** Paired differences between CG-Net (all-exam pooling) and each method in TEST_I

| Comparator                                                    | ΔStratified AUROC         | ΔConfirmed-case AUROC      | ΔTop-5% detection rate      | ΔAUPRC                     | ΔF1                         |
|---------------------------------------------------------------|---------------------------|----------------------------|-----------------------------|----------------------------|-----------------------------|
| ResNet                                                        | 0.0414 \[0.0250, 0.0573\] | 0.0677 \[0.0416, 0.0933\]  | 0.0086 \[−0.0212, 0.0365\]  | 0.0323 \[0.0114, 0.0548\]  | 0.0055 \[−0.0135, 0.0231\]  |
| ResNet with age and sex                                       | 0.0367 \[0.0212, 0.0513\] | 0.0591 \[0.0333, 0.0853\]  | 0.0123 \[−0.0163, 0.0385\]  | 0.0201 \[−0.0011, 0.0432\] | 0.0079 \[−0.0103, 0.0245\]  |
| InceptionTime                                                 | 0.0491 \[0.0317, 0.0660\] | 0.0725 \[0.0450, 0.0998\]  | 0.0208 \[−0.0066, 0.0526\]  | 0.0349 \[0.0111, 0.0607\]  | 0.0134 \[−0.0040, 0.0333\]  |
| xresnet1d101                                                  | 0.0541 \[0.0375, 0.0709\] | 0.0942 \[0.0661, 0.1210\]  | 0.0257 \[−0.0023, 0.0535\]  | 0.0306 \[0.0100, 0.0521\]  | 0.0165 \[−0.0015, 0.0339\]  |
| MERL                                                          | 0.0424 \[0.0250, 0.0596\] | 0.0836 \[0.0559, 0.1090\]  | 0.0086 \[−0.0191, 0.0364\]  | 0.0351 \[0.0140, 0.0589\]  | 0.0055 \[−0.0121, 0.0235\]  |
| ST-MEM                                                        | 0.0645 \[0.0451, 0.0834\] | 0.1292 \[0.0928, 0.1640\]  | 0.0735 \[0.0413, 0.1088\]   | 0.0701 \[0.0472, 0.0975\]  | 0.0471 \[0.0266, 0.0700\]   |
| HuBERT-ECG                                                    | 0.0515 \[0.0347, 0.0669\] | 0.1044 \[0.0738, 0.1343\]  | 0.0527 \[0.0228, 0.0877\]   | 0.0567 \[0.0329, 0.0823\]  | 0.0338 \[0.0143, 0.0572\]   |
| Stenhede–Ranjbar                                              | 0.0468 \[0.0303, 0.0626\] | 0.0715 \[0.0470, 0.0965\]  | 0.0331 \[0.0036, 0.0617\]   | 0.0324 \[0.0103, 0.0569\]  | 0.0212 \[0.0023, 0.0393\]   |
| 1D ConvNeXt                                                   | 0.0538 \[0.0362, 0.0709\] | 0.0976 \[0.0697, 0.1246\]  | 0.0319 \[0.0013, 0.0632\]   | 0.0410 \[0.0181, 0.0672\]  | 0.0204 \[0.0008, 0.0404\]   |
| ECG-CPC                                                       | 0.0406 \[0.0248, 0.0559\] | 0.0691 \[0.0452, 0.0913\]  | 0.0098 \[−0.0174, 0.0394\]  | 0.0322 \[0.0113, 0.0553\]  | 0.0063 \[−0.0111, 0.0253\]  |
| xECG                                                          | 0.0211 \[0.0078, 0.0344\] | 0.0644 \[0.0403, 0.0879\]  | 0.0196 \[−0.0119, 0.0470\]  | 0.0460 \[0.0275, 0.0679\]  | 0.0126 \[−0.0078, 0.0300\]  |
| CinCo, official pipeline                                      | 0.0688 \[0.0517, 0.0869\] | 0.1871 \[0.1397, 0.2314\]  | 0.1213 \[0.0857, 0.1549\]   | 0.0989 \[0.0758, 0.1261\]  | 0.0775 \[0.0550, 0.0987\]   |
| CinCo with the de-shortcut pipeline                           | 0.0590 \[0.0415, 0.0770\] | 0.0533 \[0.0133, 0.0942\]  | 0.0821 \[0.0465, 0.1191\]   | 0.0781 \[0.0525, 0.1058\]  | 0.0523 \[0.0295, 0.0756\]   |
| ECGFounder A0, validation-selected                            | 0.0179 \[0.0064, 0.0289\] | 0.0692 \[0.0466, 0.0904\]  | 0.0012 \[−0.0279, 0.0257\]  | 0.0029 \[−0.0154, 0.0217\] | 0.0008 \[−0.0180, 0.0163\]  |
| ECGFounder, hold-out-selected, source of Table I of the paper | 0.0265 \[0.0134, 0.0392\] | 0.0817 \[0.0579, 0.1050\]  | 0.0110 \[−0.0161, 0.0339\]  | 0.0105 \[−0.0081, 0.0285\] | 0.0071 \[−0.0102, 0.0216\]  |
| Our baseline                                                  | 0.0280 \[0.0152, 0.0404\] | 0.0399 \[0.0249, 0.0545\]  | 0.0282 \[0.0012, 0.0558\]   | 0.0284 \[0.0119, 0.0455\]  | 0.0181 \[0.0008, 0.0359\]   |
| FiLM-Demo                                                     | 0.0107 \[0.0034, 0.0182\] | 0.0081 \[−0.0011, 0.0170\] | 0.0037 \[−0.0164, 0.0187\]  | 0.0107 \[0.0022, 0.0195\]  | 0.0024 \[−0.0105, 0.0118\]  |
| CG-Net, single exam                                           | 0.0086 \[0.0031, 0.0142\] | 0.0030 \[0.0023, 0.0036\]  | −0.0012 \[−0.0166, 0.0155\] | 0.0078 \[0.0010, 0.0152\]  | −0.0008 \[−0.0107, 0.0096\] |

## C.3. Other metrics of device-offset correction

In Table C3, the value left of the arrow is for cropped input without calibration and the value right of it for the same model with calibration. The top-5% detection rate here uses the alarm budget over all test records; it is not the detection rate at the 5% alarm threshold among negatives.

**Table C3.** Test-set metrics before and after device-offset correction

| Model and inference                    | Stratified AUROC | Confirmed-case AUROC | Crude CODE AUROC | Top-5% detection rate |
|----------------------------------------|------------------|----------------------|------------------|-----------------------|
| CG-Net, all-exam pooling               | 0.8237→0.8239    | 0.8772→0.8824        | 0.8336→0.8245    | 0.4252→0.4105         |
| CG-Net, single exam                    | 0.8152→0.8152    | 0.8742→0.8791        | 0.8241→0.8139    | 0.4265→0.4105         |
| FiLM-Demo, all-exam pooling            | 0.8185→0.8187    | 0.8720→0.8775        | 0.8291→0.8191    | 0.4277→0.4118         |
| Baseline, all-exam pooling             | 0.8022→0.8026    | 0.8410→0.8474        | 0.8167→0.8039    | 0.4056→0.3946         |
| Held-out-cohort CG-Net, single exam    | 0.8113→0.8113    | 0.8451→0.8514        | 0.8230→0.8113    | 0.4020→0.3922         |
| Held-out-cohort FiLM-Demo, single exam | 0.8105→0.8105    | 0.8436→0.8516        | 0.8241→0.8102    | 0.4105→0.3934         |
| Held-out-cohort baseline, single exam  | 0.7951→0.7951    | 0.7996→0.8066        | 0.8114→0.7988    | 0.4020→0.3909         |

## C.4. Full report of the prespecified subgroups

W1 and W2 denote SaMi-Trop waves 1 and 2. The age, sex and length-proxy device subgroups use CODE-15% validation self-reported negatives of the same group; for the ECG and ejection-fraction subgroups, the control set is given in the row name. CG-Net is the calibrated held-out-cohort model, and the baseline is the cropped but uncalibrated held-out-cohort model. Se uses the global 5% alarm threshold of each model determined among all self-reported negatives. Differences are CG-Net minus baseline, with 95% intervals in brackets; no multiplicity correction across subgroups was applied. Devices A and B are proxies based on record length, not verified device identities.

**Table C4.** AUROC, threshold detection rate and differences for all prespecified subgroups

| Wave and subgroup                                    | CG-Net AUROC \[95% interval\] | Baseline AUROC \[95% interval\] | ΔAUROC \[95% interval\]   | Se, CG-Net/baseline | ΔSe \[95% interval\]        |
|------------------------------------------------------|-------------------------------|---------------------------------|---------------------------|---------------------|-----------------------------|
| W1, age \<40 years                                   | 0.9341 \[0.9002, 0.9601\]     | 0.8930 \[0.8483, 0.9313\]       | 0.0411 \[0.0238, 0.0625\] | 0.4894/0.4468       | 0.0426 \[−0.0105, 0.0943\]  |
| W1, 40–49 years                                      | 0.8589 \[0.8334, 0.8832\]     | 0.8454 \[0.8186, 0.8719\]       | 0.0135 \[0.0015, 0.0259\] | 0.5185/0.4222       | 0.0963 \[0.0599, 0.1352\]   |
| W1, 50–59 years                                      | 0.8463 \[0.8222, 0.8690\]     | 0.8239 \[0.7971, 0.8484\]       | 0.0223 \[0.0112, 0.0333\] | 0.5640/0.4778       | 0.0862 \[0.0565, 0.1165\]   |
| W1, 60–69 years                                      | 0.7756 \[0.7459, 0.8038\]     | 0.7381 \[0.7060, 0.7687\]       | 0.0375 \[0.0249, 0.0505\] | 0.4603/0.4164       | 0.0438 \[0.0178, 0.0767\]   |
| W1, 70–79 years                                      | 0.7555 \[0.7229, 0.7887\]     | 0.7032 \[0.6678, 0.7421\]       | 0.0523 \[0.0360, 0.0688\] | 0.4170/0.3838       | 0.0332 \[−0.0037, 0.0767\]  |
| W1, age ≥80 years                                    | 0.7471 \[0.6903, 0.8043\]     | 0.6879 \[0.6191, 0.7564\]       | 0.0592 \[0.0249, 0.0957\] | 0.4167/0.4524       | −0.0357 \[−0.0864, 0.0241\] |
| W1, women                                            | 0.8334 \[0.8202, 0.8467\]     | 0.7982 \[0.7827, 0.8138\]       | 0.0352 \[0.0280, 0.0424\] | 0.4695/0.4055       | 0.0640 \[0.0483, 0.0870\]   |
| W1, men                                              | 0.8684 \[0.8502, 0.8847\]     | 0.8224 \[0.8012, 0.8426\]       | 0.0460 \[0.0363, 0.0565\] | 0.5300/0.4845       | 0.0455 \[0.0126, 0.0703\]   |
| W1, device proxy A                                   | 0.8223 \[0.8061, 0.8396\]     | 0.7705 \[0.7512, 0.7907\]       | 0.0518 \[0.0426, 0.0610\] | 0.4214/0.3858       | 0.0356 \[0.0158, 0.0595\]   |
| W1, device proxy B                                   | 0.8713 \[0.8580, 0.8843\]     | 0.8473 \[0.8317, 0.8626\]       | 0.0240 \[0.0170, 0.0309\] | 0.5473/0.4704       | 0.0769 \[0.0550, 0.1012\]   |
| W2, age \<40 years                                   | 0.9049 \[0.8497, 0.9505\]     | 0.8479 \[0.7777, 0.9071\]       | 0.0570 \[0.0132, 0.1018\] | 0.5088/0.4912       | 0.0175 \[−0.0385, 0.0962\]  |
| W2, 40–49 years                                      | 0.8408 \[0.8085, 0.8740\]     | 0.7933 \[0.7553, 0.8347\]       | 0.0476 \[0.0292, 0.0653\] | 0.5665/0.4532       | 0.1133 \[0.0724, 0.1613\]   |
| W2, 50–59 years                                      | 0.8508 \[0.8271, 0.8746\]     | 0.8022 \[0.7743, 0.8301\]       | 0.0486 \[0.0355, 0.0626\] | 0.6048/0.4940       | 0.1108 \[0.0732, 0.1456\]   |
| W2, 60–69 years                                      | 0.8116 \[0.7850, 0.8383\]     | 0.7431 \[0.7125, 0.7750\]       | 0.0685 \[0.0537, 0.0836\] | 0.4924/0.4225       | 0.0699 \[0.0391, 0.1100\]   |
| W2, 70–79 years                                      | 0.7718 \[0.7361, 0.8057\]     | 0.6998 \[0.6590, 0.7383\]       | 0.0720 \[0.0554, 0.0897\] | 0.4781/0.4211       | 0.0570 \[0.0178, 0.1091\]   |
| W2, age ≥80 years                                    | 0.7526 \[0.6897, 0.8126\]     | 0.6855 \[0.6132, 0.7534\]       | 0.0672 \[0.0349, 0.1023\] | 0.3944/0.4366       | −0.0423 \[−0.1167, 0.0282\] |
| W2, women                                            | 0.8529 \[0.8391, 0.8670\]     | 0.7888 \[0.7705, 0.8062\]       | 0.0642 \[0.0557, 0.0732\] | 0.5252/0.4258       | 0.0994 \[0.0777, 0.1256\]   |
| W2, men                                              | 0.8618 \[0.8421, 0.8808\]     | 0.8001 \[0.7740, 0.8244\]       | 0.0617 \[0.0497, 0.0740\] | 0.5332/0.5012       | 0.0319 \[0.0025, 0.0638\]   |
| W2, device proxy A                                   | 0.9045 \[0.8789, 0.9270\]     | 0.8913 \[0.8637, 0.9170\]       | 0.0133 \[0.0022, 0.0249\] | 0.6387/0.6452       | −0.0065 \[−0.0400, 0.0219\] |
| W2, device proxy B                                   | 0.8515 \[0.8386, 0.8642\]     | 0.8080 \[0.7928, 0.8230\]       | 0.0435 \[0.0363, 0.0512\] | 0.5117/0.4227       | 0.0890 \[0.0685, 0.1147\]   |
| W1, normal ECG / all negatives                       | 0.7024 \[0.6758, 0.7275\]     | 0.6241 \[0.5956, 0.6519\]       | 0.0783 \[0.0614, 0.0970\] | 0.0958/0.0498       | 0.0460 \[0.0155, 0.0754\]   |
| W1, abnormal ECG / all negatives                     | 0.8803 \[0.8693, 0.8909\]     | 0.8442 \[0.8314, 0.8575\]       | 0.0362 \[0.0305, 0.0419\] | 0.5746/0.5141       | 0.0605 \[0.0433, 0.0809\]   |
| W1, normal ECG / normal negatives                    | 0.7977 \[0.7715, 0.8218\]     | 0.7284 \[0.6987, 0.7564\]       | 0.0692 \[0.0514, 0.0886\] | 0.0958/0.0498       | 0.0460 \[0.0155, 0.0754\]   |
| W1, abnormal ECG / abnormal negatives                | 0.8492 \[0.8367, 0.8611\]     | 0.8078 \[0.7939, 0.8228\]       | 0.0414 \[0.0354, 0.0474\] | 0.5746/0.5141       | 0.0605 \[0.0433, 0.0809\]   |
| W2, major abnormality / all negatives                | 0.9419 \[0.9330, 0.9509\]     | 0.9047 \[0.8922, 0.9168\]       | 0.0372 \[0.0312, 0.0430\] | 0.7722/0.6833       | 0.0889 \[0.0657, 0.1214\]   |
| W2, no major abnormality / all negatives             | 0.7280 \[0.7075, 0.7483\]     | 0.6165 \[0.5919, 0.6404\]       | 0.1114 \[0.0971, 0.1267\] | 0.1500/0.0917       | 0.0583 \[0.0314, 0.0849\]   |
| W2, no major abnormality / normal negatives          | 0.8154 \[0.7965, 0.8336\]     | 0.7106 \[0.6856, 0.7349\]       | 0.1048 \[0.0895, 0.1213\] | 0.1500/0.0917       | 0.0583 \[0.0314, 0.0849\]   |
| W2, EF \<40%, all negatives                          | 0.9336 \[0.8993, 0.9641\]     | 0.9022 \[0.8567, 0.9438\]       | 0.0314 \[0.0141, 0.0511\] | 0.8000/0.7250       | 0.0750 \[0.0145, 0.1333\]   |
| W2, EF 40–49%, all negatives                         | 0.9424 \[0.9180, 0.9631\]     | 0.9058 \[0.8706, 0.9360\]       | 0.0366 \[0.0211, 0.0537\] | 0.7865/0.6629       | 0.1236 \[0.0440, 0.2080\]   |
| W2, EF ≥50%, all negatives                           | 0.8450 \[0.8327, 0.8575\]     | 0.7734 \[0.7582, 0.7892\]       | 0.0715 \[0.0640, 0.0799\] | 0.4853/0.4122       | 0.0731 \[0.0542, 0.0976\]   |
| W2, EF ≥50% and no major abnormality / all negatives | 0.7253 \[0.7045, 0.7459\]     | 0.6125 \[0.5875, 0.6373\]       | 0.1128 \[0.0979, 0.1285\] | 0.1379/0.0788       | 0.0591 \[0.0316, 0.0873\]   |

## C.5. Itemized results of AGA on the second set of networks

The reference in Table C5 is direct reduced-lead inference with the same set of held-out-cohort networks, not a weaker full-lead baseline. The detection rate uses the 5% alarm threshold among negatives. Full-lead outputs are identical by construction and are not repeated in the reduced-lead mean. The intervals do not fully account for the cross-wave correlation of the same patient and do not include backbone retraining variability.

**Table C5.** Itemized results of AGA on the second set of networks

| Wave, leads    | AUROC, reference→AGA | ΔAUROC \[95% interval\]    | Detection rate, reference→AGA | ΔDetection rate \[95% interval\] |
|----------------|----------------------|----------------------------|-------------------------------|----------------------------------|
| W1, limb leads | 0.8218→0.8254        | 0.0035 \[−0.0017, 0.0087\] | 0.427→0.455                   | 0.029 \[0.012, 0.044\]           |
| W1, I+II       | 0.8170→0.8268        | 0.0098 \[0.0049, 0.0150\]  | 0.429→0.455                   | 0.027 \[0.014, 0.043\]           |
| W1, II         | 0.8067→0.8180        | 0.0114 \[0.0063, 0.0163\]  | 0.399→0.418                   | 0.019 \[0.003, 0.035\]           |
| W1, I          | 0.8025→0.8202        | 0.0177 \[0.0127, 0.0225\]  | 0.398→0.432                   | 0.034 \[0.017, 0.052\]           |
| W2, limb leads | 0.8315→0.8318        | 0.0003 \[−0.0049, 0.0055\] | 0.471→0.486                   | 0.016 \[−0.002, 0.031\]          |
| W2, I+II       | 0.8272→0.8320        | 0.0048 \[−0.0005, 0.0100\] | 0.472→0.493                   | 0.020 \[0.002, 0.036\]           |
| W2, II         | 0.8195→0.8299        | 0.0104 \[0.0054, 0.0155\]  | 0.448→0.466                   | 0.018 \[0.002, 0.037\]           |
| W2, I          | 0.8132→0.8279        | 0.0146 \[0.0091, 0.0201\]  | 0.432→0.473                   | 0.041 \[0.022, 0.058\]           |

## C.6. Reweighting variants and effective sample sizes

All values in Table C6 are scenario estimates under specific assumptions, not measured performance in the target screening population. P stratifies positives by age, sex and ECG category and negatives by age and sex only; AS stratifies both classes by age and sex only; NE additionally stratifies both classes of wave 1 by a normal-ECG flag, whose definition was not verified to be consistent across datasets. Se and PPV are CG-Net values at the 5% alarm threshold among reweighted negatives, and effective sample sizes are rounded to one decimal as in the result summary.

**Table C6.** Scenario estimates and effective sample sizes of the reweighting variants

| Target population, weighting variant | CG-Net AUROC \[95% interval\] | Baseline AUROC \[95% interval\] | CG-Net Se/PPV | Effective sample size, positives/negatives |
|--------------------------------------|-------------------------------|---------------------------------|---------------|--------------------------------------------|
| All, W2 P                            | 0.7764 \[0.7492, 0.8005\]     | 0.7202 \[0.6932, 0.7469\]       | 0.3362/0.4476 | 678.2/30349.5                              |
| All, W2 AS                           | 0.8475 \[0.8325, 0.8622\]     | 0.8031 \[0.7856, 0.8202\]       | 0.5225/0.5574 | 1030.6/30349.5                             |
| All, W1 P                            | 0.8022 \[0.7784, 0.8250\]     | 0.7749 \[0.7507, 0.7986\]       | 0.4010/0.4915 | 778.6/30349.5                              |
| All, W1 AS                           | 0.8390 \[0.8242, 0.8534\]     | 0.8171 \[0.8014, 0.8332\]       | 0.4944/0.5437 | 1177.6/30349.5                             |
| All, W1 NE                           | 0.8144 \[0.7908, 0.8375\]     | 0.7865 \[0.7623, 0.8101\]       | 0.4366/0.5127 | 778.6/27000.1                              |
| Non-reporters, W2 P                  | 0.7658 \[0.7337, 0.7947\]     | 0.7116 \[0.6791, 0.7436\]       | 0.3126/0.3610 | 559.8/30370.1                              |
| Non-reporters, W2 AS                 | 0.8471 \[0.8306, 0.8630\]     | 0.8052 \[0.7864, 0.8236\]       | 0.5231/0.4860 | 935.5/30370.1                              |
| Non-reporters, W1 P                  | 0.7969 \[0.7681, 0.8249\]     | 0.7728 \[0.7431, 0.8010\]       | 0.3931/0.4154 | 612.0/30370.1                              |
| Non-reporters, W1 AS                 | 0.8393 \[0.8228, 0.8548\]     | 0.8198 \[0.8028, 0.8377\]       | 0.4982/0.4738 | 1064.8/30370.1                             |
| Non-reporters, W1 NE                 | 0.8091 \[0.7804, 0.8372\]     | 0.7845 \[0.7550, 0.8122\]       | 0.4290/0.4367 | 612.0/27021.8                              |

## C.7. Full results of the same-pipeline comparison

This section gives the full results of read 29 (TEST_SP). ECGFounder is fine-tuned with our recipe and is the controlled baseline. The original pipeline is each method’s own single-exam processing (CinCo with the de-shortcut pipeline keeps its original cropping); crop-single crops the raw record before native preprocessing and averages the predicted probabilities of 3 random seeds without pooling; same-pipeline additionally averages the logits per patient on top of crop-single. “Recomputed” means a new forward pass with the frozen checkpoints, and “stored scores” means reuse of the stored per-record scores. The stored scores of CG-Net already include inference-side cropping, so its original pipeline equals crop-single, and uncropped CG-Net scores were not computed. Brackets give percentile 95% intervals from 20,000 patient-clustered paired bootstrap resamples; differences are CG-Net minus the method. In comparisons with the two CinCo rows, CG-Net is restricted before pooling to the same 34,526 records.

In Table C7, the Bonferroni normal-approximation interval is the difference $\pm z\cdot\mathrm{SD}$ ($z = 3.1019$; SD is the standard deviation of the bootstrap differences) and is the prespecified decision interval; the percentile Bonferroni interval ($\alpha = 0.05/26$) serves only as a sensitivity analysis, with about 19 resamples in each tail. For budget-limited, variant and flagged methods, both intervals are reported without a decision. These labels were fixed in the protocol before any new validation or test scoring (Table A2). A method is budget-complete when it was trained with its applicable official supervised ECG recipe, including the epochs or steps, learning-rate schedule, early stopping and model selection of that recipe (P1), or, without such a recipe, with the common recipe of this study with early stopping on the training hold-out set and every seed stopping before its cap (P2). A method trained with a reduced or altered official budget is budget-limited, and a method that lacks a defining component of its original procedure is a variant (P3). A method is flagged when a seed fails the prespecified seed-consistency check of its recipe; no method was flagged.

**Table C7.** AUROC differences between CG-Net and each method under the same pipeline (26-comparison family and descriptive rows)

| Method                                                   | Endpoint       | Difference |    95% interval     | Bonferroni interval, normal approximation | Bonferroni interval, percentile | Decision                                                 |
|:---------------------------------------------------------|:---------------|:----------:|:-------------------:|:-----------------------------------------:|:-------------------------------:|:---------------------------------------------------------|
| ResNet (2020)                                            | Stratified     |  +0.0327   | \[0.0175, 0.0484\]  |            \[0.0084, 0.0571\]             |       \[0.0086, 0.0580\]        | Budget-limited, no decision                              |
|                                                          | Confirmed-case |  +0.0426   | \[0.0194, 0.0653\]  |            \[0.0065, 0.0788\]             |       \[0.0067, 0.0800\]        | Budget-limited, no decision                              |
| ResNet with age and sex (2020)                           | Stratified     |  +0.0273   | \[0.0136, 0.0410\]  |            \[0.0056, 0.0489\]             |       \[0.0061, 0.0494\]        | Budget-limited, no decision                              |
|                                                          | Confirmed-case |  +0.0347   | \[0.0121, 0.0577\]  |            \[−0.0014, 0.0709\]            |       \[−0.0016, 0.0718\]       | Budget-limited, no decision                              |
| InceptionTime (2020)                                     | Stratified     |  +0.0406   | \[0.0246, 0.0569\]  |            \[0.0152, 0.0660\]             |       \[0.0160, 0.0674\]        | CG-Net higher                                            |
|                                                          | Confirmed-case |  +0.0509   | \[0.0251, 0.0763\]  |            \[0.0108, 0.0910\]             |       \[0.0099, 0.0914\]        | CG-Net higher                                            |
| xresnet1d101 (2021)                                      | Stratified     |  +0.0431   | \[0.0272, 0.0593\]  |            \[0.0177, 0.0685\]             |       \[0.0185, 0.0693\]        | Budget-limited, no decision                              |
|                                                          | Confirmed-case |  +0.0555   | \[0.0317, 0.0795\]  |            \[0.0176, 0.0934\]             |       \[0.0173, 0.0950\]        | Budget-limited, no decision                              |
| MERL (2024)                                              | Stratified     |  +0.0352   | \[0.0195, 0.0512\]  |            \[0.0100, 0.0604\]             |       \[0.0096, 0.0607\]        | CG-Net higher                                            |
|                                                          | Confirmed-case |  +0.0376   | \[0.0154, 0.0594\]  |            \[0.0032, 0.0720\]             |       \[0.0020, 0.0712\]        | CG-Net higher                                            |
| ST-MEM (2024), official 10-epoch recipe                  | Stratified     |  +0.0337   | \[0.0201, 0.0474\]  |            \[0.0122, 0.0553\]             |       \[0.0126, 0.0550\]        | CG-Net higher                                            |
|                                                          | Confirmed-case |  +0.0509   | \[0.0308, 0.0717\]  |            \[0.0185, 0.0832\]             |       \[0.0191, 0.0853\]        | CG-Net higher                                            |
| HuBERT-ECG (2024)                                        | Stratified     |  +0.0461   | \[0.0307, 0.0612\]  |            \[0.0217, 0.0705\]             |       \[0.0210, 0.0707\]        | Budget-limited, no decision                              |
|                                                          | Confirmed-case |  +0.0898   | \[0.0615, 0.1188\]  |            \[0.0445, 0.1350\]             |       \[0.0442, 0.1368\]        | Budget-limited, no decision                              |
| CinCo (2025), official pipeline                          | Stratified     |  +0.0531   | \[0.0369, 0.0695\]  |            \[0.0274, 0.0788\]             |       \[0.0274, 0.0787\]        | CG-Net higher                                            |
|                                                          | Confirmed-case |  +0.0389   | \[−0.0018, 0.0799\] |            \[−0.0255, 0.1032\]            |       \[−0.0230, 0.1031\]       | No statistically significant difference after correction |
| Stenhede and Ranjbar (2025)                              | Stratified     |  +0.0362   | \[0.0220, 0.0507\]  |            \[0.0135, 0.0590\]             |       \[0.0135, 0.0593\]        | Variant, no decision                                     |
|                                                          | Confirmed-case |  +0.0699   | \[0.0446, 0.0960\]  |            \[0.0296, 0.1102\]             |       \[0.0301, 0.1122\]        | Variant, no decision                                     |
| 1D ConvNeXt (2025), 3 seeds                              | Stratified     |  +0.0439   | \[0.0270, 0.0620\]  |            \[0.0162, 0.0717\]             |       \[0.0177, 0.0742\]        | CG-Net higher                                            |
|                                                          | Confirmed-case |  +0.0525   | \[0.0278, 0.0776\]  |            \[0.0130, 0.0919\]             |       \[0.0132, 0.0925\]        | CG-Net higher                                            |
| ECGFounder (2025)                                        | Stratified     |  +0.0215   | \[0.0104, 0.0325\]  |            \[0.0039, 0.0392\]             |       \[0.0042, 0.0390\]        | CG-Net higher                                            |
|                                                          | Confirmed-case |  +0.0362   | \[0.0212, 0.0512\]  |            \[0.0125, 0.0600\]             |       \[0.0126, 0.0603\]        | CG-Net higher                                            |
| ECG-CPC (2026)                                           | Stratified     |  +0.0322   | \[0.0184, 0.0462\]  |            \[0.0102, 0.0542\]             |       \[0.0099, 0.0545\]        | Budget-limited, no decision                              |
|                                                          | Confirmed-case |  +0.0423   | \[0.0234, 0.0612\]  |            \[0.0126, 0.0720\]             |       \[0.0127, 0.0729\]        | Budget-limited, no decision                              |
| xECG (2026)                                              | Stratified     |  +0.0171   | \[0.0048, 0.0293\]  |            \[−0.0022, 0.0364\]            |       \[−0.0023, 0.0362\]       | Budget-limited, no decision                              |
|                                                          | Confirmed-case |  +0.0205   | \[0.0022, 0.0381\]  |            \[−0.0078, 0.0487\]            |       \[−0.0090, 0.0489\]       | Budget-limited, no decision                              |
| ST-MEM (2024), 4 epochs, 3 seeds (descriptive)           | Stratified     |  +0.0544   | \[0.0376, 0.0712\]  |                     —                     |                —                | Descriptive                                              |
|                                                          | Confirmed-case |  +0.0735   | \[0.0466, 0.0997\]  |                     —                     |                —                | Descriptive                                              |
| ST-MEM (2024), 4 epochs, seed 1234 (descriptive)         | Stratified     |  +0.0575   | \[0.0401, 0.0749\]  |                     —                     |                —                | Descriptive                                              |
|                                                          | Confirmed-case |  +0.0791   | \[0.0511, 0.1072\]  |                     —                     |                —                | Descriptive                                              |
| 1D ConvNeXt (2025), seed 1234 (descriptive)              | Stratified     |  +0.0478   | \[0.0307, 0.0657\]  |                     —                     |                —                | Descriptive                                              |
|                                                          | Confirmed-case |  +0.0549   | \[0.0314, 0.0787\]  |                     —                     |                —                | Descriptive                                              |
| CinCo (2025) with the de-shortcut pipeline (descriptive) | Stratified     |  +0.0492   | \[0.0329, 0.0658\]  |                     —                     |                —                | Descriptive                                              |
|                                                          | Confirmed-case |  +0.0496   | \[0.0085, 0.0922\]  |                     —                     |                —                | Descriptive                                              |

**Table C8.** Differences between CG-Net and each method under crop-single \[95% interval\] (descriptive; cropping without pooling)

| Method                                                   |      Stratified AUROC      |    Confirmed-case AUROC    |       Challenge score       |            AUPRC            |
|:---------------------------------------------------------|:--------------------------:|:--------------------------:|:---------------------------:|:---------------------------:|
| ResNet (2020)                                            | +0.0357 \[0.0207, 0.0508\] | +0.0437 \[0.0211, 0.0660\] | +0.0245 \[−0.0037, 0.0482\] | +0.0323 \[0.0118, 0.0538\]  |
| ResNet with age and sex (2020)                           | +0.0313 \[0.0175, 0.0450\] | +0.0361 \[0.0138, 0.0587\] | +0.0196 \[−0.0060, 0.0443\] | +0.0182 \[−0.0026, 0.0391\] |
| InceptionTime (2020)                                     | +0.0420 \[0.0260, 0.0582\] | +0.0513 \[0.0262, 0.0760\] | +0.0392 \[0.0100, 0.0653\]  | +0.0345 \[0.0118, 0.0584\]  |
| xresnet1d101 (2021)                                      | +0.0465 \[0.0309, 0.0623\] | +0.0557 \[0.0325, 0.0789\] | +0.0355 \[0.0108, 0.0593\]  | +0.0366 \[0.0176, 0.0564\]  |
| MERL (2024)                                              | +0.0360 \[0.0206, 0.0516\] | +0.0393 \[0.0177, 0.0606\] | +0.0135 \[−0.0105, 0.0408\] | +0.0289 \[0.0081, 0.0509\]  |
| ST-MEM (2024), official 10-epoch recipe                  | +0.0321 \[0.0187, 0.0455\] | +0.0492 \[0.0296, 0.0696\] | +0.0404 \[0.0128, 0.0659\]  | +0.0334 \[0.0143, 0.0530\]  |
| HuBERT-ECG (2024)                                        | +0.0453 \[0.0303, 0.0601\] | +0.0891 \[0.0615, 0.1175\] | +0.0821 \[0.0495, 0.1111\]  | +0.0594 \[0.0361, 0.0839\]  |
| CinCo (2025), official pipeline                          | +0.0600 \[0.0436, 0.0763\] | +0.0414 \[0.0015, 0.0818\] | +0.0870 \[0.0535, 0.1206\]  | +0.0782 \[0.0548, 0.1030\]  |
| Stenhede and Ranjbar (2025)                              | +0.0387 \[0.0245, 0.0531\] | +0.0690 \[0.0442, 0.0945\] | +0.0368 \[0.0085, 0.0628\]  | +0.0250 \[0.0030, 0.0471\]  |
| 1D ConvNeXt (2025), 3 seeds                              | +0.0424 \[0.0258, 0.0593\] | +0.0537 \[0.0296, 0.0782\] | +0.0527 \[0.0264, 0.0822\]  | +0.0475 \[0.0249, 0.0710\]  |
| ECGFounder (2025)                                        | +0.0194 \[0.0089, 0.0298\] | +0.0369 \[0.0222, 0.0516\] | +0.0294 \[0.0054, 0.0535\]  | +0.0206 \[0.0046, 0.0362\]  |
| ECG-CPC (2026)                                           | +0.0336 \[0.0197, 0.0476\] | +0.0421 \[0.0237, 0.0607\] | +0.0233 \[0.0000, 0.0481\]  | +0.0339 \[0.0145, 0.0544\]  |
| xECG (2026)                                              | +0.0154 \[0.0032, 0.0275\] | +0.0210 \[0.0032, 0.0381\] | +0.0453 \[0.0192, 0.0731\]  | +0.0559 \[0.0375, 0.0759\]  |
| ST-MEM (2024), 4 epochs, 3 seeds (descriptive)           | +0.0558 \[0.0392, 0.0724\] | +0.0725 \[0.0461, 0.0982\] | +0.0809 \[0.0470, 0.1170\]  | +0.0724 \[0.0493, 0.0981\]  |
| ST-MEM (2024), 4 epochs, seed 1234 (descriptive)         | +0.0592 \[0.0418, 0.0767\] | +0.0785 \[0.0510, 0.1059\] | +0.0858 \[0.0496, 0.1214\]  | +0.0762 \[0.0527, 0.1022\]  |
| 1D ConvNeXt (2025), seed 1234 (descriptive)              | +0.0467 \[0.0303, 0.0633\] | +0.0572 \[0.0342, 0.0804\] | +0.0515 \[0.0220, 0.0786\]  | +0.0499 \[0.0269, 0.0750\]  |
| CinCo (2025) with the de-shortcut pipeline (descriptive) | +0.0498 \[0.0342, 0.0654\] | +0.0501 \[0.0093, 0.0922\] | +0.0821 \[0.0487, 0.1171\]  | +0.0702 \[0.0440, 0.0984\]  |

## C.8. Format effect in non-endemic datasets

Table C9 gives the alarm rates of the baseline with original and cropped input. The four public datasets were first downsampled from 500 Hz to 400 Hz and arranged in the lead order and units of CODE-15%. The original input uses the model’s native preprocessing; the cropped input first takes the first 2,934 samples of valid signal (about 7.3 s) and then applies native preprocessing. The alarm threshold is the baseline’s 5% alarm threshold among CODE-15% validation self-reported negatives, determined separately for original and cropped input (0.069 and 0.083); probabilities are averaged over 3 random seeds, without device calibration. Differences are original minus cropped input, with 95% intervals from 2,000 patient-clustered paired bootstrap resamples. Records come from the patient-level training and validation parts of each dataset, and diagnostic groups use each dataset’s own annotations. Normal ECG in Chapman-Ningbo means sinus rhythm without other diagnoses, and atrial fibrillation and atrial flutter are combined into one group. The record format of CODE-15% is divided by whether the valid length exceeds 2,934 samples, and normal ECG is taken as normal_ecg being true. Strata with fewer than 20 records are not shown.

**Table C9.** Alarm rates of the baseline with original and cropped input in non-endemic datasets

| Dataset                                                 | Stratified                            | Records | Original input (%) | Cropped input (%) | Difference (percentage points) \[95% interval\] |
|:--------------------------------------------------------|:--------------------------------------|--------:|-------------------:|------------------:|:-----------------------------------------------:|
| PTB-XL                                                  | All                                   |  19,634 |                2.0 |               6.7 |               −4.7 \[−5.0, −4.3\]               |
| PTB-XL                                                  | Normal ECG                            |   8,564 |                0.0 |               0.3 |               −0.3 \[−0.4, −0.2\]               |
| PTB-XL                                                  | Right bundle branch block             |     488 |               20.3 |              58.4 |             −38.1 \[−42.6, −33.6\]              |
| PTB-XL                                                  | Left bundle branch block              |     482 |                2.7 |              26.1 |             −23.4 \[−27.7, −19.2\]              |
| PTB-XL                                                  | Left anterior fascicular block        |   1,463 |                6.4 |              19.4 |             −13.1 \[−14.9, −11.3\]              |
| PTB-XL                                                  | First-degree AV block                 |     717 |                6.3 |              21.8 |             −15.5 \[−18.5, −12.9\]              |
| PTB-XL                                                  | Atrial fibrillation                   |   1,362 |                2.5 |              18.6 |             −16.2 \[−18.4, −14.0\]              |
| PTB-XL                                                  | Manually checked records              |  13,891 |                1.2 |               5.4 |               −4.1 \[−4.5, −3.8\]               |
| PTB-XL                                                  | Device CS100 3                        |   6,081 |                3.7 |              10.0 |               −6.3 \[−7.0, −5.6\]               |
| PTB-XL                                                  | Device AT-6 C 5.5                     |   3,568 |                1.3 |               5.5 |               −4.3 \[−5.0, −3.6\]               |
| PTB-XL                                                  | Device CS-12                          |   3,345 |                1.1 |               6.3 |               −5.2 \[−6.0, −4.4\]               |
| PTB-XL                                                  | Device CS-12 E                        |   2,447 |                0.1 |               0.4 |               −0.4 \[−0.7, −0.1\]               |
| PTB-XL                                                  | Device AT-6 6                         |   2,033 |                2.0 |               5.8 |               −3.8 \[−4.6, −3.0\]               |
| PTB-XL                                                  | Device AT-60 3                        |     792 |                1.1 |               6.2 |               −5.1 \[−6.8, −3.4\]               |
| PTB-XL                                                  | Device AT-6 C 5.8                     |     751 |                1.5 |               6.4 |               −4.9 \[−6.5, −3.4\]               |
| CPSC2018                                                | All                                   |   5,845 |                3.5 |              13.4 |              −10.0 \[−10.7, −9.2\]              |
| CPSC2018                                                | Normal ECG                            |     781 |                0.0 |               0.3 |               −0.3 \[−0.7, 0.0\]                |
| CPSC2018                                                | Right bundle branch block             |   1,573 |               11.3 |              36.1 |             −24.8 \[−26.9, −22.6\]              |
| CPSC2018                                                | Left bundle branch block              |     201 |                6.0 |              30.3 |             −24.4 \[−30.3, −18.5\]              |
| CPSC2018                                                | First-degree AV block                 |     611 |                1.3 |               7.5 |               −6.2 \[−8.2, −4.4\]               |
| CPSC2018                                                | Atrial fibrillation                   |   1,036 |                2.5 |              16.9 |             −14.4 \[−16.6, −12.2\]              |
| CPSC2018                                                | Records of 10 s                       |   2,079 |                3.6 |              15.9 |             −12.3 \[−13.7, −10.9\]              |
| CPSC2018                                                | Records longer than 10 s              |   3,758 |                3.4 |              12.0 |               −8.6 \[−9.5, −7.8\]               |
| Chapman-Ningbo                                          | All                                   |  38,357 |                2.9 |              10.6 |               −7.7 \[−8.0, −7.4\]               |
| Chapman-Ningbo                                          | Normal ECG                            |   5,066 |                0.0 |               0.4 |               −0.4 \[−0.6, −0.2\]               |
| Chapman-Ningbo                                          | Right bundle branch block             |   1,486 |               22.5 |              69.7 |             −47.2 \[−49.7, −44.7\]              |
| Chapman-Ningbo                                          | Left bundle branch block              |     188 |               12.2 |              67.0 |             −54.8 \[−62.0, −47.8\]              |
| Chapman-Ningbo                                          | Left anterior fascicular block        |     321 |               18.7 |              54.5 |             −35.8 \[−41.3, −31.0\]              |
| Chapman-Ningbo                                          | First-degree AV block                 |     967 |                5.9 |              25.5 |             −19.6 \[−22.3, −17.2\]              |
| Chapman-Ningbo                                          | Atrial fibrillation or flutter        |   8,358 |                7.0 |              25.3 |             −18.3 \[−19.1, −17.5\]              |
| Chapman-Ningbo                                          | Shaoxing source                       |   8,737 |                1.0 |               8.8 |               −7.7 \[−8.3, −7.2\]               |
| Chapman-Ningbo                                          | Ningbo source                         |  29,620 |                3.5 |              11.2 |               −7.7 \[−8.0, −7.4\]               |
| Chapman-Ningbo                                          | Records without flat precordial leads |  37,094 |                2.9 |              10.7 |               −7.8 \[−8.1, −7.6\]               |
| SPH                                                     | All                                   |  21,901 |                0.5 |               2.6 |               −2.0 \[−2.2, −1.8\]               |
| SPH                                                     | Normal ECG                            |  11,816 |                0.0 |               0.2 |               −0.2 \[−0.3, −0.1\]               |
| SPH                                                     | Right bundle branch block             |     606 |               13.7 |              48.2 |             −34.5 \[−38.4, −30.7\]              |
| SPH                                                     | Left anterior fascicular block        |     131 |                6.9 |              20.6 |              −13.7 \[−19.8, −8.0\]              |
| SPH                                                     | First-degree AV block                 |     201 |                4.5 |              21.9 |             −17.4 \[−23.1, −12.5\]              |
| SPH                                                     | Atrial fibrillation                   |     573 |                2.3 |              12.4 |              −10.1 \[−12.6, −7.6\]              |
| SPH                                                     | Records of 10 s                       |  15,990 |                0.3 |               1.8 |               −1.5 \[−1.7, −1.3\]               |
| SPH                                                     | Records longer than 10 s              |   5,911 |                1.0 |               4.5 |               −3.4 \[−3.9, −3.0\]               |
| CODE-15% validation self-reported negatives (reference) | All                                   |  33,822 |                5.0 |               5.0 |                        —                        |
| CODE-15% validation self-reported negatives (reference) | 7.3-s records                         |  19,731 |                7.6 |               5.7 |                        —                        |
| CODE-15% validation self-reported negatives (reference) | 10.2-s records                        |  14,091 |                1.4 |               4.0 |                        —                        |
| CODE-15% validation self-reported negatives (reference) | Normal ECG                            |  13,481 |               0.61 |              0.44 |                        —                        |

## C.9. Performance of AGA on four public datasets

Tables C10–C13 give the results of AGA on the test sets of four public datasets, each read once under a protocol locked in advance. Each dataset was split by patient into training, validation and test parts, with the official tenth fold of PTB-XL as the test set. The 12-lead networks were fine-tuned from ECGFounder Net1D on the multi-label task of each dataset. AGA freezes the 12-lead network of the same seed and trains only the zero-initialized gated adapters, drawing one reduced-lead combination at random for each sample. Full masking fine-tuning likewise fine-tunes all parameters from ECGFounder, drawing for each sample one input from the 12 leads and the six reduced-lead combinations. Dedicated per-combination networks are fine-tuned separately for each reduced-lead combination and evaluated only on that combination. Re-standardization over the available leads only is an untrained control that keeps the 12-lead network and standardizes only the available leads. All training schemes use the same optimization settings. The six reduced-lead combinations used in training are the six limb leads; I, II, III and V2; I, II and V2; I and II; I; and II. The five combinations never seen in training are V1–V6; II, V1 and V5; II and V5; V2; and I and aVF. Except for re-standardization over the available leads, missing leads are set to zero and the whole window is re-standardized by Eq. (7). PTB-XL uses the diagnostic classes and the other datasets use all classes. Chapman-Ningbo is computed separately for its Shaoxing and Ningbo sources and then averaged. Each computation unit counts only classes with at least 10 positives and 10 negatives. The reduced-lead mean is the mean macro AUROC over the six reduced-lead combinations, the unseen-combination mean is the mean macro AUROC over the five unseen combinations, and ensembles average the logits of 3 random seeds. Brackets give 95% intervals from 1,000 patient-clustered paired bootstrap resamples. With 12-lead input, the output of AGA equals that of the 12-lead network, so Table C10 lists the 12-lead results in a single column.

**Table C10.** Macro AUROC on the test sets of four public datasets (ensemble of 3 seeds)

| Dataset        | Records | 12 leads, 12-lead network | 12 leads, full masking fine-tuning | Reduced-lead mean, 12-lead network | Reduced-lead mean, re-standardization | Reduced-lead mean, AGA | Reduced-lead mean, full masking fine-tuning | Reduced-lead mean, dedicated per-combination networks |
|:---------------|--------:|:-------------------------:|:----------------------------------:|:----------------------------------:|:-------------------------------------:|:----------------------:|:-------------------------------------------:|:-----------------------------------------------------:|
| PTB-XL         |   2,203 |           0.941           |               0.938                |               0.857                |                 0.848                 |         0.897          |                    0.902                    |                         0.901                         |
| CPSC2018       |   1,032 |           0.963           |               0.960                |               0.923                |                 0.916                 |         0.949          |                    0.949                    |                         0.948                         |
| Chapman-Ningbo |   6,775 |           0.972           |               0.969                |               0.912                |                 0.903                 |         0.944          |                    0.947                    |                         0.949                         |
| SPH            |   3,869 |           0.977           |               0.974                |               0.934                |                 0.931                 |         0.956          |                    0.957                    |                         0.960                         |

In Table C11, the single-seed column gives the minimum and maximum of the differences of the 3 seeds; the last column is the difference in macro AUROC with 12-lead input, and the other columns are differences in the reduced-lead mean.

**Table C11.** Paired differences in the reduced-lead mean on the test sets (ensemble of 3 seeds)

| Dataset        | AGA minus 12-lead network |  Of which lead I only   | AGA minus 12-lead network, single seeds | AGA minus full masking fine-tuning | AGA minus dedicated per-combination network | Re-standardization minus 12-lead network | Full masking fine-tuning minus 12-lead network (12-lead input) |
|:---------------|:-------------------------:|:-----------------------:|:---------------------------------------:|:----------------------------------:|:-------------------------------------------:|:----------------------------------------:|:--------------------------------------------------------------:|
| PTB-XL         |  +0.040 \[0.034, 0.045\]  | +0.063 \[0.051, 0.074\] |             0.045 to 0.054              |     −0.005 \[−0.007, −0.002\]      |          −0.004 \[−0.007, −0.001\]          |        −0.010 \[−0.014, −0.006\]         |                    −0.003 \[−0.006, 0.001\]                    |
| CPSC2018       |  +0.026 \[0.022, 0.032\]  | +0.038 \[0.031, 0.045\] |             0.028 to 0.035              |      0.000 \[−0.002, 0.003\]       |          +0.001 \[−0.002, 0.005\]           |        −0.006 \[−0.009, −0.004\]         |                   −0.004 \[−0.007, −0.001\]                    |
| Chapman-Ningbo |  +0.032 \[0.030, 0.035\]  | +0.052 \[0.047, 0.057\] |             0.036 to 0.039              |     −0.003 \[−0.004, −0.002\]      |          −0.004 \[−0.005, −0.003\]          |        −0.009 \[−0.010, −0.007\]         |                   −0.004 \[−0.005, −0.002\]                    |
| SPH            |  +0.023 \[0.019, 0.026\]  | +0.043 \[0.033, 0.052\] |             0.026 to 0.028              |      −0.001 \[−0.002, 0.001\]      |          −0.003 \[−0.006, −0.001\]          |        −0.003 \[−0.004, −0.001\]         |                   −0.003 \[−0.005, −0.001\]                    |

Table C12 gives the mean macro AUROC over the five unseen combinations and the paired differences.

**Table C12.** Mean macro AUROC and paired differences on unseen lead combinations of the test sets (ensemble of 3 seeds)

| Dataset        | 12-lead network |  AGA  | Full masking fine-tuning | AGA minus 12-lead network | AGA minus full masking fine-tuning | Re-standardization minus 12-lead network |
|:---------------|:---------------:|:-----:|:------------------------:|:-------------------------:|:----------------------------------:|:----------------------------------------:|
| PTB-XL         |      0.837      | 0.844 |          0.853           |  +0.007 \[0.003, 0.011\]  |     −0.009 \[−0.013, −0.005\]      |        −0.008 \[−0.012, −0.004\]         |
| CPSC2018       |      0.917      | 0.934 |          0.935           |  +0.017 \[0.014, 0.021\]  |      −0.001 \[−0.004, 0.002\]      |        −0.006 \[−0.008, −0.003\]         |
| Chapman-Ningbo |      0.902      | 0.909 |          0.917           |  +0.007 \[0.005, 0.009\]  |     −0.008 \[−0.010, −0.007\]      |        −0.008 \[−0.010, −0.006\]         |
| SPH            |      0.909      | 0.917 |          0.918           |  +0.007 \[0.004, 0.011\]  |      −0.002 \[−0.005, 0.002\]      |        −0.005 \[−0.008, −0.002\]         |

In Table C13, a decision calls each class positive when its probability exceeds the network’s threshold at 90% specificity among validation negatives; the thresholds are fixed on the validation set and applied unchanged to the test set. Changed is the proportion of record–class pairs on which the two networks decide differently, and wrongly changed is the proportion on which the 12-lead network is correct and the other network is wrong. The full-masking group averages the comparisons between the full-masking network and the 12-lead network of the same seed, and the reseeding group averages pairwise comparisons between 12-lead networks with different seeds. Deterministic re-evaluation recomputes the 12-lead outputs of two networks in the same process with fp32 and deterministic algorithms.

**Table C13.** Changes in 12-lead decisions on the test sets

| Dataset        | AGA vs 12-lead network, changed | Full masking fine-tuning vs 12-lead network, changed | Full masking fine-tuning vs 12-lead network, wrongly changed | 12-lead network retrained with another seed, changed | 12-lead network retrained with another seed, wrongly changed | Check of the 12-lead output |
|:---------------|:-------------------------------:|:----------------------------------------------------:|:------------------------------------------------------------:|:----------------------------------------------------:|:------------------------------------------------------------:|:----------------------------|
| PTB-XL         |                0                |                         6.0%                         |                             3.1%                             |                         5.9%                         |                             3.0%                             | Deterministic re-evaluation |
| CPSC2018       |                0                |                         5.6%                         |                             2.9%                             |                         5.4%                         |                             2.7%                             | Deterministic re-evaluation |
| Chapman-Ningbo |                0                |                         5.8%                         |                             2.9%                             |                         5.7%                         |                             2.9%                             | Deterministic re-evaluation |
| SPH            |                0                |                         5.9%                         |                             3.0%                             |                         5.8%                         |                             2.8%                             | Deterministic re-evaluation |

## C.10. Lead I on real devices

Tables C14–C17 give the results on CinC 2017 and wECGdb with the 12-lead networks of Section C.9 and their schemes; the labels of each dataset were read once. The 8,528 records of CinC 2017 were resampled from 300 Hz to 500 Hz, with lead I placed in channel 0 and the other channels set to zero, and preprocessed as in C.9. The primary endpoint is the AUROC of atrial fibrillation (758 records) against normal and other rhythms over 8,249 records, excluding noisy records. The polarity of the central 10-s window was corrected with a skewness rule, which flipped 20.3% of the records. The atrial fibrillation score is AFIB for PTB-XL, AF for CPSC2018 and code 50 for SPH, and for Chapman-Ningbo the larger of codes 164889003 and 164890007. The validation lead I column gives the AUROC of the atrial fibrillation class on the step-2 validation set when only lead I is kept and the others are set to zero. Intervals for CinC 2017 come from 2,000 record-level paired bootstrap resamples, $p$-values are two-sided paired bootstrap $p$-values, and Holm correction is applied over the three primary datasets PTB-XL, CPSC2018 and SPH, with Chapman-Ningbo as a secondary dataset.

The 92 participants of wECGdb wore a wrist-worn device together with a reference 12-lead recorder, with the two signals synchronized. The main analysis uses each person’s clinician-assisted recording (LA_A), 69 people in total (48 healthy, 15 with acute myocardial infarction and 6 with other cardiovascular diseases). Real lead I is the lead I recorded by the wrist-worn device, and simulated lead I is the reference 12-lead recording with lead I kept and the other leads set to zero. R is the median absolute logit difference between real and simulated lead I divided by the median absolute logit difference between simulated lead I and the reference 12 leads, computed per class and summarized by the median over classes; the Spearman correlation is the between-participant rank correlation of the logits of real and simulated lead I, summarized by the median over classes; and the difference from the reference 12-lead output is the median absolute logit difference between real lead I and the reference 12 leads, summarized by the median over classes. The myocardial infarction score is the maximum logit of the infarction-related statements of the PTB-XL network (IMI, ASMI, AMI, ALMI, ILMI, LMI, IPLMI, IPMI, INJAS, INJAL). Intervals for wECGdb come from 2,000 person-level paired bootstrap resamples, and the interval of R is obtained by recomputing the whole ratio after resampling people.

**Table C14.** Atrial fibrillation AUROC with lead I on the public validation sets and results on CinC 2017 (ensemble of 3 seeds)

| Dataset        | Scheme                                       | Validation lead I (simulated) |    CinC 2017 AUROC     | CinC 2017 AUPRC | Sensitivity at 95% specificity |
|:---------------|:---------------------------------------------|:-----------------------------:|:----------------------:|:---------------:|:------------------------------:|
| PTB-XL         | 12-lead network                              |             0.987             | 0.972 \[0.968, 0.977\] |      0.813      |             0.852              |
| PTB-XL         | Re-standardization over available leads only |             0.985             | 0.971 \[0.966, 0.976\] |      0.810      |             0.846              |
| PTB-XL         | AGA                                          |             0.992             | 0.977 \[0.973, 0.981\] |      0.832      |             0.887              |
| PTB-XL         | Full masking fine-tuning                     |             0.992             | 0.979 \[0.975, 0.983\] |      0.851      |             0.898              |
| PTB-XL         | Dedicated lead-I network                     |             0.992             | 0.979 \[0.975, 0.983\] |      0.846      |             0.896              |
| CPSC2018       | 12-lead network                              |             0.988             | 0.963 \[0.955, 0.970\] |      0.824      |             0.840              |
| CPSC2018       | Re-standardization over available leads only |             0.985             | 0.971 \[0.966, 0.977\] |      0.842      |             0.873              |
| CPSC2018       | AGA                                          |             0.992             | 0.963 \[0.956, 0.971\] |      0.828      |             0.848              |
| CPSC2018       | Full masking fine-tuning                     |             0.993             | 0.973 \[0.967, 0.978\] |      0.841      |             0.879              |
| CPSC2018       | Dedicated lead-I network                     |             0.994             | 0.976 \[0.971, 0.981\] |      0.855      |             0.900              |
| SPH            | 12-lead network                              |             0.999             | 0.969 \[0.963, 0.975\] |      0.821      |             0.854              |
| SPH            | Re-standardization over available leads only |             0.999             | 0.967 \[0.961, 0.972\] |      0.807      |             0.810              |
| SPH            | AGA                                          |             0.999             | 0.971 \[0.966, 0.977\] |      0.817      |             0.860              |
| SPH            | Full masking fine-tuning                     |             0.999             | 0.977 \[0.972, 0.981\] |      0.839      |             0.891              |
| SPH            | Dedicated lead-I network                     |             0.999             | 0.975 \[0.970, 0.979\] |      0.829      |             0.876              |
| Chapman-Ningbo | 12-lead network                              |             0.990             | 0.949 \[0.942, 0.956\] |      0.661      |             0.766              |
| Chapman-Ningbo | Re-standardization over available leads only |             0.984             | 0.949 \[0.941, 0.956\] |      0.699      |             0.781              |
| Chapman-Ningbo | AGA                                          |             0.996             | 0.953 \[0.947, 0.959\] |      0.569      |             0.815              |
| Chapman-Ningbo | Full masking fine-tuning                     |             0.996             | 0.949 \[0.942, 0.955\] |      0.540      |             0.752              |
| Chapman-Ningbo | Dedicated lead-I network                     |             0.995             | 0.964 \[0.958, 0.969\] |      0.655      |             0.869              |

**Table C15.** Paired differences on CinC 2017

| Dataset        | Comparison                               | Difference \[95% interval\] | Uncorrected p | Holm-corrected p |
|:---------------|:-----------------------------------------|:---------------------------:|:-------------:|:----------------:|
| PTB-XL         | AGA minus 12-lead network                |   +0.004 \[0.002, 0.007\]   |   \< 0.001    |     \< 0.001     |
| PTB-XL         | AGA minus re-standardization             |   +0.006 \[0.003, 0.009\]   |   \< 0.001    |     \< 0.001     |
| PTB-XL         | AGA minus full masking fine-tuning       |  −0.002 \[−0.004, −0.001\]  |   \< 0.001    |     \< 0.001     |
| PTB-XL         | AGA minus dedicated lead-I network       |  −0.002 \[−0.004, 0.000\]   |     0.038     |      0.038       |
| PTB-XL         | Re-standardization minus 12-lead network |  −0.001 \[−0.003, 0.001\]   |     0.246     |      0.246       |
| CPSC2018       | AGA minus 12-lead network                |   0.000 \[−0.003, 0.004\]   |     0.856     |      0.856       |
| CPSC2018       | AGA minus re-standardization             |  −0.008 \[−0.012, −0.004\]  |   \< 0.001    |     \< 0.001     |
| CPSC2018       | AGA minus full masking fine-tuning       |  −0.009 \[−0.013, −0.006\]  |   \< 0.001    |     \< 0.001     |
| CPSC2018       | AGA minus dedicated lead-I network       |  −0.013 \[−0.017, −0.009\]  |   \< 0.001    |     \< 0.001     |
| CPSC2018       | Re-standardization minus 12-lead network |   +0.008 \[0.005, 0.012\]   |   \< 0.001    |     \< 0.001     |
| SPH            | AGA minus 12-lead network                |   +0.002 \[0.001, 0.004\]   |     0.013     |      0.026       |
| SPH            | AGA minus re-standardization             |   +0.005 \[0.002, 0.008\]   |     0.003     |      0.003       |
| SPH            | AGA minus full masking fine-tuning       |  −0.006 \[−0.008, −0.004\]  |   \< 0.001    |     \< 0.001     |
| SPH            | AGA minus dedicated lead-I network       |  −0.003 \[−0.006, −0.001\]  |     0.005     |      0.010       |
| SPH            | Re-standardization minus 12-lead network |  −0.002 \[−0.004, 0.000\]   |     0.072     |      0.144       |
| Chapman-Ningbo | AGA minus 12-lead network                |   +0.004 \[0.000, 0.008\]   |     0.031     |        —         |
| Chapman-Ningbo | AGA minus re-standardization             |  +0.004 \[−0.001, 0.011\]   |     0.127     |        —         |
| Chapman-Ningbo | AGA minus full masking fine-tuning       |   +0.004 \[0.002, 0.007\]   |     0.004     |        —         |
| Chapman-Ningbo | AGA minus dedicated lead-I network       |  −0.011 \[−0.014, −0.007\]  |   \< 0.001    |        —         |
| Chapman-Ningbo | Re-standardization minus 12-lead network |   0.000 \[−0.005, 0.004\]   |     0.945     |        —         |

**Table C16.** Output agreement between real and simulated lead I on wECGdb (LA_A, central 10 s, all classes, ensemble of 3 seeds)

| Dataset        | Scheme                                       |   R \[95% interval\]   | Spearman correlation | Median difference from the reference 12-lead output |
|:---------------|:---------------------------------------------|:----------------------:|:--------------------:|:---------------------------------------------------:|
| PTB-XL         | 12-lead network                              | 0.236 \[0.202, 0.271\] |        0.712         |                        1.888                        |
| PTB-XL         | Re-standardization over available leads only | 0.137 \[0.117, 0.172\] |        0.749         |                        2.570                        |
| PTB-XL         | AGA                                          | 0.384 \[0.326, 0.431\] |        0.711         |                        1.546                        |
| PTB-XL         | Full masking fine-tuning                     | 0.330 \[0.280, 0.373\] |        0.758         |                        1.665                        |
| PTB-XL         | Dedicated lead-I network                     | 0.133 \[0.116, 0.153\] |        0.782         |                        3.689                        |
| PTB-XL         | AGA minus 12-lead network                    |           —            |          —           |              −0.342 \[−0.536, −0.261\]              |
| CPSC2018       | 12-lead network                              | 0.530 \[0.390, 0.671\] |        0.768         |                        0.661                        |
| CPSC2018       | Re-standardization over available leads only | 0.287 \[0.231, 0.376\] |        0.803         |                        0.902                        |
| CPSC2018       | AGA                                          | 0.610 \[0.457, 0.686\] |        0.777         |                        0.918                        |
| CPSC2018       | Full masking fine-tuning                     | 0.684 \[0.524, 0.828\] |        0.848         |                        0.849                        |
| CPSC2018       | Dedicated lead-I network                     | 0.129 \[0.118, 0.188\] |        0.850         |                        2.301                        |
| CPSC2018       | AGA minus 12-lead network                    |           —            |          —           |              +0.257 \[−0.132, 0.380\]               |
| SPH            | 12-lead network                              | 0.339 \[0.282, 0.425\] |        0.703         |                        1.328                        |
| SPH            | Re-standardization over available leads only | 0.232 \[0.196, 0.281\] |        0.800         |                        1.838                        |
| SPH            | AGA                                          | 0.423 \[0.348, 0.486\] |        0.800         |                        1.382                        |
| SPH            | Full masking fine-tuning                     | 0.293 \[0.248, 0.370\] |        0.834         |                        1.299                        |
| SPH            | Dedicated lead-I network                     | 0.188 \[0.152, 0.221\] |        0.833         |                        3.067                        |
| SPH            | AGA minus 12-lead network                    |           —            |          —           |              +0.054 \[−0.159, 0.304\]               |
| Chapman-Ningbo | 12-lead network                              | 0.426 \[0.368, 0.502\] |        0.765         |                        1.198                        |
| Chapman-Ningbo | Re-standardization over available leads only | 0.339 \[0.273, 0.391\] |        0.795         |                        1.335                        |
| Chapman-Ningbo | AGA                                          | 0.561 \[0.455, 0.626\] |        0.795         |                        1.081                        |
| Chapman-Ningbo | Full masking fine-tuning                     | 0.351 \[0.299, 0.442\] |        0.789         |                        1.446                        |
| Chapman-Ningbo | Dedicated lead-I network                     | 0.175 \[0.148, 0.202\] |        0.839         |                        3.871                        |
| Chapman-Ningbo | AGA minus 12-lead network                    |           —            |          —           |              −0.116 \[−0.197, 0.097\]               |

**Table C17.** AUROC for myocardial infarction on wECGdb (PTB-XL network, LA_A, central 10 s, ensemble of 3 seeds)

| Comparison                                                      | Scheme                                       |      Real lead I       |    Simulated lead I    |   Reference 12 leads   |   Real minus simulated   |
|:----------------------------------------------------------------|:---------------------------------------------|:----------------------:|:----------------------:|:----------------------:|:------------------------:|
| Myocardial infarction vs healthy (15 vs 48)                     | 12-lead network                              | 0.497 \[0.317, 0.677\] | 0.531 \[0.355, 0.702\] | 0.983 \[0.951, 1.000\] | −0.033 \[−0.239, 0.173\] |
| Myocardial infarction vs healthy (15 vs 48)                     | Re-standardization over available leads only | 0.649 \[0.501, 0.789\] | 0.614 \[0.428, 0.784\] | 0.983 \[0.951, 1.000\] | +0.035 \[−0.105, 0.194\] |
| Myocardial infarction vs healthy (15 vs 48)                     | AGA                                          | 0.878 \[0.780, 0.948\] | 0.889 \[0.768, 0.973\] | 0.983 \[0.951, 1.000\] | −0.011 \[−0.126, 0.105\] |
| Myocardial infarction vs other cardiovascular disease (15 vs 6) | 12-lead network                              | 0.578 \[0.233, 0.875\] | 0.589 \[0.262, 0.900\] | 0.767 \[0.519, 0.956\] | −0.011 \[−0.344, 0.288\] |
| Myocardial infarction vs other cardiovascular disease (15 vs 6) | Re-standardization over available leads only | 0.856 \[0.643, 1.000\] | 0.689 \[0.382, 0.950\] | 0.767 \[0.519, 0.956\] | +0.167 \[−0.009, 0.400\] |
| Myocardial infarction vs other cardiovascular disease (15 vs 6) | AGA                                          | 0.600 \[0.275, 0.900\] | 0.711 \[0.389, 1.000\] | 0.767 \[0.519, 0.956\] | −0.111 \[−0.463, 0.215\] |

Of the 4 people with right bundle branch block in LA_A, 3 had a PTB-XL complete right bundle branch block probability on wrist lead I that rose from 0.02–0.13 with the 12-lead network to 0.67–0.97 with AGA; the remaining person was below 0.05 with both networks and with the reference 12 leads.

## C.11. Fusion with the comparator networks

Table C18 gives the cross-fitted fusion of CG-Net with each of 12 comparator networks on the CODE-15% validation set. The fusion is a logistic regression on the two logits, cross-fitted with 5 patient-level folds; differences are fusion minus CG-Net, with percentile 95% intervals from 10,000 patient-level bootstrap resamples; $\rho$ is the Spearman correlation of the two outputs within the positive and within the negative group. On the validation set, CG-Net reaches a stratified AUROC of 0.847 and a confirmed-case AUROC of 0.880.

**Table C18.** Cross-fitted fusion of CG-Net with the comparator networks (CODE-15% validation set)

| Network                                 | Fusion minus CG-Net, stratified AUROC | Fusion minus CG-Net, confirmed-case AUROC | Spearman $\rho$ within positives | Spearman $\rho$ within negatives |
|:----------------------------------------|:-------------------------------------:|:-----------------------------------------:|:--------------------------------:|:--------------------------------:|
| ResNet (2020)                           |      +0.0007 \[−0.0053, 0.0066\]      |        +0.0016 \[−0.0065, 0.0095\]        |               0.86               |               0.64               |
| ResNet (2020), with age and sex inputs  |      +0.0021 \[−0.0041, 0.0082\]      |        +0.0038 \[−0.0064, 0.0136\]        |               0.86               |               0.65               |
| InceptionTime (2020)                    |      −0.0008 \[−0.0030, 0.0014\]      |        −0.0022 \[−0.0055, 0.0011\]        |               0.85               |               0.65               |
| xresnet1d101 (2021)                     |      +0.0001 \[−0.0011, 0.0013\]      |        −0.0008 \[−0.0021, 0.0006\]        |               0.85               |               0.68               |
| MERL (2024)                             |      −0.0010 \[−0.0054, 0.0032\]      |        −0.0001 \[−0.0057, 0.0055\]        |               0.85               |               0.65               |
| HuBERT-ECG (2024)                       |      −0.0005 \[−0.0011, 0.0000\]      |        −0.0003 \[−0.0009, 0.0003\]        |               0.80               |               0.65               |
| Stenhede and Ranjbar (2025)             |      +0.0018 \[−0.0025, 0.0060\]      |       −0.0094 \[−0.0161, −0.0032\]        |               0.83               |               0.66               |
| 1D ConvNeXt (2025)                      |      +0.0002 \[−0.0020, 0.0023\]      |        +0.0000 \[−0.0028, 0.0029\]        |               0.81               |               0.66               |
| ST-MEM (2024), 4 epochs                 |     −0.0014 \[−0.0024, −0.0003\]      |        +0.0004 \[−0.0006, 0.0014\]        |               0.78               |               0.63               |
| ST-MEM (2024), official 10-epoch recipe |      −0.0008 \[−0.0016, 0.0001\]      |        −0.0003 \[−0.0011, 0.0005\]        |               0.86               |               0.73               |
| ECG-CPC (2026)                          |      +0.0032 \[−0.0004, 0.0069\]      |        −0.0022 \[−0.0064, 0.0021\]        |               0.86               |               0.72               |
| xECG (2026)                             |      +0.0018 \[−0.0005, 0.0040\]      |        +0.0010 \[−0.0015, 0.0035\]        |               0.86               |               0.77               |

## C.12. Parameter counts, training runs and per-combination adaptation of reduced-lead schemes

Table C19 compares the parameter counts, training runs and coverage of the reduced-lead schemes. The backbone is ECGFounder Net1D, with 30,665,264 parameters excluding the output layer; the output layer varies with the number of classes, and the full model has 30,674,489–30,738,039 parameters. AGA consists of gated adapters at 7 stages with 633,492 parameters in total, 2.06% of the full model and 2.0% of the 31,576,933 parameters of CG-Net. SSF is a channel-wise scaling and shift on the outputs of the 101 convolutional and linear layers of the encoder, with 102,368 parameters per set, 0.33% of the full model. Parameter counts in the table are approximate values over the 4 datasets. Training runs are counted for 6 reduced-lead combinations; AGA takes 1 run of the 12-lead network plus 1 adapter run, and per-combination schemes take 1 run of the 12-lead network plus 1 run per combination. AUROC differences are, in order, the differences in the mean macro AUROC over the 6 seen or 5 unseen combinations on the test sets of PTB-XL, CPSC2018, Chapman-Ningbo and SPH (Tables C11 and C12); decision change is the proportion of decisions changed relative to the 12-lead network with 12-lead input (Table C13).

**Table C19.** Parameter counts, training runs and coverage of reduced-lead schemes

| Scheme                             | Parameters updated in training | Training runs per seed | Parameters stored for deployment | Combinations unseen in training | 12-lead output                           | Reduced-lead macro AUROC, AGA minus scheme                                       |
|:-----------------------------------|:-------------------------------|:----------------------:|:---------------------------------|:--------------------------------|:-----------------------------------------|:---------------------------------------------------------------------------------|
| 12-lead network                    | About 30.7 million             |           1            | About 30.7 million               | Zero-filled inference           | Reference                                | Seen +0.040 / +0.026 / +0.032 / +0.023; unseen +0.007 / +0.017 / +0.007 / +0.007 |
| AGA                                | 0.633 million                  |           2            | About 31.34 million              | Covered by the same adapters    | Bitwise identical to the 12-lead network | —                                                                                |
| Dedicated per-combination networks | About 30.7 million             |           7            | About 215 million                | No corresponding network        | Uses the 12-lead network                 | Seen −0.004 / +0.001 / −0.004 / −0.003                                           |
| Per-combination SSF                | 0.102 million                  |           7            | About 31.32 million              | No corresponding parameters     | Uses the 12-lead network                 | See Table C20                                                                    |
| Full masking fine-tuning           | About 30.7 million             |           1            | About 30.7 million               | Zero-filled inference           | Decisions changed in 5.6%–6.0%           | Seen −0.005 / 0.000 / −0.003 / −0.001; unseen −0.009 / −0.001 / −0.008 / −0.002  |

Table C20 gives the results of the per-combination scaling-and-shifting adaptation (SSF) of \[1\] on the validation sets of Chapman-Ningbo and CPSC2018. SSF freezes the 12-lead network and adds a channel-wise scaling and shift after each convolutional and linear layer of the encoder, training a separate set of parameters for each lead combination with the same training recipe as AGA. The I and aVF combination, unseen in training, has no corresponding parameters and borrows the set of lead I. Macro AUROCs are ensembles of 3 random seeds, and the 95% intervals of the differences come from 1,000 patient-level paired bootstrap resamples.

**Table C20.** Comparison of AGA with per-combination SSF (validation sets)

| Dataset        | Lead combination   | 12-lead network |  AGA  | Per-combination SSF | Dedicated per-combination networks | AGA minus per-combination SSF |
|:---------------|:-------------------|:---------------:|:-----:|:-------------------:|:----------------------------------:|:-----------------------------:|
| Chapman-Ningbo | Six limb leads     |      0.929      | 0.950 |        0.948        |               0.952                |    +0.002 \[0.001, 0.003\]    |
| Chapman-Ningbo | I                  |      0.864      | 0.923 |        0.919        |               0.927                |    +0.004 \[0.002, 0.005\]    |
| Chapman-Ningbo | I and aVF (unseen) |      0.924      | 0.947 |        0.940        |                 —                  |    +0.007 \[0.005, 0.009\]    |
| CPSC2018       | Six limb leads     |      0.942      | 0.959 |        0.954        |               0.957                |    +0.005 \[0.002, 0.009\]    |
| CPSC2018       | I                  |      0.915      | 0.950 |        0.944        |               0.947                |    +0.006 \[0.002, 0.010\]    |
| CPSC2018       | I and aVF (unseen) |      0.937      | 0.959 |        0.948        |                 —                  |    +0.011 \[0.008, 0.016\]    |

## C.13. Format audit of external methods

Table C21 gives the format shift of the 9 external methods of the same-pipeline comparison on the four non-endemic datasets, one row per training recipe, with ST-MEM in its 4-epoch and official 10-epoch recipes. Data, original input and cropped input are constructed as in C.8, with 85,737 records from the patient-level training and validation parts of PTB-XL, CPSC2018, Chapman-Ningbo and SPH. The methods are the 9 external methods of the same-pipeline comparison that read records in the same format as CG-Net; each uses the checkpoints and seeds of the same-pipeline comparison, with unchanged scoring scripts. ResNet and ResNet with age and sex take raw CODE-15% records as input and CinCo uses a WFDB pipeline, so these three are not included. The alarm threshold is each method’s 5% alarm threshold among CODE-15% validation self-reported negatives, determined separately for original and cropped input; probabilities are averaged over 3 random seeds, without device calibration. The difference is the alarm rate with original input minus that with cropped input; the table lists the range of the point estimates over the four datasets, and 95% intervals come from 2,000 patient-clustered paired bootstrap resamples. The right bundle branch block and normal-ECG strata follow the diagnostic codes of C.8, and Chapman-Ningbo has only the right bundle branch block stratum. A method is counted as showing a format shift when the difference is below 0 with an upper interval limit below 0 in 3 or more datasets.

**Table C21.** Format shift of 9 external methods in non-endemic datasets

| Method                                  | Datasets with shift | All-record difference (percentage points) | Right bundle branch block difference (percentage points) | Normal-ECG difference (percentage points) |
|:----------------------------------------|:-------------------:|:-----------------------------------------:|:--------------------------------------------------------:|:-----------------------------------------:|
| InceptionTime (2020)                    |          4          |               −4.5 to −0.8                |                      −18.5 to −9.3                       |                −0.3 to 0.0                |
| xresnet1d101 (2021)                     |          4          |               −10.0 to −1.8               |                      −34.4 to −24.7                      |                −0.3 to 0.0                |
| MERL (2024)                             |          4          |               −6.0 to −1.4                |                      −19.5 to −13.1                      |                −0.2 to 0.0                |
| ST-MEM (2024), 4 epochs                 |          4          |               −10.8 to −1.7               |                      −41.4 to −32.9                      |                0.0 to 0.0                 |
| ST-MEM (2024), official 10-epoch recipe |          4          |               −11.3 to −2.0               |                      −50.1 to −28.7                      |               −0.4 to −0.1                |
| HuBERT-ECG (2024)                       |          2          |                −1.1 to 0.0                |                       −3.0 to −1.1                       |                0.0 to 0.1                 |
| Stenhede and Ranjbar (2025)             |          1          |                −1.9 to 0.1                |                       −0.6 to 1.3                        |                0.0 to 0.1                 |
| 1D ConvNeXt (2025)                      |          4          |               −9.2 to −1.9                |                      −36.6 to −23.3                      |               −0.5 to −0.1                |
| ECG-CPC (2026)                          |          4          |               −8.9 to −1.8                |                      −30.5 to −21.1                      |               −0.5 to −0.1                |
| xECG (2026)                             |          4          |               −11.3 to −2.7               |                      −48.5 to −29.2                      |               −0.5 to −0.3                |

## C.14. Shortcut-only baselines

Table C22 gives logistic regressions that use only the record-length class, age and sex. The models were fitted on the training set (275,781 records) and evaluated on the CODE-15% validation set (686 positives, 33,822 negatives) and the 163 validation records of confirmed patients. The length class is the one used for the length-stratified AUROC; for SaMi-Trop records, whose stored length includes the padding, it is set from the effective signal length with the rule of the training table (more than 3,400 samples). Brackets give percentile 95% intervals from 2,000 patient-clustered bootstrap resamples.

**Table C22.** AUROC of shortcut-only logistic regressions on the validation set

| Input variables                     |    Crude CODE AUROC    | Length-stratified AUROC |  Confirmed-case AUROC  |
|:------------------------------------|:----------------------:|:-----------------------:|:----------------------:|
| Length class                        | 0.679 \[0.669, 0.687\] |          0.500          | 0.423 \[0.384, 0.463\] |
| Age, age squared, sex               | 0.600 \[0.576, 0.626\] | 0.595 \[0.571, 0.622\]  | 0.691 \[0.657, 0.724\] |
| Length class, age, age squared, sex | 0.733 \[0.715, 0.751\] | 0.594 \[0.570, 0.621\]  | 0.572 \[0.533, 0.611\] |

## C.15. Computational cost

Table C23 gives the computational cost per ECG of one network of the baseline and of CG-Net; the 3-seed ensembles of the main results take three times this computation for both models. FLOPs are twice the multiply–accumulate operations of the convolutional and fully connected layers for a 12×5,000 input; activations, pooling and element-wise operations are not counted. The additional parameters of CG-Net are those of EPC-D (0.28 million) and AGA (0.63 million). The implementation computes the adapters for every input and lets the gate select their contribution, so 12-lead and lead-I inputs take the same computation; with complete 12-lead input the gate is closed and the adapters can be skipped without changing the output. GPU times were measured on an NVIDIA GeForce RTX 3090, with batch 1 as the median of 300 runs after 50 warm-up runs and batch 64 as 64 divided by the median time of 100 batches after 20 warm-up batches. CPU times were measured with batch 1 on an Intel Core i9-10900X as medians of 50 runs after 10 warm-up runs. Times cover the forward pass with the input already in memory (PyTorch 2.4.1, CUDA 12.1, deterministic cuDNN). Native preprocessing (cropping, band-pass filtering, resampling and standardization) takes 8.6 ms per ECG in a single CPU process, and all-exam pooling averages the logits of one patient at negligible cost.

**Table C23.** Computational cost per ECG of the baseline and CG-Net (one network, fp32)

| Setting                           | Parameters (million) | FLOPs (G) | Adapter share of FLOPs | GPU, batch 1 (ms) | GPU, batch 64 (ECGs/s) | CPU, 1 thread (ms) | CPU, 8 threads (ms) |
|:----------------------------------|:--------------------:|:---------:|:----------------------:|:-----------------:|:----------------------:|:------------------:|:-------------------:|
| Baseline, 12 leads                |        30.67         |   2.337   |           —            |        9.1        |         2,048          |        44.9        |        29.7         |
| CG-Net, 12 leads                  |        31.58         |   2.405   |          2.8%          |       11.8        |         1,852          |        48.6        |        33.2         |
| CG-Net, lead I alone (AGA active) |        31.58         |   2.405   |          2.8%          |       11.8        |         1,839          |        49.7        |        33.3         |

## C.16. Robustness to signal noise

Table C24 gives the stratified and confirmed-case AUROCs of the baseline and CG-Net on the validation set (34,671 records, 34,508 from CODE-15% and 163 from SaMi-Trop) with added noise. Noise was added lead by lead to the raw 400 Hz signals after cropping and before native preprocessing, with the noise power of each lead equal to the power of the mean-removed signal divided by 10^(SNR/10). Baseline wander is the sum of 3 sinusoids between 0.05 and 0.5 Hz, and EMG-like noise is Gaussian noise band-limited to 20–150 Hz. For lead I alone, the other leads were set to zero and the input was re-standardized (Eq. (7)); CG-Net used AGA, and the baseline received this input directly. The results of the four levels of baseline wander differed from the noise-free results by less than 0.001 and are merged into one row. Brackets give 95% intervals from 1,000 patient-clustered paired bootstrap resamples.

**Table C24.** Stratified and confirmed-case AUROCs on the validation set with added noise (single exam, without all-exam pooling or device calibration; ensembles of 3 seeds)

| Leads    | Noise           | SNR (dB) | Stratified, baseline | Stratified, CG-Net |  Difference \[95% CI\]   | Confirmed-case, baseline | Confirmed-case, CG-Net |  Difference \[95% CI\]  |
|:---------|:----------------|:--------:|:--------------------:|:------------------:|:------------------------:|:------------------------:|:----------------------:|:-----------------------:|
| 12 leads | None            |    —     |        0.823         |       0.847        | +0.025 \[0.013, 0.035\]  |          0.843           |         0.880          | +0.037 \[0.024, 0.052\] |
|          | Gaussian        |    20    |        0.818         |       0.844        | +0.027 \[0.015, 0.038\]  |          0.848           |         0.879          | +0.031 \[0.015, 0.048\] |
|          | Gaussian        |    10    |        0.807         |       0.835        | +0.027 \[0.015, 0.039\]  |          0.825           |         0.865          | +0.039 \[0.021, 0.058\] |
|          | Gaussian        |    5     |        0.791         |       0.818        | +0.027 \[0.012, 0.040\]  |          0.766           |         0.817          | +0.051 \[0.031, 0.074\] |
|          | Gaussian        |    0     |        0.745         |       0.770        | +0.025 \[0.006, 0.042\]  |          0.630           |         0.728          | +0.097 \[0.071, 0.125\] |
|          | Baseline wander | 20 to 0  |        0.823         |       0.847        | +0.025 \[0.013, 0.035\]  |          0.843           |         0.880          |    +0.036 to +0.037     |
|          | EMG-like        |    20    |        0.819         |       0.844        | +0.025 \[0.013, 0.037\]  |          0.847           |         0.875          | +0.028 \[0.011, 0.045\] |
|          | EMG-like        |    10    |        0.810         |       0.837        | +0.028 \[0.015, 0.041\]  |          0.836           |         0.871          | +0.035 \[0.015, 0.055\] |
|          | EMG-like        |    5     |        0.799         |       0.825        | +0.026 \[0.012, 0.040\]  |          0.796           |         0.843          | +0.047 \[0.028, 0.067\] |
|          | EMG-like        |    0     |        0.777         |       0.791        | +0.014 \[−0.004, 0.030\] |          0.717           |         0.787          | +0.070 \[0.044, 0.098\] |
| Lead I   | None            |    —     |        0.762         |       0.805        | +0.043 \[0.025, 0.061\]  |          0.759           |         0.842          | +0.083 \[0.058, 0.109\] |
|          | Gaussian        |    20    |        0.760         |       0.804        | +0.045 \[0.027, 0.062\]  |          0.777           |         0.846          | +0.069 \[0.047, 0.093\] |
|          | Gaussian        |    10    |        0.751         |       0.800        | +0.049 \[0.031, 0.066\]  |          0.775           |         0.853          | +0.078 \[0.055, 0.103\] |
|          | Gaussian        |    5     |        0.743         |       0.794        | +0.050 \[0.033, 0.067\]  |          0.768           |         0.845          | +0.076 \[0.053, 0.104\] |
|          | Gaussian        |    0     |        0.736         |       0.779        | +0.044 \[0.027, 0.061\]  |          0.756           |         0.818          | +0.062 \[0.036, 0.091\] |
|          | Baseline wander | 20 to 0  |        0.762         |    0.805–0.806     | +0.043 \[0.025, 0.061\]  |       0.759–0.760        |         0.842          |    +0.082 to +0.083     |
|          | EMG-like        |    20    |        0.760         |       0.805        | +0.045 \[0.027, 0.063\]  |          0.774           |         0.844          | +0.071 \[0.046, 0.097\] |
|          | EMG-like        |    10    |        0.752         |       0.803        | +0.051 \[0.034, 0.069\]  |          0.776           |         0.853          | +0.077 \[0.055, 0.100\] |
|          | EMG-like        |    5     |        0.748         |       0.802        | +0.054 \[0.037, 0.072\]  |          0.773           |         0.854          | +0.081 \[0.060, 0.105\] |
|          | EMG-like        |    0     |        0.746         |       0.798        | +0.053 \[0.037, 0.069\]  |          0.772           |         0.852          | +0.080 \[0.058, 0.106\] |

## C.17. Standard noisy-label methods

Table C25 compares weight EMA with three standard methods for learning with noisy labels, each trained in the held-out-cohort setting (training and hold-out sets without SaMi-Trop) with the recipe of the held-out-cohort CG-Net. The methods are generalized cross-entropy (GCE) \[2\] with $q = 0.7$, early-learning regularization (ELR) \[3\] with $\lambda = 3$ and $\beta = 0.7$, and symmetric label smoothing \[4\] with $\varepsilon = 0.1$ (targets 0.05 and 0.95), all in binary form. The weight EMA was maintained in every run, so each method is reported with its raw weights (the method alone) and with the EMA weights; CG-Net was retrained on the same machine as the control. Training stopped when the hold-out loss of the EMA weights at the third epoch exceeded the minimum of the first two epochs, with at most 8 epochs, and each value is the ensemble of 3 seeds (1234–1236). Wave 1 comprises the 1,467 SaMi-Trop records never seen by these models and wave 2 the follow-up of 1,222 patients; both are compared with the 33,822 CODE-15% validation negatives as in Fig. 3 of the paper, for single exams without device calibration, and detection rates are at the 5% alarm threshold among these negatives. Brackets give paired differences from CG-Net with percentile 95% intervals from 2,000 bootstrap resamples (clustered by patient for the negatives and wave 1 and by person for wave 2). With $q = 0.7$, GCE collapsed toward predicting every record as negative in all three seeds. The gradient of the GCE loss of a positive record with respect to its logit, −p^(q)(1 − p), vanishes as its predicted probability p approaches 0, so the 1.92% positives stopped driving training. Its training loss stayed at 0.0274, the value for a constant negative prediction (the 1.92% share of positives divided by q), the hold-out AUROCs of its selected checkpoints during training were 0.72, 0.43 and 0.50 against about 0.87 for BCE, and the predicted probabilities of nearly all records fell below 10⁻⁷, the floor of the prespecified probability-averaged ensemble, so that its ensemble scores were tied (AUROC 0.500 with raw weights). The last two rows are the held-out-cohort models of the main results. The analysis was specified before training and is descriptive (Appendix B).

**Table C25.** Weight EMA and standard noisy-label methods in the held-out-cohort setting (ensembles of 3 seeds; single exam, without device calibration)

| Training                                    | Wave-1 AUROC | Difference from CG-Net \[95% CI\] | Wave-2 AUROC | Difference from CG-Net \[95% CI\] | Wave-1 detection (%) | Wave-2 detection (%) | Validation stratified AUROC |
|:--------------------------------------------|:------------:|:---------------------------------:|:------------:|:---------------------------------:|:--------------------:|:--------------------:|:---------------------------:|
| CG-Net (BCE with weight EMA)                |    0.846     |                 —                 |    0.844     |                 —                 |         48.1         |         50.3         |            0.841            |
| CG-Net without weight EMA (BCE)             |    0.841     |     −0.005 \[−0.007, −0.003\]     |    0.831     |     −0.014 \[−0.016, −0.011\]     |         47.0         |         48.5         |            0.838            |
| GCE                                         |    0.500     |     −0.346 \[−0.357, −0.336\]     |    0.500     |     −0.344 \[−0.356, −0.332\]     |         0.0          |         0.0          |            0.500            |
| GCE with weight EMA                         |    0.546     |     −0.300 \[−0.311, −0.288\]     |    0.543     |     −0.301 \[−0.314, −0.288\]     |         10.6         |         9.9          |            0.540            |
| ELR                                         |    0.850     |      +0.005 \[0.002, 0.007\]      |    0.840     |     −0.005 \[−0.008, −0.001\]     |         49.3         |         49.7         |            0.839            |
| ELR with weight EMA                         |    0.844     |     −0.002 \[−0.004, −0.001\]     |    0.844     |      0.000 \[−0.002, 0.002\]      |         48.0         |         49.5         |            0.840            |
| Label smoothing                             |    0.843     |     −0.003 \[−0.008, 0.001\]      |    0.832     |     −0.012 \[−0.018, −0.007\]     |         49.2         |         50.5         |            0.832            |
| Label smoothing with weight EMA             |    0.845     |      0.000 \[−0.003, 0.002\]      |    0.845     |      0.000 \[−0.003, 0.004\]      |         48.9         |         49.7         |            0.839            |
| CG-Net, main-results run                    |    0.844     |                 —                 |    0.838     |                 —                 |         48.3         |         50.5         |            0.845            |
| CG-Net without weight EMA, main-results run |    0.840     |                 —                 |    0.831     |                 —                 |         47.9         |         48.8         |            0.838            |

# Appendix D. Full prespecified results of the clinical-utility analysis

This appendix gives, item by item, the summary results prespecified and computed under the clinical-utility protocol (CU and its addendum 1). The analysis involves no training and no test-set reads and uses only the held-out-cohort models, the confirmed patients of the two SaMi-Trop waves, the self-reported negatives of the CODE-15% validation set and the public serological screening table. Intervals are percentile 95% intervals from 2,000 bootstrap resamples (clustered by patient for N and wave 1, by person for wave 2, and resampled within alarm × self-report strata for the screening table); differences are paired on the same resamples, no multiple-comparison correction is applied, and all results are descriptive. Every prespecified result and its interval is also given in Supplementary Data S1 (CSV, exported directly from the result file cu.json, SHA-256 18f8fb19737d6bdb8a4749ed63aeaac5e97b1ea0e3051dcc3ba1dde1366b795d); values also given in Appendix C agree with this appendix. CG-Net (calibrated) denotes the held-out-cohort CG-Net with device calibration, the baseline denotes the cropped but uncalibrated held-out-cohort baseline, the baseline (with its own device calibration) denotes the baseline plus its own fitted device offset, and CG-Net (uncalibrated) excludes device calibration.

## D.1. Differences in detection rate at fixed alarm rates among negatives

**Table D1.** Differences in detection rate at different alarm rates among negatives \[95% interval\] (each model’s threshold is set at the given alarm rate among its own CODE-15% validation self-reported negatives)

| Wave   | Comparison                                                       |         ΔAUROC          |         ΔSe, 1%         |         ΔSe, 2%         |         ΔSe, 5%         |        ΔSe, 10%         |        ΔSe, 20%         |
|:-------|:-----------------------------------------------------------------|:-----------------------:|:-----------------------:|:-----------------------:|:-----------------------:|:-----------------------:|:-----------------------:|
| Wave 1 | CG-Net (calibrated) − baseline                                   | +0.044 \[0.038, 0.050\] | +0.052 \[0.030, 0.080\] | +0.067 \[0.046, 0.089\] | +0.058 \[0.042, 0.076\] | +0.061 \[0.046, 0.080\] | +0.069 \[0.050, 0.088\] |
| Wave 1 | CG-Net (calibrated) − baseline (with its own device calibration) | +0.038 \[0.032, 0.044\] | +0.046 \[0.020, 0.067\] | +0.055 \[0.033, 0.075\] | +0.045 \[0.031, 0.064\] | +0.051 \[0.035, 0.068\] | +0.057 \[0.037, 0.075\] |
| Wave 2 | CG-Net (calibrated) − baseline                                   | +0.066 \[0.059, 0.074\] | +0.071 \[0.052, 0.107\] | +0.086 \[0.065, 0.113\] | +0.077 \[0.058, 0.100\] | +0.086 \[0.066, 0.106\] | +0.087 \[0.067, 0.106\] |
| Wave 2 | CG-Net (calibrated) − baseline (with its own device calibration) | +0.044 \[0.037, 0.051\] | +0.054 \[0.036, 0.084\] | +0.066 \[0.046, 0.091\] | +0.051 \[0.034, 0.071\] | +0.047 \[0.028, 0.065\] | +0.050 \[0.032, 0.068\] |

Note: Each model’s threshold is taken from its scores on the self-reported negatives of the CODE-15% validation set.

## D.2. Positive predictive value and workload under prevalence scenarios

**Table D2.** PPV / serological tests per detected case / ECGs screened per detected case under prevalence scenarios (point estimates)

| Wave   | Model               | Alarm rate among negatives |    Prevalence 1%    |   Prevalence 2%    |   Prevalence 5%    | Prevalence 8.25%  | Prevalence 10.72% |
|:-------|:--------------------|:--------------------------:|:-------------------:|:------------------:|:------------------:|:-----------------:|:-----------------:|
| Wave 1 | CG-Net (calibrated) |             1%             | 0.187 / 5.34 / 438  | 0.318 / 3.15 / 219 | 0.546 / 1.83 / 88  | 0.672 / 1.49 / 53 | 0.733 / 1.36 / 41 |
|        |                     |             2%             | 0.151 / 6.63 / 284  | 0.264 / 3.79 / 142 | 0.481 / 2.08 / 57  | 0.613 / 1.63 / 34 | 0.679 / 1.47 / 27 |
|        |                     |             5%             | 0.090 / 11.11 / 204 | 0.167 / 6.01 / 102 | 0.340 / 2.94 / 41  | 0.468 / 2.14 / 25 | 0.540 / 1.85 / 19 |
|        |                     |            10%             | 0.057 / 17.66 / 168 | 0.108 / 9.24 / 84  | 0.238 / 4.20 / 34  | 0.348 / 2.87 / 20 | 0.416 / 2.40 / 16 |
|        |                     |            20%             | 0.035 / 28.35 / 138 | 0.069 / 14.54 / 69 | 0.160 / 6.25 / 28  | 0.246 / 4.07 / 17 | 0.303 / 3.30 / 13 |
|        | Baseline            |             1%             | 0.151 / 6.63 / 569  | 0.264 / 3.79 / 284 | 0.481 / 2.08 / 114 | 0.613 / 1.63 / 69 | 0.679 / 1.47 / 53 |
|        |                     |             2%             | 0.126 / 7.95 / 351  | 0.225 / 4.44 / 175 | 0.429 / 2.33 / 70  | 0.562 / 1.78 / 43 | 0.631 / 1.58 / 33 |
|        |                     |             5%             | 0.080 / 12.47 / 232 | 0.150 / 6.68 / 116 | 0.312 / 3.20 / 46  | 0.437 / 2.29 / 28 | 0.509 / 1.97 / 22 |
|        |                     |            10%             | 0.051 / 19.55 / 187 | 0.098 / 10.18 / 94 | 0.219 / 4.56 / 37  | 0.324 / 3.08 / 23 | 0.391 / 2.56 / 17 |
|        |                     |            20%             | 0.032 / 31.23 / 153 | 0.063 / 15.96 / 76 | 0.147 / 6.80 / 31  | 0.228 / 4.40 / 19 | 0.282 / 3.54 / 14 |
| Wave 2 | CG-Net (calibrated) |             1%             | 0.209 / 4.79 / 383  | 0.348 / 2.88 / 192 | 0.579 / 1.73 / 77  | 0.701 / 1.43 / 46 | 0.758 / 1.32 / 36 |
|        |                     |             2%             | 0.162 / 6.16 / 261  | 0.281 / 3.55 / 130 | 0.502 / 1.99 / 52  | 0.633 / 1.58 / 32 | 0.697 / 1.43 / 24 |
|        |                     |             5%             | 0.096 / 10.38 / 189 | 0.177 / 5.64 / 95  | 0.357 / 2.80 / 38  | 0.487 / 2.05 / 23 | 0.559 / 1.79 / 18 |
|        |                     |            10%             | 0.060 / 16.71 / 159 | 0.114 / 8.78 / 79  | 0.249 / 4.02 / 32  | 0.362 / 2.76 / 19 | 0.431 / 2.32 / 15 |
|        |                     |            20%             | 0.036 / 27.79 / 135 | 0.070 / 14.26 / 68 | 0.163 / 6.14 / 27  | 0.249 / 4.01 / 16 | 0.307 / 3.25 / 13 |
|        | Baseline            |             1%             | 0.161 / 6.21 / 527  | 0.279 / 3.58 / 263 | 0.500 / 2.00 / 105 | 0.631 / 1.59 / 64 | 0.695 / 1.44 / 49 |
|        |                     |             2%             | 0.131 / 7.65 / 336  | 0.233 / 4.29 / 168 | 0.439 / 2.28 / 67  | 0.573 / 1.75 / 41 | 0.641 / 1.56 / 31 |
|        |                     |             5%             | 0.083 / 11.98 / 222 | 0.155 / 6.43 / 111 | 0.322 / 3.11 / 44  | 0.448 / 2.23 / 27 | 0.520 / 1.92 / 21 |
|        |                     |            10%             | 0.052 / 19.19 / 184 | 0.100 / 10.00 / 92 | 0.223 / 4.49 / 37  | 0.329 / 3.04 / 22 | 0.395 / 2.53 / 17 |
|        |                     |            20%             | 0.032 / 31.36 / 153 | 0.062 / 16.03 / 77 | 0.146 / 6.83 / 31  | 0.227 / 4.41 / 19 | 0.281 / 3.55 / 14 |

Note: $\mathrm{PPV} = p_{\mathrm{inf}}\,\mathrm{DR}_{\alpha}/(p_{\mathrm{inf}}\,\mathrm{DR}_{\alpha} + (1-p_{\mathrm{inf}})\,\alpha)$, tests per detected case $= 1/\mathrm{PPV}$ and ECGs per detected case $= 1/(p_{\mathrm{inf}}\,\mathrm{DR}_{\alpha})$, with $p_{\mathrm{inf}}$ set to the prevalence of each column and $\alpha$ to the alarm rate among negatives; 8.25% is the seropositivity among people in the screening table who did not self-report, and 10.72% is the overall positivity of the screening table. All values are scenario estimates; intervals are given in Supplementary Data S1.

## D.3. Scenario estimates reweighted to the screening population

**Table D3.** AUROC, differences, effective sample sizes and unsupported target mass after reweighting to the screening-table population \[95% interval\]

| Target population, weighting variant         | Target prevalence |      CG-Net AUROC      |     Baseline AUROC     |    CG-Net − baseline    | CG-Net − third-party AI-ECG | Effective sample size, positives/negatives | Unsupported target mass, positives/negatives |
|:---------------------------------------------|:-----------------:|:----------------------:|:----------------------:|:-----------------------:|:---------------------------:|:------------------------------------------:|:--------------------------------------------:|
| All screened, wave 2 P                       |       0.108       | 0.776 \[0.749, 0.800\] | 0.720 \[0.693, 0.747\] | +0.056 \[0.040, 0.073\] |   +0.077 \[0.032, 0.123\]   |              678.2 / 30349.5               |                0.000 / 0.000                 |
| All screened, wave 2 AS                      |       0.108       | 0.848 \[0.832, 0.862\] | 0.803 \[0.786, 0.820\] | +0.044 \[0.035, 0.054\] |   +0.148 \[0.102, 0.195\]   |              1030.6 / 30349.5              |                0.000 / 0.000                 |
| All screened, wave 1 P                       |       0.108       | 0.802 \[0.778, 0.825\] | 0.775 \[0.751, 0.799\] | +0.027 \[0.013, 0.041\] |   +0.102 \[0.058, 0.149\]   |              778.6 / 30349.5               |                0.000 / 0.000                 |
| All screened, wave 1 AS                      |       0.108       | 0.839 \[0.824, 0.853\] | 0.817 \[0.801, 0.833\] | +0.022 \[0.013, 0.031\] |   +0.139 \[0.092, 0.185\]   |              1177.6 / 30349.5              |                0.000 / 0.000                 |
| All screened, wave 1 NE                      |       0.108       | 0.814 \[0.791, 0.837\] | 0.786 \[0.762, 0.810\] | +0.028 \[0.013, 0.042\] |   +0.115 \[0.071, 0.161\]   |              778.6 / 27000.1               |                0.000 / 0.000                 |
| All screened, third-party AI-ECG (measured)  |       0.108       | 0.700 \[0.657, 0.742\] |           —            |            —            |              —              |                     —                      |                      —                       |
| Non-reporters, wave 2 P                      |       0.083       | 0.766 \[0.734, 0.795\] | 0.712 \[0.679, 0.744\] | +0.054 \[0.034, 0.075\] |   +0.077 \[0.021, 0.135\]   |              559.8 / 30370.1               |                0.000 / 0.000                 |
| Non-reporters, wave 2 AS                     |       0.083       | 0.847 \[0.831, 0.863\] | 0.805 \[0.786, 0.824\] | +0.042 \[0.031, 0.053\] |   +0.158 \[0.100, 0.217\]   |              935.5 / 30370.1               |                0.000 / 0.000                 |
| Non-reporters, wave 1 P                      |       0.083       | 0.797 \[0.768, 0.825\] | 0.773 \[0.743, 0.801\] | +0.024 \[0.007, 0.041\] |   +0.108 \[0.051, 0.167\]   |              612.0 / 30370.1               |                0.000 / 0.000                 |
| Non-reporters, wave 1 AS                     |       0.083       | 0.839 \[0.823, 0.855\] | 0.820 \[0.803, 0.838\] | +0.019 \[0.009, 0.030\] |   +0.150 \[0.092, 0.208\]   |              1064.8 / 30370.1              |                0.000 / 0.000                 |
| Non-reporters, wave 1 NE                     |       0.083       | 0.809 \[0.780, 0.837\] | 0.784 \[0.755, 0.812\] | +0.025 \[0.007, 0.041\] |   +0.120 \[0.063, 0.179\]   |              612.0 / 27021.8               |                0.000 / 0.000                 |
| Non-reporters, third-party AI-ECG (measured) |       0.083       | 0.689 \[0.635, 0.743\] |           —            |            —            |              —              |                     —                      |                      —                       |

Note: The stratifications P, AS and NE are defined in Table C6. The values of the third-party AI-ECG were measured in the screening table without reweighting, so the comparison with it is indirect (different people and different negatives). Unsupported target mass is the mass of target-population strata without corresponding samples in the source data.

## D.4. Mortality association in infected people

Wave 1 contains 1,467 confirmed patients with 92 deaths and a median follow-up of 2.08 years. The standard deviation of the CG-Net (calibrated) logit is 1.513, 0.489 of the patients raise an alarm at the 5% threshold, and the mortality proportions of patients with and without an alarm are 0.092 and 0.035; the corresponding values for the baseline are 1.391, 0.431, 0.098 and 0.036. The reference cohort consists of 23,001 CODE-15% self-reported negatives with follow-up, with 784 deaths. All are exploratory secondary associations.

**Table D4.** Hazard ratios of Cox models \[95% Wald interval\]

| Cohort                                       | Model               | Score unit            | Adjustment variables      |    Hazard ratio     |
|:---------------------------------------------|:--------------------|:----------------------|:--------------------------|:-------------------:|
| Wave-1 confirmed patients                    | CG-Net (calibrated) | Per SD of logit       | Unadjusted                | 1.58 \[1.29, 1.95\] |
| Wave-1 confirmed patients                    | CG-Net (calibrated) | Per SD of logit       | Age, sex                  | 2.02 \[1.58, 2.57\] |
| Wave-1 confirmed patients                    | CG-Net (calibrated) | Per SD of logit       | Age, sex, ECG abnormality | 1.82 \[1.41, 2.34\] |
| Wave-1 confirmed patients                    | CG-Net (calibrated) | Alarm at 5% threshold | Age, sex                  | 3.06 \[1.93, 4.83\] |
| Wave-1 confirmed patients                    | CG-Net (calibrated) | Alarm at 5% threshold | Age, sex, ECG abnormality | 2.48 \[1.55, 3.95\] |
| Wave-1 confirmed patients                    | Baseline            | Per SD of logit       | Unadjusted                | 1.66 \[1.34, 2.07\] |
| Wave-1 confirmed patients                    | Baseline            | Per SD of logit       | Age, sex                  | 1.73 \[1.38, 2.17\] |
| Wave-1 confirmed patients                    | Baseline            | Per SD of logit       | Age, sex, ECG abnormality | 1.55 \[1.22, 1.96\] |
| Wave-1 confirmed patients                    | Baseline            | Alarm at 5% threshold | Age, sex                  | 2.83 \[1.83, 4.39\] |
| Wave-1 confirmed patients                    | Baseline            | Alarm at 5% threshold | Age, sex, ECG abnormality | 2.30 \[1.47, 3.59\] |
| CODE-15% self-reported negatives (reference) | CG-Net (calibrated) | Per SD of logit       | Age, sex                  | 1.35 \[1.24, 1.47\] |
| CODE-15% self-reported negatives (reference) | CG-Net (calibrated) | Per SD of logit       | Age, sex, ECG abnormality | 1.30 \[1.20, 1.42\] |
| CODE-15% self-reported negatives (reference) | Baseline            | Per SD of logit       | Age, sex                  | 1.20 \[1.11, 1.29\] |
| CODE-15% self-reported negatives (reference) | Baseline            | Per SD of logit       | Age, sex, ECG abnormality | 1.17 \[1.08, 1.26\] |

## D.5. Decision curves

The logits of each model were recalibrated on one wave plus half of the N patients (class-balanced logistic regression, with the prior shifted to the target prevalence), net benefit was read on the other wave plus the other half of the N patients, and the two folds were swapped and averaged. The calibration slopes at evaluation were 1.121 \[1.062, 1.188\] for CG-Net and 1.007 \[0.938, 1.085\] for the baseline when recalibrated on wave 1 and evaluated on wave 2, and 1.137 \[1.073, 1.212\] for CG-Net and 0.945 \[0.880, 1.018\] for the baseline when recalibrated on wave 2 and evaluated on wave 1.

**Table D5.** Net benefit of the decision curves, differences \[95% interval\], tests saved per 100 people and standardized net benefit

| Evaluation wave | Prevalence | Probability threshold | CG-Net net benefit | Baseline net benefit |      CG-Net − baseline      | CG-Net − better default strategy | Tests saved per 100 people | Standardized net benefit |
|:----------------|:----------:|:---------------------:|:------------------:|:--------------------:|:---------------------------:|:--------------------------------:|:--------------------------:|:------------------------:|
| Wave 1          |     2%     |          1%           |       0.0135       |        0.0126        | +0.0009 \[0.0006, 0.0012\]  |    +0.0034 \[0.0030, 0.0037\]    |            33.5            |          0.674           |
|                 |            |          2%           |       0.0105       |        0.0090        | +0.0014 \[0.0011, 0.0018\]  |    +0.0105 \[0.0100, 0.0110\]    |            51.4            |          0.524           |
|                 |            |          3%           |       0.0089       |        0.0076        | +0.0013 \[0.0010, 0.0017\]  |    +0.0089 \[0.0084, 0.0094\]    |            62.1            |          0.445           |
|                 |            |          5%           |       0.0073       |        0.0060        | +0.0013 \[0.0009, 0.0016\]  |    +0.0073 \[0.0068, 0.0079\]    |            73.9            |          0.367           |
|                 |            |         7.5%          |       0.0059       |        0.0045        | +0.0014 \[0.0010, 0.0018\]  |    +0.0059 \[0.0053, 0.0065\]    |            80.6            |          0.293           |
|                 |            |          10%          |       0.0049       |        0.0034        | +0.0015 \[0.0011, 0.0020\]  |    +0.0049 \[0.0044, 0.0055\]    |            84.4            |          0.246           |
|                 |            |          15%          |       0.0034       |        0.0017        | +0.0017 \[0.0012, 0.0022\]  |    +0.0034 \[0.0027, 0.0041\]    |            88.6            |          0.168           |
|                 |            |          20%          |       0.0023       |        0.0007        | +0.0015 \[0.0010, 0.0020\]  |    +0.0023 \[0.0016, 0.0029\]    |            90.9            |          0.113           |
|                 |            |          30%          |       0.0006       |        0.0000        | +0.0006 \[−0.0001, 0.0012\] |   +0.0006 \[−0.0002, 0.0013\]    |            93.5            |          0.030           |
|                 |   8.25%    |          1%           |       0.0742       |        0.0725        | +0.0016 \[0.0013, 0.0020\]  |    +0.0009 \[0.0005, 0.0014\]    |            9.3             |          0.899           |
|                 |            |          2%           |       0.0670       |        0.0641        | +0.0029 \[0.0021, 0.0035\]  |    +0.0032 \[0.0025, 0.0040\]    |            15.7            |          0.812           |
|                 |            |          3%           |       0.0613       |        0.0580        | +0.0033 \[0.0023, 0.0043\]  |    +0.0072 \[0.0062, 0.0085\]    |            23.3            |          0.743           |
|                 |            |          5%           |       0.0528       |        0.0477        | +0.0051 \[0.0035, 0.0062\]  |    +0.0186 \[0.0169, 0.0202\]    |            35.4            |          0.640           |
|                 |            |         7.5%          |       0.0451       |        0.0395        | +0.0056 \[0.0042, 0.0070\]  |    +0.0370 \[0.0351, 0.0389\]    |            45.6            |          0.547           |
|                 |            |          10%          |       0.0395       |        0.0341        | +0.0055 \[0.0041, 0.0071\]  |    +0.0395 \[0.0375, 0.0417\]    |            53.1            |          0.479           |
|                 |            |          15%          |       0.0331       |        0.0285        | +0.0046 \[0.0034, 0.0061\]  |    +0.0331 \[0.0309, 0.0354\]    |            63.8            |          0.402           |
|                 |            |          20%          |       0.0292       |        0.0243        | +0.0048 \[0.0036, 0.0064\]  |    +0.0292 \[0.0268, 0.0315\]    |            70.4            |          0.353           |
|                 |            |          30%          |       0.0220       |        0.0159        | +0.0062 \[0.0044, 0.0076\]  |    +0.0220 \[0.0196, 0.0243\]    |            77.6            |          0.267           |
|                 |   10.72%   |          1%           |       0.0989       |        0.0974        | +0.0016 \[0.0012, 0.0020\]  |    +0.0008 \[0.0002, 0.0012\]    |            7.5             |          0.923           |
|                 |            |          2%           |       0.0915       |        0.0886        | +0.0029 \[0.0024, 0.0038\]  |    +0.0025 \[0.0017, 0.0034\]    |            12.4            |          0.854           |
|                 |            |          3%           |       0.0851       |        0.0813        | +0.0038 \[0.0028, 0.0049\]  |    +0.0056 \[0.0044, 0.0067\]    |            18.0            |          0.794           |
|                 |            |          5%           |       0.0747       |        0.0705        | +0.0042 \[0.0031, 0.0062\]  |    +0.0145 \[0.0128, 0.0164\]    |            27.6            |          0.697           |
|                 |            |         7.5%          |       0.0653       |        0.0589        | +0.0064 \[0.0049, 0.0084\]  |    +0.0305 \[0.0283, 0.0326\]    |            37.6            |          0.609           |
|                 |            |          10%          |       0.0579       |        0.0505        | +0.0073 \[0.0056, 0.0093\]  |    +0.0499 \[0.0475, 0.0523\]    |            44.9            |          0.540           |
|                 |            |          15%          |       0.0485       |        0.0411        | +0.0074 \[0.0054, 0.0090\]  |    +0.0485 \[0.0456, 0.0512\]    |            56.0            |          0.452           |
|                 |            |          20%          |       0.0419       |        0.0362        | +0.0057 \[0.0041, 0.0076\]  |    +0.0419 \[0.0390, 0.0449\]    |            63.2            |          0.391           |
|                 |            |          30%          |       0.0339       |        0.0265        | +0.0074 \[0.0052, 0.0093\]  |    +0.0339 \[0.0306, 0.0369\]    |            72.2            |          0.316           |
| Wave 2          |     2%     |          1%           |       0.0137       |        0.0118        | +0.0019 \[0.0015, 0.0023\]  |    +0.0036 \[0.0032, 0.0039\]    |            35.3            |          0.683           |
|                 |            |          2%           |       0.0108       |        0.0090        | +0.0018 \[0.0014, 0.0022\]  |    +0.0108 \[0.0103, 0.0113\]    |            53.0            |          0.541           |
|                 |            |          3%           |       0.0096       |        0.0077        | +0.0018 \[0.0014, 0.0022\]  |    +0.0096 \[0.0090, 0.0101\]    |            64.2            |          0.478           |
|                 |            |          5%           |       0.0080       |        0.0065        | +0.0015 \[0.0011, 0.0020\]  |    +0.0080 \[0.0074, 0.0086\]    |            75.2            |          0.400           |
|                 |            |         7.5%          |       0.0067       |        0.0049        | +0.0018 \[0.0014, 0.0023\]  |    +0.0067 \[0.0060, 0.0073\]    |            81.6            |          0.334           |
|                 |            |          10%          |       0.0057       |        0.0037        | +0.0020 \[0.0015, 0.0024\]  |    +0.0057 \[0.0051, 0.0063\]    |            85.2            |          0.286           |
|                 |            |          15%          |       0.0042       |        0.0021        | +0.0021 \[0.0016, 0.0026\]  |    +0.0042 \[0.0035, 0.0048\]    |            89.0            |          0.208           |
|                 |            |          20%          |       0.0030       |        0.0009        | +0.0021 \[0.0015, 0.0026\]  |    +0.0030 \[0.0023, 0.0037\]    |            91.2            |          0.148           |
|                 |            |          30%          |       0.0012       |        0.0000        | +0.0012 \[0.0005, 0.0018\]  |    +0.0012 \[0.0004, 0.0019\]    |            93.6            |          0.059           |
|                 |   8.25%    |          1%           |       0.0740       |        0.0725        | +0.0015 \[0.0011, 0.0021\]  |    +0.0008 \[0.0003, 0.0013\]    |            7.6             |          0.897           |
|                 |            |          2%           |       0.0675       |        0.0638        | +0.0037 \[0.0026, 0.0046\]  |    +0.0037 \[0.0028, 0.0044\]    |            18.2            |          0.818           |
|                 |            |          3%           |       0.0614       |        0.0563        | +0.0050 \[0.0040, 0.0064\]  |    +0.0072 \[0.0061, 0.0084\]    |            23.4            |          0.744           |
|                 |            |          5%           |       0.0537       |        0.0451        | +0.0086 \[0.0072, 0.0103\]  |    +0.0195 \[0.0178, 0.0211\]    |            37.0            |          0.651           |
|                 |            |         7.5%          |       0.0464       |        0.0386        | +0.0078 \[0.0063, 0.0095\]  |    +0.0383 \[0.0363, 0.0403\]    |            47.3            |          0.563           |
|                 |            |          10%          |       0.0418       |        0.0343        | +0.0074 \[0.0058, 0.0089\]  |    +0.0418 \[0.0395, 0.0439\]    |            55.1            |          0.506           |
|                 |            |          15%          |       0.0363       |        0.0290        | +0.0073 \[0.0058, 0.0089\]  |    +0.0363 \[0.0341, 0.0388\]    |            65.6            |          0.440           |
|                 |            |          20%          |       0.0324       |        0.0253        | +0.0072 \[0.0052, 0.0086\]  |    +0.0324 \[0.0299, 0.0347\]    |            71.7            |          0.393           |
|                 |            |          30%          |       0.0253       |        0.0174        | +0.0080 \[0.0062, 0.0099\]  |    +0.0253 \[0.0227, 0.0278\]    |            78.4            |          0.307           |
|                 |   10.72%   |          1%           |       0.0988       |        0.0972        | +0.0016 \[0.0009, 0.0022\]  |    +0.0007 \[0.0001, 0.0011\]    |            6.6             |          0.922           |
|                 |            |          2%           |       0.0915       |        0.0888        | +0.0028 \[0.0019, 0.0038\]  |    +0.0026 \[0.0016, 0.0034\]    |            12.6            |          0.854           |
|                 |            |          3%           |       0.0857       |        0.0801        | +0.0057 \[0.0042, 0.0070\]  |    +0.0061 \[0.0048, 0.0071\]    |            19.8            |          0.800           |
|                 |            |          5%           |       0.0756       |        0.0668        | +0.0089 \[0.0073, 0.0109\]  |    +0.0154 \[0.0136, 0.0171\]    |            29.3            |          0.706           |
|                 |            |         7.5%          |       0.0663       |        0.0550        | +0.0112 \[0.0092, 0.0132\]  |    +0.0314 \[0.0292, 0.0338\]    |            38.8            |          0.618           |
|                 |            |          10%          |       0.0594       |        0.0495        | +0.0099 \[0.0079, 0.0120\]  |    +0.0514 \[0.0488, 0.0541\]    |            46.3            |          0.555           |
|                 |            |          15%          |       0.0516       |        0.0419        | +0.0098 \[0.0076, 0.0117\]  |    +0.0516 \[0.0489, 0.0545\]    |            57.8            |          0.482           |
|                 |            |          20%          |       0.0465       |        0.0373        | +0.0092 \[0.0071, 0.0112\]  |    +0.0465 \[0.0434, 0.0495\]    |            65.0            |          0.434           |
|                 |            |          30%          |       0.0381       |        0.0278        | +0.0102 \[0.0079, 0.0124\]  |    +0.0381 \[0.0347, 0.0413\]    |            73.2            |          0.355           |

Note: The better default strategy is whichever of test-all and test-none has the higher net benefit. Tests saved per 100 people and standardized net benefit are computed for CG-Net only, with intervals in Supplementary Data S1. Positives are not patient-separated between recalibration and evaluation (both waves contain the same people).

# References

\[1\] M. K. Reza, A. Prater-Bennette, and M. S. Asif, “Robust multimodal learning with missing modalities via parameter-efficient adaptation,” *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 47, no. 2, pp. 742–754, 2025, doi: [10.1109/TPAMI.2024.3476487](https://doi.org/10.1109/TPAMI.2024.3476487).

\[2\] Z. Zhang and M. R. Sabuncu, “Generalized cross entropy loss for training deep neural networks with noisy labels,” in *Advances in Neural Information Processing Systems*, 2018, pp. 8778–8788.

\[3\] S. Liu, J. Niles-Weed, N. Razavian, and C. Fernandez-Granda, “Early-learning regularization prevents memorization of noisy labels,” in *Advances in Neural Information Processing Systems*, 2020, pp. 20331–20342.

\[4\] M. Lukasik, S. Bhojanapalli, A. K. Menon, and S. Kumar, “Does label smoothing mitigate label noise?” in *Proceedings of the 37th International Conference on Machine Learning*, PMLR, 2020, pp. 6448–6458.
