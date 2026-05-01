import pandas as pd
import os

print("=" * 80)
print("FINAL SUBMISSION VERIFICATION")
print("=" * 80)

# 1. Check folder structure
print("\n1. FOLDER STRUCTURE:")
print(f"   support_issues/ exists: {os.path.exists('support_issues')}")
print(f"   code/ exists: {os.path.exists('code')}")

# 2. Check input file
print("\n2. INPUT FILE:")
if os.path.exists('support_issues/support_issues.csv'):
    df_in = pd.read_csv('support_issues/support_issues.csv')
    print(f"   support_issues/support_issues.csv: EXISTS ({len(df_in)} rows)")
else:
    print(f"   support_issues/support_issues.csv: MISSING")

# 3. Check output file
print("\n3. OUTPUT FILE:")
if os.path.exists('support_issues/output.csv'):
    df_out = pd.read_csv('support_issues/output.csv')
    print(f"   support_issues/output.csv: EXISTS ({len(df_out)} rows)")
    print(f"   Columns: {list(df_out.columns)}")
    
    # Check required columns
    required = ['status', 'product_area', 'response', 'justification', 'request_type']
    has_all = all(c in df_out.columns for c in required)
    print(f"   Has all required columns: {has_all}")
    
    # Check row count match
    if os.path.exists('support_issues/support_issues.csv'):
        matches = len(df_in) == len(df_out)
        print(f"   Output matches input row count: {matches}")
        if not matches:
            print(f"      WARNING: Input has {len(df_in)} rows, output has {len(df_out)} rows")
else:
    print(f"   support_issues/output.csv: MISSING")

# 4. Check code folder
print("\n4. CODE FOLDER:")
code_files = os.listdir('code')
print(f"   Number of files: {len(code_files)}")
print(f"   main.py present: {'main.py' in code_files}")
print(f"   agent.py present: {'agent.py' in code_files}")

# 5. Check .gitignore and .env
print("\n5. SECRETS HANDLING:")
print(f"   .gitignore exists: {os.path.exists('.gitignore')}")
print(f"   .env file exists: {os.path.exists('.env')} (should be NO for submission)")

# 6. Check for excluded folders
print("\n6. EXCLUDED FOLDERS (should NOT be in submission):")
exclude = ['data', 'venv', '__pycache__', 'node_modules', '.git']
for folder in exclude:
    if os.path.exists(folder):
        print(f"   {folder}: EXISTS (should be excluded from zip)")
    
print("\n" + "=" * 80)
print("SUBMISSION CHECKLIST:")
print("=" * 80)
print("[ ] support_issues/support_issues.csv exists (input)")
print("[ ] support_issues/output.csv exists (predictions)")
print("[ ] code/ folder with all .py files")
print("[ ] .env file NOT included (secrets safe)")
print("[ ] data/ folder excluded from zip")
print("[ ] Chat transcript at $HOME/hackerrank_orchestrate/log.txt")
print("[ ] Ready to upload to HackerRank")
