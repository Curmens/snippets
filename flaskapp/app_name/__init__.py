from flask import Flask
from app_name.config import Config
# Custom imports



# Initialize imports here


def create_app(config_class=Config):
    app = Flask(__name__)
    # configure imports
    return app                                 