# usr/bin/env/python3
# -*- coding=utf-8 -*-
# time: 
# __author__ = Aidan
from flask import g, session, redirect
from flask_sqlalchemy import SQLAlchemy
from app import app
from configs import default

app.config.from_object(default)
db = SQLAlchemy(app)


@app.before_request
def before_request():
    if session.get('email'):
        g.name = session.get('email')
    else:
        g.name = None


if __name__ == "__main__":
    app.run(debug=True)
