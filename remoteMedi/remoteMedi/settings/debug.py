from .base import *

DEBUG=True
ALLOWED_HOSTS = ["*"]

AUTH_SERVER_LOGIN = ROOT_SERVER + "/login"

AUTH_SERVER_AUTHENTICATE = ROOT_SERVER + "/authenticate"

AUTH_SERVER_LOGOUT = ROOT_SERVER + "/logout"

AUTH_SERVER_TOKEN = ROOT_SERVER + "/token"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
