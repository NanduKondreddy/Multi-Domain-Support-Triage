import pandas as pd

df = pd.read_csv('final_results.csv')

print("Empty cell analysis:")
print()

for col in df.columns:
    empty = df[col].isnull().sum() + (df[col] == '').sum()
    if empty > 0:
        print(f"Column '{col}': {empty} empty cells")

print("\n" + "="*80)
print("CRITICAL OUTPUT COLUMNS CHECK:")
print("="*80)

critical_cols = ['status', 'product_area', 'request_type', 'response', 'justification']
for col in critical_cols:
    empty = df[col].isnull().sum() + (df[col] == '').sum()
    status = "OK" if empty == 0 else f"PROBLEM: {empty} empty"
    print(f"{col}: {status}")

print("\n" + "="*80)
print("VERDICT:")
print("="*80)

all_critical_full = all(
    (df[col].isnull().sum() + (df[col] == '').sum()) == 0 
    for col in critical_cols
)

if all_critical_full:
    print("✓ ALL CRITICAL COLUMNS FULL - READY FOR SUBMISSION")
else:
    print("✗ CRITICAL COLUMNS HAVE EMPTY VALUES - NEEDS FIX")
