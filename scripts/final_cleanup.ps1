# 1. Purge trash
Remove-Item temp_log2.txt, code.zip, submission.zip, hackerrank_orchestrate_code_final.zip -ErrorAction SilentlyContinue

# 2. Re-verify directories
New-Item -ItemType Directory -Path docs, scripts, archive, archive\old_results, archive\old_zips -ErrorAction SilentlyContinue

# 3. Move scripts
Get-ChildItem check_*.py, debug_*.py, verify_*.py, find_*.py, manual_spot_check.py, log_phase1.py, test_decision_engine.py, final_check*.py, final_judge_check.py, final_verification.py, spot_check_analysis.py, audit_validator.py, final_submission_check.py, submission_checklist.py, run_final2.py | Move-Item -Destination scripts\ -ErrorAction SilentlyContinue

# 4. Move Docs
Get-ChildItem AUDIT_REPORT.md, SUBMISSION_READY.md, FINAL_SUBMISSION_GUIDE.md, Testcases.txt | Move-Item -Destination docs\ -ErrorAction SilentlyContinue

# 5. Archive
Get-ChildItem *.csv | Move-Item -Destination archive\old_results\ -ErrorAction SilentlyContinue
Get-ChildItem agent_original.py | Move-Item -Destination archive\ -ErrorAction SilentlyContinue
Get-ChildItem *.zip | Move-Item -Destination archive\old_zips\ -ErrorAction SilentlyContinue
