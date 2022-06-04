from os import getenv
from dotenv import load_dotenv
import os

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    TESTING = getenv('TESTING', True),
    DEBUG = getenv('DEBUG', True)
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    SECRET_KEY = getenv('SECRET_KEY', '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf')

    SQLALCHEMY_COMMIT_ON_TEARDOWN = getenv('SQLALCHEMY_COMMIT_ON_TEARDOWN', True)
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI', 'mysql://dev:dev@db/test')
    
    @staticmethod
    def init_app(app):
        pass
