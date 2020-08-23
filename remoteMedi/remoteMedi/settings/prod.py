from .base import *
import os

DEBUG=False

ALLOWED_HOSTS = ["127.0.0.1"]
if os.getenv("GITHUB_WORKFLOW"):
   DATABASES = {
        'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'github_actions',
           'USER': 'postgres',
           'PASSWORD': 'postgres',
           'HOST': '127.0.0.1',
           'PORT': '5432',
        }
    }
else: # .env
    pass
    # DATABASES = {
    #     'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': os.getenv('DB_NAME'),
    #     'USER': os.getenv('DB_USER'),
    #     'PASSWORD': os.getenv('DB_PASSWORD'),
    #     'HOST': os.getenv('DB_HOST'),
    #     'PORT': os.getenv('DB_PORT')
    # }
