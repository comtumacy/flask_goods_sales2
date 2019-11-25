# coding=utf-8
import pymysql


# 分类商品获取
def public_get_goods_detailed_sql(good_type, content, page_num):
    goods_content = []
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    if good_type == 1 or good_type == 2:
        sql0 = "SELECT Stid FROM shoptype WHERE Sclassification = '{}'".format(content)
        cursor.execute(sql0)
        conn.commit()
        result0 = cursor.fetchall()
        type_id = str(result0[0][0])[0:3]
        page_num = (int(page_num) - 1) * 20

    if good_type == 1:
        sql1 = "SELECT `goodId`,`Name`,Price,book_img FROM (SELECT * FROM `bookinfo` WHERE Stid LIKE '{}%')  as  tmp LIMIT {},20".format(type_id, page_num)
        cursor.execute(sql1)
        conn.commit()
        result1 = cursor.fetchall()
        for i in range(len(result1)):
            goods_content.append({'good_id': result1[i][0], 'name': result1[i][1], 'price': result1[i][2], 'imgUrl': result1[i][3]})
        sql2 = "SELECT COUNT(*) FROM bookinfo WHERE Stid LIKE '{}%'".format(type_id)
        cursor.execute(sql2)
        conn.commit()
        page_num_all = cursor.fetchall()[0][0]

    elif good_type == 2:
        sql1 = "SELECT `goodId`,`title`,price,img FROM (SELECT * FROM `phoneinfo` WHERE Stid LIKE '{}%')  as  tmp LIMIT {},20".format(type_id, page_num)
        cursor.execute(sql1)
        conn.commit()
        result1 = cursor.fetchall()
        for i in range(len(result1)):
            goods_content.append({'good_id': result1[i][0], 'name': result1[i][1], 'price': result1[i][2], 'imgUrl': result1[i][3]})
        sql2 = "SELECT COUNT(*) FROM phoneinfo WHERE Stid LIKE '{}%'".format(type_id)
        cursor.execute(sql2)
        conn.commit()
        page_num_all = cursor.fetchall()[0][0]

    elif good_type == 3:
        sql1 = "SELECT `goodId`,`Name`,Price,book_img  FROM bookinfo LIMIT {},20".format(page_num)
        cursor.execute(sql1)
        conn.commit()
        result1 = cursor.fetchall()
        for i in range(len(result1)):
            goods_content.append({'good_id': result1[i][0], 'name': result1[i][1], 'price': result1[i][2], 'imgUrl': result1[i][3]})
        sql2 = "SELECT COUNT(*) FROM bookinfo"
        cursor.execute(sql2)
        conn.commit()
        page_num_all = cursor.fetchall()[0][0]

    else:
        sql1 = "SELECT `good_no`,`good_title`,price,img  FROM phoneinfo LIMIT {},20".format(page_num)
        cursor.execute(sql1)
        conn.commit()
        result1 = cursor.fetchall()
        for i in range(len(result1)):
            goods_content.append({'good_id': result1[i][0], 'name': result1[i][1], 'price': result1[i][2], 'imgUrl': result1[i][3]})
        sql2 = "SELECT COUNT(*) FROM phoneinfo"
        cursor.execute(sql2)
        conn.commit()
        page_num_all = cursor.fetchall()[0][0]

    cursor.close()
    conn.close()
    return goods_content, page_num_all


# public_get_goods_detailed_sql(1, '小说', 1)
