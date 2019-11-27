# coding=utf-8
import pymysql


# 删除收藏
def delete_favorites_sql(username, good_id):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsbuyer',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "DELETE FROM Favoritesgood WHERE goodid = {} AND Uname = '{}'".format(int(good_id), username)
    cursor.execute(sql1)
    conn.commit()
    cursor.close()
    conn.close()
