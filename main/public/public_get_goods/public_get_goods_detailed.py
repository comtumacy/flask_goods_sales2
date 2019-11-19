# coding=utf-8
from flask import Blueprint, make_response, request
import json
from main.public.public_get_goods.public_get_goods_detailed_sql import public_get_goods_detailed_sql


# 创建一个蓝图的对象，蓝图就是一个小模块的概念
public_get_goods_detailed = Blueprint("public_get_goods_detailed", __name__)


@public_get_goods_detailed.route('/public_get_goods_detailed', methods=['POST', 'GET'])
def public_get_goods_detailed_fun():
    # 获取请求头的数据
    get_data = request.json
    # 获取数据
    goods_content, page_num_all = public_get_goods_detailed_sql(get_data['type'], get_data['content'], get_data['pageNum'])
    post_data = {'goodsContent': goods_content, 'pageNumber': page_num_all}
    #  返回的内容
    response = make_response(json.dumps(post_data))
    #  返回的json格式设定
    response.content_type = 'application/json'
    #  设置HTTP状态码
    response.status_code = 200
    return response
