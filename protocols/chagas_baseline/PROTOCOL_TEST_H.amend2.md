# PROTOCOL_TEST_H amendment 2 - test scoring of final arms may start before the ABL val analysis

Written 2026-10-28 03:49:47 Beijing time (clock). INT1 has adopted the integrated model (val; PROTOCOL_INT1.result.md) and EXP12 is NO_GAIN, so the
conditions of the read hold. Change to amendment 1, point 4 (order): the local test scoring of arms whose checkpoints are final (AGADSE
full, AGADSE --base-only, AGADSE orig; later AGADSR, AGABE, BASEER as they finish) may start before the ABL val analysis, to save time.
No test analysis (test_h_abl_eval.py --split test) is run, and no test score file is opened, before (a) the ABL val analysis
(analysis/abl_eval.py) and (b) the val dry run of test_h_abl_eval.py on the real val files are complete. The scorer never reads labels
(test_rows_F45.csv has no label column). Every checkpoint passes the val1024 check (max |diff| < 1e-3 vs the host lead scores) before its
test scoring.
