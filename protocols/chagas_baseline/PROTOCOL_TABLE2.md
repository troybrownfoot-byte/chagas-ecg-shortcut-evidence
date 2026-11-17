# PROTOCOL_TABLE2 - Table 2 row of the integrated CG-Net (descriptive test read 14)

Status: written 2026-10-28 15:59:07 Beijing time (clock), after test read 13 (TEST_H) and before any Table-2 metric of the new model was computed; locked
by sha256 in PROTOCOL_TABLE2.lock. User 2026-10-28 15:5x: "按这个对比表格，重新给我一份最新版的表格" (Table 2 of the manuscript) and approval
of the comparison plan ("批准你的计划").
What: analysis/table2_update.py computes the five Table-2 metrics (pooled V1, length-stratified V1, cross-cohort V2, source V3,
challenge score; definitions of analysis/test_d_eval.py) for BASE, MS, FULL and FULL_P from the read-13 test score files (no new model
scoring), with paired patient-cluster bootstrap CIs (2,000x, seed 1234) for FULL - MS, FULL_P - MS and FULL_P - BASE.
Check: BASE and MS must reproduce the manuscript rows (ECGFounder + de-shortcut .809/.796/.837/.537/.397; CG-Net .824/.814/.866/.559/.429).
Descriptive only: no hypothesis; the Bonferroni family stays m = 43. Run once; logged as read 14 in TEST_USE_LOG.md.
