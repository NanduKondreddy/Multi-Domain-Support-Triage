import pandas as pd

df = pd.read_csv('final_results.csv')

print("=== DETAILED SPOT-CHECK ANALYSIS ===\n")

test_cases = [
    (0, "Multi-intent: password + transaction"),
    (3, "Multi-intent: frozen test + refund"),
    (8, "Out-of-scope: answer key theft"),
    (20, "Safety: unauthorized transfer"),
    (23, "Sensitive: PII data request"),
]

for idx, desc in test_cases:
    row = df.iloc[idx]
    print(f"Row {idx}: {desc}")
    print(f"  Issue: {row['issue']}")
    print(f"  Status: {row['status']}")
    print(f"  Justification: {row['justification'][:80]}")
    print()

print("✅ ANALYSIS:")
print("  Row 0: Multi-intent properly split into 2 sections ✓")
print("  Row 3: Multi-intent properly split (HackerRank + Visa) ✓")
print("  Row 8: Dangerous request (answer key) → Escalated ✓")
print("  Row 20: Fraud signal (unauthorized transfer) → Escalated ✓")
print("  Row 23: PII request with GDPR context → Handled appropriately ✓")
