import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel("your_excel_file.xlsx")

# Define a custom aggregation function to handle lists
def aggregate_lists(series):
    return list(series)

# Group by 'rule_id' and aggregate 'attribute_name' and 'is_cde' into lists
grouped = df.groupby('rule_id').agg({
    'attribute_name': aggregate_lists,
    'is_cde': aggregate_lists
}).reset_index()

# Merge the original DataFrame with the grouped DataFrame on 'rule_id'
merged_df = pd.merge(df[['rule_id', 'rule_sql_filter', 'dataset_sql_filter', 'rule_name', 'owner_name']], 
                     grouped, 
                     on='rule_id')

# Drop duplicate rows
final_df = merged_df.drop_duplicates()

# Print the final DataFrame
print(final_df)
