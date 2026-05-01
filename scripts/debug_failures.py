import pandas as pd

df = pd.read_csv('audit_results.csv')

failed_tests = [3, 11, 16, 17, 6, 7, 14, 19]

print("=== DETAILED FAILURE INVESTIGATION ===\n")

for idx in failed_tests:
    if idx <= len(df):
        row = df.iloc[idx-1]
        print(f"\nTest {idx}:")
        print(f"Issue: {row['issue']}")
        print(f"Status: {row['status']}")
        print(f"Product Area: {row.get('product_area', 'N/A')}")
        print(f"Justification: {row.get('justification', 'N/A')[:100]}")
        print("-" * 80)
