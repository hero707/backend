from .base import *

DEBUG=True
ALLOWED_HOSTS = ["*"]

AUTH_SERVER_LOGIN = ROOT_SERVER + "/login"

AUTH_SERVER_AUTHENTICATE = ROOT_SERVER + "/authenticate"