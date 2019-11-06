# coding=utf-8
import pymysql
import sys


# 注册在用户信息表添加个人信息
def register_sql(Uname, Upwd, Uquestion, Uresult, Usafetycode, Uroleid):
    status = 0
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "INSERT INTO users ( Uname, Upwd, Uquestion, Uresult, Usafetycode, Uroleid) VALUES ( '{}', '{}', '{}', '{}', '{}', {});".format(Uname, Upwd, Uquestion, Uresult, Usafetycode, Uroleid)
    try:
        cursor.execute(sql1)
        conn.commit()
        status = 1
    except:
        # 捕获异常
        info = sys.exc_info()
        info_num = str(info[1])[1:5]
        if info_num == '1062':
            status = 0
    finally:
        cursor.close()
        conn.close()
    return status
