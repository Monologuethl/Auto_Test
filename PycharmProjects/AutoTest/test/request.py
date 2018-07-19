import requests
import xlrd
import time
import datetime
from collections import OrderedDict
from pyexcel_xls import save_data

def Get_Content(str):
    book = xlrd.open_workbook("InterfaceCase.xls")  # 文件名，把文件与py文件放在同一目录下
    sheet = book.sheet_by_name(str)  # execl里面的表明
    sheet_1_name=sheet.name
    Content=[]
    for r in range(1, sheet.nrows):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
        # 编号
        id=sheet.cell(r, 0).value
        # 接口名称
        name=sheet.cell(r, 1).value
        # 调用方式
        fun=sheet.cell(r, 2).value
        # 接口url
        url=sheet.cell(r, 3).value
        # 参数个数
        arg_num=int(sheet.cell(r, 4).value)
        # 参数初始化
        arg=[]
        for i in range(0,6):
            arg.append(sheet.cell(r,5+i).value)
            # print(arg)
        # 存放参数内容
        arg_content=[]
        # 参数小于等于3,赋值一个参数
        if arg_num<3:
            arg_content.append(sheet.cell(r,11))
        # 参数大于3
        if arg_num>=3:
            arg_content.append(sheet.cell(r,11))
            i=3
            for i in range(3,6):
                if arg[i] != "":
                    arg_content.append(sheet.cell(r,i+9))

        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)

        # 昨天开始时间戳
        yesterday_start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
        # 昨天结束时间戳
        yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1


        if arg_num==3:
            if arg[1] & arg[2]:
                Test_url=url+'?'+arg[0]+'='+str(arg_content[0])+'&'+arg[1]+'='+str(yesterday_start_time)+'&'+arg[2] + '='+str(yesterday_end_time)
        if arg_num>3:

            Test_url=url+'?'+arg[0]+'='+str(arg_content[0])+'&'+arg[1]+'='+str(yesterday_start_time)+'&'+arg[2] + '='+str(yesterday_end_time)
        if fun == "GET" or "get":
            responnse=requests.get(Test_url)
            Content.append(responnse.text)
    # print(Content)
    return Content


def save_xls_file(Content):
    data = OrderedDict()
    # sheet表的数据
    sheet_1 = []
    for row in Content:
        row_1_data =[row]
        # print(row_1_data)
        sheet_1.append(row_1_data)
    # 添加sheet表
    data.update({u"这是XX表": sheet_1})

    # 保存成xls文件
    save_data(r"Auto_Test.xls", data)

if __name__ == '__main__':
    save_xls_file(Get_Content("内容网络全景图"))

