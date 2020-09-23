from .base import *

DEBUG=True
HOST = "http://127.0.0.1:10637"
ALLOWED_HOSTS = ["*"]

AUTH_SERVER_LOGIN = ROOT_SERVER + "/login"

AUTH_SERVER_AUTHENTICATE = ROOT_SERVER + "/authenticate"

AUTH_SERVER_LOGOUT = ROOT_SERVER + "/logout"

AUTH_SERVER_TOKEN = ROOT_SERVER + "/token"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'), # dbname
        'USER': os.getenv('MYSQL_ID'), # master username
        'PASSWORD': os.getenv('MYSQL_PW'), # master password
        'HOST': os.getenv('MYSQL_IP'), # Endpoint
        'PORT': os.getenv('MYSQL_PORT'),
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}
