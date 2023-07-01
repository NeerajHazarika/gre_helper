import sqlite3

conn = sqlite3.connect('../database.db')
cursor = conn.cursor()

# Execute the DELETE statement to remove data from the table
delete_query = "DELETE FROM questions WHERE question_id = 1;"
cursor.execute(delete_query)

delete_query = "DELETE FROM questions WHERE question_id = 2;"
cursor.execute(delete_query)

delete_query = "DELETE FROM questions WHERE question_id = 3;"
cursor.execute(delete_query)

# Commit the changes and close the connection
conn.commit()
conn.close()