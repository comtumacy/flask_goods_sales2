# coding=utf-8
from flask import Blueprint, make_response, request
import json
from main.public.search_good.search_good_sql import search_good_sql


# 创建一个蓝图的对象，蓝图就是一个小模块的概念
search_good = Blueprint("search_good", __name__)


@search_good.route('/search_good', methods=['POST', 'GET'])
def search_good_fun():
    # 获取请求头的数据
    get_data = request.json
    # 获取数据
    goods_content, page_num_all = search_good_sql(int(get_data['type']), get_data['content'], get_data['pageNum'])
    post_data = {'goodsContent': goods_content, 'pageNumber': page_num_all, 'type': get_data['type'], 'search_content': get_data['content']}
    #  返回的内容
    response = make_response(json.dumps(post_data))
    #  返回的json格式设定
    response.content_type = 'application/json'
    #  设置HTTP状态码
    response.status_code = 200
    return response
