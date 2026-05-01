import pandas as pd

df = pd.read_csv('support_issues/output.csv')

print("Rows with NULL values:")
for i, row in df.iterrows():
    nulls = row.isnull().sum()
    if nulls > 0:
        print(f"\nRow {i}:")
        print(f"  Issue: {row['issue'][:60]}")
        print(f"  Null columns: {[col for col in df.columns if pd.isnull(row[col])]}")
        for col in df.columns:
            if pd.isnull(row[col]):
                print(f"    {col}: NULL")
