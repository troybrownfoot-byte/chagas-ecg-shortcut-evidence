# PROTOCOL_EPCD result — part 1: validation decision (2026-10-27 03:25 Beijing time)

Locked: PROTOCOL_EPCD.lock (22:10:09 10-26), amend1 (23:18:12, execution only), amend2 (03:24:15 10-27, test path), amend3 (03:20:11,
AGADS training). Runs: EPCD/EPCDS x seeds 1234-1236 on the compshare RTX 4090 (torch 2.4.1+cu121, cuDNN 9.1.0, 3 concurrent runs per
wave, no micro-batch fallback); gate (amend. 1) passed: DEME and BASE smoke runs bitwise identical under old and new code; EPCD/EPCDS
running means updated exactly once per step. Best epochs: EPCD 2/1/2, EPCDS 1/1/2 (DEME 2/2/2). Fetched checkpoints sha256-verified.
Val scored locally (analysis/epcd_score.py; DEME_s1234 full-val check max |diff| 1.3e-4). Evaluation: analysis/results/epcd/epcd_eval.json.

Val, crop format, 3-seed ensembles (stratified V1 / V2 / V3 / challenge):
BASE .8229 / .8431 / .5015 / .4252;  DEME (= EPC) .8426 / .8717 / .5129 / .4511;  EPCD .8385 / .8726 / .5201 / .4464;
EPCDS .8447 / .8752 / .5191 / .4558.
Contrasts (paired patient-cluster bootstrap 2,000x):
E1 EPCD - DEME: stratified V1 -0.0041 [-0.0104, +0.0027] (lower bound < -0.005 -> NOT non-inferior), V2 +0.0009 [-0.0079, +0.0098]
E2 not met; E3 EPCD - BASE: +0.0156 [+0.0067, +0.0250], V2 +0.0296 [+0.0192, +0.0407] (met)
S1 EPCDS - EPCD: stratified V1 +0.0062 [+0.0010, +0.0114] (met)
S2 EPCDS - DEME: stratified V1 +0.0022 [-0.0033, +0.0078], V2 +0.0035 [-0.0035, +0.0107] (non-inferior: met)
S3 EPCDS - BASE: stratified V1 +0.0219 [+0.0113, +0.0333], V2 +0.0322 [+0.0202, +0.0452] (met)
DECISION: ADOPT EPCDS (replaces EPC in CG-Net, pending test confirmation TF1/TF2; TF3 not tested since the val condition fails).
Subgroups (CODE-15%, stratified): EPCDS vs DEME age<40 .866 vs .852; age>=75 .775 vs .768; RBBB .733 vs .740; AF .771 vs .749.
Calibration (CODE-15%): Brier .0178 vs .0178; calibration slope 1.067 vs 1.045.
Mechanism audit (analysis/results/epcd/audit.json; 4,000 CODE-15% val records, 1,000 for EPCDS; female age range 20-90):
DEME: age effect through the network 2.33-2.86 logits, through the prior 0.000-0.003 (max |ADE| 2.88-3.44).
EPCD: through the prior 2.94, through the network 0.25-0.28 (max |ADE| 0.24-0.27; not the ~0 expected: the training running mean
differs from the val feature mean). EPCDS: prior 2.94, network 0.63-1.23 (stage-wise FiLM inside the backbone, as anticipated).
=> the demographic main effect moved from the free FiLM shift to the frozen CODE-only prior (91% of the age range for EPCD, ~70% for
EPCDS, ~0% for DEME); EPCD alone lost a little discrimination; stage-wise conditioning recovered it (+0.006 over EPCD).

# Part 2: one-shot test confirmation (2026-10-27 04:22 Beijing time; TEST_USE_LOG read 10)
Test memmaps verified (sha256 296e547e...73cb, 51b0ab1e...72e5); EPCDS scored locally (epcd_score.py --split test), BASE/DEME
stored TEST_B scores; analysis/epcd_test_eval.py (locked, exact val dry run) -> analysis/results/epcd/test_eval.json.
Test, crop, 3-seed ensembles (stratified V1 / V2 / V3 / challenge): BASE .7957 / .8373 / .5374 / .3971;
DEME .8142 / .8662 / .5593 / .4289; EPCDS .8102 / .8661 / .5621 / .4228.
TF1 EPCDS - BASE: stratified V1 +0.0145 [+0.0047, +0.0240], V2 +0.0288 [+0.0149, +0.0419] -> SUPPORTED
   (Bonferroni m = 34: approximate p 0.0017 vs alpha 0.0015 -> does not pass the conservative family correction).
TF2 EPCDS - DEME: stratified V1 -0.0040 [-0.0091, +0.0018] (lower bound below -0.005), V2 -0.0001 [-0.0076, +0.0072] -> NOT SUPPORTED.
TF3 not tested (val condition false). Descriptive: DEME - BASE stratified V1 +0.0185 [+0.0079, +0.0286] (as TEST_B).
CONCLUSION: the decoupled module beats BASE on test but is not shown non-inferior to the published EPC; the val gain over EPC
(+0.0022) did not replicate (-0.0040), consistent with selection among two candidates on val. The mechanism change is real
(age effect carried by the frozen CODE-only prior: 2.94 logits vs ~0 in EPC), but no metric gain was achieved.
Recommendation (for the user): keep EPC (test-confirmed in TEST_B) as the paper's module and correct its text (the monotone prior
does not carry the age effect; the FiLM shift does, learned partly from the case-only cohort); report EPC-D as a mechanism analysis
(decoupled variant: interpretable prior, similar accuracy, val +0.002 n.s., test -0.004 n.s.). AGADS (amendment 3) is then
descriptive only.

# Part 3: amendment 3 — AGA adapters re-trained on frozen EPCDS (AGADS), val only (2026-10-27 06:06 Beijing time)
Gate (amend. 3): EPCD and AGA smoke runs bitwise identical under the locked and the amendment-3 code; AGAD/AGADS ran end to end with the
base unchanged; GATE3_PASS. AGADS x 3 seeds on the 4090 (03:24-04:35): best epochs 4/4/3, epochs run 9/9/8, 633,492 trainable
parameters, frozen EPCDS bitwise unchanged in every run (asserted; read on the host before it went offline). Lead-subset val scoring
on the host with the locked code (EPCDS: /root/cf2; AGADS: /root/cf3), fetched sha256-verified; analysis/agads_eval.py (locked 03:35,
exact stand-in dry run) -> analysis/results/epcd/agads_eval.json.
H1 AGADS - EPCDS reduced stratified V1 +0.0154 [+0.0076, +0.0232] (TRUE); reduced V2 +0.0253 [+0.0141, +0.0366].
H2 AGADS 12-lead scores == EPCDS exactly for all three seeds (TRUE).
H3 AGADS - AGA (on DEME) reduced stratified V1 +0.0016 [-0.0029, +0.0061] (TRUE, non-inferior); 12-lead +0.0022 (= EPCDS - DEME).
Reduced-lead stratified V1: AGADS .8130, AGA .8114, EPCDS .7976, DEME .7968. RETAINED AGADS (meaningful only if EPCDS replaces EPC).
Not fetched (host went offline ~05:56): AGADS best.pt x3 and AGADS_s1236/result.json; they stay on the compshare system disk.
