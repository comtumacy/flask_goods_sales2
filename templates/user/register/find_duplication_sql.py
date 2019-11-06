# coding=utf-8
import pymysql


# 查询是否已经存在相同的用户名
def find_duplication_sql(Uname, Uroleid):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "select * FROM users WHERE Uroleid = {} AND Uname = '{}';".format(Uroleid, Uname)
    try:
        cursor.execute(sql1)
        conn.commit()
        tup = cursor.fetchall()
        if len(tup) == 0:
            status = 1
        else:
            status = 0
    finally:
        cursor.close()
        conn.close()
    return status
