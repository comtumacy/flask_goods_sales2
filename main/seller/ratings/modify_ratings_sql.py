# coding=utf-8
import pymysql


# 修改评论
def modify_ratings_sql(good_type, text, start, to_examine, good_id, no):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    #  如果商品为书籍
    if good_type == 1:
        sql1 = "UPDATE ratings SET Rtext = '{}', Rstarts = '{}', toexamine = '{}' WHERE Rgoodsno = {} and Rno = {};".format(text, start, to_examine, good_id, no)
        cursor.execute(sql1)
        conn.commit()
        pass
    #  如果商品为电子产品
    else:
        sql0 = "SELECT good_no FROM `phoneinfo` WHERE goodId = {}".format(int(good_id))
        cursor.execute(sql0)
        conn.commit()
        good_no = cursor.fetchall()
        good_no = good_no[0][0]
        sql1 = "UPDATE ratings SET Rtext = '{}', Rstarts = '{}', toexamine = '{}' WHERE Rgoodsno = {} and Rno = {};".format(
            text, start, to_examine, good_no, no)
        cursor.execute(sql1)
        conn.commit()
