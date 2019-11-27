# coding=utf-8
import pymysql


# 添加收藏
def add_favorites_sql(username, good_type, good_id):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsbuyer',
                           charset='utf8')
    cursor = conn.cursor()
    try:
        sql1 = "INSERT INTO Favoritesgood (Uname,typeid,goodid) VALUES ('{}', {}, {})".format(username, good_type, good_id)
        cursor.execute(sql1)
        conn.commit()
        status = 1
    except Exception:
        status = 0
    # tup = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return status
