# Evidence package: shortcut-aware ECG screening for Chagas disease

This repository accompanies the manuscript *Shortcut-aware electrocardiogram screening for Chagas disease with demographic context and missing leads* by Yunhe Zhang, Hao Zhao and Ju Zhou (School of Information and Control Engineering, Southwest University of Science and Technology, Mianyang, China), submitted for publication. Corresponding author: Hao Zhao (zhaohao@swust.edu.cn).

It holds the evidence the paper refers to: the locked protocols of all test-set reads and their hashes, the complete list of test-set reads with their hypothesis families, the training budgets of all compared methods and the extended results. No data are included (see [Data](#data)). The code will be released upon acceptance. Version 1.0.0 corresponds to the submitted manuscript.

## Contents

| Path | Contents |
|---|---|
| [`test_reads/test_read_list.md`](test_reads/test_read_list.md) | Appendix B. The 24 executed test-set reads (Table B1) with the cumulative count of the 57 module-confirmation hypotheses used for the Bonferroni correction, the separate family of 26 same-pipeline comparisons (read 29, Table I of the paper) and the 5 registered reads that were not executed (Table B2). |
| [`protocols/`](protocols/) | The protocols, amendments and lock files of every test-set read and the test-set usage log [`protocols/chagas_baseline/TEST_USE_LOG.md`](protocols/chagas_baseline/TEST_USE_LOG.md), published unchanged (92 files). |
| [`comparators/compared_methods.md`](comparators/compared_methods.md) | Appendix A. Pretraining-corpus overlap of the foundation models (Table A1) and the training budgets and decision eligibility of all compared methods (Table A2). |
| [`extended_results/extended_results.md`](extended_results/extended_results.md) | Appendix C (Tables C1–C25): full test metrics, paired differences, device-offset correction, prespecified subgroups, the lead-availability gated adapters on further backbones and on four public datasets, lead I on real devices, fusion with the compared networks, reduced-lead schemes, format audit of the external methods, shortcut-only baselines, computational cost, signal noise and noisy-label methods. Appendix D (Tables D1–D5): the prespecified clinical-utility analysis. |
| [`verify_locks.py`](verify_locks.py) | Checks every protocol file against its lock files (Python standard library). |
| [`SHA256SUMS.txt`](SHA256SUMS.txt) | SHA-256 of every file in this package. |

## How the test set was protected

Before each read of the test set, the comparisons, metrics, decision rules and evaluation scripts were written into a protocol and locked: their SHA-256 hashes were recorded, with a timestamp, in a lock file next to the protocol (`*.lock`, `*.sha256` or `*.lock.json`). Every read is entered in the test-set usage log, including reads whose hypotheses were not supported, and registered reads that were never run are listed as such. Confirmatory claims use a Bonferroni correction over the 57 hypotheses registered over the project; the comparison with existing methods (read 29) is a separate prespecified family of 26 comparisons.

## Verifying the locks

```
python verify_locks.py            # or: python verify_locks.py --markdown
sha256sum -c SHA256SUMS.txt       # integrity of the whole package
```

`verify_locks.py` computes the SHA-256 of every file under `protocols/` and looks for it in the lock files. In this release, 36 of the 50 protocol files have their current hash recorded in a lock file. Three more consist of a locked version followed by lines appended after the read, and the script identifies the locked part: `PROTOCOL_TEST_D.md` (first 19 of 20 lines locked, then the result), `PROTOCOL_TEST_E.md` (first 44 of 52 lines locked, then the result) and `TEST_USE_LOG.md` (first 85 of 117 lines match its last lock entry of 2026-11-05; the later lines are two status updates on read 28, which was never run, and the entries of read 29). The remaining 11 are result notes (`*.result.md`) written after the reads. The lock files also list evaluation scripts and result files that are not part of this package; their hashes can be checked when the code is released.

## Notes on the protocol files

- The protocol files are working documents and are published exactly as locked, so that their hashes can be checked. Times are Beijing time (UTC+8) unless a file states otherwise; some entries use the local time of the machine that ran the script. Paths refer to the authors' machines, a laboratory workstation and rented GPU servers, whose names appear as internal labels.
- The protocols were written, locked and executed by the authors with the help of an AI coding assistant, which is named in some entries; this use of AI is declared in the paper. Every read of the test set required the explicit approval of the first author, which the protocols and the usage log record verbatim in Chinese (for example 批准使用测试集, "approved to use the test set").
- Abbreviations of the endpoints (S, P, V1–V3 and others) are defined at the start of Appendix B.

## Data

No data are included. CODE-15% (doi:10.5281/zenodo.4916206) and SaMi-Trop (doi:10.5281/zenodo.4905618) are available from Zenodo, PTB-XL from PhysioNet, CPSC2018, Chapman-Ningbo and SPH through the routes of their original publications, the SaMi-Trop wave-2 data at github.com/samitrop/AI-ECG-Chagas and the serological screening table at doi:10.5281/zenodo.20736282.

## License and citation

The contents are licensed under [CC BY 4.0](LICENSE). Please cite the paper and this archive: Y. Zhang, H. Zhao and J. Zhou, "Evidence package for shortcut-aware electrocardiogram screening of Chagas disease: locked protocols, hashes, test-set reads and extended results," Zenodo, 2026. The DOI is shown on the Zenodo record of this release.
