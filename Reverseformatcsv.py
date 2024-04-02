import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("your_csv_file.csv")

# Split the 'attribute_name' and 'is_cde' columns back into lists
df['attribute_name'] = df['attribute_name'].str.split(', ')
df['is_cde'] = df['is_cde'].str.split(', ')

# Create a list of dictionaries for each row with exploded lists
rows = []
for index, row in df.iterrows():
    for attr, cde in zip(row['attribute_name'], row['is_cde']):
        rows.append({
            'rule_id': row['rule_id'],
            'rule_sql_filter': row['rule_sql_filter'],
            'dataset_sql_filter': row['dataset_sql_filter'],
            'rule_name': row['rule_name'],
            'owner_name': row['owner_name'],
            'attribute_name': attr,
            'is_cde': cde
        })

# Create a DataFrame from the list of dictionaries
df_final = pd.DataFrame(rows)

# Write the DataFrame to an Excel file
df_final.to_excel("original_excel_file.xlsx", index=False)
