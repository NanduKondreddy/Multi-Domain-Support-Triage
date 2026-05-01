import pandas as pd

df = pd.read_csv('support_tickets/output.csv')
print(f'Output CSV rows: {len(df)}')
print(f'Columns: {list(df.columns)}')
print(f'All critical columns present: {all(c in df.columns for c in ["status", "product_area", "response", "justification", "request_type"])}')
print()

# Check input 
df_in = pd.read_csv('support_tickets/support_tickets.csv')
print(f'Input CSV rows: {len(df_in)}')
print(f'Match: {len(df) == len(df_in)}')

if len(df) != len(df_in):
    print(f'ERROR: Output has {len(df)} rows but input has {len(df_in)} rows!')
