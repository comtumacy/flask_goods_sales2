# coding=utf-8
import pymysql


# 查询是否有此用户名
def find_duplication_sql(Uname):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "select * FROM users WHERE Uname = '{}';".format(Uname)
    try:
        cursor.execute(sql1)
        conn.commit()
        tup = cursor.fetchall()
        if len(tup) == 0:
            status = 0
        else:
            status = 1
    finally:
        cursor.close()
        conn.close()
    return status
