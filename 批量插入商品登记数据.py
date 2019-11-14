# coding=utf-8
import pymysql
import random


# 用户密码验证
def login_sql():
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "SELECT goodId FROM `phoneinfo`  ORDER BY goodId  ASC  LIMIT 190,50"
    cursor.execute(sql1)
    conn.commit()
    result = cursor.fetchall()
    result_list = []
    for i in range(len(result)):
        result_list.append(result[i][0])
    print(result_list)
    sql2 = "SELECT Stid FROM `phoneinfo`  ORDER BY goodId  ASC  LIMIT 190,50"
    cursor.execute(sql2)
    conn.commit()
    result2 = cursor.fetchall()
    result_list2 = []
    for i in range(len(result2)):
        result_list2.append(result2[i][0])
    print(result_list2)
    cursor.close()
    conn.close()
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsseller',
                           charset='utf8')
    cursor = conn.cursor()
    for i in range(len(result_list2)):
        sql3 = "INSERT INTO goodsmanagement  (sellername, goodsid,goodstype, registrationtime) VALUES ('seller6','{}',{},'2019-0{}-0{}');".format(result_list[i], result_list2[i], random.randint(1, 9), random.randint(1, 9))
        cursor.execute(sql3)
        conn.commit()
        print(sql3)
        print(i)
    cursor.close()
    conn.close()


login_sql()
