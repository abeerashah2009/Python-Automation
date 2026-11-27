import pandas as pd

df = pd.read_csv('employees.csv')

filtered_df = df[df['Age'] > 30]

print(filtered_df)
print(len(filtered_df), 'rows kept out of', len(df))

filtered_df.to_csv('filtered_data.csv', index=False)
