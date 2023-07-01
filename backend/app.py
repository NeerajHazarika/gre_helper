import logging
from flask import Flask
from frontend import frontend_bp
from api import api_bp

app = Flask(__name__)

# Add the handler to the Flask app's logger
app.logger.setLevel(logging.INFO)

# Create a file handler for the log file
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

# Create a log formatter and add it to the file handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
app.logger.addHandler(file_handler)

app.register_blueprint(frontend_bp)
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)