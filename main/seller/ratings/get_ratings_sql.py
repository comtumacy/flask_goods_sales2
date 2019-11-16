# coding=utf-8
import pymysql


# 根据商品id获取评论
def get_ratings_sql(good_type, good_id):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    #  如果商品为书籍
    if good_type == 1:
        sql1 = "SELECT * FROM ratings WHERE Rgoodsno = {}".format(int(good_id))
        sql2 = "SHOW full COLUMNS FROM `ratings`"
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
        cursor.close()
        conn.close()
    #  如果商品为电子产品
    else:
        sql0 = "SELECT good_no FROM `phoneinfo` WHERE goodId = {}".format(int(good_id))
        cursor.execute(sql0)
        conn.commit()
        good_no = cursor.fetchall()
        if len(good_no) == 0:
            all_list = ''
            cursor.close()
            conn.close()
        else:
            good_no = good_no[0][0]
            sql1 = "SELECT * FROM ratings WHERE Rgoodsno = {}".format(int(good_no))
            sql2 = "SHOW full COLUMNS FROM `ratings`"
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
            cursor.close()
            conn.close()
    return all_list


# get_ratings_sql(97875502609171)
