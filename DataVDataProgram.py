#!/usr/bin/python3
import time
import pymysql
import random
# 打开数据库连接
db = pymysql.connect("120.55.158.179", "root", "Aa196810", "test")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
id=0
while 1:
    try:
          # 执行SQL语句
        cursor.execute("UPDATE test SET x=%d, y=%d WHERE id = %d" %(random.randint(0,100),random.randint(0,100),id))
         # 提交修改
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    id=id+1
    if  id == 9:
        id=0
        time.sleep(1)


# 关闭连接
db.close()