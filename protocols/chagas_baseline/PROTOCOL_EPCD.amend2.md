# PROTOCOL_EPCD amendment 2 — test-read path (section 5), locked before any EPC-D test score exists

Written 2026-10-27 03:24 Beijing time. Val decision (analysis/results/epcd/epcd_eval.json, locked rules): ADOPT EPCDS (S1 EPCDS-EPCD stratified V1
+0.0062 [+0.0010, +0.0114]; S2 EPCDS-DEME stratified V1 +0.0022 [-0.0033, +0.0078], V2 +0.0035 [-0.0035, +0.0107]; S3 EPCDS-BASE
+0.0219 [+0.0113, +0.0333], V2 +0.0322 [+0.0202, +0.0452]); E1 failed for EPCD alone (-0.0041 [-0.0104, +0.0027]).
M* = EPCDS. TF3 is not tested: on val EPCDS-DEME stratified V1 lower bound is -0.0033 (not > 0).
Script: analysis/epcd_test_eval.py (sha256 in PROTOCOL_EPCD.amend2.lock). Val dry run (--split val, M* from epcd_eval.json):
every EPCDS contrast (points and CI bounds, crop and orig) equals the locked val evaluation exactly (max |difference| 0.0);
output analysis/results/epcd/test_eval_dryrun_val.json.
Test read (one shot; user approval 2026-10-26 23:2x "允许使用测试集"): verify sha256 of /home/hyhz/tb_build/test/test.f16.dat
(296e547e...73cb) and test_crop.f16.dat (51b0ab1e...72e5); score EPCDS s1234/1235/1236 with analysis/epcd_score.py --split test
-> collected/epcd/runs/EPCDS_s<seed>/test_scores_tb.csv; then epcd_test_eval.py --split test -> analysis/results/epcd/test_eval.json;
TEST_USE_LOG read 10; Bonferroni family m = 34. All results reported whatever the outcome.
