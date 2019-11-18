# coding=utf-8
import pymysql


# 主页商品栏商品获取
def public_get_goods_sql(good_type):
    good_ids = []
    goods_content = []
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    sql0 = "SELECT goodid FROM `homeproductbar` WHERE `type` = {}".format(good_type)
    cursor.execute(sql0)
    conn.commit()
    result0 = cursor.fetchall()
    for i in range(4):
        good_ids.append(int(result0[i][0]))

    if good_type == 1:
        for i in range(4):
            sql1 = "SELECT `Name`,Price,book_img FROM `bookinfo` WHERE goodId = {}".format(good_ids[i])
            cursor.execute(sql1)
            conn.commit()
            result1 = cursor.fetchall()
            goods_content.append({'name': result1[0][0], 'price': result1[0][1], 'imgUrl': result1[0][2]})
    else:
        for i in range(4):
            sql1 = "SELECT `title`,price,img FROM `phoneinfo` WHERE goodId = {}".format(good_ids[i])
            cursor.execute(sql1)
            conn.commit()
            result1 = cursor.fetchall()
            goods_content.append({'name': result1[0][0], 'price': result1[0][1], 'imgUrl': result1[0][2]})
    cursor.close()
    conn.close()
    return goods_content, good_ids


# public_get_goods_sql(2)
