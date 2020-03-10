# usr/bin/env/python3
# -*- coding=utf-8 -*-
# time: 
# __author__ = Aidan
from flask import g
from manager import db


# 储存用户信息
class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.String(100), nullable=False, unique=True)
    pwd = db.Column(db.CHAR(50), nullable=False, unique=True)
    net_name = db.Column(db.String(100), nullable=False, unique=True)


db.create_all()

# 储存博客内容
# class BlogInfo(db.Model):
#     __tablename__ = 'bloginfo'
