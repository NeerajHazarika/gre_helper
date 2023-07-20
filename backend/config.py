import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    API_URL = 'http://localhost:5000'

class ProductionConfig(Config):
    API_URL = os.environ.get('API_URL')  # HTTPS URL for production

# Define a dictionary to map the config names to their corresponding classes
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}