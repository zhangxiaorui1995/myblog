# usr/bin/env/python3
# -*- coding=utf-8 -*-
# time: 
# __author__ = Aidan
from flask import Blueprint
blueprint = Blueprint('tourist', __name__, template_folder='templates')
from . import tourist_index