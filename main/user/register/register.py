# coding=utf-8
from flask import Blueprint, make_response, request
from redis import StrictRedis
import json
# 导入查询重复值SQL文件
from main.user.register.find_duplication_sql import find_duplication_sql
# 导入注册SQL文件
from main.user.register.register_sql import register_sql


# 创建一个蓝图的对象，蓝图就是一个小模块的概念
register = Blueprint("register", __name__)


@register.route('/register', methods=['POST', 'GET'])
def register_fun():
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
            status = find_duplication_sql(data['Uname'], data['Uroleid'])
            if status == 1:
                status = register_sql(data['Uname'], data['Upwd'], data['Uquestion'], data['Uresult'], data['Usafetycode'], data['Uroleid'])
                if status == 1:
                    post_data = {"info": "注册成功"}
                    post_data = json.dumps(post_data)
                    response.set_data(post_data)
                    response.status_code = 200
                else:
                    post_data = {"info": "未知错误，请联系管理员"}
                    post_data = json.dumps(post_data)
                    response.set_data(post_data)
                    response.status_code = 403
            else:
                post_data = {"info": "用户名已经存在"}
                post_data = json.dumps(post_data)
                response.set_data(post_data)
                response.status_code = 403
    return response
