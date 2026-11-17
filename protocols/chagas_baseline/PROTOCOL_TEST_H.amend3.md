# PROTOCOL_TEST_H amendment 3 - the local scorer reads the model classes from the ABL code version

Written 2026-10-28 07:57:10 Beijing time (clock). The val1024 pre-read check failed to load the AGADSR and AGABE checkpoints ("Error(s) in loading
state_dict"): analysis/test_h_score.py v1 executes the model classes of chagas_founder/train_module.exp12.py, whose AGAX / AGA_INIT tables do
not contain the ablation arms added in train_module.abl.py, so these arms were built without adapters. No test score of any affected arm
was produced (the check stopped the chain). Fix (v2): the scorer executes the classes and tables of train_module.abl.py instead. The Model
class code is identical in both versions (diff of the class body: none); for AGADSE the v2 output equals the v1 output bit for bit on the
first 1,024 val rows (seed 1234), so the AGADSE / EPCDSE / orig test scores already produced with v1 are unaffected. v1 is kept as
analysis/test_h_score.v1.py. Everything else in TEST_H and amendments 1-2 is unchanged.
