from os import getenv
from dotenv import load_dotenv
import os

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    TESTING = getenv('TESTING'),
    DEBUG = getenv('DEBUG')
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    SECRET_KEY = getenv('SECRET_KEY')

    SQLALCHEMY_COMMIT_ON_TEARDOWN = getenv('SQLALCHEMY_COMMIT_ON_TEARDOWN')
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')

    @staticmethod
    def init_app(app):
        pass
