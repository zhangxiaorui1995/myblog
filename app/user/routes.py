# usr/bin/env/python3
# -*- coding=utf-8 -*-
# time: 
# __author__ = Aidan
from flask import url_for, render_template, redirect, g, request, session
from . import blueprint
from models.model import UserInfo, db


@blueprint.route('/')
@blueprint.route('/index')
def index():
    if g.uid:
        uid = g.uid
        user_info = UserInfo.query.filter(UserInfo.user == uid).first()
        user_name = user_info.net_name
        return render_template('index.html', name=user_name, speciality='python', personal_signature="这里是用户的个人签名",
                               personal_profile="这里是个人简介", personal_expectation="这里是个人期望")
    else:
        return redirect(url_for('user.log_in'))
        # return redirect('login')


@blueprint.route('/login')
def log_in():
    return render_template('login.html')


@blueprint.route('/login/success', methods=["GET", "POST"])
def log_in_success():
    # 登陆的接口为POST
    if request.method == "POST":
        if request.form.get('user_name'):
            return "error"  # TODO
        else:
            uid = request.form.get('email', None)
            session['uid'] = uid
            upw = request.form.get('password', None)
            user = UserInfo.query.filter(UserInfo.user == uid).first()
            if user.pwd == upw:
                return redirect(url_for('user.index'))
            else:
                return "error"  # TODO
    # 注册的接口为GET
    elif request.method == "GET":
        if request.args.get('user_name'):
            uid = request.args.get('email')
            upw = request.args.get('password')
            net_name = request.args.get('user_name')
            new_user_info = UserInfo()
            new_user_info.user = uid
            new_user_info.pwd = upw
            new_user_info.net_name = net_name
            db.session.add(new_user_info)
            db.session.commit()
            return redirect(url_for('user.log_in'))
        else:
            return "error"  # TODO
    else:
        return "请求方式错误"  # TODO


# @blueprint.route('/test')
# def test():
#     return render_template('index.html', name='福成', speciality='python', personal_signature="这里是用户的个人签名",
#                            personal_profile="这里是个人简介", personal_expectation="这里是个人期望")
