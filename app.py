# coding=utf-8
from flask import Flask, current_app
from flask_cors import CORS
from redis import StrictRedis
import os


# 导入蓝图子模块
# 用户模块
from templates.user.register.verification_code.verification_code import verification_code  # 获取验证码
from templates.user.register.register import register  # 注册
from templates.user.login.login import login  # 登录
from templates.user.out_login.out_login import out_login  # 退出登录


# 设置SECRET_KEY为随机数
app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
appContent = app.app_context()
appContent.push()
# 将SECRET_KEY存入Redis数据库
redis = StrictRedis(host='localhost', port=6379, db=0, password='Liyitong97!')
redis.set('SECRET_KEY', current_app.config['SECRET_KEY'])
appContent.pop()


# 跨域请求设置
CORS(app, resources=r'/*')


# 注册蓝图,蓝图添加链接前缀
# 用户模块
app.register_blueprint(verification_code, url_prefix='/user')  # 获取验证码
app.register_blueprint(register, url_prefix='/user')  # 注册
app.register_blueprint(login, url_prefix='/user')  # 登录
app.register_blueprint(out_login, url_prefix='/user')  # 退出登录


if __name__ == '__main__':
    app.run(host='172.27.0.13', port=5002, debug=True)
