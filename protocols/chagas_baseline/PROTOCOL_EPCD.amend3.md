# PROTOCOL_EPCD amendment 3 — AGA adapters re-trained on the adopted EPC-D module (arm AGADS); training only, evaluation later

Written 2026-10-27 03:20 Beijing time, after the val decision (analysis/results/epcd/epcd_eval.json: ADOPT EPCDS) and before any AGADS run.
Why: CG-Net's lead module AGA (PROTOCOL_LEAD amendment 1) sits on a frozen DEME; with EPC replaced by EPCDS, AGA must sit on the
frozen EPCDS of the same seed for a consistent final network (section 7 of the protocol: "separate amendment"). Authority: user,
2026-10-26 23:2x: "后面你自行接着推进模块优化实验吧，允许使用测试集" (continue the module optimisation autonomously); the rented
4090 is idle and still billed. No test read for AGADS under this amendment.
Arm AGADS: GatedAdapter after each of the 7 Net1D stages (identical to AGA), placed after the EPCDS stage FiLM so a closed gate
(all 12 leads) reproduces EPCDS exactly; frozen EPCDS (best.pt of the same seed, host /hy-tmp/runs_epcd/EPCDS_s<seed>/best.pt,
sha256 equal to collected/epcd/runs); recipe identical to AGA: only the adapters train (AdamW lr 1e-4, wd 1e-2), batch 64,
every draw a reduced-lead configuration (TRAIN_SUBSETS), checkpoint on the mean hold-out BCE over limb6, I+II, II and I,
patience 5, max 30 epochs, seeds 1234/1235/1236 concurrently. The frozen base must be bitwise unchanged at the end (asserted);
its running means are never updated (case-only flag ignored for AGAD/AGADS).
Code: chagas_founder/train_module.amend3.py (host /root/cf3/train_module.py), sha256 in PROTOCOL_EPCD.amend3.lock. CPU equivalence
tests (old locked vs new code, identical weights): DEME, AGA, EPCD, EPCDS outputs bitwise identical; AGAD/AGADS with zero adapters
equal their base at 12 leads and lead II; non-zero adapters leave the 12-lead output unchanged (gate closed). The amendment-3 file
replaces chagas_founder/train_module.py only after the EPC-D test read (the test path executes the locked code).
Gate (host, GPU, smoke, seed 1234, one pair at a time; remote/epcd_gate3.sh + epcd_compare3.py): EPCD and AGA identical under the
locked and the new code; AGAD and AGADS run end to end with base_unchanged. Training only if GATE3_PASS (remote/epcd_train3.sh).
Planned evaluation (later; lead-subset scoring needs a Linux GPU or the local scorer extended; rules fixed now):
H1 AGADS - EPCDS: mean over the 4 reduced configurations of stratified V1, CI lower bound > 0 (val, crop format);
H2 AGADS 12-lead scores identical to EPCDS (exact); H3 AGADS - AGA (on DEME) reduced stratified V1 lower bound > -0.005.
