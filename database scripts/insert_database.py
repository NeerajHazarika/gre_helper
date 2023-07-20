import os
import pymysql
from google.cloud.sql.connector import Connector, IPTypes
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    connector = Connector(IPTypes.PUBLIC)  # Use IPTypes.PRIVATE if using a private IP

    instance_connection_name = os.environ.get("INSTANCE_CONNECTION_NAME")  # e.g. 'project:region:instance'
    db_user = os.environ.get("DB_USER")  # e.g. 'my-db-user'
    db_pass = os.environ.get("DB_PASSWORD")  # e.g. 'my-db-password'
    db_name = os.environ.get("DB_NAME")  # e.g. 'my-database'
    
    if not instance_connection_name:
        raise ValueError("The environment variable 'INSTANCE_CONNECTION_NAME' is not set.")

    conn = connector.connect(
        instance_connection_name,
        "pymysql",
        user=db_user,
        password=db_pass,
        db=db_name,
    )
    
    return conn

# Get the Cloud SQL connection
conn = get_db_connection()

# Create a cursor to execute queries
with conn.cursor() as cursor:
    # Insert Data: Use the execute() method to insert data into the tables.
    insert_query = """
    INSERT INTO questions (img_src, topic, type, passage_chart_img_src, correct_ans, section)
    VALUES (%s, %s, %s, %s, %s, %s);
    """ 

    # Edit values to insert rows to questions table
    values = [
        ('verbal_1.png', 'vocabulary, context', '1FIB', '', 'personable', 'verbal'),
        ('verbal_2.png', 'vocabulary, context', '1FIB', '', 'ersatz', 'verbal'),
        ('verbal_3.png', 'vocabulary, context', '2FIB', '', 'iteration, current', 'verbal'),
        ('verbal_4.png', 'vocabulary, context', '2FIB', '', 'solipsistic, arresting', 'verbal'),
        ('verbal_5.png', 'vocabulary, context', '3FIB', '', 'ran the gamut, ape, shabby', 'verbal'),
        ('verbal_6.png', 'vocabulary, context', '3FIB', '', 'hoi-polloi, parochial, facile', 'verbal'),
        ('verbal_7.png', 'vocabulary, context', 'SMCQ', '', 'c', 'verbal'),
        ('verbal_8.png', 'vocabulary, context', 'SMCQ', '', 'c', 'verbal'),
        ('verbal_9.png', 'vocabulary, context', 'PSMCQ', 'passage_1.png', 'c', 'verbal'),
        ('verbal_10.png', 'vocabulary, context', 'PSMCQ', 'passage_1.png', 'd', 'verbal'),
        ('verbal_11.png', 'vocabulary, context', 'PSMCQ', 'passage_1.png', 'a', 'verbal'),
        ('verbal_12.png', 'vocabulary, context', 'PSMCQ', 'passage_1.png', 'c', 'verbal'),
        ('verbal_13.png', 'vocabulary, context', '6DMCQ', '', 'patronizing, condescending', 'verbal'),
        ('verbal_14.png', 'vocabulary, context', '6DMCQ', '', 'ambivalent, equivocal', 'verbal'),
        ('verbal_15.png', 'vocabulary, context', '6DMCQ', '', 'overtake, outstrip', 'verbal'),
        ('verbal_16.png', 'vocabulary, context', '6DMCQ', '', 'foibles, peccadilloes', 'verbal'),
        ('verbal_17.png', 'vocabulary, context', 'PSMCQ', 'passage_2.png', 'b', 'verbal'),
        ('verbal_18.png', 'vocabulary, context', 'PSMCQ', 'passage_2.png', 'e', 'verbal'),
        ('verbal_19.png', 'vocabulary, context', '3PMMCQ', 'passage_3.png','a, b', 'verbal'),
        ('verbal_20.png', 'vocabulary, context', '3PMMCQ', 'passage_3.png', 'c', 'verbal'),
        ('math_1.png', 'vocabulary, context', 'QC', '', 'c', 'math'),
        ('math_2.png', 'vocabulary, context', 'QC', '', 'a', 'math'),
        ('math_3.png', 'vocabulary, context', 'QC', '', 'd', 'math'),
        ('math_4.png', 'vocabulary, context', 'QC', '', 'a', 'math'),
        ('math_5.png', 'vocabulary, context', 'QC', '', 'b', 'math'),
        ('math_6.png', 'vocabulary, context', 'QC', '', 'b', 'math'),
        ('math_7.png', 'vocabulary, context', 'QC', '', 'd', 'math'),
        ('math_8.png', 'vocabulary, context', 'QC', '', 'b', 'math'),
        ('math_9.png', 'vocabulary, context', 'SMCQ', '', 'b', 'math'),
        ('math_10.png', 'vocabulary, context', 'NEB', '', '7', 'math'),
        ('math_11.png', 'vocabulary, context', 'SMCQ', '', 'b', 'math'),
        ('math_12.png', 'vocabulary, context', 'NEB', '', '4800', 'math'),
        ('math_13.png', 'vocabulary, context', 'NEB', '', '917', 'math'),
        ('math_14.png', 'vocabulary, context', '3MMCQ', '', 'c', 'math'),
        ('math_15.png', 'vocabulary, context', 'PSMCQ', 'chart_1.png', 'a', 'math'),
        ('math_16.png', 'vocabulary, context', 'PSMCQ', 'chart_1.png', 'e', 'math'),
        ('math_17.png', 'vocabulary, context', 'PSMCQ', 'chart_1.png', 'd', 'math'),
        ('math_18.png', 'vocabulary, context', 'PSMCQ', 'chart_1.png', 'd', 'math'),
        ('math_19.png', 'vocabulary, context', 'PSMCQ', 'chart_1.png', 'd', 'math'),
        ('math_20.png', 'vocabulary, context', 'PSMCQ', 'chart_1.png', 'd', 'math')
        # Add other rows here
    ]

    # Execute the insert statements in a loop for each row
    for row_values in values:
        cursor.execute(insert_query, row_values)

    # Commit the changes to the database
    conn.commit()

# Close the connection to release the database resources
conn.close()
