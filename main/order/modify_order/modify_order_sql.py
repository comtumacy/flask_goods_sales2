# coding=utf-8
import pymysql


# 修改订单状态
def modify_order_sql(good_status, buyer, good_id, good_number):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!',  db='goodsorder',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "UPDATE `order` SET `status` = '{}' WHERE buyer = '{}' AND goodid = {} AND `number` = {}".format(good_status, buyer, good_id, good_number)
    cursor.execute(sql1)
    conn.commit()
