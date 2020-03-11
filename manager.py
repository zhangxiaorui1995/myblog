# usr/bin/env/python3
# -*- coding=utf-8 -*-
# time: 
# __author__ = Aidan
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import generate_csrf
from app.user import blueprint as user_blueprint
from configs import default
from flask import Flask, g, session
app = Flask(__name__)
app.config.from_object(default)
app.config['SECRET_KEY'] = default.SECRET_KEY
db = SQLAlchemy(app)
app.register_blueprint(user_blueprint, url_prefix='/user')


@app.before_request
def before_request():
    if session.get('uid'):
        g.uid = session.get('uid')
    else:
        g.uid = None


@app.after_request
def after_request(response):
    # 调用函数生成 csrf_token
    csrf_token = generate_csrf()
    # 通过 cookie 将值传给前端
    response.set_cookie("csrf_token", csrf_token)
    return response


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
