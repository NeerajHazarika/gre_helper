import sqlite3

# Connect to the database
conn = sqlite3.connect('../database.db')

# Create a cursor
cursor = conn.cursor()

# Execute the query to fetch the table names
query = "SELECT name FROM sqlite_master WHERE type='table';"
cursor.execute(query)

# Fetch all the table names
tables = cursor.fetchall()

# Print the table names
for table in tables:
    print(table[0])

# Close the cursor and connection
cursor.close()
conn.close()
