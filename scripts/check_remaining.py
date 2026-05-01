import pandas as pd
df = pd.read_csv('final_results.csv')
print("\n=== REMAINING ESCALATION REVIEW ===\n")
for idx in [1, 6, 22, 29]:
    row = df.iloc[idx]
    issue = row['issue']
    status = row['status']
    print(f"Row {idx}:")
    print(f"  Issue: {issue}")
    print(f"  Status: {status}")
    print(f"  Has 'and': {' and ' in issue}")
    print()
