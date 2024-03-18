 import pandas as pd

# Read the CSV into a DataFrame
df = pd.read_csv("your_file.csv")

# Filter rows where cde is 1
df_filtered = df[df['cde'] == 1]

# Group by "rule ID" and concatenate attributes where cde is 1
grouped = df_filtered.groupby('rule ID')['attribute'].apply(lambda x: ', '.join(x)).reset_index()

# Merge with the original DataFrame to include all columns except "cde" and "attribute"
result = pd.merge(df.drop(columns=['cde', 'attribute']).drop_duplicates(), grouped, on='rule ID', how='left')

# Save the modified DataFrame to a new CSV file
result.to_csv("target_attributes.csv", index=False)
