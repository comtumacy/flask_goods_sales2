# coding=utf-8
from flask import Blueprint, make_response, request
import json
from main.public.public_get_goods.public_get_goods_id_sql import public_get_goods_id_sql


# 创建一个蓝图的对象，蓝图就是一个小模块的概念
public_get_goods_id = Blueprint("public_get_goods_id", __name__)


@public_get_goods_id.route('/public_get_goods_id', methods=['POST', 'GET'])
def public_get_goods_id_fun():
    # 获取请求头的数据
    get_data = request.json
    # 获取数据
    goods_content, all_rating_list = public_get_goods_id_sql(get_data['type'], get_data['good_id'])
    post_data = {'goodsContent': goods_content, 'goodsRating': all_rating_list}
    #  返回的内容
    response = make_response(json.dumps(post_data))
    #  返回的json格式设定
    response.content_type = 'application/json'
    #  设置HTTP状态码
    response.status_code = 200
    return response
