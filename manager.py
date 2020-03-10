# usr/bin/env/python3
# -*- coding=utf-8 -*-
# time: 
# __author__ = Aidan
from flask_sqlalchemy import SQLAlchemy
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


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
