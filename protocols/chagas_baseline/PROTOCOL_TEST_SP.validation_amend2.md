# PROTOCOL_TEST_SP validation amendment 2 - validation attempt 2 stopped at G1: ECG-CPC was rescored with TF32 convolutions, its stored scores are FP32

Written on 2026-11-10 (Beijing time) after validation attempt 2 failed. It is locked in PROTOCOL_TEST_SP.validation_amend2.lock before the sp_core.py correction is applied and before the seal is run again. At this point:
- no val.json, no val_pass.sha256, no test session marker and no test score exist;
- the test set has not been read;
- no validation metric has been computed by any run.

It follows protocol line 139 (operator archive and relock procedure). The protocol text itself (d3fb2695...) is not changed. Validation amendment 1 (4784789f..., lock 2efab4e8...) stays in force.

## What happened
- 19:56:15: seal attempt 2 passed, PROTOCOL_TEST_SP.lock.json 36a2680d7584e3f7f04dd2504e6eac8d48aebbdc103abbf13fcf550d2525d2a6.
- 19:56:17: remote/test_sp_ws.sh val started (collected/b1v2_val.out line 7). val.started.json records "started_bj": "2026-11-10T20:08:09+08:00" and "authorization": "validation only".
- 20:08 to 21:31:25: the runner scored the original-format validation inputs, 12 rescored methods x 3 seeds (36 jobs, all DONE).
- 21:43:40: reproduction() (analysis/test_sp_eval.py line 62) stopped with "RuntimeError: G1/G2 failed cpc s1234: 0.00014698505401608553". At 21:43:41 the chain wrote "VAL_DONE rc=1 status=NONE".
- The run computed no metric:
  - no crop, hold-out, calibration, analysis or bootstrap job started;
  - no val.json or val_pass.sha256 was written;
  - no test cache, test score or test label was opened (they are read only in test mode).
- Logs, renamed below: b1v2_val.out 849503b8de9e34a4a83c734f960dfd57dfe9afb548d8467644ec036be3382ee0, b1v2_event.txt c3cc1e7a17c3a3603d97b71e37b7748788a29933cd35e20edbe5ae7596258517, b1v2_seal.out 6cec37bb512c62704f1a99749c581468100e4fe61136028ecf3aed7bf0fafb8e.

## Investigation (validation only; absolute score differences, no metric, no label)
Files are in collected/g1_investigation_20261110/.

1. Read-only comparison of every rescored attempt-2 file with its stored reference, loaded exactly as reproduction() loads them (sp_core.scored / sp_core.stored). Script g1_diag.py (d87833a0d986dc80bf1ee491ccd904a3601ba4c91ec6a12e3ff49726cfd03f14), output g1_diag_attempt2.txt (ca050f669464b9992f26269f37173ab43f28203ed366920e493925238b370cc9).
   - 10 of the 11 methods with historical references reproduce. 24 of the 29 method-seeds with a reference have max |diff| = 0. ResNet s1234 has 6.9e-5; its reference is rebuilt from the stored three-seed mean, so it carries CSV rounding. xECG s1234 has 9.4e-7.
   - ECG-CPC exceeds 1e-4 on all three seeds:

     | Seed | max abs diff | mean abs diff | records above 1e-4 (of 34,671) |
     |---|---|---|---|
     | s1234 | 1.470e-4 | 2.1e-6 | 16 |
     | s1235 | 2.516e-4 | 7.0e-6 | 123 |
     | s1236 | 1.266e-4 | 3.3e-6 | 4 |

2. Cause: where the stored ECG-CPC scores were computed.
   - The stored ECG-CPC validation and test scores were computed by baselines_e/score_e2_local.py (c2af57f4...) on the GTX 1650 of the user's PC, on 2026-10-28 between 18:53 and 20:22 Beijing time. The scorer's docstring says "PROTOCOL_TEST_E2 local scoring on this PC ... GTX 1650 guard".
   - The six workstation files collected/test_e2/cpc_s{1234,1235,1236}/{val,test}_scores.csv are byte-identical to the PC's files, for example val s1234 3863b193..., s1235 9d63818f..., s1236 f4c14c9d....
   - A GTX 1650 (Turing) has no TF32, so its cuDNN convolutions run in IEEE FP32.
   - On the RTX 3090 (Ampere), torch 2.4.1+cu121 defaults to torch.backends.cudnn.allow_tf32 = True. The workstation prints "2.4.1+cu121 True False" for torch.backends.cudnn.allow_tf32 and torch.backends.cuda.matmul.allow_tf32. So in attempt 2 the convolutions of the ECG-CPC encoder ran in TF32 (10-bit mantissa).
   - xECG is different. PROTOCOL_TEST_E2 amendment 4 moved its scoring to this RTX 3090 with the default settings, and the workstation scores of all three seeds are its stored scores. It reproduces without change (above).
   - The E1 and ResNet references reproduce exactly on this workstation with the default settings.

