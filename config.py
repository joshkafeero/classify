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

class Utilities:
    features_file = 'features.txt'
    features_file2 = 'features2.txt'
    model ='finalized_model.sav'
    final_data ='final_data.csv'