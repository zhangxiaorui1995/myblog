#` usr/bin/env/python3
# -*- coding=utf-8 -*-
# time: 
# __author__ = Aidan
from flask import Flask, g, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import generate_csrf
from app.user import blueprint as user_blueprint
from configs import default
app = Flask(__name__)
app.config.from_object(default)
app.config['SECRET_KEY'] = default.SECRET_KEY
db = SQLAlchemy(app)


from app.user import blueprint as user_blueprint
from tourist import blueprint as tourist_blueprint
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(tourist_blueprint, url_prefix='/tourist')


@app.before_request
def before_request():
    if session.get('uid'):
        g.uid = session.get('uid')
    else:
        g.uid = None


# csrf_token = generate_csrf()
@app.after_request
def after_request(response):
    # 调用函数生成 csrf_token
    csrf_token = generate_csrf()
    # 通过 cookie 将值传给前端
    response.set_cookie("csrf_token", csrf_token)
    return response


@app.route('/')
def blog_index():
    return redirect(url_for('tourist.tourist_index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
