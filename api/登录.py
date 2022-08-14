# import app
from flask import session
import os

def main(info):
    密码 = os.getenv('PWD')
    if 密码:
        raise Exception("未设置PWD环境变量")
    if 密码 == info.get('pwd'):
        # app.session['login'] == True
        session['login'] == True
    else:
        raise Exception("登录密码错误")
