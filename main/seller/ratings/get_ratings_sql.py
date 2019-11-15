# coding=utf-8
import pymysql


# 查询卖家商品信息
def look_goods_sql(username):
    for k in range(2):
        # 插入数据
        # 书籍数据整合、收集数据整合
        conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                               charset='utf8')
        cursor = conn.cursor()
        sql1 = "SELECT * FROM ratings WHERE Rgoodsno = 9787550260917"
        sql2 = "SHOW full COLUMNS FROM `goodsmanagement`"
        cursor.execute(sql1)
        conn.commit()
        result1 = cursor.fetchall()
        cursor.execute(sql2)
        conn.commit()
        result2 = cursor.fetchall()

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
