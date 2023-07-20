from flask import Blueprint, current_app, send_from_directory, jsonify, request, send_file
import os
from google.cloud.sql.connector import Connector, IPTypes
from google.cloud import storage
import pymysql
import random
import time
import json
from io import BytesIO

api_bp = Blueprint('api_bp', __name__)

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

@api_bp.route('/api/filestore/<path:filename>')
def serve_file(filename):
    """
    Used to generate a URL for question images which are used in image src links in the test page template.
    """
    # Initialize the Cloud Storage client
    storage_client = storage.Client()

    bucket = storage_client.bucket(os.environ.get('CLOUD_STORAGE_BUCKET'))
    blob = bucket.blob(f"file_store/{filename}")
    if blob.exists():
        # Set appropriate content-type based on the file type
        content_type = 'image/jpeg'  # Adjust as per your file type
        # Download the blob data as bytes
        file_data = blob.download_as_bytes()

        # Create a BytesIO object from the file data
        file_obj = BytesIO(file_data)
        
        # Return the file-like object using send_file
        return send_file(file_obj, mimetype=content_type)
    else:
        return "File not found", 404


@api_bp.route('/api/create_test/', methods=['POST'])
def create_test():
    """
    Takes in various test parameters and generates a question set for test_id, adds it to the database, and returns the test_id.
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        query = "SELECT question_id FROM questions WHERE section='verbal' ORDER BY RAND() LIMIT 20;"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Extract the first element from each tuple and convert it to a string
        converted_list = [str(item[0]) for item in rows]

        query = "SELECT question_id FROM questions WHERE section='math' ORDER BY RAND() LIMIT 20;"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Extract the first element from each tuple and convert it to a string
        converted_list += [str(item[0]) for item in rows]

        # Join the converted elements with commas
        output_string = ','.join(converted_list)

        query = "INSERT INTO tests (question_set_list) VALUES (%s);"
        cursor.execute(query, (output_string, ))

        test_id = str(cursor.lastrowid)

        conn.commit()

    conn.close()

    return jsonify(test_id=test_id)


@api_bp.route('/api/create_attempt/', methods=['POST'])
def create_attempt():
    """
    Create a random attempt id and check with the attempt table if it is available.
    If not, create a new attempt id until no collision occurs.
    Create empty column values except timestamp and update the attempt table.
    """ 
    conn = get_db_connection()
    with conn.cursor() as cursor:
        test_id = request.form.get('test_id')

        flag = [1]

        while len(flag) != 0:
            flag = None

            attempt_id = random.randint(0, 100000)

            query = "SELECT attempt_id FROM attempts WHERE attempt_id = %s"

            cursor.execute(query, (attempt_id,))
            flag = cursor.fetchall()

            if len(flag) == 0:
                validity = 1
                time_created = str(time.time())
                submission = "{}"
                recommended_test_id = -1
                tips = ""

                query = "INSERT INTO attempts (attempt_id, validity, test_id, time_created, submission, tips, recommended_test_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"

                cursor.execute(query, (attempt_id, validity, test_id, time_created, submission, tips, recommended_test_id))

                conn.commit()
                return jsonify(attempt_id=attempt_id)
    
    conn.close()
    return "Error"


@api_bp.route("/api/update_attempt/", methods=["POST"])
def update_attempt():
    """
    Updates attempt table with new submission data using question_no and selected_ans.
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        attempt_id = request.json.get("attempt_id")
        question_no = request.json.get("question_no")
        test_id = request.json.get("test_id")
        selected_ans = request.json.get("selected_ans")

        query = "SELECT question_set_list FROM tests WHERE test_id = %s"
        cursor.execute(query, (test_id,))
        ques_set = cursor.fetchone()[0]
        ques_set = ques_set.split(",")

        query = "SELECT submission FROM attempts WHERE attempt_id = %s"
        cursor.execute(query, (attempt_id,))
        submission = cursor.fetchone()[0]
        submission = json.loads(submission)

        submission[str(ques_set[int(question_no)])] = selected_ans
        submission = json.dumps(submission)

        query = "UPDATE attempts SET submission = %s WHERE attempt_id = %s"

        cursor.execute(query, (submission, attempt_id))

        conn.commit()

    conn.close()
    
    return jsonify({
        "success": True,
        "message": "Attempt updated successfully"
    }), 200


