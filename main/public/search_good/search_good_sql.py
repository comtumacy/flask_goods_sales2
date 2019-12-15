# coding=utf-8
import pymysql


# 模糊搜索商品
def search_good_sql(good_type, content, page_num):
    goods_content = []
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    page_num = (int(page_num) - 1) * 20
    cursor = conn.cursor()
    if good_type == 1:
        sql1 = "SELECT goodId,`Name`,Price,book_img FROM `bookinfo` WHERE `Name` LIKE '%{}%' OR goodId LIKE '%{}%' LIMIT {},20;".format(content, content, page_num)
        sql2 = "SELECT COUNT(*) FROM `bookinfo` WHERE `Name` LIKE '%{}%' OR goodId LIKE '%{}%'".format(content, content)
        cursor.execute(sql1)
        conn.commit()
        result1 = cursor.fetchall()
        for i in range(len(result1)):
            goods_content.append({'good_id': result1[i][0], 'name': result1[i][1], 'price': result1[i][2], 'imgUrl': result1[i][3]})
        cursor.execute(sql2)
        conn.commit()
        result2 = cursor.fetchall()[0][0]
    else:
        sql1 = "SELECT goodId,`title`,price,img FROM `phoneinfo` WHERE `title` LIKE '%{}%' OR goodId LIKE '%{}%' LIMIT {},20;".format(content, content, page_num)
        sql2 = "SELECT COUNT(*) FROM `phoneinfo` WHERE `title` LIKE '%{}%' OR goodId LIKE '%{}%'".format(content, content)
        cursor.execute(sql1)
        conn.commit()
        result1 = cursor.fetchall()
        for i in range(len(result1)):
            goods_content.append({'good_id': result1[i][0], 'name': result1[i][1], 'price': result1[i][2], 'imgUrl': result1[i][3]})
        cursor.execute(sql2)
        conn.commit()
        result2 = cursor.fetchall()[0][0]

    cursor.close()
    conn.close()
    return goods_content, result2


# search_good_sql(2, 'vivo', '1')
