# PROTOCOL_EPCD amendment 1 — execution only (no change to code, recipe, prior, decision rules or analysis)

Written 2026-10-26 23:18 Beijing time, after the first gate run and before any training run.
Host: compshare RTX 4090 (24 GB), torch 2.4.1+cu121, cuDNN 9.1.0, numpy 1.26.4 (same torch build as the DEME reference runs);
train memmap sha256 7e406842... verified on the host; bundle files match PROTOCOL_EPCD.lock.

Observation (first gate run, 6 smoke runs concurrently): GPU memory was exhausted and 5 of 6 runs fell back to micro-batch 32
at different steps (DEME_old in epoch 2, DEME_new in epoch 1). DEME and BASE old/new histories then differed in the sixth
significant digit (e.g. DEME epoch-1 train loss 0.1553792 vs 0.1553786; BASE 0.1659252 vs 0.1659265), which the different
fallback points explain (different summation order). EPCD and EPCDS ran end to end. Side effect found: under the fallback, a
forward pass whose backward runs out of memory has already updated EPC-D's running mean once, so the retry updates it again
(119 updates instead of 60 in the EPCD smoke run); harmless in size but avoidable.
Changes:
1 Gate rerun with only one old/new pair on the GPU at a time (DEME pair, BASE pair, then EPCD + EPCDS), identity required as
  before (remote/epcd_gate_pairs.sh -> /hy-tmp/smoke_epcd_gpu2).
2 Training in two waves of three concurrent runs (wave 1 EPCD s1234/1235/1236, wave 2 EPCDS), as the DEME reference runs
  (three concurrent, micro-batch 64 throughout) (remote/epcd_train_waves.sh). Any run that still falls back is reported.
  Expected wall time unchanged (~2.8 h).
