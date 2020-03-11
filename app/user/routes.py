# usr/bin/env/python3
# -*- coding=utf-8 -*-
# time: 
# __author__ = Aidan
from flask import url_for, render_template, redirect, g, request, session
from . import blueprint
from models.model import UserInfo, db, gen_id, BlogInfo
from .user_forms import UserForm


@blueprint.route('/')
@blueprint.route('/index')
def index():
    if g.uid:
        uid = g.uid
        user_info = UserInfo.query.filter(UserInfo.id == uid).first()
        user_name = user_info.net_name
        blog_info = BlogInfo.query.filter(BlogInfo.id == uid).first()
        admin_name = '站长'
        # return render_template('index.html', name=user_name, speciality=blog_info.speciality,
        #                        personal_signature=blog_info.personal_signature,
        #                        personal_profile=blog_info.personal_peofile,
        #                        personal_expectation=blog_info.personal_expectation)
        return render_template('index.html', **locals())
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
            uem = request.form.get('email', None)
            user = UserInfo.query.filter(UserInfo.user == uem).first()
            uid = user.id
            session['uid'] = uid
            upw = request.form.get('password', None)

            if user.pwd == upw:
                return redirect(url_for('user.index'))
            else:
                return "error"  # TODO
    # 注册的接口为GET
    elif request.method == "GET":
        if request.args.get('user_name'):
            uid = gen_id()
            uem = request.args.get('email')
            upw = request.args.get('password')
            net_name = request.args.get('user_name')
            new_user_info = UserInfo()
            new_user_info.id = uid
            new_user_info.user = uem
            new_user_info.pwd = upw
            new_user_info.net_name = net_name
            db.session.add(new_user_info)
            db.session.commit()
            g.uid = uid
            return redirect(url_for('user.user_form'))
        else:
            return "error"  # TODO
    else:
        return "请求方式错误"  # TODO


# 用户填写基本信息
@blueprint.route('/user_form', methods=["GET", "POST"])
def user_form():
    if not g.uid:
        if request.method == "GET":
            form = UserForm()
            return render_template('user_form.html', forms=form)
        form = UserForm()
        # request.method==' post '  and  from.validate() = form.validate_on_submit()
        if form.validate():
            return "验证成功"
        else:
            return render_template('user_form.html', forms=form)
    else:
        return redirect(url_for('user.log_in'))
