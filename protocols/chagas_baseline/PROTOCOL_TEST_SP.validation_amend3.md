# PROTOCOL_TEST_SP validation amendment 3 - reproduction tolerance 1e-3 for the score-reproduction checks (validation attempt 3 stopped at the CG-Net calibration forward)

Locked in PROTOCOL_TEST_SP.validation_amend3.lock after the user's approval, which is quoted below verbatim with its Beijing time. The test_sp_eval.py change and the next seal come after the lock.

Written on 2026-11-11 (Beijing time), after validation attempt 3 failed and was archived. At this point:
- no val.json, no val_pass.sha256, no test session marker and no test score exist;
- the test set has not been read;
- no validation metric has been written or seen. Attempt 3 computed G6 and the metric-equivalence check in memory before it stopped; neither was printed or stored.

User approval: "同意" (received 2026-11-11 11:30 Beijing).
- It answers the choice put to the user after attempt 3 was archived (sent on 2026-11-11 after 00:51 Beijing, repeated at 11:27). The two options, as sent:
  - "同意": 所有"重算分数和已存分数对比"的复现检查（验证集、测试集、CG-Net 校准）统一用 0.001，其余门槛和判定规则都不变，实测差值写进补充材料。 At 11:27: 回复"同意"：我补跑验证和测试，大约 10 小时后出含同流程结果的版本。
  - "不同意": 不读测试集，同流程比较到此为止，按现有正文出终稿（原流程的描述性比较加局限说明）。
- The narrower request of 2026-11-10 22:25 (1e-3 for the CG-Net calibration forward only) was never answered. This approval supersedes it.
- The test-read consents of 2026-11-09 (11:10, 12:10, 14:29) recorded for this protocol are unchanged.

This amendment deviates from the protocol (d3fb2695...):
- line 103: "a validation check against stored crop probabilities at <=1e-4";
- lines 111 and 113: G1 and G2 compare historical per-seed references at <=1e-4;
- line 125: "Do not relax thresholds ... after observing outcomes".
The deviation is made before any test read, with the user's approval. It is disclosed here, in the results-note addendum and in supplement D.3. The procedure follows protocol line 139. The protocol text itself is not changed. Validation amendments 1 (4784789f..., lock 2efab4e8...) and 2 (7b10f287..., lock e2694b18...) stay in force, except for the factual correction of amendment 2 below.

## What happened in attempt 3
- 22:09:33: the locked chain remote/b1_seal_val_ws_v2.sh started.
- 22:19:25: the seal passed, PROTOCOL_TEST_SP.lock.json 6cb63675d15b2a167f5e94fa2a7fb4d9d1830447e083b9fe8cd6b48714096cac.
- 22:19:27: the validation run started.
- 22:28:53 to 23:51:48: the 36 original-format validation scoring jobs ran, all DONE.
- The run then passed G1 for every method/seed with a historical reference. It also computed G6 and the metric equivalence in memory. This is shown by execute() reaching the calibration forward, which comes after these steps (analysis/test_sp_eval.py lines 368-385).
- 23:51:54 to 23:53:40: the calibration forwards ran (ECGFounder BASE s1234-s1236, CG-Net s1234).
- 23:53:40: cal_val_gate stopped with "G1 calibration forward failed cgn 1234 0.00012352999999998282".
- The final hash verification, which runs even on failure, passed (no second exception). At 00:05:49 the chain wrote "VAL_DONE rc=1 status=NONE".
- No crop, hold-out, analysis or bootstrap job started. No test file was opened.
- Logs, renamed below:
  - b1v2_val.attempt3.out 0223501a14930d30842cc057c18d3c5a92651697068bbfe8e5c2d9f6b2a7f3da;
  - b1v2_event.attempt3.txt 8c84dd9459d3681ef6d31cbf646d5f65a6c76b9e98bd37b6f5b7579790ddd769;
  - b1v2_seal.attempt3.out 6cec37bb512c62704f1a99749c581468100e4fe61136028ecf3aed7bf0fafb8e.

## Evidence (validation only; absolute score differences, no metric, no label)
Files are in collected/attempt3_investigation_20261111/ unless noted.

### 1. CG-Net calibration forward: stored scores from another GPU
- The stored CG-Net validation crop probabilities (collected/exp12/runs/AGADSE_s{s}/val_scores_leads.csv, score_12) were computed on the gpushare RTX 4090 host (EXP12, train_module.exp12.py 0d89c44b...).
- The calibration forward rescoring runs on this workstation's RTX 3090.
- The pre-check ran during the attempt-3 seal, with the same scorer and environment (collected/g1_investigation_20261110/: calcheck_ws.sh c83b25c2..., calcheck_diag.py bf5f9c6a..., output calcheck_diag.txt 980b7911...):

  | Rescoring | max abs diff | mean abs diff | records above 1e-4 (of 34,671) |
  |---|---|---|---|
  | CG-Net s1234, TF32 on (runner default) | 1.235e-4 | 2.5e-6 | 7 |
  | CG-Net s1234, TF32 off | 1.768e-4 | 3.0e-6 | 19 |
  | CG-Net s1235, TF32 on | 1.784e-4 | 2.8e-6 | 5 |
  | CG-Net s1236, TF32 on | 1.440e-4 | 2.3e-6 | 3 |
  | ECGFounder BASE s1234-s1236 | 0 | 0 | 0 |

