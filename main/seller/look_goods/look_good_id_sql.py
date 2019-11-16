# coding=utf-8
import pymysql


# 根据商品id精确查询商品
def look_good_id_sql(good_type, good_id, Uname):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    if good_type == 1:
        sql1 = "SELECT `Name` FROM `bookinfo` WHERE goodId = {}".format(int(good_id))
    else:
        sql1 = "SELECT `title` FROM `phoneinfo` WHERE goodId = {}".format(int(good_id))
    cursor.execute(sql1)
    conn.commit()
    content = cursor.fetchall()
    cursor.close()
    conn.close()
    # 查询是否为该卖家的商品
    if len(content) == 0:
        content = 'null'
    else:
        conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsseller',
                               charset='utf8')
        cursor = conn.cursor()
        sql2 = "SELECT sellername FROM goodsmanagement WHERE goodsid = {}".format(int(good_id))
        cursor.execute(sql2)
        conn.commit()
        result2 = cursor.fetchall()
        user_name = result2[0][0]
        if user_name != Uname:
            content = 'null'
        else:
            sql3 = "SELECT * FROM goodsmanagement WHERE goodsid = {}".format(int(good_id))
            cursor.execute(sql3)
            conn.commit()
            content_all = cursor.fetchall()
            content = {'goodtitle': content[0][0], 'goodsid': content_all[0][1], 'goodstype': content_all[0][2],'registrationtime': content_all[0][3]}
        cursor.close()
        conn.close()
    return content


# look_good_id_sql(2, 1)
