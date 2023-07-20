from flask import Blueprint, current_app, send_from_directory, jsonify, request
import sqlite3
import random
import time
import json

api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/api/filestore/<path:filename>')
def serve_file(filename):
    """
    used to generate url for question images which are used in image src links in test page template
    """
    return send_from_directory('../file_store', filename)


@api_bp.route('/api/create_test/', methods=['POST'])
def create_test():
    """
    takes in various test parameters () and generates a question set for test_id and adds it to the database and returns the test_id
    """
    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()

    query = "SELECT question_id FROM questions WHERE section='verbal' ORDER BY RANDOM() LIMIT 20;"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Extract the first element from each tuple and convert it to a string
    converted_list = [str(item[0]) for item in rows]

    query = "SELECT question_id FROM questions WHERE section='math' ORDER BY RANDOM() LIMIT 20;"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Extract the first element from each tuple and convert it to a string
    converted_list += [str(item[0]) for item in rows]

    # Join the converted elements with commas
    output_string = ','.join(converted_list)

    query = "INSERT INTO tests (question_set_list) VALUES (?);"
    cursor.execute(query, (output_string, ))

    test_id = str(cursor.lastrowid)

    conn.commit()
    conn.close()

    return jsonify(test_id=test_id)

@api_bp.route('/api/create_attempt/', methods=['POST'])
def create_attempt():
    """
    Create a random attempt id and 
    check with attempt table if available
    if not create a new attempt id until no collision

    create empty column values except timestamp
    and update attempt table
    """ 

    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()

    test_id = request.form.get('test_id')

    flag = [1]

    while len(flag) != 0:
        flag = None

        attempt_id = random.randint(0, 100000)

        query = "SELECT attempt_id FROM attempts WHERE attempt_id = ?"

        cursor.execute(query, (attempt_id, ))

        flag = cursor.fetchall()

        if len(flag) == 0:
            validity = 1;
            time_created = str(time.time())
            submission = "{}"
            recommended_test_id = -1
            tips = ""

            query = "INSERT INTO attempts (attempt_id, validity, test_id, time_created, submission, tips, recommended_test_id) VALUES (?, ?, ?, ?, ?, ?, ?)"

            cursor.execute(query, (attempt_id, validity, test_id, time_created, submission, tips, recommended_test_id))

            conn.commit()
            conn.close()
            return jsonify(attempt_id=attempt_id)
    
    conn.close()
    return "Error"


@api_bp.route("/api/update_attempt/", methods=["POST"])
def update_attempt():
    """
    updates attempt table with new submission data using question_no and selected_ans
    """
    conn = sqlite3.connect("../database.db")
    cursor = conn.cursor()

    attempt_id = request.json.get("attempt_id")
    question_no = request.json.get("question_no")
    test_id = request.json.get("test_id")
    selected_ans = request.json.get("selected_ans")

    query = "SELECT question_set_list FROM tests WHERE test_id = ?"
    cursor.execute(query, (test_id,))
    ques_set = cursor.fetchone()[0]
    ques_set = ques_set.split(",")

    query = "SELECT submission FROM attempts WHERE attempt_id = ?"
    cursor.execute(query, (attempt_id,))
    submission = cursor.fetchone()[0]
    submission = json.loads(submission)

    submission[str(ques_set[int(question_no)])] = selected_ans
    submission = json.dumps(submission)

    query = "UPDATE attempts SET submission = ? WHERE attempt_id = ?"

    cursor.execute(query, (submission, attempt_id))

    conn.commit()
    conn.close()
    
    return jsonify({
        "success": True,
        "message": "Attempt updated successfully"
    }), 200


