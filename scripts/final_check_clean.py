import pandas as pd
import os

df = pd.read_csv('support_issues/output.csv')

print("="*80)
print("FINAL VERIFICATION AFTER FIX")
print("="*80)
print()
print("1. CSV Columns (8 required):", "CORRECT" if len(df.columns) == 8 else "WRONG")
print("2. Row count:", f"{len(df)} (should be 29) - {'CORRECT' if len(df) == 29 else 'WRONG'}")
print("3. Null values:", f"{df.isnull().sum().sum()} (should be 0) - {'CORRECT' if df.isnull().sum().sum() == 0 else 'WRONG'}")

log_path = os.path.expanduser("~/hackerrank_orchestrate/log.txt")
print("4. Log file exists:", "YES" if os.path.exists(log_path) else "NO")
print()

all_pass = (
    len(df.columns) == 8 and 
    len(df) == 29 and 
    df.isnull().sum().sum() == 0 and
    os.path.exists(log_path)
)

if all_pass:
    print("="*80)
    print("✅ ALL CHECKS PASSED - READY FOR SUBMISSION")
    print("="*80)
else:
    print("❌ Issues remaining")
