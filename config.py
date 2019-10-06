import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'aksfnvoaibgfvowane12kmnppwekgfnwpi'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@localhost:3306/vehiclemgmt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False