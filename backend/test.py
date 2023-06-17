from flask import Blueprint, render_template

test_bp = Blueprint('test_bp', __name__)

def test_id_gen():
    """
    takes in various test parameters () and generates a question set for test_id and adds it to the database and returns the test_id
    """
    return test_id

@test_bp.route('/test/<test_id>')
@test_bp.route('/test/<test_id>/question/<question_id>')
def test(test_id, question_id=0):
    """
    based on the test id return question set in pagination form
    """

    question_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    return render_template('testpage.html', test_id = test_id, question_id = int(question_id), question_set = question_set)

