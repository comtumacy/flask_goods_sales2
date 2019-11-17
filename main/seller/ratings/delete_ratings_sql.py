# coding=utf-8
import pymysql


# 根据商品id删除评论
def delete_ratings_sql(good_type, good_id, r_no):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    #  如果商品为书籍
    if good_type == 1:
        sql1 = "DELETE FROM `ratings` WHERE Rgoodsno = {} and Rno = {}".format(good_id, r_no)
        cursor.execute(sql1)
        conn.commit()
    #  如果商品为电子产品
    else:
        sql0 = "SELECT good_no FROM `phoneinfo` WHERE goodId = {}".format(int(good_id))
        cursor.execute(sql0)
        conn.commit()
        good_no = cursor.fetchall()[0][0]
        sql1 = "DELETE FROM `ratings` WHERE Rgoodsno = {} and Rno = {}".format(good_no, r_no)
        cursor.execute(sql1)
        conn.commit()
    cursor.close()
    conn.close()
