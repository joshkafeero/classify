from os import environ
from dotenv import load_dotenv
import psycopg2 


load_dotenv() # Helps you load things from .env file , exposes contents of the .env files 


class Config(object):
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = environ.get('SECRET_KEY')
    
    #SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI='sqlite:///classify.db'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:SomePassword@localhost/classify_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = environ.get('EMAIL_USER')
    MAIL_PASSWORD = environ.get('EMAIL_PASS')
    #AWS
    import os

    AWS_DEFAULT_REGION = os.environ["AWS_REGION"]
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_COOKIE_SECURE = True

    # We're ok to set this off, as Cognito OAuth state provides protection
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_ALGORITHM = "RS256"
    JWT_IDENTITY_CLAIM = "sub"

    SECRET_KEY = os.environ["SECRET_KEY"]
    JWT_PRIVATE_KEY = os.environ["JWT_PRIVATE_KEY"]
    #  We're using Cognito to generate keys, so this is never used
    JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
    AWS_COGNITO_DOMAIN = os.environ["AWS_COGNITO_DOMAIN"]
    AWS_COGNITO_USER_POOL_ID = os.environ["AWS_COGNITO_USER_POOL_ID"]
    AWS_COGNITO_USER_POOL_CLIENT_ID = os.environ["AWS_COGNITO_USER_POOL_CLIENT_ID"]
    AWS_COGNITO_USER_POOL_CLIENT_SECRET = os.environ["AWS_COGNITO_USER_POOL_CLIENT_SECRET"]
    AWS_COGNITO_REDIRECT_URL = os.environ["SITE_URL"] + "/loggedin"

class Utilities:
    features_file = 'features.txt'
    features_file2 = 'features2.txt'
    model ='finalized_model.sav'
    final_data ='final_data.csv'