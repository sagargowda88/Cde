 import pandas as pd

# Read the pre-grouped Excel file into a pandas DataFrame
grouped_df = pd.read_excel("grouped_excel_file.xlsx")

# Load the original dataset from the Excel file
original_df = pd.read_excel("your_excel_file.xlsx")

# Merge original_df with grouped_df on 'rule_id' to add 'is_cde' column
merged_df = pd.merge(original_df, grouped_df[['rule_id', 'is_cde']], on='rule_id')

# Define a function to check if all 'is_cde' values are False
def all_false(series):
    return all(val == 'False' for val in series)

# Group by 'rule_id' and check if all 'is_cde' values are False
all_false_rules = merged_df.groupby('rule_id')['is_cde'].apply(all_false)

# Get the rule_ids where all 'is_cde' values are False
all_false_rule_ids = all_false_rules[all_false_rules].index

# Filter original DataFrame to get rows where 'rule_id' is in 'all_false_rule_ids'
test_df = original_df[original_df['rule_id'].isin(all_false_rule_ids)]

# Save the test DataFrame to test.csv
test_df.to_csv('test.csv', index=False)

# Filter original DataFrame to get rows where 'rule_id' is not in 'all_false_rule_ids'
train_df = original_df[~original_df['rule_id'].isin(all_false_rule_ids)]

# Save the train DataFrame to train.csv
train_df.to_csv('train.csv', index=False)