3. Confirmation: tf32off_ws.sh (48d49e25314a94520e0786bedb8ef134dfea08a23c265c0943e6a40282c1f20a) rescored the three ECG-CPC runs and xECG s1234 once more.
   - Same inputs and settings as sp_core.call(): the same validation cache, wrapper (analysis/sp_history.py), scorer, traced models (TRACE hashes), batch sizes and environment.
   - One addition: NVIDIA_TF32_OVERRIDE=0, NVIDIA's documented switch that disables TF32 in cuBLAS and cuDNN for the process.
   - Results (output g1_diag_tf32off.txt, e52958960b15c70ce4d24049424b97bb4aa9dd02307c6c753a9b4d80e4cb9aa0):
     - ECG-CPC s1234, s1235 and s1236 have a max |diff| to the stored scores of 5.96e-8 each (mean 1.1e-9 to 1.5e-9), and no record above 2e-5. Their differences from the attempt-2 (TF32) files equal the attempt-2 failures above.
     - xECG s1234 is identical to its attempt-2 file (max |diff| 0) and 9.4e-7 from its stored scores, so TF32 does not change the xECG computation.
     - The operator stopped xecg_s1235 and xecg_s1236 at about 22:05: s1235 had written nothing and s1236 had not started. They were not needed, because xECG is not changed (tf32off_chain.out 1398879be52dc395e82e248e481bcaa1a9eaae2120fcc80799541354c1b968bb).
   - These four score files are investigation evidence only. No later run reads them; the attempt-3 runner rescores everything itself.

## Correction
- analysis/sp_core.py, function call(): one line is added after the env.update(...) line. It sets NVIDIA_TF32_OVERRIDE=0 for exactly the ECG-CPC scoring jobs. Their tags are f'{split}_{fmt}_{m}_s{s}' with m = cpc, for every split and format: val, test and hold; original and crop.
  - Those are the only jobs whose stored references are FP32 results from the GTX 1650.
  - No other job changes. xECG, E1, ResNet, ECGFounder and CinCo keep the environment under which they reproduced in attempt 2.
- sp_core.py sha256 before 43741803e077c23969499981a5d8c05916016c950793b86d622195f3a9db076f. The old file is kept as collected/sp_core.43741803.py. The new hash is frozen by the next seal and reported with the results.
- Diff:
  ```
  160a161
  >     if re.fullmatch(r'(val|test|hold)_(orig|crop)_cpc_s[0-9]+',tag): env['NVIDIA_TF32_OVERRIDE']='0'  # validation amendment 2: the ECG-CPC references were scored in FP32 on a GTX 1650 (no TF32)
  ```
- Why this is a correction and not a relaxation:
  - Protocol line 60 makes the historical code the numerical specification. The stored ECG-CPC scores are FP32, so a TF32 rescoring departs from that specification in the execution environment.
  - The G1/G2 tolerance (1e-4), the seeds, the references, the scorers and every other gate and decision rule are unchanged.
  - Attempt 2 computed no metric, so the correction cannot depend on a result.
- Effect on the test session:
  - G2 compares the ECG-CPC test rescoring with the stored FP32 test scores. With TF32, that comparison would most likely have failed like G1.
  - All ECG-CPC scores of attempt 3 and of the test session are FP32, as in Table 2. That includes the crop and hold-out scores used by the same-pipeline comparison.

## Unchanged
- The protocol and runner files:
  - PROTOCOL_TEST_SP.md (d3fb2695...);
  - analysis/sp_v4.py (967514ea...) and analysis/test_sp_eval.py (f50fe268...);
  - remote/test_sp_ws.sh (319f30fa...) and remote/b1_seal_val_ws_v2.sh (9ac464cf...).
- The scoring inputs: baselines_e/score_e2_local.py (c2af57f4...), analysis/sp_history.py, the traced models and all caches.
- Validation amendment 1 and its lock.
- PRELOCK_REPORT_SP.lock (8012ca5d...), which hashes neither analysis/sp_core.py nor any score.
- PRELOCK_REPORT_SP addendum 1 (lock 572b590c...). It binds the attempt-2 seal lock 36a2680d..., which is archived below and frozen by the next seal.

## Archive of attempt 2 (nothing deleted)
- analysis/results/test_sp is renamed to /media/hyhz/GZR/chagas_baseline/analysis/results/test_sp_failed_20261110_214341. Its 76 files, including the moved lock, are listed with their SHA-256 in collected/g1_investigation_20261110/attempt2_archive.sha256 (73d68ce1a9d641d0dc29e563d135594ac2b7b708d69f46b02bd6e4b59cda8a94). Archived at 22:08:15. They include:
  - val.started.json, cinco_missing_native.csv and self_test.json;
  - the 36 job logs and the 36 original-format validation score files.
- PROTOCOL_TEST_SP.lock.json is moved into that directory under the same name. Previous lock SHA256: 36a2680d7584e3f7f04dd2504e6eac8d48aebbdc103abbf13fcf550d2525d2a6.
- The attempt-2 logs are renamed so that the rerun cannot overwrite them:
  - collected/b1v2_seal.out, b1v2_event.txt, b1v2_val.out and b1v2_nohup.out become collected/b1v2_seal.attempt2.out, b1v2_event.attempt2.txt, b1v2_val.attempt2.out and b1v2_nohup.attempt2.out;
  - collected/stlong/inspect.json and inspect.err, which the chain rewrites, are copied to inspect.attempt2.json and inspect.attempt2.err;
  - collected/b1v2_auto.log stays in place, and the rerun appends to it.
- The rerun is the same locked remote/b1_seal_val_ws_v2.sh with the same expected sp_v4.py hash. Its seal() freezes both validation amendments and their locks, plus the archived attempt-2 lock and its val.started.json.
- The failed attempt is reported with the TEST_SP results: the results-note addendum and supplement D.3.
