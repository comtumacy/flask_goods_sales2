# coding=utf-8
from flask import Blueprint, make_response, request
from redis import StrictRedis
import json

# 创建一个蓝图的对象，蓝图就是一个小模块的概念
out_login = Blueprint("out_login", __name__)


@out_login.route('/out_login', methods=['POST', 'GET'])
def out_login_fun():
    # 清空token
    username = request.headers.get('username')
    redis = StrictRedis(host='localhost', port=6379, db=0, password='Liyitong97!')
    redis.set(username, 'None')

    #  设置响应体
    response = make_response()
    #  返回的json格式设定
    response.content_type = 'application/json'
    post_data = {"info": "退出登录成功"}
    post_data = json.dumps(post_data)
    response.set_data(post_data)
    # 设置HTTP状态码
    response.status_code = 200
    return response
