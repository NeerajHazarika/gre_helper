import sqlite3 # Import the SQLite3 Module: In your database_setup.py script, import the sqlite3 module to enable interaction with the SQLite database.

conn = sqlite3.connect('../database.db') # Establish a Connection: Use the connect() function from the sqlite3 module to establish a connection to the SQLite database. Provide the desired database name as an argument, and SQLite will create a new database file if it doesn't already exist.

cursor = conn.cursor() # Create a Cursor: A cursor object allows you to execute SQL statements and interact with the database. Create a cursor using the cursor() method on the connection object.

# Insert Data: Use the execute() method to insert data into the tables. Write SQL statements with placeholders (?) for the values that will be inserted. Pass the values as a tuple or a list as the second argument of the execute() method.
update_query = """
UPDATE questions
SET correct_ans = 'ersatz'
WHERE id = 2;
""" 
cursor.execute(update_query)

# Commit and Close: After executing the necessary SQL statements, commit the changes to the database using the commit() method on the connection object. Then, close the connection to release the database resources.
conn.commit()
conn.close()
