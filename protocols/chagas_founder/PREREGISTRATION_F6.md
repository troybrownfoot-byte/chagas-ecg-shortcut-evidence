# F6: fine-tuning recipe for ECGFounder in Chagas screening (12-lead and lead II) — preregistration incl. test protocol

Written 2026-10-21 after the F4/F5/F45 results (disclosed below) and before any F6 run. Development on validation only; the test evaluation at the end is fully specified here and run regardless of the validation outcome (user authorised test use without leakage, 2026-10-21).

## Background (disclosed)
Test (TEST_PROTOCOL_F45): ECGFounder fine-tuned with the F1 recipe (constant LR 1e-4, ≤30 epochs, early stop on val BCE) beat the in-domain ResNet (12-lead ΔV1 +0.0145 [0.0048, 0.0238]; lead II +0.0087 [0.0011, 0.0163]) and moved lead-II V3 from 0.638 to 0.443; fusion added no V1 over ECGFounder alone on test. The F1 recipe overfits from epoch 2–3 (train BCE → 0.01). F6 tests better-founded adaptation recipes, including the linear-probe-then-fine-tune post-training recipe proposed for ECGFounder (arXiv 2509.12991; stochastic depth not available in Net1D and therefore omitted).

## Fixed elements (all arms)
Data, preprocessing and inputs as F1 (12-lead) and F5 (lead II: channel 1 re-standardised; single-lead checkpoint). BCE on hard labels; AdamW, weight decay 1e-2; batch 64; permutation RandomState(seed + epoch); no age/sex; no augmentation; float32. Checkpoint = lowest validation BCE over the epochs run. "Cosine(E, peak)" = linear warm-up over the first 500 optimizer steps to `peak`, then cosine decay to 0 at the end of epoch E (per-step schedule).

## Arms
- **A0 (reference, existing)**: F1 recipe — 12-lead `runs/F1`, `runs_F4/F_s{1235,1236}`; lead II `runs_F5/FII_s*`.
- **A1 short-cosine**: full fine-tuning, Cosine(3, 1e-4), 3 epochs.
- **A2 LP-FT**: Dropout(0.2) before the head. Epoch 1: backbone frozen (requires_grad False), head only, constant LR 1e-3. Epochs 2–4: all parameters, Cosine(3, 5e-5) restarted at epoch 2. 4 epochs.
- **A3 partial freeze**: `first_conv` and `stage_list[0:3]` frozen throughout; remaining stages and head fine-tuned with Cosine(3, 1e-4), 3 epochs.

## Stage 1 — screening (seed 1234, both lead settings: 6 runs)
Δ_arm,L = V1(arm, s1234) − V1(A0, s1234) for L ∈ {12-lead, lead II}.
Winner = arm with the largest mean of the two Δ among arms with Δ > 0 in both settings. If no arm qualifies: stop; the paper uses A0.

## Stage 2 — confirmation (winner, seeds 1235/1236, both settings: 4 runs)
Hypotheses (3-seed mean-probability ensembles, paired patient-cluster bootstrap 2,000×, seed 1234, validation):
- H1: V1(winner) − V1(A0), 12-lead: lower bound > 0.
- H2: same for lead II.
Secondary: V3 and top-5% recall; winner vs R / R-II; RA and DCGF-s fusion of (R, winner) with the F4 cross-fitting procedure; per-seed results. Selection of the winner on s1234 makes the 3-seed validation contrast slightly optimistic (disclosed); the test evaluation is the independent check.

## Test (run after Stage 2 regardless of H1/H2; only if a winner exists)
Leakage rules as TEST_PROTOCOL_F45: models and fusion parameters fixed on train/validation only; reuse the existing test memmap (`/home/hyhz/chagas_founder_memmap/test.f16.dat`, sha256 296e547e…73cb) and existing test scores (R, R-II, A0 from `test_F45/`); test labels read only by the final evaluation step.
Test contrasts (3-seed, paired patient-cluster bootstrap 2,000×, seed 1234): T1 V1 winner − A0 (12-lead); T2 V1 winner − A0 (lead II); T3 V1 winner − R and winner − R-II; T4 V3 of winner vs A0 and vs R/R-II (descriptive); RA and DCGF-s (fusion parameters refit on full validation) of (R, winner) — descriptive.
All results are reported.
