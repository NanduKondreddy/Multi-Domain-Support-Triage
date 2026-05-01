import pandas as pd

df = pd.read_csv('support_issues/output.csv')

# Check critical output columns (not input columns)
critical_output = ['response', 'product_area', 'status', 'request_type', 'justification']

print("CRITICAL OUTPUT COLUMNS CHECK:")
print()

for col in critical_output:
    nulls = df[col].isnull().sum()
    print(f"{col}: {nulls} nulls - {'✓ GOOD' if nulls == 0 else '❌ BAD'}")

print()
all_output_good = all(df[col].isnull().sum() == 0 for col in critical_output)

if all_output_good:
    print("✅ ALL CRITICAL OUTPUT COLUMNS ARE COMPLETE")
    print("   (Nulls in input columns like 'subject' and 'company' are acceptable)")
else:
    print("❌ Critical output columns have nulls - CANNOT SUBMIT")
