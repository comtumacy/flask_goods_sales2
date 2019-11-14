# coding=utf-8
from flask import Blueprint, make_response, request
from redis import StrictRedis
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import json
# 查询是否有此用户名
from main.user.login.find_username_sql import find_duplication_sql
# 用户密码验证
from main.user.login.login_sql import login_sql

# 创建一个蓝图的对象，蓝图就是一个小模块的概念
login = Blueprint("login", __name__)


@login.route('/login', methods=['POST', 'GET'])
def login_fun():
    # 获取data
    data = request.json
    # 获取头部信息
    code = request.headers.get('code')
    ctoken = request.headers.get('ctoken')

    # 获取code
    redis = StrictRedis(host='localhost', port=6379, db=0, password='Liyitong97!')
    code_get = redis.get(ctoken)

    #  设置响应体
    response = make_response()
    #  返回的json格式设定
    response.content_type = 'application/json'

    #  获取验证码
    code_get = str(code_get)
    if code_get == 'None':
        post_data = {"info": "验证码失效"}
        post_data = json.dumps(post_data)
        response.set_data(post_data)
        # 设置HTTP状态码
        response.status_code = 403
    else:
        code_get = code_get.replace("'", "")
        code_get = code_get.replace("b", "")
        #  判断验证码是否正确
        if code != code_get:
            post_data = {"info": "验证码错误"}
            post_data = json.dumps(post_data)
            response.set_data(post_data)
            # 设置HTTP状态码
            response.status_code = 403
        else:
            status = find_duplication_sql(data['Uname'])
            if status == 1:
                status = login_sql(data['Uname'], data['Upwd'])
                if status == 1:

                    # 获取SECRET_KEY
                    redis = StrictRedis(host='localhost', port=6379, db=0, password='Liyitong97!')
                    secret_key = redis.get('SECRET_KEY')

                    expiration = 3600
                    s = Serializer(secret_key, expires_in=expiration)  # expiration是过期时间
                    token = s.dumps({'Uname': data['Uname']})
                    token = str(token, 'utf-8')

                    # token存入redis, 无操作3600s后过期
                    redis.set(data['Uname'], token)
                    redis.expire(data['Uname'], 3600)

                    #  设置headers
                    response.headers = {'username': data['Uname'], 'token': token}

                    post_data = {"info": "登录成功"}
                    post_data = json.dumps(post_data)
                    response.set_data(post_data)
                    response.content_type = 'application/json'
                    # 设置HTTP状态码
                    response.status_code = 200
                else:
                    post_data = {"info": "密码错误"}
                    post_data = json.dumps(post_data)
                    response.set_data(post_data)
                    # 设置HTTP状态码
                    response.status_code = 403
            else:
                post_data = {"info": "此用户不存在"}
                post_data = json.dumps(post_data)
                response.set_data(post_data)
                # 设置HTTP状态码
                response.status_code = 403
    return response
