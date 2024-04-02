 import pandas as pd

# Read the pre-grouped Excel file into a pandas DataFrame
grouped_df = pd.read_excel("grouped_excel_file.xlsx")

# Check if all 'is_cde' values are False for each 'rule_id'
all_false_rules = grouped_df[grouped_df['is_cde'].str.contains('False')]

# Load the original dataset from the Excel file
original_df = pd.read_excel("your_excel_file.xlsx")

# Get the indices of rows where 'rule_id' is in 'all_false_rules'
test_indices = original_df[original_df['rule_id'].isin(all_false_rules['rule_id'])].index

# Create the test DataFrame
test_df = original_df.loc[test_indices]

# Save the test DataFrame to test.csv
test_df.to_csv('test.csv', index=False)
