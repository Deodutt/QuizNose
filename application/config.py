import os
import secretstuff
import boto3

app_dir = os.path.abspath(os.path.dirname(__file__))

def get_ssm_param(param_name: str):
    """Returns SSM value given a parameter name"""
    ssm = boto3.client("ssm")  # selecting what service

    parameter = ssm.get_parameter(
        Name=param_name, WithDecryption=True
    )  # grabbing the paramaeter that has the name/prod/db/password
    return parameter["Value"]

class BaseConfig:
    SECRET_KEY= 'testkey' #needed for cookie sessions. add to secrets file later
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USERNAME = secretstuff.emailusername
    MAIL_PASSWORD = secretstuff.emailpassword
    UPLOAD_FOLDER = "UPLOAD_FOLDER"
    DB_HOST = get_ssm_parameter("/QUIZNOSE/DB_ENDPOINT") #"database-1.cet4jo0trfys.us-east-1.rds.amazonaws.com"
    DB_USER = "admin"
    DB_PASSWORD = get_ssm_parameter("/QUIZNOSE/DB_PASS")# "KuraLabs#123"
    DB = "final"


class DevelopementConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') or  \
    #     'mysql+pymysql://root:pass@localhost/flask_app_db'
    

class TestingConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_DATABASE_URI') or \
    #                           'mysql+pymysql://root:pass@localhost/flask_app_db'    

class ProductionConfig(BaseConfig):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI') or  \
    #     'mysql+pymysql://root:pass@localhost/flask_app_db'

