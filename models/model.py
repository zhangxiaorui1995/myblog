# usr/bin/env/python3
# -*- coding=utf-8 -*-
# time: 
# __author__ = Aidan
import uuid
from manager import db


def gen_id():
    return uuid.uuid4().hex


# 储存用户信息
class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.String(32), default=gen_id, primary_key=True)
    user = db.Column(db.String(100), nullable=False, unique=True)
    pwd = db.Column(db.CHAR(50), nullable=False, unique=False)
    net_name = db.Column(db.String(100), nullable=False, unique=True)


# 储存博客首页内容
class BlogInfo(db.Model):
    __tablename__ = 'blog_info'
    id = db.Column(db.String(32), default=gen_id, primary_key=True, unique=True)
    sex = db.Column(db.Integer, nullable=False, unique=False)
    phone = db.Column(db.String(100), nullable=True, unique=False)
    qq = db.Column(db.String(100), nullable=True, unique=False)
    wx = db.Column(db.String(100), nullable=True, unique=False)
    speciality = db.Column(db.String(100), nullable=False, unique=False)
    personal_signature = db.Column(db.String(100), nullable=False, unique=False)
    personal_profile = db.Column(db.String(100), nullable=False, unique=False)
    personal_expectation = db.Column(db.String(100), nullable=False, unique=False)
    status = db.Column(db.Integer, nullable=False, comment='0：审核通过， 1：删除， 2：未审核， 3：审核未通过')


# # 文章信息
# class BlogArticleInfo(db.Model):
#     __tablename__ = 'article_info'
#     # 文章内容
#     # 文章分类
#     # 文章时间
#
#
# # 文章点击量信息
# class BlogArticleClickInfo(db.Model):
#
#
db.create_all()
