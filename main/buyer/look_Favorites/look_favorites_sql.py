# coding=utf-8
import pymysql


# 查询该用户的收藏
def look_favorites_sql(username, page_number):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsbuyer',
                           charset='utf8')
    cursor = conn.cursor()

    sql1 = "SELECT * FROM Favoritesgood WHERE Uname = '{}' order by id LIMIT {}, 5".format(username, (int(page_number) - 1) * 5)
    sql2 = "SHOW full COLUMNS FROM Favoritesgood"
    sql3 = "SELECT count(*) FROM Favoritesgood WHERE Uname = '{}'".format(username)
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
    if len(all_list) == 0:
        page_all_number = 0
    else:
        cursor.execute(sql3)
        conn.commit()
        tup3 = cursor.fetchall()
        page_all_number = tup3[0][0]
    cursor.close()
    conn.close()

    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    all_list2 = []
    for i in range(len(all_list)):
        good_type = all_list[i]['typeid']
        good_id = int(all_list[i]['goodid'])
        if good_type == 1:
            sql4 = "SELECT book_img,`Name`,Price,Discount,Old_price FROM bookinfo WHERE goodId = {}".format(good_id)
            cursor.execute(sql4)
            conn.commit()
            tup4 = cursor.fetchall()
            all_list2.append({'img': tup4[0][0], 'name': tup4[0][1], 'price': tup4[0][2], 'disCount': tup4[0][3], 'oldPrice': tup4[0][4], 'goodId': good_id})
        else:
            sql4 = "SELECT img,title,price FROM phoneinfo WHERE goodId = {}".format(good_id)
            cursor.execute(sql4)
            conn.commit()
            tup4 = cursor.fetchall()
            all_list2.append({'img': tup4[0][0], 'name': tup4[0][1], 'price': tup4[0][2], 'disCount': '无', 'oldPrice': '无', 'goodId': good_id})
    cursor.close()
    conn.close()
    return all_list2, page_all_number


look_favorites_sql('lytlyt', 1)
