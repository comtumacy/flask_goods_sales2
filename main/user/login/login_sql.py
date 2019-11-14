# coding=utf-8
import pymysql


# 用户密码验证
def login_sql(Uname, Upwd):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsUser',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "select Upwd FROM users WHERE Uname = '{}';".format(Uname)
    cursor.execute(sql1)
    conn.commit()
    tup = cursor.fetchall()
    if tup[0][0] == Upwd:
        status = 1
    else:
        status = 0
    cursor.close()
    conn.close()
    return status
