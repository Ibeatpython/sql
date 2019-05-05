
import sqlite3



#如果数据库不存在，创建一个新的数据库，
conn = sqlite3.connect("new.db")

#conn = sqlite3.connect(":memory:")  相当于连接临时数据库，当关闭数据库连接后，在memory中创建的说有表都会消失

#获取一个执行sql命令的游标对象
cursor = conn.cursor()

#创建一个表
cursor.execute("""CREATE TABLE population(city TEXT, state TEXT, population INT)""")

#关闭数据库连接
conn.close()