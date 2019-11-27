# coding=utf-8
from flask import Blueprint, make_response, request
from redis import StrictRedis
import json
from main.seller.look_goods.look_good_id_sql import look_good_id_sql


# 创建一个蓝图的对象，蓝图就是一个小模块的概念
look_good_id = Blueprint("look_good_id", __name__)


@look_good_id.route('/look_good_id', methods=['POST', 'GET'])
def look_good_id_fun():
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
        return response
    # token对比成功
    else:
        redis.expire(username, 3600)
        look_goods_list = look_good_id_sql(get_data['type'], get_data['good_id'], username)
        if look_goods_list == 'null':
            post_data = {'info': '查询失败，请检查是否有此商品ID'}
            #  返回的内容
            response = make_response(json.dumps(post_data))
            #  返回的json格式设定
            response.content_type = 'application/json'
            #  设置HTTP状态码
            response.status_code = 403
            return response
        else:
            post_data = {'lookGoodsList': look_goods_list}
            #  返回的内容
            response = make_response(json.dumps(post_data))
            #  返回的json格式设定
            response.content_type = 'application/json'
            #  设置HTTP状态码
            response.status_code = 200
            return response
