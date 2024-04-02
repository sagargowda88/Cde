import pandas as pd
import pyodbc

# Connect to your SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=your_server;'
                      'DATABASE=your_database;'
                      'UID=your_username;'
                      'PWD=your_password')

# Define your SQL query
sql_query = "SELECT * FROM your_table"

# Execute the query and fetch the results into a pandas DataFrame
df = pd.read_sql(sql_query, conn)

# Close the connection
conn.close()

# Save the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
