# usr/bin/env/python3
# -*- coding=utf-8 -*-
# time: 
# __author__ = Aidan
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, ValidationError, \
    core, IntegerField
from wtforms.validators import DataRequired, Length, Regexp


# class LoginForm(Form):
#     username = StringField('用户名', validators=[DataRequired()])
#     password = PasswordField('密码', validators=[DataRequired(), Length(1, 32)])
#     # remember = BooleanField('记住我')
#     submit = SubmitField('登录')

class UserForm(Form):
    sex = SelectField(label='性别', choices=((0, "男"), (1, "女"),), coerce=int)
    phone = StringField(label="手机", validators=[DataRequired('手机号码'),
                                                Regexp("1[3578]\d{9}", message="手机格式不正确")],
                        description="手机", render_kw={"class": "form-control",
                                                     "placeholder": "请输入手机号码", "required": 'required'
                                                     }
                        )
    qq = StringField('QQ号', validators=[DataRequired(), Length(6, 12)])
    wx = StringField('微信', validators=[DataRequired()])
    speciality = StringField('擅长语言', validators=[DataRequired()])
    personal_signature = StringField('个人签名', validators=[DataRequired()])
    personal_profile = StringField('个人简介', validators=[DataRequired()])
    personal_expectation = StringField('个人期望', validators=[DataRequired()])
