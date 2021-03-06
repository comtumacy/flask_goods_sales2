# coding=utf-8
from flask import Blueprint, make_response, request
from redis import StrictRedis
import json
from main.public.modify_user_info.modify_user_info_sql import modify_user_info_sql


# 创建一个蓝图的对象，蓝图就是一个小模块的概念
modify_user_info = Blueprint("modify_user_info", __name__)


@modify_user_info.route('/modify_user_info', methods=['POST', 'GET'])
def modify_user_info_fun():
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
        modify_user_info_sql(get_data['sex'], get_data['province'], get_data['city'], get_data['phone'], get_data['trueName'], get_data['address'], get_data['postalCode'], get_data['email'], get_data['codeTypes'], get_data['codenumber'], username)
        post_data = {'info': '修改成功'}
        #  返回的内容
        response = make_response(json.dumps(post_data))
        #  返回的json格式设定
        response.content_type = 'application/json'
        #  设置HTTP状态码
        response.status_code = 200
        return response

