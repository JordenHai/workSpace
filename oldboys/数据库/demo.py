import pymysql

# 创建了连接
conn = pymysql.connect(host='192.168.235.131',port=3306,user='root',passwd='123456',db='oldboydb')

#创建游标
cursor = conn.cursor()

data = [
    ("NiLiang", 23, "2019-8-24", "M"),
    ("ChenZhong", 25, "2019-8-23", "F"),
    ("WangTian", 27, "2019-8-25", "M"),
]

effect_row = cursor.executemany("insert into student (name,age,register_date,sex) values (%s,%s,%s,%s)",data)
conn.commit()

# effect_row = cursor.execute("select * from student")

# print(cursor.fetchone())
print(cursor.fetchall())





