# PROTOCOL_EPCD — decoupled epidemiological prior conditioning (EPC-D): validation decision, then one-shot test confirmation

Status: written 2026-10-26 (Beijing time, UTC+8) before any EPC-D network was trained or scored. Locked by sha256 (this file,
train_module.py, epcd_prior.json and the analysis scripts) in PROTOCOL_EPCD.lock. User request 2026-10-26: redesign EPC; option A
(decoupled EPC) chosen with "选择a，但最好多少还是提升一些指标"; test use approved in principle after a validation success
("允许使用测试集"), to be confirmed again by the user immediately before the test read.

## 1 Why (measured before this protocol)
D1 What EPC (= DEME in code) actually learned. EPC = DemFiLM (scale gamma(e) and free shift beta(e), e = GELU(W[a, a^2, s]))
+ MonoPrior (alpha*a + c*s, alpha >= 0, prior gradient blocked for SaMi-Trop rows). The block covers only the 2-parameter prior.
Audit dry run (analysis/epcd_audit.py on DEME_s1234; val crop format; 4,000 CODE-15% records; labels not used): the average direct
effect of demographics through the FiLM (every ECG re-scored with each age/sex) spans 2.86 logits between age 20 and 50 (female;
-2.86 at 20, -1.38 at 30, -0.38 at 40, 0 at 50, -1.25 at 90), while the prior carries 0.003 (learned alpha 7e-6 to 8.5e-4 over the
three seeds, at its bound). The FiLM adds a male effect of -0.35 at age 50 on top of the prior's -0.116, whereas the CODE-15%
marginal male coefficient is -0.18. So "the prior carries the epidemiological age effect" and "the module is immune to selection
bias from the case-only cohort" (paper contribution 2, limitation 4) do not describe the trained model: the free shift learns the
demographic main effect from all rows, SaMi-Trop included.
D2 Shape of the prior (train split, CODE-15% fit rows = train minus the checkpoint hold-out; 260,807 records, 4,995 positives):
prevalence 0.13% (< 20 y), 0.24% (20-29), 0.95% (30-39), 2.28% (40-49), 2.72% (50-59), 2.51% (60-69), 2.54% (70-79), 2.19% (80-89):
a steep rise between 20 and 50, then a plateau and a mild decline in the oldest, consistent with birth-cohort exposure before
vector control and excess mortality from chronic Chagas cardiomyopathy. EPC's quadratic basis fits clearly worse (BIC table in
section 2); a monotone prior cannot represent the decline after 80.
D3 Expected size of effects. SaMi-Trop demographics are close to those of CODE-15% positives (SMD age -0.10, male -0.06;
PROTOCOL_EPC2_PRECHECK D1), so the selection bias at stake is small, and demographic interactions did not beat main effects at
probe level (-0.002). The redesign is therefore mainly about making the module do what the paper says while staying non-inferior;
a gain over EPC is tested but not expected (prior estimate about 15-20%). The secondary arm EPCDS tests deeper (stage-wise)
conditioning for a gain (prior estimate about 30%; DAFT, Polsterl et al. MICCAI 2021; HyperFusion, Duenias et al. 2025).

