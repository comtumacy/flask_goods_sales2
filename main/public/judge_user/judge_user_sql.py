# coding=utf-8
import pymysql


# 判断用户类型
def judge_user_sql(username):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsUser',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "select Uroleid FROM users WHERE Uname = '{}'".format(username)
    cursor.execute(sql1)
    conn.commit()
    user_type = cursor.fetchall()[0][0]
    cursor.close()
    conn.close()
    return user_type


# judge_user_sql('lytlyt')
