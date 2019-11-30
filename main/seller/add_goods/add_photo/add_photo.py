# coding=utf-8
from flask import Blueprint, make_response, request
from redis import StrictRedis
import json
import os
# import base64
from main.seller.add_goods.add_photo.add_photo_sql import add_photo_sql

# 创建一个蓝图的对象，蓝图就是一个小模块的概念
add_photo = Blueprint("add_photo", __name__)


@add_photo.route('/add_photo', methods=['POST', 'GET'])
def add_photo_fun():
    # 获取请求头的数据
    # get_data = request.json
    # 获取头部信息
    username = request.headers.get('Uname')
    token = request.headers.get('token')
    good_id = request.headers.get('goodId')
    photo_type = request.headers.get('type')

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
        # 创建图片文件夹
        path = '/home/flask/goods_sale/static/goods_photo/{}'.format(good_id)
        is_exists = os.path.exists(path)
        if is_exists:
            pass
        else:
            os.mkdir(path)

        # 保存照片
        # img = base64.b64decode(get_data['base64_str'])
        img = request.files.get('img')
        # file = open('/home/flask/goods_sale/static/goods_photo/{}/good.jpg'.format(good_id), 'wb')
        # file.write(img.encode())
        # file.close()
        img.save('/home/flask/goods_sale/static/goods_photo/{}/good.jpg'.format(good_id))
        # 图片地址
        # # photo_url = 'https://yitongli.cn/goods_photo/{}/good.jpg'.format(get_data['good_id'])
        photo_url = 'http://139.155.33.105/goods_photo/{}/good.jpg'.format(good_id)
        # 判断插入图片的类型
        if int(photo_type) == 1:
            table_name = 'bookinfo'
        else:
            table_name = 'phoneinfo'
        add_photo_sql(table_name, photo_url, good_id)
        post_data = {'info': '图片上传保存成功', 'url': photo_url}
        #  返回的内容
        response = make_response(json.dumps(post_data))
        #  返回的json格式设定
        response.content_type = 'application/json'
        #  设置HTTP状态码
        response.status_code = 200
        return response
