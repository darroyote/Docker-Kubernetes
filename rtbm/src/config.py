import logging
import base64
import boto3
import json
import os
import sys
from botocore.exceptions import ClientError

#REGION_NAME = os.getenv('REGION_NAME')
#SECRET_NAME = os.getenv('SECRET_NAME')

class Config:
    #MYSQL_DATABASE = 'db'
    #DB_USERNAME = 'root'
    #DB_HOST = '172.17.0.2'
    #MYSQL_ROOT_PASSWORD = 'password'
    #MYSQL_USER = 'root'
    #MYSQL_ALLOW_EMPTY_PASSWORD = True

    #SQLALCHEMY_DATABASE_URI = 'mysql://root:password@172.17.0.2/db'
    DB_URI = "mysql://%s:%s@%s/%s" % (os.environ['MYSQL_USER'], os.environ['MYSQL_ROOT_PASSWORD'], os.environ['DB_HOST'], os.environ['MYSQL_DATABASE'])
    SQLALCHEMY_DATABASE_URI = DB_URI


    SQLALCHEMY_TRACK_MODIFICATIONS = False
