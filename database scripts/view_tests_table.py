import sqlite3

# Connect to the database
conn = sqlite3.connect('../database.db')

# Create a cursor
cursor = conn.cursor()

# Execute a query to retrieve data from a table
cursor.execute('SELECT * FROM tests')

# Fetch and display the results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