@api_bp.route("/api/get_question_type_page/<test_id>/<question_no>", methods=["GET"])
def get_question_type_page(test_id, question_no):
    type_to_templates = {
        "5DMCQ": "MCQ/DMCQ/5DMCQ.html",
        "6DMCQ": "MCQ/DMCQ/6DMCQ.html",
        "5PDMCQ": "MCQ/DMCQ/5PDMCQ.html",
        "6PDMCQ": "MCQ/DMCQ/6PDMCQ.html",
        "3MMCQ": "MCQ/MMCQ/3MMCQ.html",
        "4MMCQ": "MCQ/MMCQ/4MMCQ.html",
        "5MMCQ": "MCQ/MMCQ/5MMCQ.html",
        "6MMCQ": "MCQ/MMCQ/6MMCQ.html",
        "3PMMCQ": "MCQ/MMCQ/3PMMCQ.html",
        "4PMMCQ": "MCQ/MMCQ/4PMMCQ.html",
        "5PMMCQ": "MCQ/MMCQ/5PMMCQ.html",
        "6PMMCQ": "MCQ/MMCQ/6PMMCQ.html",
        "PSMCQ": "MCQ/SMCQ/PSMCQ.html",
        "QC": "MCQ/SMCQ/QC.html",
        "SMCQ": "MCQ/SMCQ/SMCQ.html",
        "4TMCQ": "MCQ/TMCQ/4TMCQ.html",
        "4PTMCQ": "MCQ/TMCQ/4PTMCQ.html",
        "1FIB": "NEB/FIB/1FIB.html",
        "2FIB": "NEB/FIB/2FIB.html",
        "3FIB": "NEB/FIB/3FIB.html",
        "FNEB": "NEB/FNEB/FNEB.html",
        "NEB": "NEB/NEB/NEB.html"
    }

    conn = get_db_connection()
    with conn.cursor() as cursor:
        # GET ques_set from tests table
        query = "SELECT question_set_list FROM tests WHERE test_id = %s"
        cursor.execute(query, (test_id,))
        ques_set = cursor.fetchone()[0]
        ques_set = ques_set.split(",")

        ques_id = ques_set[int(question_no)]

        # GET ques_img_src FROM questions table
        query = "SELECT type FROM questions WHERE question_id = %s"
        cursor.execute(query, (ques_id,))
        question_type = cursor.fetchone()[0]

    conn.close()

    return jsonify(type_to_templates=type_to_templates[question_type])


@api_bp.route("/api/get_ques_img_src/test/<test_id>/question/<question_no>/", methods=["GET"])
def get_ques_img_src(test_id, question_no):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        # GET ques_set from tests table
        query = "SELECT question_set_list FROM tests WHERE test_id = %s"
        cursor.execute(query, (test_id,))
        ques_set = cursor.fetchone()[0]
        ques_set = ques_set.split(",")

        ques_id = ques_set[int(question_no)]

        # GET ques_img_src FROM questions table
        query = "SELECT img_src FROM questions WHERE question_id = %s"
        cursor.execute(query, (ques_id,))
        ques_img_src = cursor.fetchone()[0]

        # GET passage_chart_img_src FROM questions table
        query = "SELECT passage_chart_img_src FROM questions WHERE question_id = %s"
        cursor.execute(query, (ques_id,))
        passage_chart_img_src = cursor.fetchone()[0]

    conn.close()

    return jsonify(ques_img_src=ques_img_src, passage_chart_img_src=passage_chart_img_src)


@api_bp.route('/api/submit_attempt/', methods=['POST'])
def submit_attempt():
    """
    Updates attempt validity to False and returns back with a score between 260 and 340.
    """
    conn = get_db_connection()
    with conn.cursor() as cursor:
        attempt_id = request.json.get("attempt_id")

        query = "UPDATE attempts SET validity = 0 WHERE attempt_id = %s"
        cursor.execute(query, (attempt_id,))

        conn.commit()

    conn.close()
        
    return jsonify({
        "success": True,
        "message": "Attempt submitted successfully"
    }), 200


@api_bp.route('/api/get_score/<attempt_id>')
def get_score(attempt_id):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        query = "SELECT submission FROM attempts WHERE attempt_id = %s"
        cursor.execute(query, (attempt_id,))
        submission = cursor.fetchone()[0]
        submission = json.loads(submission)

        score = 260

        for question_id, selected_ans in submission.items():
            query = "SELECT correct_ans FROM questions WHERE question_id = %s"
            cursor.execute(query, (question_id,))
            correct_answer = cursor.fetchone()[0]
            correct_answer = correct_answer.split(",")

            # Handle cases where selected_ans is None or an empty list
            if selected_ans is None:
                selected_ans = []

            # If selected_ans is not None, split the string into a list
            elif isinstance(selected_ans, str):
                selected_ans = selected_ans.split(",")

            # Sort both selected_ans and correct_answer lists for comparison
            selected_ans.sort()
            correct_answer.sort()

            if selected_ans == correct_answer:
                score += 2

    conn.close()

    return jsonify({
        "success": True,
        "score": score,
    }), 200

