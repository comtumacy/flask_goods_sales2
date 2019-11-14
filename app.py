# coding=utf-8
from flask import Flask, current_app
from flask_cors import CORS
from redis import StrictRedis
import os


# 导入蓝图子模块
# 用户模块
from main.user.register.verification_code.verification_code import verification_code  # 获取验证码
from main.user.register.register import register  # 注册
from main.user.login.login import login  # 登录
from main.user.out_login.out_login import out_login  # 退出登录
# 卖家模块
# 卖家模块---添加商品
from main.seller.add_goods.select_type.select_type import select_type  # 选择添加类型
from main.seller.add_goods.add_good import add_good  # 添加商品
from main.seller.delete_goods.delete_goods import delete_goods  # 删除商品
from main.seller.add_goods.add_photo.add_photo import add_photo  # 添加商品图片


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
# 卖家模块
# 卖家模块---添加商品
app.register_blueprint(select_type, url_prefix='/seller')  # 选择添加类型
app.register_blueprint(add_good, url_prefix='/seller')  # 添加商品
app.register_blueprint(delete_goods, url_prefix='/seller')  # 删除商品
app.register_blueprint(add_photo, url_prefix='/seller')  # 添加商品图片

if __name__ == '__main__':
    app.run(host='172.27.0.13', port=5002, debug=True)
