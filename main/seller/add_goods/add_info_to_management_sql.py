# coding=utf-8
import pymysql


# 插入书籍信息
def add_info_to_management_sql(sellername, goodsid, goodstype, registrationtime):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsseller',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "INSERT INTO goodsmanagement (sellername, goodsid, goodstype, registrationtime) VALUES ('{}','{}',{},'{}')".format(sellername, goodsid, goodstype, registrationtime)
    cursor.execute(sql1)
    conn.commit()
    result = cursor.fetchall()
    # 判断是否id值重复
    if len(result) == 0:
        status = 1
    else:
        status = 0
    cursor.close()
    conn.close()
    return status
