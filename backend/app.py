from flask import Flask
from home import homepage_bp
from test import test_bp

app = Flask(__name__)

app.register_blueprint(homepage_bp)
app.register_blueprint(test_bp)

if __name__ == '__main__':
    app.run(debug=True)