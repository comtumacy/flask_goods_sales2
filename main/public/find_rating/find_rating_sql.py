# coding=utf-8
import pymysql


# 搜索评论
def find_rating_sql(username, page_number, content):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "select * FROM ratings WHERE ratinguser = '{}' AND (Rgoodsno LIKE '%{}%' OR ratinguser LIKE '%{}%') order by `Rid` LIMIT {}, 5;".format(username, content, content, (int(page_number) - 1) * 5)
    sql2 = "SHOW full COLUMNS FROM ratings"
    sql3 = "select COUNT(*) FROM ratings WHERE ratinguser = '{}' AND (Rgoodsno LIKE '%{}%' OR ratinguser LIKE '%{}%');".format(username, content, content)
    cursor.execute(sql1)
    conn.commit()
    tup1 = cursor.fetchall()

    tup3 = 0
    if len(tup1) == 0:
        all_list = []
    else:
        cursor.execute(sql2)
        conn.commit()
        tup2 = cursor.fetchall()
        cursor.execute(sql3)
        conn.commit()
        tup3 = cursor.fetchall()[0][0]
        all_list = []  # 数组列表
        tup2list = []  # 字段列表
        for item in tup2:  # 提取字段至字段列表
            tup2list.append(item[0])

        for i in range(len(tup1)):  # 把每个字段转为字典
            tup_list = list(tup1[i])
            all_dict = dict(zip(tup2list, tup_list))
            all_list.append(all_dict)
        for i in range(len(all_list)):
            sql4 = "SELECT `Name`,`book_img` FROM bookinfo WHERE `goodId` = {}".format(int(all_list[i]['Rgoodsno']))
            cursor.execute(sql4)
            conn.commit()
            tup4 = cursor.fetchall()
            if len(tup4) == 0:
                sql4 = "SELECT `title`,`img` FROM phoneinfo WHERE `good_no` = {}".format(int(all_list[i]['Rgoodsno']))
                cursor.execute(sql4)
                conn.commit()
                tup4 = cursor.fetchall()
            title = tup4[0][0]
            img = tup4[0][1]
            all_list[i]['title'] = title
            all_list[i]['img'] = img
        cursor.close()
        conn.close()
        # print(all_list)

    return tup3, all_list


# look_rating_sql('lytlyt', 35)
