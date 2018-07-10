import IPy
import pymysql

connect=pymysql.connect("localhost", "root", "root", "IP_Excel", charset='utf8')
cursor1=connect.cursor()
cursor2=connect.cursor()
sql_1='select * from ip '

# sql_2="select ip.users isp.isp_name from ip isp where beingip=(selcet IP_Domain from ISP)"

sql_3='select IP_Domain from ISP'
try:
    cursor1.execute(sql_1)
    # cursor2.execute(sql_3)
   # 获取所有记录列表
    results1 = cursor1.fetchall()
    # results2 = cursor2.fetchall()
    for row1  in results1:
      beingip = row1[1]
      endip = row1[2]
      mask = row1[3]
      print(beingip in IPy.IP(beingip))
      print (beingip)


except Exception as e :
    print(e)