@api_bp.route("/api/get_question_type_page/<test_id>/<question_no>", methods=["GET"])
def get_question_type_page(test_id, question_no):
    type_to_templates = {"5DMCQ":"MCQ/DMCQ/5DMCQ.html",
                         "6DMCQ":"MCQ/DMCQ/6DMCQ.html", 
                         "5PDMCQ":"MCQ/DMCQ/5PDMCQ.html", 
                         "6PDMCQ":"MCQ/DMCQ/6PDMCQ.html", 
                         "3MMCQ":"MCQ/MMCQ/3MMCQ.html", 
                         "4MMCQ":"MCQ/MMCQ/4MMCQ.html", 
                         "5MMCQ":"MCQ/MMCQ/5MMCQ.html", 
                         "6MMCQ":"MCQ/MMCQ/6MMCQ.html", 
                         "3PMMCQ":"MCQ/MMCQ/3PMMCQ.html", 
                         "4PMMCQ":"MCQ/MMCQ/4PMMCQ.html", 
                         "5PMMCQ":"MCQ/MMCQ/5PMMCQ.html", 
                         "6PMMCQ":"MCQ/MMCQ/6PMMCQ.html", 
                         "PSMCQ":"MCQ/SMCQ/PSMCQ.html",
                         "QC":"MCQ/SMCQ/QC.html", 
                         "SMCQ":"MCQ/SMCQ/SMCQ.html", 
                         "4TMCQ":"MCQ/TMCQ/4TMCQ.html",
                         "4PTMCQ":"MCQ/TMCQ/4PTMCQ.html",
                         "1FIB": "NEB/FIB/1FIB.html",
                         "2FIB": "NEB/FIB/2FIB.html",
                         "3FIB": "NEB/FIB/3FIB.html",
                         "FNEB":"NEB/FNEB/FNEB.html", 
                         "NEB":"NEB/NEB/NEB.html"
                         }

    conn = sqlite3.connect("../database.db")
    cursor = conn.cursor()

    # GET ques_set from tests table
    query = "SELECT question_set_list FROM tests WHERE test_id = ?"
    cursor.execute(query, (test_id,))
    ques_set = cursor.fetchone()[0]
    ques_set = ques_set.split(",")

    ques_id = ques_set[int(question_no)]

    # GET ques_img_src FROM questions table
    query = "SELECT type FROM questions WHERE question_id = ?"
    cursor.execute(query, (ques_id,))
    type = cursor.fetchone()[0]

    conn.close()

    current_app.logger.info(jsonify(type_to_templates=type_to_templates[type]))

    return jsonify(type_to_templates=type_to_templates[type])

@api_bp.route("/api/get_ques_img_src/test/<test_id>/question/<question_no>/", methods=["GET"])
def get_ques_img_src(test_id, question_no):
    conn = sqlite3.connect("../database.db")
    cursor = conn.cursor()

    # GET ques_set from tests table
    query = "SELECT question_set_list FROM tests WHERE test_id = ?"
    cursor.execute(query, (test_id,))
    ques_set = cursor.fetchone()[0]
    ques_set = ques_set.split(",")

    ques_id = ques_set[int(question_no)]

    # GET ques_img_src FROM questions table
    query = "SELECT img_src FROM questions WHERE question_id = ?"
    cursor.execute(query, (ques_id,))
    ques_img_src = cursor.fetchone()[0]

    # GET passage_chart_img_src FROM questions table
    query = "SELECT passage_chart_img_src FROM questions WHERE question_id = ?"
    cursor.execute(query, (ques_id,))
    passage_chart_img_src = cursor.fetchone()[0]

    conn.close()

    current_app.logger.info(jsonify(ques_img_src=ques_img_src, passage_chart_img_src=passage_chart_img_src))

    return jsonify(ques_img_src=ques_img_src, passage_chart_img_src=passage_chart_img_src)


@api_bp.route('/api/submit_attempt/', methods=['POST'])
def submit_attempt():
    """
    updates attempt validity to False and return back with score 260-340
    """
    conn = sqlite3.connect("../database.db")
    cursor = conn.cursor()

    attempt_id = request.json.get("attempt_id")

    query = "UPDATE attempts SET validity = 0 WHERE attempt_id = ?"
    cursor.execute(query, (attempt_id,))

    conn.commit()
    conn.close()
        
    return jsonify({
        "success": True,
        "message": "Attempt submitted successfully"
    }), 200


@api_bp.route('/api/get_score/<attempt_id>')
def get_score(attempt_id):
    conn = sqlite3.connect("../database.db")
    cursor = conn.cursor()

    query = "SELECT submission FROM attempts WHERE attempt_id = ?"
    cursor.execute(query, (attempt_id,))
    submission = cursor.fetchone()[0]
    submission = json.loads(submission)

    score = 260

    for question_id, selected_ans in submission.items():
        query = "SELECT correct_ans FROM questions WHERE question_id = ?"
        cursor.execute(query, (question_id,))
        correct_answer = cursor.fetchone()[0]
        correct_answer = correct_answer.split(",")

        selected_ans = selected_ans.split(",")

        if correct_answer == selected_ans:
            score += 2
    
    return jsonify({
        "success": True,
        "score": score,
    }), 200