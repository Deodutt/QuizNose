import os
import secretstuff
import aws_param as aws

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = "testkey"  # needed for cookie sessions. add to secrets file later
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = aws.get_ssm_parameter("/QUIZNOSE/MAIL_USER")
    MAIL_PASSWORD = aws.get_ssm_parameter("/QUIZNOSE/MAIL_PASS")
    UPLOAD_FOLDER = "UPLOAD_FOLDER"
    DB_HOST = aws.get_ssm_parameter("/QUIZNOSE/DB_ENPOINT")  # "database-1.cet4jo0trfys.us-east-1.rds.amazonaws.com"
    DB_USER = aws.get_ssm_parameter("/QUIZNOSE/DB_USER")
    DB_PASSWORD = aws.get_ssm_parameter("/QUIZNOSE/DB_PASS")  # "KuraLabs#123"
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
