# coding=utf-8
from flask import Blueprint, make_response, request
from redis import StrictRedis
import json
from main.seller.add_goods.select_type.select_type_sql import select_type_sql


# 创建一个蓝图的对象，蓝图就是一个小模块的概念
select_type = Blueprint("select_type", __name__)


@select_type.route('/select_type', methods=['POST', 'GET'])
def select_type_fun():
    # 获取请求头的数据
    get_data = request.json
    # 获取头部信息
    username = request.headers.get('Uname')
    token = request.headers.get('token')

    # 获取token
    redis = StrictRedis(host='localhost', port=6379, db=0, password='Liyitong97!')
    token_get = redis.get(username)
    token_get = str(token_get)
    token_get = token_get.replace("b'", "")
    token_get = token_get.replace("'", "")

    # token失效
    if token != token_get:
        post_data = {'info': '登录失效，请重新登录'}
        #  返回的内容
        response = make_response(json.dumps(post_data))
        #  返回的json格式设定
        response.content_type = 'application/json'
        #  设置HTTP状态码
        response.status_code = 401
    else:
        result = select_type_sql(get_data['num'], get_data['content'])
        # 设置返回对象
        response = make_response(json.dumps(result))
        # 设置状态码
        response.status_code = 200
        #  返回的json格式设定
        response.content_type = 'application/json'
        return response
