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
    # CREATE TABLE questions if it doesnt exist
    create_questions_table_query = """
    CREATE TABLE IF NOT EXISTS questions (
        question_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        img_src TEXT,
        topic TEXT,
        type TEXT,
        passage_chart_img_src TEXT,
        correct_ans TEXT,
        section TEXT
    );
    """ 

    cursor.execute(create_questions_table_query) # Use the execute() method of the cursor object to execute the SQL statements.

    # CREATE TABLE test if it doesnt exist
    create_test_table_query = """
    CREATE TABLE IF NOT EXISTS tests (
        test_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        question_set_list TEXT
    );
    """ 

    cursor.execute(create_test_table_query) # Use the execute() method of the cursor object to execute the SQL statements.

    # CREATE TABLE attempt if it doesnt exist
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
