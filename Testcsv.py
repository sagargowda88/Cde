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

# Merge the original DataFrame with the grouped DataFrame on 'rule_id'
merged_df = pd.merge(df[['rule_id', 'rule_sql_filter', 'dataset_sql_filter', 'rule_name', 'owner_name']], 
                     grouped, 
                     on='rule_id')

# Define a function to check if all 'is_cde' values are False for a given 'is_cde' string
def all_false_cde(is_cde):
    return all(val == 'False' for val in is_cde.split(','))

# Filter rows where all 'is_cde' values are False
all_false_rows = merged_df[merged_df['is_cde'].apply(all_false_cde)]

# Save the filtered DataFrame to a test file
all_false_rows.to_csv('test.csv', index=False)

# Drop the filtered rows from the original DataFrame to create the train dataset
train_df = merged_df.drop(all_false_rows.index)

# Save the train dataset to a train file
train_df.to_csv('train.csv', index=False)

# Print confirmation message
print("Train and test datasets have been created.")
