# coding=utf-8
import pymysql


# 根据id获取商品和商品评论
def public_get_goods_id_sql(good_type, good_id):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()

    if good_type == 1:
        sql1 = "SELECT * FROM bookinfo WHERE goodId = {}".format(good_id)
        sql2 = "SHOW full COLUMNS FROM bookinfo"
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

    else:
        sql1 = "SELECT * FROM phoneinfo WHERE goodId = {}".format(good_id)
        sql2 = "SHOW full COLUMNS FROM phoneinfo"
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

    sql3 = "SELECT * FROM ratings WHERE Rgoodsno = {}".format(good_id)
    cursor.execute(sql3)
    conn.commit()
    result3 = cursor.fetchall()
    if len(result3) != 0:
        sql4 = "SHOW full COLUMNS FROM ratings"
        cursor.execute(sql4)
        conn.commit()
        result4 = cursor.fetchall()
        all_rating_list = []  # 数组列表
        result4list = []  # 字段列表
        for item in result4:  # 提取字段至字段列表
            result4list.append(item[0])

        for i in range(len(result3)):  # 把每个字段转为字典
            tup_list = list(result3[i])
            all_dict = dict(zip(result4list, tup_list))
            all_rating_list.append(all_dict)
    else:
        all_rating_list = []

    cursor.close()
    conn.close()
    return all_list, all_rating_list


# public_get_goods_id_sql(1, 20718719)
