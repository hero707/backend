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
    help = 'Creates the initial database'

    def handle(self, *args, **options):
        print('Starting db creation')
        try:
            db = MySQLdb.connect(host=rds_host, user=user_name,
                                 password=password, db="mysql", connect_timeout=5)
            c = db.cursor()
            print("connected to db server")
            c.execute(f"""CREATE DATABASE {db_name};""")
            c.execute(
                f"""GRANT ALL PRIVILEGES ON db_name.* TO '{user_name}' IDENTIFIED BY '{password}';""")
            c.close()
            print("closed db connection")
        except Exception as e:
            logger.error(
                f"ERROR: Unexpected error: Could not connect to MySql instance. \n{e}")
            sys.exit()
