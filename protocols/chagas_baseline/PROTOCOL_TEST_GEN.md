# PROTOCOL_TEST_GEN - one-shot test read 23 (conditional on PROTOCOL_GEN)

Status: written and locked 2026-11-03 ~16:35 Beijing time together with PROTOCOL_GEN, before any GEN training run and before any GEN val metric.
Test use approved by the user on 2026-11-02 (~20:25, "批准使用测试集") for reads that follow a passed, locked val rule.

- Runs only if analysis/results/gen/gen_val.json has GEN_PASS true (checked inside the script and by remote/gen_ws.sh).
- Script analysis/test_gen.py (sha256 in PROTOCOL_TEST_GEN.lock). Networks: B = BASE, C = EPCDSE of train_module.gen.py --backbone merl, seeds
  1234-1236 (peft_ws/gen). Test crop memmap /home/hyhz/tb_build/test/test_crop.f16.dat (as reads 16 and 22); 3-seed mean logit; offsets = the
  gen_val.json offsets (CODE-15% train hold-out negatives), fixed before the read; device from the test record length (CODE-15%) and the signal span
  (SaMi-Trop < 3,400); longitudinal mean pooling after the offset.
- Gates before the labels: config of every run (arm, seed, backbone merl); every run re-scores its own crop-format val scores (first 2,048 rows,
  max |dp| < 1e-4). Labels (chagas_step2_20261013/exam_id_split.csv, split test) are read only after every gate.
- Metrics as read 16: S, V2, P, challenge; paired patient-cluster bootstrap 2,000x, seed 1234.
- TGEN1 (the hypothesis of this read) iff the CI of pooled S(C_P_O) - S(B_P_O) is above 0 and pooled V2(C_P_O) - V2(B_P_O) >= -.005.
  TGEN_V2 is reported, not decided: CI of that V2 difference above 0.
- Dry run before the lock: the script with the smoke runs and the dry val JSON, stopped before the label read (no test label touched).
- TEST_USE_LOG row 23 added at the lock; project hypothesis count +1 if the read runs.
