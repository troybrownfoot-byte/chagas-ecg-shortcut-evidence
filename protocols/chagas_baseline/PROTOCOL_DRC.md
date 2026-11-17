# PROTOCOL_DRC - adoption path of a device-response (style) module, with a conditional one-shot test read (read 28)

Status: written 2026-11-05 ~01:50 Beijing time and locked by sha256 in PROTOCOL_DRC.lock BEFORE any of these results existed: PRECHECK_STYLE3
(FC2, RR), PRECHECK_FCB (FC weight .3 / 1.0), PRECHECK_STYLE_EXT and PRECHECK_STYLE2_EXT (external reads of MX, FS, FC, FB). Known at lock time:
PRECHECK_STYLE (MX, FS CLOSED) and PRECHECK_STYLE2 (FC, FB CLOSED) val reads.
Approval: the user, 2026-11-05 ~01:50 Beijing: "行，按你的步骤来，允许使用测试集" after being told that the locked in-distribution rules had closed
these arms and that any adoption would need a new, pre-specified protocol with a non-inferiority standard, a third seed and a test read.
This protocol does not reopen any precheck decision: those stay CLOSED as screens. It defines, in advance, a separate adoption standard for a
training-time module whose value is source robustness (unseen cohorts) at no in-distribution cost.

## Stage A - in-distribution non-inferiority on val (2 seeds; from the locked precheck JSONs, no new computation)
Arm X (any of MX, FS, FB, FC, FC2, RR, B03, B10) passes NI_VAL iff X_P - REF_P (pooled, own ANCC offset): S >= -.002 AND V2 >= -.005 (points).
At lock time: FS, FB, FC pass; MX fails (S -.0025).

## Stage B - external gain (SaMi-Trop-naive, unseen cohorts W1 / W2)
X must have EXT_GAIN in the final read of its locked external protocol (PRECHECK_STYLE_EXT for MX / FS; PRECHECK_STYLE2_EXT for FC / FB): WM
gain over the same-host control > NB (.0046) with CI lower bound > 0, and over the mean of the three fresh retrains > NB. Arms without an
external read (FC2, RR, B03, B10) are candidates only after their own external read under a new lock (not part of this decision round).
Selection: among arms with NI_VAL and EXT_GAIN, the largest WM gain over its control; tie (within .001) -> the smaller own device offset.
Only one arm goes on (multiplicity). If none qualifies: stop here, no test read, project count unchanged.

## Stage C - three-seed val confirmation (descriptive gate for the test read)
The selected arm's seed-1236 run already trained ahead before any of its scores existed (PRECHECK_STYLE_S3 for MX / FS, PRECHECK_STYLE2_S3 for FC /
FB; workstation) is re-designated as its third seed; its use is disclosed. 3-seed val read through the same pipeline (seeds 1234 / 1235 from
h4090, 1236 from the workstation; host mix disclosed): the test read runs only if X_P - REF3_P (pooled, own ANCC): S >= -.002 and V2 >= -.005.

## Stage D - one-shot test read 28 (implementation locked separately, before any test label is touched)
Models: X (3 seeds, as Stage C) and its SaMi-Trop-naive versions LSO_X (3 seeds from its external protocol); references CGN = ref9 EPCDSE
(3 seeds; gate: reproduces the stored TEST_H / read-16 FULL 12-lead scores) and LSO_CGN = lso2. Offsets fixed before the read from the
CODE-15% train hold-out negatives (age/sex-adjusted, as ANCC). Test crop format, 3-seed mean probability, patient pooling; metrics, devices
and bootstrap as read 19 (PROTOCOL_TEST_PPRQ: S, V2, P, challenge, device AUROC among CODE-15% test negatives; patient-cluster bootstrap
2,000x, seed 1234).
Hypotheses (fixed now):
- TD1 (primary, deployment with vs without the module, both calibrated, pooled): X_P_O - CGN_P_O: S and V2 CI lower bounds above -.005.
- TD2 (unseen-cohort positives): LSO_X_O - LSO_CGN_O: V2 CI lower bound above 0.
- TD3 (the module replaces the post-hoc offset): X_P (no offset) - CGN_P_O: S and V2 CI lower bounds above -.005.
Reported without a hypothesis: uncalibrated contrasts, exam level, P, challenge, device AUROC, mean p. Multiplicity: three new hypotheses,
project count 57 -> 60 if the read runs.

## Use (fixed now)
- TD1 and TD2 hold: X enters CG-Net as a training-time module of the 12-lead network (source robustness at no in-distribution cost); with
  TD3 also holding, the deployment may drop the post-hoc offset for the 12-lead path. The reduced-lead AGA adapters are then retrained on
  the X bases under their own protocol before any manuscript table changes.
- TD1 only: reported as non-inferior, not adopted. TD1 fails: not adopted; reported as a finding of the robustness / discrimination
  trade-off only if the user asks for it (failed screens stay out of the paper).
