# coding=utf-8
from flask import Blueprint, make_response, request
from redis import StrictRedis
import json
from main.buyer.buy_good.find_number_sql import find_number_sql
from main.buyer.buy_good.new_order_sql import new_order_sql


# 创建一个蓝图的对象，蓝图就是一个小模块的概念
buy_good = Blueprint("buy_good", __name__)


@buy_good.route('/buy_good', methods=['POST', 'GET'])
def buy_good_fun():
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
        good_id = []
        good_number = []
        good_type = []
        content = get_data['content']
        for i in range(len(content)):
            if content[i]['ID'] in good_id:
                good_index = good_id.index(content[i]['ID'])
                number = good_number[good_index] + content[i]['number']
                good_number[good_index] = number
            else:
                good_id.append(content[i]['ID'])
                good_number.append(content[i]['number'])
                good_type.append(content[i]['type'])
        status = find_number_sql(good_id, good_number, good_type)
        if status == 0:
            post_data = {'info': '库存不足，请重新选择商品'}
            #  返回的内容
            response = make_response(json.dumps(post_data))
            #  返回的json格式设定
            response.content_type = 'application/json'
            #  设置HTTP状态码
            response.status_code = 403
            return response
        else:
            new_order_sql(good_id, good_number, good_type, username)
            post_data = {'info': '订单生成成功'}
            #  返回的内容
            response = make_response(json.dumps(post_data))
            #  返回的json格式设定
            response.content_type = 'application/json'
            #  设置HTTP状态码
            response.status_code = 200
            return response
