# usr/bin/env/python3
# -*- coding=utf-8 -*-
# time: 
# __author__ = Aidan
import os

# 数据库配置
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
# PASSWORD = '123456tt'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'myblog'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.urandom(24)
