from flask import Blueprint, render_template, send_from_directory, request
import random

homepage_bp = Blueprint('homepage_bp', __name__)

@homepage_bp.route('/filestore/<path:filename>')
def serve_file(filename):
    """
    used to generate url for question images which are used in image src links in test page template
    """
    return send_from_directory('../file_store', filename)

@homepage_bp.route('/')
def homepage():
    """
    get request then show homepage
    (on click start test button redirected to instruction page)
    """
    return render_template('homepage.html')

@homepage_bp.route('/instruction', method = 'GET')
def instruction():
    """
    if get request then show instruction page and generate a test id and generate question set for that test id in database
    (onclick next button, test id will be sent as parameter and redirected /test route)
    """

    if request.args.get('test_id'):
        test_id = request.args.get('test_id')

    test_id = test_id_generator(-1)

    return render_template('instructionpage.html', test_id=test_id)

