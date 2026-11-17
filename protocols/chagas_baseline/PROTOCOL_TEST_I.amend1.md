# PROTOCOL_TEST_I amendment 1 - source of the "ECGFounder (2025) full fine-tuning" row (written 2026-10-31 12:40 Beijing time, after the read)

Deviation found after the test read (read 15, 12:14-12:31): the protocol named analysis/results/test_a_test/a0_scores.csv a0_s*_orig as
the source of the ECGFounder full fine-tuning row. That file holds the TEST_A A0 models (runs/F1, runs_F4), whose checkpoints were
selected on VALIDATION loss. The manuscript's Table 2 row (V1 .841 / strat .797 / V2 .796 / V3 .461 / challenge .414) is instead the
TEST_B BASE models (collected/rent4090/runs/BASE_s*/test_scores_tb.csv, score_orig: .8412 / .7973 / .7955 / .4605 / .4142), which use the
same 5% train hold-out checkpoint selection as every other row (section 4.1.3). The protocol's own reproduction checks named only the
CG-Net and baseline rows, so the mismatch was not caught before the read.
Correction: the row keeps its manuscript source (BASE score_orig). Its new metrics (AUPRC, F1, ECE, Brier, alert point) are computed with
the unchanged code of analysis/test_i_eval.py (metrics(), bootstrap with seed 1234, so the resamples equal those of the main read) by
analysis/test_i_amend1.py (sha in the lock), which differs from test_i_eval.py only in the list of rows.
Direction of the change, stated plainly: the A0 models score higher on test (strat .8058, challenge .4240, AUPRC .2149) than the BASE
models, so the correction makes this comparator weaker. Both rows are therefore reported: BASE score_orig in Table 2 (consistent
selection protocol, as in the manuscript), and the A0 row in a table note with its own numbers and CG-Net differences.
This additional computation is part of read 15 (same authorisation, same table); TEST_USE_LOG.md is annotated.
