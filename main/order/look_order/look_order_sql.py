# coding=utf-8
import pymysql


# 查询订单信息
def look_order_sql(date_content, username, page_number):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!',  db='goodsorder',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "SELECT * FROM `order` WHERE (goodid LIKE '%{}%' OR date LIKE '%{}%') AND (`buyer` = '{}' OR `seller` = '{}') order by `orderid` LIMIT {}, 10;".format(date_content, date_content, username, username, (int(page_number) - 1) * 10)
    sql2 = "SHOW full COLUMNS FROM `order`"
    sql3 = "SELECT COUNT(*) FROM `order` WHERE goodid LIKE '%{}%' OR date LIKE '%{}%' AND `buyer` = '{}' OR `seller` = '{}';".format(date_content, date_content, username, username)
    cursor.execute(sql1)
    conn.commit()
    result1 = cursor.fetchall()

    result3 = 0
    if len(result1) == 0:
        all_list = []
    else:
        cursor.execute(sql2)
        conn.commit()
        result2 = cursor.fetchall()
        cursor.execute(sql3)
        conn.commit()
        result3 = cursor.fetchall()[0][0]
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
    return all_list, result3
