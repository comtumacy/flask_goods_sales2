# coding=utf-8
import pymysql


# 插入书籍信息
def add_book_sql(good_id, name, price, discount, old_price, author, area, publishing_time, open_book, paper, packing, suit, introduction, book_img, stid, new_and_old_degree, number):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='goods',
                           charset='utf8')
    try:
        cursor = conn.cursor()
        sql1 = "INSERT INTO bookinfo (goodId,`Name`,Price,Discount,Old_price,Author,Area,Publishing_time,Open_book,Paper,Packing,Suit,Introduction,book_img,Stid,NewAndOldDegree,`number`) VALUES('{}','{}',{},{},{},'{}','{}','{}','{}','{} ','{}','{}','{}','{}',{},{},{}})".format(good_id, name, price, discount, old_price, author, area, publishing_time, open_book, paper, packing, suit, introduction, book_img, stid, new_and_old_degree, number)
        cursor.execute(sql1)
        conn.commit()
        status = 1
    # 判断是否有值重复
    except BaseException as e:
        status = 0
        print(e)
    finally:
        cursor.close()
        conn.close()
    return status
