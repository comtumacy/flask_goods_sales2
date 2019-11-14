# coding=utf-8
import pymysql


# 根据请求不同返回去重后的结果
def select_type_sql(num, content):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "SELECT * FROM shoptype"
    sql2 = "SHOW full COLUMNS FROM shoptype"
    cursor.execute(sql1)
    conn.commit()
    result = cursor.fetchall()
    cursor.execute(sql2)
    conn.commit()
    result2 = cursor.fetchall()

    all_list = []  # 数组列表
    result2list = []  # 字段列表
    for item in result2:  # 提取字段至字段列表
        result2list.append(item[0])

    for i in range(len(result)):  # 把每个字段转为字典
        result_list = list(result[i])
        all_dict = dict(zip(result2list, result_list))
        all_list.append(all_dict)

    cursor.close()
    conn.close()

    # 获取索引，去除重复值并返回结果
    Stid = []
    Stname = []
    Stype = []
    Sclassification = []
    index_list = []
    return_list = []
    for i in range(len(all_list)):
        Stid.append(all_list[i]['Stid'])
        Stname.append(all_list[i]['Stname'])
        Stype.append(all_list[i]['Stype'])
        Sclassification.append(all_list[i]['Sclassification'])
    # 判断所请求的数据类型
    if num == 1:
        # 查找索引
        for index, value in enumerate(Stype):
            if value == content:
                index_list.append(index)
        # 根据索引查找下一个类别的值
        for i in range(len(index_list)):
            return_list.append(Sclassification[index_list[i]])
        # 去重
        return_list = list(set(return_list))
    elif num == 2:
        # 查找索引
        for index, value in enumerate(Sclassification):
            if value == content:
                index_list.append(index)
        # 根据索引查找下一个类别的值
        for i in range(len(index_list)):
            return_list.append(Stname[index_list[i]])
        # 去重
        return_list = list(set(return_list))
    elif num == 3:
        # 查找最后的Stid
        for index, value in enumerate(Stname):
            if value == content:
                index_list.append(index)
        return_list.append(Stid[index_list[0]])
    return return_list
