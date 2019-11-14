# coding=utf-8
import pymysql


# 插入书籍信息
def add_phone_sql(title, price, good_title, good_weight, good_from, good_system, signal, screen_size, img, stid):
    # 插入数据
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "INSERT INTO phoneinfo (title,Price,good_title,good_weight,good_from,good_system,`signal`,screen_size,img,stid) VALUES ('{}',{},'{}','{}','{}','{}','{}','{}','{}',{})".format(title, price, good_title, good_weight, good_from, good_system, signal, screen_size, img, stid)
    cursor.execute(sql1)
    conn.commit()
    cursor.close()
    conn.close()

    # 获取最后id
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    sql2 = 'SELECT COUNT(*) FROM phoneinfo'
    cursor.execute(sql2)
    conn.commit()
    num = cursor.fetchall()[0][0]
    cursor.close()
    conn.close()

    return num


