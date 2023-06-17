import sqlite3 # Import the SQLite3 Module: In your database_setup.py script, import the sqlite3 module to enable interaction with the SQLite database.

conn = sqlite3.connect('../database.db') # Establish a Connection: Use the connect() function from the sqlite3 module to establish a connection to the SQLite database. Provide the desired database name as an argument, and SQLite will create a new database file if it doesn't already exist.

cursor = conn.cursor() # Create a Cursor: A cursor object allows you to execute SQL statements and interact with the database. Create a cursor using the cursor() method on the connection object.

# Create Tables: Write SQL statements to create the necessary tables in your SQLite database. 
create_table_query = """
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    img TEXT,
    topic TEXT,
    type TEXT,
    correct_ans TEXT,
    section TEXT
);
""" 

cursor.execute(create_table_query) # Use the execute() method of the cursor object to execute the SQL statements.

# Insert Data: Use the execute() method to insert data into the tables. Write SQL statements with placeholders (?) for the values that will be inserted. Pass the values as a tuple or a list as the second argument of the execute() method.
insert_query = """
INSERT INTO questions (img, topic, type, correct_ans, section)
VALUES (?, ?, ?, ?, ?);
""" 
values = ('verbal_3.png', 'vocabulary, context', 'fitb', 'iteration, current', 'verbal')
cursor.execute(insert_query, values)

# Commit and Close: After executing the necessary SQL statements, commit the changes to the database using the commit() method on the connection object. Then, close the connection to release the database resources.
conn.commit()
conn.close()
