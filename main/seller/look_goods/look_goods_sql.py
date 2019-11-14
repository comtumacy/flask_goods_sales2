# coding=utf-8
import pymysql


# 插入书籍信息
def delete_goods_sql(username):
    # 插入数据
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsseller',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "SELECT * FROM `goodsmanagement` WHERE sellername = '{}' AND goodstype LIKE '2%' ORDER BY goodstype ASC".format(username)
    sql2 = "SHOW full COLUMNS FROM `goodsmanagement`"
    cursor.execute(sql1)
    conn.commit()
    result1 = cursor.fetchall()
    cursor.execute(sql2)
    conn.commit()
    result2 = cursor.fetchall()

    all_list = []  # 数组列表
    result2list = []  # 字段列表
    for item in result2:  # 提取字段至字段列表
        result2list.append(item[0])

    for i in range(len(result1)):  # 把每个字段转为字典
        tup_list = list(result1[i])
        all_dict = dict(zip(result2list, tup_list))
        all_list.append(all_dict)

    phone_id = []
    for i in range(len(all_list)):
        phone_id.append(all_list[i]['goodsid'])

    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    phone_title = []
    for i in range(len(phone_id)):
        sql3 = "SELECT title FROM `phoneinfo` where goodId = {}".format(phone_id[i])
        cursor.execute(sql3)
        conn.commit()
        result3 = cursor.fetchall()[0][0]
        phone_title.append(result3)

    return_list = []
    for i in range(len(all_list)):
        return_list.append({'goodtitle': phone_title[i], 'goodsid': all_list[i]['goodsid'], 'goodstype': all_list[i]['goodstype'], 'registrationtime': all_list[i]['registrationtime']})
    print(return_list)
    cursor.close()
    conn.close()

    return ''


delete_goods_sql('seller4')
