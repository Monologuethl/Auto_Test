import xlrd
import pymysql

book = xlrd.open_workbook("IDC_IP.xlsx")  # 文件名，把文件与py文件放在同一目录下
sheet = book.sheet_by_name("Sheet1")  # execl里面的表明
# pymysql.connect("localhost","root","root","IP_Excel" )
database = pymysql.connect(host="127.0.0.1",
                           user="root",
                           passwd="root",
                           db="IP_Excel",
                           charset="utf8mb4")  # 连接数据库

cursor = database.cursor()

query = """INSERT INTO ISP (ISP_Name,IP_Domain) VALUES (%s, %s)"""  # 插入语句

for r in range(1, sheet.nrows):  # 第一行是我的标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1

    ISP_Name = sheet.cell(r, 0).value
    IP_Domain = sheet.cell(r, 1).value

    values = (ISP_Name, IP_Domain)
    try:
        cursor.execute(query, values)  # 执行sql语句
        print("Done! ")
    except Exception as e:
        print(e)
cursor.close()  # 关闭连接
database.commit()  # 提交
database.close()  # 关闭数据
