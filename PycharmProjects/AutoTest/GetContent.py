import requests
import time
import datetime
from Tools.ReadExcel import ReadeExcel
from Tools.GetLog import Log

Log(r'C:\Users\Tong\PycharmProjects\AutoTest\log\log.log')


class GetContent(object):

    @staticmethod
    def content(page_index, file_path):
        start = time.clock()
        sheet = ReadeExcel().read_excel(page_index, file_path)
        sheet_1_name = sheet.name
        Content = []
        process = 1
        for r in range(1, sheet.nrows):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
            print("读取数据中，请稍等：：：：：：：：：" + format(process / sheet.nrows, '0.1%'))
            # 编号
            # id = sheet.cell(r, 0).value
            # 接口名称
            name = sheet.cell(r, 1).value
            # 调用方式
            fun = sheet.cell(r, 2).value
            # 接口url
            url = sheet.cell(r, 3).value
            # 参数个数
            # arg_num = int(sheet.cell(r, 4).value)
            # 参数初始化
            arg = sheet.cell(r, 5).value
            list: [] = arg.split(',')

            today = datetime.date.today()
            yesterday = today - datetime.timedelta(days=1)
            # 昨天开始时间戳
            yesterday_start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
            # 昨天结束时间戳
            yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1
            if len(list) > 1:
                for i in range(0, len(list)):
                    if list[i] == 'beginTime=':
                        list[i] = list[i] + str(yesterday_start_time)
                    if list[i] == 'endTime=':
                        list[i] = list[i] + str(yesterday_end_time)
            for i in range(0, len(list) - 1):
                list[i] = list[i] + '&'
            auto_url = url + '?' + ''.join(list)
            print("获得第" + str(process) + "条url：：：：：：：：" + auto_url)
            if fun == "GET" or "get":
                response = requests.get(auto_url)
                Content.append([name, sheet_1_name, response.text])
                process = process + 1
        print("数据读取完毕！：：：：：：：：" + format(process / sheet.nrows, '0.1%'))
        elapsed = (time.clock() - start)
        print("Read file was used:%.2fs" % elapsed)
        return Content
