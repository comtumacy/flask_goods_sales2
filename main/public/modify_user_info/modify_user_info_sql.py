# coding=utf-8
import pymysql


# 根据用户名修改用户信息
def modify_user_info_sql(sex, province, city, phone, truename, address, postalcode, emain, codetype, codenumber, username):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goodsUser',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "UPDATE userinfo set Ufsex = '{}',Ufprovince = '{}',Ufcity = '{}',Ufphone = '{}', Uftruename = '{}',Ufaddress = '{}', Ufpostalcode = '{}', Uemain = '{}', Ucodetype = '{}', Ucodenumber = '{}' WHERE Uname = '{}'".format(sex, province, city, phone, truename, address, postalcode, emain, codetype, codenumber, username)
    cursor.execute(sql1)
    conn.commit()
    # tup1 = cursor.fetchall()
    
    cursor.close()
    conn.close()
