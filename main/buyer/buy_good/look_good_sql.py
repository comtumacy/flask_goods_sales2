# coding=utf-8
import pymysql


# 根据ID查询商品
def look_good_sql(good_id, good_type):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    all_list2 = []
    if int(good_type) == 1: 
        sql1 = "SELECT * FROM bookinfo WHERE goodId = {}".format(good_id)
        sql2 = "SHOW full COLUMNS FROM bookinfo"
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
        all_list2.append({'img': all_list[0]['book_img'], 'name': all_list[0]['Name'], 'price': all_list[0]['Price'], 'disCount': all_list[0]['Discount'], 'oldPrice': all_list[0]['Old_price'], 'goodId': all_list[0]['goodId']})
        cursor.close()
        conn.close()
    else:
        sql1 = "SELECT * FROM phoneinfo WHERE goodId = {}".format(good_id)
        sql2 = "SHOW full COLUMNS FROM phoneinfo"
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
        all_list2.append({'img': all_list[0]['img'], 'name': all_list[0]['title'], 'price': all_list[0]['price'],
                          'disCount': '无', 'oldPrice': '无',
                          'goodId': int(all_list[0]['goodId'])})
        cursor.close()
        conn.close()

    return all_list2


# look_good_sql(1, 2)
