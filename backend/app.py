import logging
import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from config import app_config
from frontend import frontend_bp
from api import api_bp

# Load environment variables from .env
load_dotenv()

def create_app(config_name):
    app = Flask(__name__)
    
    # Set the app configuration based on the provided config name
    app.config.from_object(app_config[config_name])

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

    frontend_base_url = os.environ.get("FRONTEND_BASE_URL", "http://localhost:3000")
    CORS(app, resources={r"*": {"origins": frontend_base_url}}, supports_credentials=True)
    
    return app


if __name__ == '__main__':
    # take app env as a cmdline argument (dev or prod) with --env flag
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--env', help='Environment')
    # args = parser.parse_args()
    # app_env = args.env
    app = create_app('development')

    app.run(host='0.0.0.0', port=5000)
else:
    gunicorn_app = create_app('development')