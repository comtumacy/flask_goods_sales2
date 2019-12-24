# coding=utf-8
import pymysql


# 查询库存种类-数量
def stock_reports_sql(username):
    stock_reports_list_all = []
    stock_reports_list = []
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsseller',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "SELECT goodstype FROM `goodsmanagement` where sellername = '{}' ".format(username)
    cursor.execute(sql1)
    conn.commit()
    result1 = cursor.fetchall()
    for i in range(len(result1)):
        stock_reports_list_all.append(result1[i][0])
    for i in range(len(stock_reports_list_all)):
        sign = 0
        for j in range(len(stock_reports_list)):
            if stock_reports_list_all[i] in stock_reports_list[j].values():
                stock_reports_list[j]['value'] = stock_reports_list[j]['value'] + 1
                sign = 1
        if sign == 0:
            stock_reports_list.append({'type': stock_reports_list_all[i], 'value': 1})
    print(stock_reports_list)
    cursor.close()
    conn.close()

    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    for i in range(len(stock_reports_list)):
        sql1 = "SELECT Stname FROM `shoptype` WHERE Stid = {}".format(stock_reports_list[i]['type'])
        cursor.execute(sql1)
        conn.commit()
        result1 = cursor.fetchall()
        stock_reports_list[i]['type'] = result1[0][0]
    cursor.close()
    conn.close()
    return stock_reports_list

# stock_reports_sql('seller1')
