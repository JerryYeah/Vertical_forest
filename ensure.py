# coding=utf-8

import MySQLdb


db = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="vertical_forest",
                     port=3306, charset="utf8")
cursor =db.cursor()

sql = """select Uname from user where Uid=2"""

cursor.execute(sql)
result=cursor.fetchone()
print(result)

db.close()