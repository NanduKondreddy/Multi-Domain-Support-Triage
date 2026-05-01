import pandas as pd
df = pd.read_csv('final_results.csv')
row = df.iloc[1]
print("Row 1 Full Details:")
print("Issue:", row['issue'])
print("Status:", row['status'])
print("Justification:", row['justification'])
