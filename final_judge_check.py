import pandas as pd
import os

print("="*80)
print("FINAL JUDGE-LEVEL VERIFICATION")
print("="*80)

# 1. CSV FORMATTING MISTAKE
print("\n[1] CSV FORMATTING CHECK:")
df = pd.read_csv('support_issues/output.csv')

# Check exact column names
required_cols = ['issue', 'subject', 'company', 'response', 'product_area', 'status', 'request_type', 'justification']
actual_cols = list(df.columns)

print(f"\nRequired columns: {required_cols}")
print(f"Actual columns:   {actual_cols}")
print(f"Match: {required_cols == actual_cols}")

if required_cols != actual_cols:
    print("ERROR: Column mismatch!")
    missing = set(required_cols) - set(actual_cols)
    extra = set(actual_cols) - set(required_cols)
    if missing:
        print(f"  Missing: {missing}")
    if extra:
        print(f"  Extra: {extra}")

# Check for empty rows
empty_rows = df.isnull().sum(axis=1) > 0
if empty_rows.sum() > 0:
    print(f"\nERROR: {empty_rows.sum()} rows with null values!")
else:
    print(f"\n✓ No empty cells in critical fields")

# Check row count
print(f"\nRow count: {len(df)} (should be 29)")
if len(df) != 29:
    print(f"ERROR: Expected 29 rows, got {len(df)}")

# 2. ZIP MISTAKE
print("\n" + "="*80)
print("[2] ZIP CONTENTS VERIFICATION:")
print("="*80)

exclude_items = ['data/', '.git/', '.env', '__pycache__/', 'venv/', '.venv/', '*.pyc']
print(f"\nItems to EXCLUDE from zip:")
for item in exclude_items:
    if os.path.exists(item.rstrip('/')):
        print(f"  ❌ {item} - EXISTS (will be excluded manually)")
    else:
        print(f"  ✓ {item} - not found")

# Verify code/ folder contents
code_files = []
for root, dirs, files in os.walk('code'):
    # Skip __pycache__
    dirs[:] = [d for d in dirs if d != '__pycache__']
    for f in files:
        if not f.endswith('.pyc'):
            code_files.append(os.path.join(root, f).replace('\\', '/'))

print(f"\nFiles in code/ folder: {len(code_files)}")
print(f"main.py present: {'code/main.py' in code_files}")
print(f"agent.py present: {'code/agent.py' in code_files}")

# 3. LOG FILE
print("\n" + "="*80)
print("[3] CHAT TRANSCRIPT (log.txt):")
print("="*80)

log_path = os.path.expanduser('~/hackerrank_orchestrate/log.txt')
if os.path.exists(log_path):
    size = os.path.getsize(log_path)
    lines = len(open(log_path).readlines())
    print(f"✓ Log file exists")
    print(f"  Path: {log_path}")
    print(f"  Size: {size:,} bytes")
    print(f"  Lines: {lines}")
else:
    print(f"ERROR: Log file not found at {log_path}")

# FINAL SUMMARY
print("\n" + "="*80)
print("FINAL VERDICT:")
print("="*80)

checks_pass = (
    required_cols == actual_cols and
    empty_rows.sum() == 0 and
    len(df) == 29 and
    os.path.exists(log_path)
)

if checks_pass:
    print("\n✅ ALL CHECKS PASSED - READY FOR SUBMISSION")
    print("\nNext steps:")
    print("  1. Compress-Archive -Path code -DestinationPath code.zip")
    print("  2. Upload code.zip to HackerRank")
    print("  3. Upload support_issues/output.csv")
    print("  4. Upload log.txt")
    print("  5. Submit")
else:
    print("\n❌ ISSUES FOUND - DO NOT SUBMIT")
