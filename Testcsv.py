import pandas as pd

# Read the pre-grouped Excel file into a pandas DataFrame
grouped_df = pd.read_excel("grouped_excel_file.xlsx")

# Load the original dataset from the Excel file
original_df = pd.read_excel("your_excel_file.xlsx")

# Define a lambda function to check if all 'is_cde' values are False for each 'rule_id'
all_false_cde = lambda x: all(val == 'False' for val in x.split(','))

# Filter 'rule_id' values where all 'is_cde' values are False
all_false_rule_ids = grouped_df[grouped_df['is_cde'].apply(all_false_cde)]['rule_id']

# Filter original DataFrame to get rows where 'rule_id' is in 'all_false_rule_ids' for test data
test_df = original_df[original_df['rule_id'].isin(all_false_rule_ids)]

# Save the test DataFrame to test.csv
test_df.to_csv('test.csv', index=False)

# Filter original DataFrame to get rows where 'rule_id' is not in 'all_false_rule_ids' for train data
train_df = original_df[~original_df['rule_id'].isin(all_false_rule_ids)]

# Save the train DataFrame to train.csv
train_df.to_csv('train.csv', index=False)
