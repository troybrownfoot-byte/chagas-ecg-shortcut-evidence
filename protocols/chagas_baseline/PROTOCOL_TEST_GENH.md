# PROTOCOL_TEST_GENH - one-shot test read 24 (conditional on PROTOCOL_GENH)

Status: written and locked together with PROTOCOL_GENH (2026-11-03 Beijing time; the lock line is authoritative), before any GENH training run
and before any GENH val metric. Test use approved by the user on 2026-11-02 (~20:25, "批准使用测试集") for reads that follow a passed, locked
val rule.

- Runs only if analysis/results/genh/genh_val.json has GENH_PASS true (checked inside the script and by remote/genh_ws.sh).
- Script analysis/test_genh.py (sha256 in PROTOCOL_TEST_GENH.lock) = analysis/test_gen.py (read 23) for the hubert backbone: networks B = BASE and
  C = EPCDSE of train_module.genh.py --backbone hubert, seeds 1234-1236 (peft_ws/genh); test crop memmap as reads 16 / 22 / 23; offsets = the
  genh_val.json offsets; device from the test record length (CODE-15%) and the signal span (SaMi-Trop < 3,400); pooling after the offset.
- Gates before the labels: config of every run (arm, seed, backbone hubert); val re-score of every run (first 2,048 crop rows, max |dp| < 1e-4).
- Metrics as read 16; paired patient-cluster bootstrap 2,000x, seed 1234.
- TGENH1 iff the CI of pooled S(C_P_O) - S(B_P_O) is above 0 and pooled V2(C_P_O) - V2(B_P_O) >= -.005; TGENH_V2 reported.
- Dry run before the lock: stopped before the label read (no test label touched).
- TEST_USE_LOG row 24 added at the lock; project hypothesis count +1 if the read runs.
