# PROTOCOL_TEST_GENA - one-shot test read 25 (conditional on PROTOCOL_GENA)

Status: written and locked together with PROTOCOL_GENA (2026-11-04 Beijing time; the lock line is authoritative), before any GENA training run
and before any GENA val metric. Test use approved by the user on 2026-11-02 (~20:25, "批准使用测试集") for reads that follow a passed, locked
val rule.

- Runs only if analysis/results/gena/gena_val.json has GENA_PASS true (checked inside the script and by remote/gena_ws.sh).
- Script analysis/test_gena.py (sha256 in PROTOCOL_TEST_GENA.lock). A = AGADSE --backbone merl, N = the frozen PROTOCOL_GEN EPCDSE networks
  without adapters (peft_ws/gena), seeds 1234-1236; scores from --score-only --lead-subsets --score-split test on the test crop memmap
  /home/hyhz/tb_build/test/test_crop.f16.dat (labels never read there); 3-seed mean probability -> logit; longitudinal mean pooling; no offset.
- Gates before the labels: config of every run (arm, seed, backbone merl); A's 12-lead test outputs equal N's (max |dp| < 1e-6).
- Metrics: S and V2 per configuration and the reduced mean; paired patient-cluster bootstrap 2,000x, seed 1234.
- TGENA1 iff the CI of the pooled reduced-mean dS (A - N) is above 0 and the pooled reduced-mean dV2 >= -.005; TGENA_V2 reported.
- Dry run before the lock: stopped before the label read (no test label touched).
- TEST_USE_LOG row 25 added at the lock; project hypothesis count +1 if the read runs.
