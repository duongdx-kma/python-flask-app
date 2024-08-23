import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Writer database connection string
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(
        os.environ.get('WRITE_DB_USER', 'duongdx'),
        os.environ.get('WRITE_DB_PASSWORD', 'duongdx1'),
        os.environ.get('WRITE_DB_HOST', 'localhost'),
        os.environ.get('DB_PORT', 3306),
        os.environ.get('DB_NAME', 'webappdb')
    )

    # Reader database connection string
    SQLALCHEMY_BINDS = {
        'read': "mysql+pymysql://{}:{}@{}:{}/{}".format(
            os.environ.get('READ_DB_USER', 'duongdx'),
            os.environ.get('READ_DB_PASSWORD', 'duongdx1'),
            os.environ.get('READ_DB_HOST', 'localhost'),
            os.environ.get('DB_PORT', 3306),
            os.environ.get('DB_NAME', 'webappdb')
        )
    }

    # Security key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'

    # SQLAlchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
