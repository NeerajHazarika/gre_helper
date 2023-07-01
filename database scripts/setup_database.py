import sqlite3 # Import the SQLite3 Module: In your database_setup.py script, import the sqlite3 module to enable interaction with the SQLite database.

conn = sqlite3.connect('../database.db') # Establish a Connection: Use the connect() function from the sqlite3 module to establish a connection to the SQLite database. Provide the desired database name as an argument, and SQLite will create a new database file if it doesn't already exist.

cursor = conn.cursor() # Create a Cursor: A cursor object allows you to execute SQL statements and interact with the database. Create a cursor using the cursor() method on the connection object.

## CREATE TABLE questions if it doesnt exist
# create_questions_table_query = """
# CREATE TABLE IF NOT EXISTS questions (
#     question_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     img_src TEXT,
#     topic TEXT,
#     type TEXT,
#     passage_chart_img_src TEXT,
#     correct_ans TEXT,
#     section TEXT
# );
# """ 

# cursor.execute(create_questions_table_query) # Use the execute() method of the cursor object to execute the SQL statements.

# ## CREATE TABLE test if it doesnt exist
# create_test_table_query = """
# CREATE TABLE IF NOT EXISTS tests (
#     test_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     question_set_list TEXT
# );
# """ 

# cursor.execute(create_test_table_query) # Use the execute() method of the cursor object to execute the SQL statements.

## CREATE TABLE attempt if it doesnt exist
create_attempt_table_query = """
CREATE TABLE IF NOT EXISTS attempts (
    attempt_id INTEGER PRIMARY KEY,
    validity INTEGER,
    test_id INTEGER,
    time_created TEXT,
    submission TEXT,
    tips TEXT,
    recommended_test_id INTEGER
);
""" 

cursor.execute(create_attempt_table_query)

# Commit and Close: After executing the necessary SQL statements, commit the changes to the database using the commit() method on the connection object. Then, close the connection to release the database resources.
conn.commit()
conn.close()
