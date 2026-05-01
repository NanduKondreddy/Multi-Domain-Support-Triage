import pandas as pd
import random

df = pd.read_csv('final_results.csv')
random.seed(42)
sample_indices = random.sample(range(len(df)), 5)

print("=== MANUAL SPOT CHECK: 5 RANDOM ROWS ===\n")

for idx in sorted(sample_indices):
    row = df.iloc[idx]
    issue = row['issue']
    status = row['status']
    response = str(row['response'])[:100]
    
    print(f"Row {idx}:")
    print(f"  Issue: {issue[:70]}")
    print(f"  Status: {status}")
    print(f"  Response preview: {response}...")
    print()
