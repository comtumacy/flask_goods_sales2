# coding=utf-8
import pymysql


# 图片地址写入商品表格
def add_photo_sql(table_name, url, good_id):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    if table_name == 'bookinfo':
        sql1 = "UPDATE {} SET book_img = '{}' WHERE goodId = {}".format(table_name, url, int(good_id))
    else:
        sql1 = "UPDATE {} SET img = '{}' WHERE goodId = {}".format(table_name, url, int(good_id))
    cursor.execute(sql1)
    conn.commit()
    cursor.close()
    conn.close()
