# coding=utf-8
import pymysql


# 根据ID查询商品
def find_number_sql(good_id, good_number, good_type):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    status = 1
    for i in range(len(good_id)):
        if int(good_type[i]) == 1:
            sql1 = "SELECT number FROM `bookinfo`  WHERE goodId = {}".format(int(good_id[i]))
            cursor.execute(sql1)
            conn.commit()
            tup1 = cursor.fetchall()
            number = tup1[0][0]
            if number < int(good_number[i]):
                cursor.close()
                conn.close()
                status = 0
                return status
        else:
            sql1 = "SELECT number FROM `phoneinfo`  WHERE goodId = {}".format(int(good_id[i]))
            cursor.execute(sql1)
            conn.commit()
            tup1 = cursor.fetchall()
            number = tup1[0][0]
            if number < int(good_number[i]):
                cursor.close()
                conn.close()
                status = 0
                return status
    cursor.close()
    conn.close()
    return status
