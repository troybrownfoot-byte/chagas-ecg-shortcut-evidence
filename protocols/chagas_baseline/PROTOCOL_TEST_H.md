# PROTOCOL_TEST_H — one-shot test read of the integrated CG-Net (whole-model check) with a leave-one-module-out ablation

Status: written 2026-10-28 01:45-01:52 Beijing time (clock), before any INT1 or EXP12 val result existed; locked by sha256 in PROTOCOL_TEST_H.lock.
Authority: user 2026-10-27 (test use allowed for a val-confirmed method) and 2026-10-28 ~01:00 ("我们的网络模型是一个整体，所有设计的模块拼在
一起得有效果才行"). Condition: executed only if PROTOCOL_INT1 adopts the integrated model (H1, H2 and H4). If EXP12 is a GAIN, this read is
not made; a protocol for the EXP12-based integrated model (AGA re-trained on EPCDSERK) replaces it.

## Models (all crop-then-preprocess format; 3-seed ensembles; seeds 1234-1236)
FULL = integrated CG-Net: AGADSE (INT1) — EPC-D with stage FiLM (EPCDS) trained with weight EMA (EXP9 runs, gpushare 4090) + AGA adapters;
       12-lead output == the EPCDSE base exactly; + longitudinal pooling (FULL_P).
NOAGA = the same EPCDSE base without adapters (reduced-lead inputs; --base-only from the AGADSE checkpoints).
NOEMA = AGADS on EPCDS (amendment 3; no EMA); 12-lead == EPCDS.
MS = the manuscript's CG-Net: AGA on DEME (TEST_C scores); 12-lead == DEME.  BASE = 12-lead only (TEST_B scores).
Scoring: on this PC with analysis/test_h_score.py (model classes AST-executed from train_module.exp12.py; lead handling from Rec; batch 128).
Validated before locking on 1,024 val rows: AGADS max |diff| 1.9e-4 vs the host lead scores; --base-only vs EPCDS 7.6e-5. Before the test
read it is re-checked on 1,024 val rows of AGADSE_s1234 (max |diff| < 1e-3 vs the INT1 host scores). AGADSE best.pt x3 fetched sha256-verified.
Order: AGADSE x3 (full), AGADSE x3 --base-only (NOAGA), AGADS x3 (NOEMA); output <run>/test_scores_leads_th.csv; labels never read by the
scorer (test_rows_F45.csv has no label column).
Val dry run of the identical analysis (analysis/test_h_eval.py --split val, real INT1 val lead scores) before the test read.

## Hypotheses (analysis/test_h_eval.py; paired patient-cluster bootstrap 2,000x, seed 1234; reduced = mean of limb6, I_II, II, I)
TH1 (12 leads): FULL_P - MS stratified V1 95% lower bound > 0.
TH2 (reduced leads): FULL_P - MS reduced stratified V1 95% lower bound > 0.
Descriptive with CIs and Bonferroni-adjusted p (m = 38 after this read): leave-one-module-out — pooling (FULL_P - FULL), EMA (FULL_P -
NOEMA_P), AGA (reduced FULL_P - NOAGA_P); EPC-D enters through the cumulative chain BASE -> EPCDS (NOEMA 12) -> EPCDSE (FULL 12) -> FULL_P
(a strict EPC-D leave-one-out needs a BASE + EMA + AGA model, not trained); V2, V3 and challenge for every contrast.
Engineering checks: FULL 12-lead == NOAGA 12-lead exactly (every seed); NOEMA 12-lead vs the host-scored EPCDS crop scores (read 10).
The read is logged as read 13 in TEST_USE_LOG.md.
