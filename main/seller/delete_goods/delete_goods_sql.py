# coding=utf-8
import pymysql


# 删除商品
def delete_goods_sql(table_name, good_id):
    # 插入数据
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "DELETE FROM {} WHERE goodId = {}".format(table_name, good_id)
    cursor.execute(sql1)
    conn.commit()
    cursor.close()
    conn.close()

    return num
