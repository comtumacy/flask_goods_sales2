# coding=utf-8
import pymysql


# 根据用户名获取用户信息
def get_user_info_sql(username):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsUser',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "SELECT * FROM userinfo WHERE Uname = '{}'".format(username)
    sql2 = "SHOW full COLUMNS FROM userinfo"
    cursor.execute(sql1)
    conn.commit()
    tup1 = cursor.fetchall()
    cursor.execute(sql2)
    conn.commit()
    tup2 = cursor.fetchall()
    all_list = []  # 数组列表
    tup2list = []  # 字段列表
    for item in tup2:  # 提取字段至字段列表
        tup2list.append(item[0])

    for i in range(len(tup1)):  # 把每个字段转为字典
        tup_list = list(tup1[i])
        all_dict = dict(zip(tup2list, tup_list))
        all_list.append(all_dict)
    cursor.close()
    conn.close()
    # print(all_list)
    return all_list

# get_user_info_sql('lytlyt')
