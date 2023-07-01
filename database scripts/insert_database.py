import sqlite3 # Import the SQLite3 Module: In your database_setup.py script, import the sqlite3 module to enable interaction with the SQLite database.

conn = sqlite3.connect('../database.db') # Establish a Connection: Use the connect() function from the sqlite3 module to establish a connection to the SQLite database. Provide the desired database name as an argument, and SQLite will create a new database file if it doesn't already exist.

cursor = conn.cursor() # Create a Cursor: A cursor object allows you to execute SQL statements and interact with the database. Create a cursor using the cursor() method on the connection object.

# Insert Data: Use the execute() method to insert data into the tables. Write SQL statements with placeholders (?) for the values that will be inserted. Pass the values as a tuple or a list as the second argument of the execute() method.
insert_query = """
INSERT INTO questions (img_src, topic, type, passage_chart_img_src, correct_ans, section)
VALUES (?, ?, ?, ?, ?, ?);
""" 

# Edit values to insert rows to questions table

values = ('verbal_1.png', 'vocabulary, context', '1FIB', '', 'personable', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_2.png', 'vocabulary, context', '1FIB', '', 'ersatz', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_3.png', 'vocabulary, context', '2FIB', '', 'iteration, current', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_4.png', 'vocabulary, context', '2FIB', '', 'solipsistic, arresting', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_5.png', 'vocabulary, context', '3FIB', '', 'ran the gamut, ape, shabby', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_6.png', 'vocabulary, context', '3FIB', '', 'hoi-polloi, parochial, facile', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_7.png', 'vocabulary, context', 'SMCQ', '', 'c', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_8.png', 'vocabulary, context', 'SMCQ', '', 'c', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_9.png', 'vocabulary, context', 'PSMCQ', 'passage_1.png', 'c', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_10.png', 'vocabulary, context', 'PSMCQ', 'passage_1.png', 'd', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_11.png', 'vocabulary, context', 'PSMCQ', 'passage_1.png', 'a', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_12.png', 'vocabulary, context', 'PSMCQ', 'passage_1.png', 'c', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_13.png', 'vocabulary, context', '6DMCQ', '', 'patronizing, condescending', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_14.png', 'vocabulary, context', '6DMCQ', '', 'ambivalent, equivocal', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_15.png', 'vocabulary, context', '6DMCQ', '', 'overtake, outstrip', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_16.png', 'vocabulary, context', '6DMCQ', '', 'foibles, peccadilloes', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_17.png', 'vocabulary, context', 'PSMCQ', 'passage_2.png', 'b', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_18.png', 'vocabulary, context', 'PSMCQ', 'passage_2.png', 'e', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_19.png', 'vocabulary, context', '3PMMCQ', 'passage_3.png','a, b', 'verbal')
cursor.execute(insert_query, values)

values = ('verbal_20.png', 'vocabulary, context', '3PMMCQ', 'passage_3.png', 'c', 'verbal')
cursor.execute(insert_query, values)

# Edit values to insert rows to questions table
values = ('math_1.png', 'vocabulary, context', 'QC', '', 'c', 'math')
cursor.execute(insert_query, values)

values = ('math_2.png', 'vocabulary, context', 'QC', '', 'a', 'math')
cursor.execute(insert_query, values)

values = ('math_3.png', 'vocabulary, context', 'QC', '', 'd', 'math')
cursor.execute(insert_query, values)

values = ('math_4.png', 'vocabulary, context', 'QC', '', 'a', 'math')
cursor.execute(insert_query, values)

values = ('math_5.png', 'vocabulary, context', 'QC', '', 'b', 'math')
cursor.execute(insert_query, values)

values = ('math_6.png', 'vocabulary, context', 'QC', '', 'b', 'math')
cursor.execute(insert_query, values)

values = ('math_7.png', 'vocabulary, context', 'QC', '', 'd', 'math')
cursor.execute(insert_query, values)

values = ('math_8.png', 'vocabulary, context', 'QC', '', 'b', 'math')
cursor.execute(insert_query, values)

values = ('math_9.png', 'vocabulary, context', 'SMCQ', '', 'b', 'math')
cursor.execute(insert_query, values)

values = ('math_10.png', 'vocabulary, context', 'NEB', '', '7', 'math')
cursor.execute(insert_query, values)

values = ('math_11.png', 'vocabulary, context', 'SMCQ', '', 'b', 'math')
cursor.execute(insert_query, values)

values = ('math_12.png', 'vocabulary, context', 'NEB', '', '4800', 'math')
cursor.execute(insert_query, values)

values = ('math_13.png', 'vocabulary, context', 'NEB', '', '917', 'math')
cursor.execute(insert_query, values)

values = ('math_14.png', 'vocabulary, context', '3MMCQ', '', 'c', 'math')
cursor.execute(insert_query, values)

values = ('math_15.png', 'vocabulary, context', 'PSMCQ', 'chart_1.png', 'a', 'math')
cursor.execute(insert_query, values)

values = ('math_16.png', 'vocabulary, context', 'PSMCQ', 'chart_1.png', 'e', 'math')
cursor.execute(insert_query, values)

values = ('math_17.png', 'vocabulary, context', 'PSMCQ', 'chart_1.png', 'd', 'math')
cursor.execute(insert_query, values)

values = ('math_18.png', 'vocabulary, context', 'PSMCQ', 'chart_1.png', 'd', 'math')
cursor.execute(insert_query, values)

values = ('math_19.png', 'vocabulary, context', 'PSMCQ', 'chart_1.png', 'd', 'math')
cursor.execute(insert_query, values)

values = ('math_20.png', 'vocabulary, context', 'PSMCQ', 'chart_1.png', 'd', 'math')
cursor.execute(insert_query, values)


# Commit and Close: After executing the necessary SQL statements, commit the changes to the database using the commit() method on the connection object. Then, close the connection to release the database resources.
conn.commit()
conn.close()
