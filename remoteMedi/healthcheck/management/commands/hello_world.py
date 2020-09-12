import sys
import os
import logging
import MySQLdb

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from dotenv import load_dotenv
load_dotenv()

rds_host = os.getenv('MYSQL_IP')
db_name = os.getenv('DB_NAME')
user_name = os.getenv('MYSQL_ID')
password = os.getenv('MYSQL_PW')
port = os.getenv('MYSQL_PORT')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Command(BaseCommand):
    help = 'hi'

    print('hi')