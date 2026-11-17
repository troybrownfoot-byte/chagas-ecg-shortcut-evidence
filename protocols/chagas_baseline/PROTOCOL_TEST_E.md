# PROTOCOL_TEST_E — additional published comparison methods (Table 2), descriptive

Status: written 2026-10-25 before any training of these methods; locked (sha256 in PROTOCOL_TEST_E.lock) after smoke tests and
before the first full training run. Test use approved by the user on 2026-10-25 ("允许使用测试集"). Results are descriptive
comparisons for Table 2; they do not enter the confirmatory Bonferroni family (m = 31 stays unchanged).

## Methods (re-trained; same records for all)
| key | method | year | origin of code / recipe |
|---|---|---|---|
| inception | InceptionTime (Ismail Fawaz et al., DMKD) | 2020 | InceptionNetwork from Ahus-AIM repo (6 modules, residual/3, 32 filters, bottleneck 32, kernels 39/19/9); Adam 1e-3, bs 64 |
| xresnet | xresnet1d101 (Strodthoff et al., IEEE JBHI) | 2021 | ptbxl benchmark recipe: 100 Hz, global standardisation, random 2.5-s crops, AdamW one-cycle lr 1e-2 wd 1e-2, bs 128, concat-pool head; eval sliding windows (stride 1.25 s), max aggregation; final epoch |
| merl | MERL ResNet18 (Liu et al., ICML) | 2024 | official pretrained encoder res18_best_encoder.pth; record-wise min-max [0,1], 500 Hz 5000 samples; full fine-tuning with the same FM recipe as ECGFounder (AdamW 1e-4 wd 1e-2, bs 64) |
| stmem | ST-MEM ViT-B/75 (Na et al., ICLR) | 2024 | official encoder; 250 Hz, random 2250 crop, Butterworth-5 HP 0.67 / LP 40 (zero phase), standardise; AdamW blr 1e-3 (lr = blr·bs/256), wd 0.05, 10 epochs, 3 warm-up + cosine; eval mean of 3 crops; RandAugment not used |
| hubert | HuBERT-ECG small (Coppola et al., medRxiv) | 2024 | official SSL weights (30.5 M); FIR band-pass 0.05-47 Hz, per-lead min-max [-1,1], 5-s window, flattened, decimate ×5; AdamW 1e-5 (0.9, 0.98), wd 0.01, warm-up 8 % + linear decay, dropout ×(-2) → 0, conv feature extractor frozen, pos_weight; train random 5-s crop, eval first 5 s; select max hold-out AUROC; 8 epochs (instead of 70 k steps) |
| ahus | Stenhede & Ranjbar (CinC 2025, 5th) | 2025 | official code: drop I/II/III/aVR, zero-padding removed, random 2-s crop at 400 Hz, z-norm, InceptionNetworkWithDownsampling, AdamMuon lr 1e-3, CosineToConstantLR, bs 128, mean label for patients with conflicting labels; eval mean of 10 overlapping 2-s windows. Without MIMIC biomarker pre-training |
| emory | 1D ConvNeXt-V2, team ECG_ChD_25 (Emory, CinC 2025) | 2025 | official code: 400 Hz, edge-pad to 4096, notch 60/50, wavelet baseline removal, band-pass 1-47, z-score, augmentations; focal loss (class weights 1:9, label smoothing 0.02 on CODE-15%) + ramped pairwise ranking loss, 50 % positive oversampling, EMA 0.999, AdamW 2e-4 wd 1e-3, cosine 12 epochs, grad clip 5; select max hold-out challenge score of the EMA model. Without PTB-XL negatives |

Already in Table 2 (unchanged): ResNet (Ribeiro 2020) ± age/sex (TEST_D), CinCo (2025), ECGFounder (2025), FiLM-Demo.

## Data and input
- Records: frozen patient split; fit = train minus chagas_founder/holdout_rows.csv (5 %, patient-grouped); checkpoint choice on the
  hold-out only; val/test used only for scoring.
- Common input (deviation from the original pipelines, reported in the paper): the CG-Net input memmaps (original record span,
  ECGFounder band-pass, 500 Hz, centred in a 10-s window, window z-score). The padding is the exact constant c (all leads equal),
  so x - c restores a zero-padded record and the original span is recovered exactly (checked on 3,000 val records: spans 3,668 / 5,000).
  Each method then applies its own resampling (to 400/250/100 Hz where required), filters, normalisation, windows and aggregation.
  Reason: raw 400 Hz arrays cannot be uploaded to the rented GPU in time (uplink ~2 MB/s); the CG-Net input is on OSS.
- Mixed precision bf16 (training and inference) for all methods except emory (FP32 training and inference, as in the original).

## Seeds, scheduling and reporting
- Seeds 1234, 1235, 1236 per method, scheduled seed-major (all methods seed 1234 first). Reported score = mean probability
  over the seeds finished by the reporting deadline (2026-10-25 ~17:00 PDT); the number of seeds per method is reported.
  No run is restarted or re-tuned after seeing val or test results.
- Scoring: score-only mode on val and test memmaps (orig format; no length-consistent crop for these methods).
- Metrics and CIs exactly as TEST_D (analysis/test_d_eval.py): pooled, length-stratified, cross-cohort (V2), source (V3) AUROC,
  challenge score; paired patient-cluster bootstrap 2,000×, seed 1234, CG-Net (EPC crop ensemble) minus method.
- Val dry run first (must run end to end), then test.

## Amendment 1 (2026-10-25 ~10:20 PDT; only training-loss logs seen, no hold-out/val/test result of any method)
Measured throughput with 4 concurrent jobs on the 4090: ST-MEM ~1 step/s (10 epochs ≈ 11 h), Emory ~2.6 steps/s (12 epochs ≈ 5 h),
beyond the reporting deadline. Changes: Emory 8 epochs (the number stated in its CinC 2025 paper; the released code uses 12);
ST-MEM 4 epochs with 1 warm-up epoch (same 3:10 warm-up proportion) — a shortened schedule, reported as such; ST-MEM and Emory
run seed 1234 only; the other methods keep 3 seeds as time allows. ST-MEM/Emory seed-1234 runs restarted with these settings.

## Result (test, 2026-10-25 21:03 PDT; analysis/test_e_eval.py -> analysis/results/test_e/test_e_test_all.json; val dry run test_e_val_all.json)
Seeds used: 3 each except ST-MEM and Emory (1, amendment 1). Point estimates (pooled / stratified / V2 / V3 / challenge):
InceptionTime .814/.775/.805/.507/.404; xresnet1d101 .816/.770/.783/.469/.400; MERL .829/.781/.794/.480/.417;
ST-MEM .816/.759/.748/.456/.352; HuBERT-ECG .813/.772/.773/.495/.373; Stenhede (Ahus) .810/.777/.806/.519/.392;
Emory ConvNeXt .816/.770/.780/.478/.393; CG-Net .825/.814/.866/.559/.429.
CG-Net minus each: stratified +.033..+.055, V2 +.061..+.118, V3 +.040..+.103 (all 95% CI > 0); pooled n.s. except Ahus.
Scoring note: local scoring was first slowed by BLAS thread oversubscription in DataLoader workers; rerun with
OMP/MKL/OPENBLAS_NUM_THREADS=1 (speed only; identical computations).