## 2 Arms (only the module differs; recipe identical to DEME; chagas_founder/train_module.py)
EPCD: logit = pi(z) + w . f~ + b, with f~ = f + gamma(e(z)) * (f - mu), f the 1024-d GAP embedding of the ECGFounder backbone.
- pi(z): frozen epidemiological prior, fitted once by maximum likelihood on the CODE-15% fit rows only
  (analysis/fit_epcd_prior.py -> chagas_founder/epcd_prior.json, sha256 b6da9d9f500cd0d9a5fd06181ed249167af2d03dd66c236fb0a62e7c563ef7cd):
  pi = b0 + sum_k theta_k * clip(age - K_k, 0, 10) / 10 + b_m * male, knots K = 20, 30, ..., 90 years, flat outside.
  Fitted: b0 -6.454; slopes per decade +1.049, +1.540, +0.353, -0.029, -0.042, -0.025, -0.475; male -0.176.
  Form chosen by BIC among four forms fitted on the same rows (BIC): spline + sex 47,873.3 (chosen); spline + sex + age x sex
  47,876.5; spline + sex x spline 47,928.3; quadratic (EPC's z) + sex 47,931.7.
  pi has no trainable parameter (buffers only), so no row of any cohort updates it; its float32 implementation is checked
  against the float64 fit at stored reference points at start-up (max error 3.5e-7).
- Centred FiLM: e(z) = GELU(Linear(3 -> 64)), gamma = Linear(64 -> 1024), zero-initialised; mu = running mean of f over CODE-15%
  training rows (momentum 0.01, updated before use, training mode only; stored with the checkpoint); no free shift.
  Property: for every z, the FiLM term averaged over the reference population is zero, i.e. no average direct demographic effect
  outside pi (unit test: -1e-6 versus -25 for a free shift with the same random weights).
- Initialisation: the network part equals BASE exactly at start (asserted); e(z) initialises as DEME's encoder (same RNG order).
EPCDS (secondary; trained only if the user approves before training): EPCD + centred channel-wise FiLM after each of the 7 Net1D
stages (own encoder, gamma_k zero-initialised, mu_k running channel means over CODE-15% rows), created after all EPCD modules so
shared parameters initialise exactly as in EPCD. Inside the backbone the zero-ADE property is not exact; the audit measures it.
References: BASE and DEME (= EPC) existing runs (collected/rent4090/runs; same recipe, hold-out and seeds; stored val scores).
Recipe: ECGFounder 12-lead weights + fresh head, AdamW lr 1e-4 wd 1e-2, batch 64, BCE, fp32, no augmentation, max 30 epochs,
early stopping patience 5 and checkpoint on the hold-out BCE (holdout_rows.csv sha256 1da3bcd3...), seeds 1234/1235/1236, data
order RandomState(seed + epoch). Code: train_module.py sha256 in PROTOCOL_EPCD.lock; earlier arms' code paths are unchanged.

## 3 Execution
Host: a rented GPU (RTX 4090 class; or the user's own 3090 when back online). The train memmap comes from the gpushare instance
(/hy-tmp/fm/train.f16.dat, re-verified 2026-10-26 21:07) directly or through the user's Baidu Netdisk backup (raw 4 GiB parts
plus SHA256SUMS); on the training host it must have sha256 7e40684228ffd0d16276aa738eb00f5f9ae1d7ff4e6427d85c1d6929fa8c44b2.
Code bundle (cf_bundle.tar): /root/cf2 (this version), /root/cf (version before this protocol, sha256 8a12f024...), exams tables
/root/cf_data, ECGFounder checkpoint, scripts train_epcd.sh and compare_smoke.py; every listed file's sha256 is checked against
PROTOCOL_EPCD.lock on the host before the gate. No data are downloaded from OSS. GPU runs use cudnn deterministic mode (seed_all),
as all earlier runs.
Gate before training (GPU mode, seed 1234, --smoke --no-val): EPCD and EPCDS run end to end; DEME and BASE give identical
history (all columns except timing) and identical best.pt tensors under the old and the new code (remote compare_smoke.py).
If the gate fails, nothing is trained and the code is fixed under an amendment.
Training: EPCD (and EPCDS if approved) x 3 seeds, all concurrently, --no-val, outputs /hy-tmp/runs_epcd/<ARM>_s<seed>.
Fetch best.pt, config.json, history.csv, result.json and the log to chagas_baseline/collected/epcd/runs (sha256-verified).
Scoring (local, val only): analysis/epcd_score.py (model classes executed verbatim from train_module.py; best.pt loaded strictly;
batch 128, eval mode). Validation of this path: DEME_s1234 rescored on this PC versus its stored scores (see section 6).
Audit: analysis/epcd_audit.py on every EPCD/EPCDS run and the three DEME runs -> analysis/results/epcd/audit.json.
Evaluation: analysis/epcd_eval.py collected/epcd/runs analysis/results/epcd/epcd_eval.json.

## 4 Decision rules (val; crop format primary, orig secondary; 3-seed mean-probability ensembles;
## paired patient-cluster bootstrap 2,000x, seed 1234; metric code verbatim from analysis/mod_eval.py)
E1 non-inferiority to EPC: EPCD - DEME stratified V1 CI lower bound > -0.005 and V2 lower bound > -0.010.
E2 superiority to EPC: EPCD - DEME stratified V1 lower bound > 0.
E3 still beats BASE: EPCD - BASE stratified V1 lower bound > 0 and V2 lower bound > 0.
S1 stage-wise gain: EPCDS - EPCD stratified V1 lower bound > 0.
S2 EPCDS non-inferior to EPC: EPCDS - DEME stratified V1 lower bound > -0.005 and V2 lower bound > -0.010.
S3 EPCDS beats BASE: EPCDS - BASE stratified V1 lower bound > 0 and V2 lower bound > 0.
Adopt EPCDS if S1, S2 and S3 hold; otherwise adopt EPCD if E1 and E3 hold; otherwise keep EPC (DEME) and correct the paper text.
Reported in every case (descriptive): all contrasts in both formats (V1, stratified V1, V2, V3, challenge); CODE-15% subgroups
(age < 40, age >= 75, RBBB, AF; length-stratified AUROC) with bootstrap CIs; calibration on CODE-15% val (Brier, calibration
intercept and slope); best epochs and hold-out curves; mechanism audit M1 (max |ADE| of the network part over the grid age 20-90
x sex; EPCD expected < 0.05 logit, DEME as measured) and M2 (age range carried by the prior versus by the network part).

## 5 Test confirmation (one shot, only if an arm is adopted; user confirmation immediately before the read)
The adopted module M* (3 seeds) is scored on the frozen test split with epcd_score.py --split test (test memmaps built for
TEST_B in /home/hyhz/tb_build/test: test.f16.dat sha256 296e547e...73cb, test_crop.f16.dat 51b0ab1e..., both re-verified just
before the read; the scorer never reads labels) and compared with the stored BASE and DEME
test scores (test_scores_tb.csv). Fixed sequence, each step only if the previous one holds:
TF1 M* - BASE: V2 lower bound > 0 and stratified V1 lower bound > 0 (replicates the paper's EPC claim; as TEST_B).
TF2 M* - DEME: stratified V1 lower bound > -0.005 and V2 lower bound > -0.010 (non-inferior to the published EPC).
TF3 only if, on val, E2 held (M* = EPCD) or EPCDS - DEME stratified V1 lower bound > 0 (M* = EPCDS): M* - DEME stratified V1
lower bound > 0.
Bonferroni sensitivity with family m = 34 (31 earlier + 3). The test evaluation script reuses analysis/test_b_eval.py's label
join (test labels from chagas_step2_20261013/exam_id_split.csv), metric and bootstrap code; it is written and locked, with a dry
run on val, as an amendment before the read. TEST_USE_LOG read 10.

## 6 Scoring path validation (before lock)
DEME_s1234 rescored on this PC (GTX 1650) with epcd_score.py: first 1,024 val rows max |diff| 8.4e-5 versus the stored scores
(both formats); full val (34,671 rows): max |diff| 1.16e-4 (orig) and 1.31e-4 (crop); single-model metrics equal to five decimals
(crop V1 .84898, stratified V1 .83635, V2 .85644, challenge .45347; V3 .50549 vs .50550; orig likewise, V3 .41727 vs .41729).
BASE and DEME keep their stored scores; EPCD/EPCDS are scored on this PC; the hardware difference is far below the decision margins.

## 7 Consequences, costs, disclosures
If M* replaces EPC, AGA (trained on frozen DEME) must be re-trained on frozen M* (3 seeds) and its lead-subset results re-scored
(as PROTOCOL_LEAD / TEST_C) under a separate amendment and approval; paper tables are updated afterwards.
Cost: 6 concurrent runs ~ 7 epochs x ~23 min ~ 2.7 h of one 4090 (EPCD only: 3 runs ~ 1.4 h); no transfer fees.
Disclosures: the val split was used for the BASE/DEM/DEME decisions and for PROTOCOL_EPC2_PRECHECK (frozen-feature probes);
the EPC-D design used the train split (prior fit, BIC) and the label-free DEME audit on val; subgroup weaknesses seen on val
(age >= 75, RBBB, AF) motivated EPCDS. The test split has not been used for any EPC-D decision.
