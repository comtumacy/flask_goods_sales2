# coding=utf-8
import pymysql


# 查询卖家商品信息
def look_goods_sql(username):
    look_goods_list = []
    for k in range(2):
        conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsseller',
                               charset='utf8')
        cursor = conn.cursor()
        sql1 = "SELECT * FROM `goodsmanagement` WHERE sellername = '{}' AND goodstype LIKE '{}%' ORDER BY goodstype ASC".format(username, k + 1)
        sql2 = "SHOW full COLUMNS FROM `goodsmanagement`"
        cursor.execute(sql1)
        conn.commit()
        result1 = cursor.fetchall()
        cursor.execute(sql2)
        conn.commit()
        result2 = cursor.fetchall()

        # 获取全部数据
        print('获取全部数据...')
        all_list = []  # 数组列表
        result2list = []  # 字段列表
        for item in result2:  # 提取字段至字段列表
            result2list.append(item[0])

        # 全部商品数据汇总
        print('全部商品数据汇总...')
        for i in range(len(result1)):  # 把每个字段转为字典
            tup_list = list(result1[i])
            all_dict = dict(zip(result2list, tup_list))
            all_list.append(all_dict)

        # 获取卖家发布的商品ID
        print('获取卖家发布的商品ID...')
        phone_id = []
        for i in range(len(all_list)):
            phone_id.append(all_list[i]['goodsid'])

        conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                               charset='utf8')
        cursor = conn.cursor()
        phone_title = []

        if k == 0:
            table_name = 'bookinfo'
            name = 'Name'
        else:
            table_name = 'phoneinfo'
            name = 'title'
        # 获取卖家发布的商品名字
        print('获取卖家发布的商品名字...')
        for i in range(len(phone_id)):
            sql3 = "SELECT {} FROM `{}` where goodId = {}".format(name, table_name, phone_id[i])
            cursor.execute(sql3)
            conn.commit()
            result3 = cursor.fetchall()[0][0]
            phone_title.append(result3)

        # 卖家发布的商品整合
        print('卖家发布的商品整合...')
        return_list = []
        for i in range(len(all_list)):
            return_list.append({'goodtitle': phone_title[i], 'goodsid': all_list[i]['goodsid'], 'goodstype': all_list[i]['goodstype'], 'registrationtime': all_list[i]['registrationtime']})
        look_goods_list.append({table_name: return_list})
        cursor.close()
        conn.close()
    return look_goods_list


# look_goods_sql('seller0')
