# PROTOCOL_TEST_PPRQ - one-shot test read 19: the learned acquisition-period offset (PPR-Q) at 12 leads (written 2026-11-03 ~02:17 Beijing; locked before any test label of a PPR model)

Approval: the user approved test use on 2026-11-02 ~20:25 Beijing ("批准使用测试集"); each read gets its own lock. Origin: PROTOCOL_PPR stage B1 (11-02 21:42) chose arm Q for a 12-lead test read and held it until PROTOCOL_ADH reported, so that one test read would cover whichever of PPR-Q and ADH qualified. ADH failed its stage B1 (11-03 02:07), and its locked reads 17 and 18 did not run. Numbering: 17 and 18 stay reserved for those locked, not-run reads; this is read 19.

## What is tested
PPR-Q (EPCDSEQ) trains CG-Net's 12-lead network with a learned scalar acquisition-period offset on the CODE-15% device-A rows in the likelihood (training only; the deployed network is architecturally EPCDSE). On val with each model's own calibration (ANCC), Q vs the current deployment: pooled S +.0011 [-.0014, +.0037], V2 -.0031 [-.0079, +.0016] (B1 PASS); external (SaMi-Trop-naive models, W1/W2) WM +.0073 with its own calibration. Known caveat: the learned offset drifted to about -3.2 (stage A), so the offset is not an interpretable label-period estimate.

## Inputs (analysis/test_pprq.py on the 3090 workstation; sha in the lock)
- Q: EPCDSEQ seeds 1234-1236 (peft_ws/ppr; sha 75eb6139, 0de8872c, 532ddb50); LSO_Q: SaMi-Trop-naive EPCDSEQ seeds 1234-1236 (effd94b2, 9c87d1fd, 5679051f).
- CGN: ref9 EPCDSE seeds 1234-1236 (gate: equal to the TEST_H FULL 12-lead scores on every row, max |diff| < 1e-3); LSO_CGN: lso2 LSO_EPCDSE (as read 16).
- Offsets fixed before the read (CODE-15% train hold-out negatives): CGN .2466 / LSO_CGN .2640 (ancc.json), Q .3161 (ppr_stageB1.json), LSO_Q .2325 (ppr_ext.json).
- Test crop memmap, 3-seed mean probability, pooling = mean logit over a patient's test exams (offset before pooling). Device: CODE-15% from the test record length, SaMi-Trop from the signal span (< 3,400). Labels read only after every gate; after the labels CGN_P, CGN_P_O, LSO_CGN, LSO_CGN_O must reproduce read 16 (< 1e-4).
Metrics as read 16: S, V2, P, challenge; device AUROC among CODE-15% test negatives. Paired patient-cluster bootstrap 2,000x, seed 1234.

## Hypotheses (fixed now)
- TQ1 (primary; the deployment with the module vs without, both calibrated, pooled): Q_P_O - CGN_P_O: S and V2 CI lower bounds above -.005 (non-inferiority, EPC-D margin).
- TQ2 (unseen-cohort positives): LSO_Q_O - LSO_CGN_O: V2 CI lower bound above 0.
Reported without a hypothesis: the uncalibrated contrasts, exam level, P and challenge, device AUROC, mean p. Multiplicity: two new hypotheses; project count 47 -> 49 (reads 17 and 18 added none, they did not run). CIs unadjusted, count stated.

## Use
TQ1 and TQ2 hold: PPR-Q enters CG-Net as a training-time module of the acquisition-period problem (with ANCC at deployment); the paper reports the learned-offset caveat. TQ1 only: reported as non-inferior in-distribution without a confirmed external-like gain. Otherwise: val and external findings only.
