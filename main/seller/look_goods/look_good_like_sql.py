# coding=utf-8
import pymysql


# 查询卖家商品信息
def look_good_like_sql(find_content, Uname):
    # 查询该卖家的商品ID总和
    ids_list = []
    title_list = []
    index_list = []
    return_list = []
    print('查询该卖家的商品ID')
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsseller',
                           charset='utf8')
    cursor = conn.cursor()
    sql0 = "SELECT goodsid FROM `goodsmanagement` WHERE sellername = '{}'".format(Uname)
    cursor.execute(sql0)
    conn.commit()
    ids = cursor.fetchall()
    for i in range(len(ids)):
        ids_list.append(ids[i][0])
    cursor.close()
    conn.close()

    # 查询符合此商品ID的商品的标题
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    print('查询符合此商品ID的商品的标题')
    for i in range(len(ids_list)):
        sql1 = "SELECT title FROM `phoneinfo` WHERE title LIKE '%{}%' and goodId = {}".format(find_content, ids_list[i])
        cursor.execute(sql1)
        conn.commit()
        content = cursor.fetchall()
        if len(content) != 0:
            title_list.append(content[0][0])
            # 将符合模糊查询的ID下标记录
            index_list.append(i)
        sql1 = "SELECT `Name` FROM `bookinfo` WHERE `Name` LIKE '%{}%' and goodId = {}".format(find_content, ids_list[i])
        cursor.execute(sql1)
        conn.commit()
        content = cursor.fetchall()
        if len(content) != 0:
            title_list.append(content[0][0])
            # 将符合模糊查询的ID下标记录
            index_list.append(i)
    cursor.close()
    conn.close()

    # 商品数据汇总
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsseller',
                           charset='utf8')
    cursor = conn.cursor()
    print('商品数据汇总')
    for i in range(len(index_list)):
        sql2 = "SELECT * FROM `goodsmanagement` WHERE goodsid = {}".format(ids_list[index_list[i]])
        cursor.execute(sql2)
        conn.commit()
        result = cursor.fetchall()
        return_list.append({'goodtitle': title_list[i], 'goodsid': ids_list[index_list[i]], 'goodstype': result[0][2],'registrationtime': result[0][3]})
    cursor.close()
    conn.close()

    return return_list


# look_good_like_sql('华为', 'seller4')
