import pandas as pd
import os

print('=' * 80)
print('FINAL REQUIREMENT VERIFICATION')
print('=' * 80)

# 1. CSV Formatting Check
print('\n1. CSV STRUCTURE CHECK:')
df = pd.read_csv('final_results.csv')
print(f'   Rows: {len(df)} (expected: 30)')
print(f'   Columns: {list(df.columns)}')

required_cols = ['issue', 'status', 'product_area', 'request_type', 'response', 'justification']
has_all = all(col in df.columns for col in required_cols)
print(f'   Has all required columns: {has_all}')

# 2. Data Quality Check
print('\n2. DATA QUALITY CHECK:')
empty_count = df.isnull().sum().sum()
print(f'   Empty cells: {empty_count} (expected: 0)')

for col in required_cols:
    empty_in_col = df[col].isnull().sum() + (df[col] == '').sum()
    if empty_in_col > 0:
        print(f'   WARNING: {col} has {empty_in_col} empty values')

# 3. Status Values Check
print('\n3. STATUS VALUES CHECK:')
status_values = df['status'].unique()
print(f'   Unique statuses: {status_values}')
print(f'   Expected: ["replied", "escalated"]')
valid_statuses = set(status_values).issubset({'replied', 'escalated'})
print(f'   All valid: {valid_statuses}')

# 4. Response Quality Check
print('\n4. RESPONSE QUALITY CHECK:')
short_responses = (df['response'].astype(str).str.len() < 10).sum()
print(f'   Responses < 10 chars: {short_responses}')
if short_responses > 0:
    print('   WARNING: Some very short responses detected')

# 5. Justification Quality Check
print('\n5. JUSTIFICATION CHECK:')
empty_just = (df['justification'].astype(str).str.len() < 10).sum()
print(f'   Justifications < 10 chars: {empty_just}')
if empty_just > 0:
    print('   WARNING: Some very short justifications')

# 6. File existence check
print('\n6. REQUIRED FILES CHECK:')
required_files = [
    'final_results.csv',
    'code/main.py',
    'code/agent.py',
    'code/retriever.py',
    'code/gates.py',
]
for f in required_files:
    exists = os.path.exists(f)
    status = 'OK' if exists else 'MISSING'
    print(f'   {f}: {status}')

print('\n' + '=' * 80)
print('SAMPLE ROWS (first 3):')
print('=' * 80)
for i in range(min(3, len(df))):
    print(f'\nRow {i}:')
    print(f'  Issue: {df.iloc[i]["issue"][:70]}')
    print(f'  Status: {df.iloc[i]["status"]}')
    print(f'  Product Area: {df.iloc[i]["product_area"]}')
    print(f'  Request Type: {df.iloc[i]["request_type"]}')

print('\n' + '=' * 80)
print('OVERALL STATUS:')
print('=' * 80)

all_pass = (
    len(df) == 30 and
    has_all and
    empty_count == 0 and
    valid_statuses and
    short_responses == 0
)

if all_pass:
    print('✓ ALL CHECKS PASSED - READY FOR SUBMISSION')
else:
    print('✗ ISSUES DETECTED - SEE ABOVE')
