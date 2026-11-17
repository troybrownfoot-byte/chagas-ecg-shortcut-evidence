# PRECHECK_NEX2 - a normal-ECG routed expert head on the frozen CG-Net (frozen-base module; val decision, conditional test read 26)

Status: written 2026-11-04 ~02:00 Beijing time, after PRECHECK_NEX (01:02-01:25) and before any NEX2 computation; locked by sha256 in
PRECHECK_NEX2.lock. Stage-1 parameter files get their sha256 appended to the lock before the val read.

## Why a second precheck (disclosed design flaw of PRECHECK_NEX)
- PRECHECK_NEX said NO_BUILD, but its headroom probes were fit on val folds (about 27,700 records) and were far weaker than the trained CG-Net head
  (N_sami: probes .714 / .711 vs the network's own .892; N_code: .732 / .673 vs .820). Its probe comparison therefore says nothing about a head trained
  on the 262,046 fit rows, which is what a module would be. NEX did confirm the gap (val V2_norm .810 vs V2_abn .899) and TRAIN_N = 1,078.
- NEX also located the weakness: within the normal-ECG stratum the network ranks well (N_sami .892); the low V2_norm comes from CODE-15% negatives
  with abnormal ECGs (60% of the negatives) outranking infected people with a normal ECG.

## Module (frozen base, like AGA on a frozen base)
- Base: the CG-Net reference ref9 EPCDSE seeds 1234-1236, frozen. f = input of the final linear layer (after the centred FiLM), z = the network logit.
- Gate: L2 logistic regression of normal_ecg (both exam tables) on standardised f over the fit rows (lambda 1e-4); g = 1[gate logit > 0].
- Routed expert: z' = z + g * (w.f + b), fit on the fit rows with g = 1 by L2 logistic regression with z as a fixed offset; lambda in
  (1e-4, 1e-3, 1e-2, 1e-1, 1) chosen by the BCE of z' over all hold-out rows (native training format). Records the gate does not route keep
  z exactly. Bias-only variant (w = 0) reported as the mechanism check.
- Stage 1 on the rented 4090 (analysis/nex2_fit.py; train rows only; train memmap 7e406842; checkpoints sha-checked). Stage 2 on the workstation
  (analysis/nex2_eval.py) in the crop format, 3-seed mean probability -> logit; gate G1 = the base reproduces val S .8474 / V2 .8797.

## Val decision (analysis/nex2_eval.py val)
PASS iff the CI of dV2_norm (NEX2 - BASE; SaMi-Trop normal-ECG positives vs all CODE-15% negatives) is above 0, dV2_norm >= +.01, dS >= -.003 and
dV2 >= -.003; paired patient-cluster bootstrap 2,000x, seed 1234; record level, no offset, no pooling. Also reported: V2_abn, S_norm, N_sami, BIAS - BASE.
If the bias-only variant carries most of the gain, the result is reported as a phenotype offset, not as a feature-level expert.

## Test read 26, only if PASS (same script, split test; user approval of 2026-11-02 ~20:25 for reads after a passed, locked val rule)
Test crop memmap of reads 16 / 22; G1 recomputed on val before the labels; labels read after all gates. TNEX2 iff the CI of dV2_norm on test is above 0,
dS >= -.003 and dV2 >= -.003. TEST_USE_LOG row 26 at the lock; project count +1 if the read runs.
