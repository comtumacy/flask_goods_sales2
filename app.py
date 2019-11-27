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
# 买家模块
# 买家模块---收藏
from main.buyer.add_Favorites.add_favorites import add_favorites  # 添加收藏
from main.buyer.look_Favorites.look_favorites import look_favorites  # 查询该用户的收藏
from main.buyer.delete_favorites.delete_favorites import delete_favorites  # 删除收藏
# 买家模块---购买
from main.buyer.buy_good.look_good import look_good  # 购买商品根据ID查询商品详情
from main.buyer.buy_good.buy_good import buy_good  # 购买商品
# 卖家模块
# 卖家模块---添加商品
from main.seller.add_goods.select_type.select_type import select_type  # 选择添加类型
from main.seller.add_goods.add_good import add_good  # 添加商品
from main.seller.add_goods.add_photo.add_photo import add_photo  # 添加商品图片
# 卖家模块---删除商品
from main.seller.delete_goods.delete_goods import delete_goods  # 删除商品
# 卖家模块---查询商品
from main.seller.look_goods.look_goods import look_goods  # 查询商品
from main.seller.look_goods.look_good_id import look_good_id  # 根据ID精确查找此用户的商品
from main.seller.look_goods.look_good_like import look_good_like  # 模糊查找此用户的商品
# 卖家模块---评论
from main.seller.ratings.get_ratings import get_ratings  # 根据商品ID获取评论
from main.seller.ratings.modify_ratings import modify_ratings  # 修改评论
from main.seller.ratings.delete_ratings import delete_ratings  # 根据商品id删除评论
# 订单模块
# 订单模块---查询订单
from main.order.look_order.look_order import look_order  # 查询订单
from main.order.look_order.look_order_super import look_order_super  # 超管订单
# 公共模块
from main.public.public_get_goods.public_get_goods import public_get_goods  # 获取主页商品栏商品
from main.public.public_get_goods.public_get_goods_detailed import public_get_goods_detailed  # 获取分类商品分页（20）商品
from main.public.public_get_goods.public_get_goods_id import public_get_goods_id  # 根据id获取商品和商品评论
from main.public.get_user_info.get_user_info import get_user_info  # 根据用户名获取用户信息
from main.public.modify_user_info.modify_user_info import modify_user_info  # 根据用户名修改用户信息


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
# 买家模块
# 买家模块---收藏
app.register_blueprint(add_favorites, url_prefix='/buyer')  # 添加收藏
app.register_blueprint(look_favorites, url_prefix='/buyer')  # 查询该用户的收藏
app.register_blueprint(delete_favorites, url_prefix='/buyer')  # 删除收藏
# 买家模块---购买
app.register_blueprint(look_good, url_prefix='/buyer')  # 购买商品根据ID查询商品详情
app.register_blueprint(buy_good, url_prefix='/buyer')  # 购买商品
# 卖家模块
# 卖家模块---添加商品
app.register_blueprint(select_type, url_prefix='/seller')  # 选择添加类型
app.register_blueprint(add_good, url_prefix='/seller')  # 添加商品
app.register_blueprint(add_photo, url_prefix='/seller')  # 添加商品图片
# 卖家模块---删除商品
app.register_blueprint(delete_goods, url_prefix='/seller')  # 删除商品
# 卖家模块---查询商品
app.register_blueprint(look_goods, url_prefix='/seller')  # 查询商品
app.register_blueprint(look_good_id, url_prefix='/seller')  # 根据ID精确查找此用户的商品
app.register_blueprint(look_good_like, url_prefix='/seller')  # 模糊查找此用户的商品
# 卖家模块---评论
app.register_blueprint(get_ratings, url_prefix='/seller')  # 根据商品ID获取评论
app.register_blueprint(modify_ratings, url_prefix='/seller')  # 修改评论
app.register_blueprint(delete_ratings, url_prefix='/seller')  # 根据商品id删除评论
# 订单模块
# 订单模块---查询订单
app.register_blueprint(look_order, url_prefix='/order')  # 查询订单
app.register_blueprint(look_order_super, url_prefix='/order')  # 超管查询订单
# 公共模块
app.register_blueprint(public_get_goods, url_prefix='/public')  # 获取主页商品栏商品，无需token
app.register_blueprint(public_get_goods_detailed, url_prefix='/public')  # 获取分类商品分页（20）商品，无需token
app.register_blueprint(public_get_goods_id, url_prefix='/public')  # 根据id获取商品和商品评论，无需token
app.register_blueprint(get_user_info, url_prefix='/public')  # 根据用户名获取用户信息
app.register_blueprint(modify_user_info, url_prefix='/public')  # 根据用户名修改用户信息

if __name__ == '__main__':
    app.run(host='172.27.0.13', port=5002, debug=True)
    # app.run()
