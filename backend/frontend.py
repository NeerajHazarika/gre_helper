from flask import Blueprint, render_template, current_app, request
import requests

frontend_bp = Blueprint('frontend_bp', __name__)

@frontend_bp.route('/')
def homepage():
    """
    get request then show homepage
    (on click start test button redirected to instruction page)
    """
    return render_template('homepage.html')


@frontend_bp.route('/instruction', methods = ['GET'])
def instruction():
    """
    if get request then show instruction page and generate a test id and generate question set for that test id in database
    (onclick next button, test id will be sent as parameter and redirected /test route)
    """

    test_id = request.args.get('test_id')
    attempt_id = request.args.get('attempt_id')

    return render_template('instructionpage.html', test_id = test_id, attempt_id = attempt_id)


@frontend_bp.route('/test/<test_id>')
@frontend_bp.route('/test/<test_id>/question/<question_no>')
def test(test_id, question_no=0):
    """
    based on the test id return question set in pagination form
    """

    # Make API call to get ques_img_src
    response = requests.get(f'http://localhost:5000/api/get_ques_img_src/test/{test_id}/question/{question_no}/')
    ques_img_src = response.json().get('ques_img_src')

    return render_template('testpage.html', ques_img_src=ques_img_src, test_id=test_id, question_no=question_no)


@frontend_bp.route('/test/<test_id>/attempt/<attempt_id>/question/<question_no>', methods = ['GET'])
def test_attempt(test_id, attempt_id, question_no):
    """
    display question template according to question type
    """

    # Make API call to get template name
    response = requests.get(f'http://localhost:5000/api/get_question_type_page/{test_id}/{question_no}')
    question_type_html = response.json().get('type_to_templates')

    # Make API call to get ques_img_src & passage_chart_img_src
    response = requests.get(f'http://localhost:5000/api/get_ques_img_src/test/{test_id}/question/{question_no}/')
    ques_img_src = response.json().get('ques_img_src')
    passage_chart_img_src = response.json().get('passage_chart_img_src')

    return render_template(f"questions/{question_type_html}", ques_img_src=ques_img_src, passage_chart_img_src=passage_chart_img_src, test_id=test_id, attempt_id=attempt_id, question_no=question_no)


@frontend_bp.route('/performancereport/<attempt_id>')
def perform_performacepage(attempt_id):
    return render_template("performancereport.html", attempt_id=attempt_id)


@frontend_bp.route('/frontend/testing/')
def frontend_testing():

    # Make API call to get ques_img_src
    response = requests.get('http://localhost:5000/api/get_ques_img_src/test/1/question/1/')
    ques_img_src = response.json().get('ques_img_src')

    return render_template('testpage.html', ques_img_src=ques_img_src, question_no=1)