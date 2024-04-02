import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel("your_excel_file.xlsx")

# Convert 'attribute_name' and 'is_cde' columns to strings
df['attribute_name'] = df['attribute_name'].astype(str)
df['is_cde'] = df['is_cde'].astype(str)

# Group by 'rule_id' and aggregate 'attribute_name' and 'is_cde' into lists
grouped = df.groupby('rule_id').agg({
    'attribute_name': ', '.join,
    'is_cde': ', '.join
}).reset_index()

# Check if all 'is_cde' values are False for each 'rule_id'
all_false_rules = grouped[grouped['is_cde'].str.contains('False')]

# Get the indices of rows where 'rule_id' is in 'all_false_rules'
test_indices = df[df['rule_id'].isin(all_false_rules['rule_id'])].index

# Create the test DataFrame
test_df = df.loc[test_indices]

# Save the test DataFrame to test.csv
test_df.to_csv('test.csv', index=False)
