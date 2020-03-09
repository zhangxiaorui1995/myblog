# usr/bin/env/python3
# -*- coding=utf-8 -*-
# time: 
# __author__ = Aidan
from flask import Flask
app = Flask(__name__)
from . import routes
