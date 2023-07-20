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

    # Execute a query to retrieve data from a table
    cursor.execute('SELECT * FROM questions')

    # Fetch and display the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

conn.close()
