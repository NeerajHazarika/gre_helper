from flask import Flask
from frontend import frontend_bp
from api import api_bp
from config import app_config
from dotenv import load_dotenv

load_dotenv()

def create_app(config_name):
    app = Flask(__name__)
    
    # Set the app configuration based on the provided config name
    app.config.from_object(app_config[config_name])

    app.register_blueprint(frontend_bp)
    app.register_blueprint(api_bp)
    
    return app


if __name__ == '__main__':
    app = create_app('development')

    app.run(host='0.0.0.0', port=5000)
else:
    gunicorn_app = create_app('development')
