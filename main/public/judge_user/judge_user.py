# coding=utf-8
from flask import Blueprint, make_response, request
from redis import StrictRedis
import json
from main.public.judge_user.judge_user_sql import judge_user_sql


# 创建一个蓝图的对象，蓝图就是一个小模块的概念
judge_user = Blueprint("judge_user", __name__)


@judge_user.route('/judge_user', methods=['POST', 'GET'])
def judge_user_fun():
    # 获取请求头的数据
    # get_data = request.json
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
        user_type = judge_user_sql(username)
        post_data = {'userType': user_type}
        #  返回的内容
        response = make_response(json.dumps(post_data))
        #  返回的json格式设定
        response.content_type = 'application/json'
        #  设置HTTP状态码
        response.status_code = 200
        return response
