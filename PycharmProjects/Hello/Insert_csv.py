import pymysql
import csv
conn = pymysql.Connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'root',
    db = 'IP_Excel',
    charset = 'utf8')

cursor = conn.cursor()
sql = "insert into test  values (%s,%s,%s,%s)"

file = open('chengyuwang.csv','r',encoding='UTF-8')
data=[]
for row in csv.reader(file):
   data.append(row)

file.close()
cursor.executemany(sql,data)
conn.commit()
conn.close()
