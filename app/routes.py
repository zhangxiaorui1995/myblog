# usr/bin/env/python3
# -*- coding=utf-8 -*-
# time: 
# __author__ = Aidan
from flask import url_for, render_template, redirect, g, request
from app import app


@app.route('/')
@app.route('/index')
def index():
    if g.name:
        return render_template('index.html', name=g.name, speciality='python', personal_signature="这里是用户的个人签名",
                               personal_profile="这里是个人简介", personal_expectation="这里是个人期望")
    else:
        return redirect('login')


@app.route('/login', methods=["GET", "POST"])
def log_in():
    form = request.form.get('sign-in')
    uid = form.get('email', None)
    upw = form.get('password', None)
    return render_template('login.html')
