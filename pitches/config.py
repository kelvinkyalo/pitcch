import os

class Config:
    SECRET_KEY='c1dd1056ef414905719940d2a9f3bef9mai'
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')