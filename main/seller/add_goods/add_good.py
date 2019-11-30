# coding=utf-8
from flask import Blueprint, make_response, request
from redis import StrictRedis
import json
import time
from main.seller.add_goods.add_book_sql import add_book_sql
from main.seller.add_goods.add_phone_sql import add_phone_sql
from main.seller.add_goods.add_info_to_management_sql import add_info_to_management_sql

# 创建一个蓝图的对象，蓝图就是一个小模块的概念
add_good = Blueprint("add_good", __name__)


@add_good.route('/add_good', methods=['POST', 'GET'])
def add_good_fun():
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
        # 类型为书籍
        if int(get_data['type']) == 1:
            status = add_book_sql(get_data['good_id'], get_data['name'], get_data['price'], get_data['discount'], get_data['old_price'], get_data['author'], get_data['area'], get_data['publishing_time'], get_data['open_book'], get_data['paper'], get_data['packing'], get_data['suit'], get_data['introduction'], get_data['book_img'], get_data['stid'], get_data['new_and_old_degree'], get_data['number'])
            if status == 1:
                add_info_to_management_sql(username, get_data['good_id'], get_data['stid'], time.strftime("%Y-%m-%d", time.localtime()))
                result = {'info': '书籍添加成功', 'good_id': get_data['good_id']}
                # 设置返回对象
                response = make_response(json.dumps(result))
                # 设置状态码
                response.status_code = 200
                #  返回的json格式设定
                response.content_type = 'application/json'
                return response
            else:
                result = {'info': '商品添加失败，书籍ISBN编号已经存在，此书籍已经有人在售，请更换其他书籍'}
                # 设置返回对象
                response = make_response(json.dumps(result))
                # 设置状态码
                response.status_code = 403
                #  返回的json格式设定
                response.content_type = 'application/json'
                return response
        # 类型为手机
        else:
            num = add_phone_sql(get_data['title'], get_data['price'], get_data['good_title'], get_data['good_weight'], get_data['good_from'], get_data['good_system'], get_data['signal'], get_data['screen_size'], get_data['img'], get_data['stid'], get_data['number'])
            status = add_info_to_management_sql(username, int(num) + 1, get_data['stid'], time.strftime("%Y-%m-%d", time.localtime()))
            if status == 1:
                result = {'info': '电子设备添加成功', 'good_id': num}
                # 设置返回对象
                response = make_response(json.dumps(result))
                # 设置状态码
                response.status_code = 200
                #  返回的json格式设定
                response.content_type = 'application/json'
                return response
            else:
                result = {'info': '商品添加失败'}
                # 设置返回对象
                response = make_response(json.dumps(result))
                # 设置状态码
                response.status_code = 403
                #  返回的json格式设定
                response.content_type = 'application/json'
                return response
