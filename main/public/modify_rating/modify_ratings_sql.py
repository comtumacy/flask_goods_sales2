# coding=utf-8
import pymysql


# 修改评论
def modify_ratings_sql(text, start, to_examine, good_id, no):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "UPDATE ratings SET Rtext = '{}', Rstarts = '{}', toexamine = '{}' WHERE Rgoodsno = {} and Rno = {};".format(text, start, to_examine, good_id, no)
    cursor.execute(sql1)
    conn.commit()
    cursor.close()
    conn.close()