- Attempt 3's own CG-Net s1234 file differs from the stored scores by 1.235e-4, the same as the pre-check (attempt3_diag.py 827efe20..., output attempt3_diag.txt da16454c...).
- Turning TF32 off does not help. The difference comes from the two GPU architectures (different cuDNN kernels), not from the numeric format.
- The ECGFounder BASE stored crop scores were computed on this workstation and reproduce exactly.

### 2. Repeated runs on the same GPU: 1D ConvNeXt (emory)
- The numerical specification of the E1 methods is their historical code, run unchanged through analysis/sp_history.py.
- baselines_e/train_e.py (86aa1bbe...) line 27 sets torch.backends.cudnn.benchmark = True with TF32 enabled. cuDNN therefore chooses convolution algorithms by timing in every new process, and the choice can differ between runs.
- Validation attempts 2 and 3 compared on the same workstation, checkpoints and inputs (run_variation.py 70677631..., output run_variation.txt c90c8529...):
  - emory s1234: max 9.966e-5, mean 1.1e-5, 13,902 records above 1e-5;
  - emory s1235: max 8.959e-5;
  - ECG-CPC differs by design (validation amendment 2);
  - every other method and seed is bit-identical.
- Attempt 2 reproduced the stored emory s1234 scores exactly. Attempt 3 passed G1 at 9.966e-5, 0.3% below 1e-4.
- G2 runs the same code in the test session, in a new process, on 34,603 test records. At 1e-4 its emory comparison could fail by chance after the test labels are loaded: execute() loads labels before test_gates(). Under protocol line 125, a failed started test session needs a new amendment, a new TEST_USE_LOG entry and new consent.

### 3. How large a real mismatch is
Stored validation crop probabilities of two seeds of the same model (attempt3_diag.txt):
- CG-Net s1234 vs s1235 and s1236: max 0.376 and 0.353, mean 7.9e-3 and 7.7e-3;
- ECGFounder BASE: max 0.293 and 0.695, mean 1.0e-2 and 1.2e-2.

A wrong checkpoint, input pipeline or scorer exceeds 1e-3 by orders of magnitude, so a 1e-3 tolerance still detects it.

### 4. Precedent
- TEST_H, whose BASE/AGADSE definitions protocol line 103 uses, measured 1.9e-4 across hosts for the same model family and used 1e-3.
- TEST_E2 amendment 4 used 1e-3 for its cross-machine checks.

## Correction
analysis/test_sp_eval.py, two constants:
- reproduction() (line 62, G1 and G2): `demand(d<=1e-4,...)` becomes `demand(d<=1e-3,...)`;
- cal_val_gate() (line 151, calibration forward): `demand(d<=1e-4,...)` becomes `demand(d<=1e-3,...)`.

Nothing else changes. The measured maxima are still written to val.json and test.json (gate entries max_abs and G1_calibration_forward) and are reported. The old file is kept as collected/test_sp_eval.f50fe268.py. The new hash is frozen by the next seal.

Unchanged:
- the Table 2 metric check (1e-6), G3 (1e-6), G4, G5 and G7;
- the G6 rule and every decision rule, seed, reference and scorer;
- every cache;
- analysis/sp_core.py (8605e7e9...), analysis/sp_v4.py (967514ea...), remote/test_sp_ws.sh and remote/b1_seal_val_ws_v2.sh.

The report tools were tested against the copy collected/report_prelock/src/test_sp_eval.py (f50fe268..., PRELOCK_REPORT_SP.lock). That copy differs from the evaluator used only in these two constants. No report tool reads or checks them.

## Correction of a statement in validation amendment 2
Amendment 2 says the ResNet s1234 reference "is rebuilt from the stored three-seed mean, so it carries CSV rounding". That is wrong:
- The locked reference is /media/hyhz/GZR/chagas_ppt/analysis/val_scores.csv, a per-seed file written on 2026-10-15 by chagas_ppt/analysis/shortcut_val.py. sp_core.stored() reads it directly. Its 6.9e-5 difference from the TEST_SP scorer comes from that script's own computation.
- The stored ResNet test references of all three seeds were written on 2026-10-17 by chagas_reduced_lead/evaluate_test.py (through chagas_tricks/test_eval_tricks).
- A validation-only replay of that script's scoring path (resnet_path_replay.py c8a47cd7..., output resnet_path_replay.txt 2e50431d...) matches the TEST_SP scorer to at most 2.9e-8 on every seed.

## Archive of attempt 3 (nothing deleted)
- analysis/results/test_sp was renamed at 00:45:06 by amend3_archive_ws.sh (720711f8...) to /media/hyhz/GZR/chagas_baseline/analysis/results/test_sp_failed_20261111_000549.
  - Its 84 files, including the moved lock, are listed with their SHA-256 in attempt3_archive.sha256 (627eee32299b1043037283951993ceaf1ded863d3ddfb4aad7d98e96bcbc3400).
  - They include val.started.json 8618658f..., the 36 original-format score files, the 4 calibration-forward files and their logs.
- PROTOCOL_TEST_SP.lock.json was moved into that directory under the same name. Previous lock SHA256: 6cb63675d15b2a167f5e94fa2a7fb4d9d1830447e083b9fe8cd6b48714096cac.
- The attempt-3 logs were renamed to collected/b1v2_*.attempt3.*. collected/stlong/inspect.json and inspect.err were copied to inspect.attempt3.*.
- The rerun is the same locked chain with the same expected sp_v4.py hash. Its seal() requires and freezes:
  - the three validation amendments and their locks;
  - the archived seal locks of attempts 2 and 3 and their val.started.json.
- The failed attempt and this amendment are reported in the results-note addendum and in supplement D.3.
