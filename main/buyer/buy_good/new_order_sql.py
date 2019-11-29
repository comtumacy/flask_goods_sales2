# coding=utf-8
import pymysql
import time


# 生成订单
def new_order_sql(good_id, good_number, good_type, username):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    for i in range(len(good_id)):
        if int(good_type[i]) == 1:
            sql1 = "SELECT number FROM bookinfo  WHERE goodId = {}".format(good_id[i])
            cursor.execute(sql1)
            conn.commit()
            tup1 = cursor.fetchall()
            number = int(tup1[0][0])
            number = number - int(good_number[i])
            sql2 = "UPDATE bookinfo SET number = {} WHERE goodId = {}".format(number, good_id[i])
            cursor.execute(sql2)
            conn.commit()
        else:
            sql1 = "SELECT number FROM phoneinfo  WHERE goodId = {}".format(good_id[i])
            cursor.execute(sql1)
            conn.commit()
            tup1 = cursor.fetchall()
            number = int(tup1[0][0])
            number = number - int(good_number[i])
            sql2 = "UPDATE phoneinfo SET number = {} WHERE goodId = {}".format(number, good_id[i])
            cursor.execute(sql2)
            conn.commit()
    cursor.close()
    conn.close()

    for i in range(len(good_id)):
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                               charset='utf8')
        cursor = conn.cursor()
        if int(good_type[i]) == 1:
            sql3 = "SELECT `Name`, `Price` FROM bookinfo  WHERE goodId = {}".format(good_id[i])
            cursor.execute(sql3)
            conn.commit()
            tup3 = cursor.fetchall()
            title = tup3[0][0]
            price = tup3[0][1]
        else:
            sql3 = "SELECT `title`, `price` FROM phoneinfo  WHERE goodId = {}".format(good_id[i])
            cursor.execute(sql3)
            conn.commit()
            tup3 = cursor.fetchall()
            title = tup3[0][0]
            price = tup3[0][1]
        cursor.close()
        conn.close()

        conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsseller',
                               charset='utf8')
        cursor = conn.cursor()
        sql4 = "SELECT sellername FROM goodsmanagement  WHERE goodsid = {}".format(good_id[i])
        cursor.execute(sql4)
        conn.commit()
        tup4 = cursor.fetchall()
        seller = tup4[0][0]
        cursor.close()
        conn.close()

        conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsUser',
                               charset='utf8')
        cursor = conn.cursor()
        sql5 = "SELECT Ufaddress,Ufphone FROM userinfo  WHERE Uname = '{}'".format(username)
        cursor.execute(sql5)
        conn.commit()
        tup5 = cursor.fetchall()
        address = tup5[0][0]
        phone = tup5[0][1]
        cursor.close()
        conn.close()

        conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsorder',
                               charset='utf8')
        cursor = conn.cursor()
        sql6 = "INSERT INTO `order` (goodid,goodname,`number`,`status`,price,`date`,buyer,seller,address,tel) VALUES ({},'{}',{},'{}',{},'{}','{}','{}','{}','{}')".format(good_id[i], title, good_number[i], '待付款', price * good_number[i], time_now, username, seller, address, phone)
        cursor.execute(sql6)
        conn.commit()
        cursor.close()
        conn.close()
