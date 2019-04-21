import tempfile


db_file = tempfile.NamedTemporaryFile()


#mail client settings
MAIL_SETTINGS = {
    'mail_server': 'smtp.gmail.com',
    'mail_port': 465,
    'mail_use_ssl': True,
    'mail_use_tls': False,
    'mail_username': '',
    'mail_password': ''
}


class Config(object):
    SECRET_KEY = 'secret key'


class ProdConfig(Config):
    ENV = 'prod'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'

    CACHE_TYPE = 'simple'


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://CervisoftUser:CervisoftPassword@localhost/cervisoftdb'

    CACHE_TYPE = 'null'
    ASSETS_DEBUG = True
    MAIL_SERVER = MAIL_SETTINGS['mail_server']
    MAIL_PORT = MAIL_SETTINGS['mail_port']
    MAIL_USE_SSL = MAIL_SETTINGS['mail_use_ssl']
    MAIL_USE_TLS = MAIL_SETTINGS['mail_use_tls']
    MAIL_USERNAME = MAIL_SETTINGS['mail_username']
    MAIL_PASSWORD = MAIL_SETTINGS['mail_password']

class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_file.name
    SQLALCHEMY_ECHO = True

    CACHE_TYPE = 'null'
    WTF_CSRF_ENABLED = False
