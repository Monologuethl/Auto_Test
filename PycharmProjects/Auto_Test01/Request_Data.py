from Tools.Read_Excel import ReadExcel
import requests
import time
import datetime


class RequestData:
    def __init__(self, request_info):
        # 模块名称
        self.module = request_info['module']
        # 接口url
        self.url = request_info['url']
        # 接口请求方式
        self.operation = request_info['operation']
        # 参数
        arg_dict = request_info['arg_dict']
        self.arg_list = []
        # 今天日期
        today = datetime.date.today()
        # 昨天时间
        yesterday = today - datetime.timedelta(days=1)
        # 昨天开始时间戳
        yesterday_start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
        # 今天开始时间戳
        today_start_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d')))

        for key in arg_dict:
            if key.lower() == 'begintime':
                if arg_dict[key] == '':
                    if 'begin_offset' in request_info:
                        if request_info['begin_offset'] == '':
                            beginoffset = 0
                        else:
                            beginoffset = request_info['begin_offset']
                        yesterday_start_time = yesterday_start_time + beginoffset * 3600

                    self.arg_list.append(key + '=' + str(yesterday_start_time))
                else:
                    begintimeArray = time.strptime(arg_dict[key], "%Y-%m-%d %H:%M:%S")
                    # 指定时间格式 "2018-07-20 16:28:54"
                    self.arg_list.append(key + '=' + str(time.mktime(begintimeArray)))
            elif key.lower() == 'endtime':
                if arg_dict[key] == '':
                    if 'end_offset' in request_info:
                        if request_info['end_offset'] == '':
                            endoffset = 0
                        else:
                            endoffset = request_info['begin_offset']
                        today_start_time = today_start_time + endoffset * 3600

                    self.arg_list.append(key + '=' + str(today_start_time))
                else:
                    endtimeArray = time.strptime(arg_dict[key], "%Y-%m-%d %H:%M:%S")
                    # 指定时间格式 "2018-07-20 16:28:54"
                    self.arg_list.append(key + '=' + str(time.mktime(endtimeArray)))
            else:
                self.arg_list.append(key + '=' + arg_dict[key])

        # 数据范围
        self.range_dict = request_info['range_dict']

    def get_request_url(self):
        return self.url + '?' + '&'.join(self.arg_list)

    def request_data(self):
        operation = self.operation
        if operation.lower() == 'get':
            res = requests.get(self.get_request_url())
            return res.text
        return ''


def test(filepath):
    config = ReadExcel(filepath)
    config.load_config()
    res_list = []
    range_list = []
    for i in range(0, len(config.interface_list)):
        data = RequestData(config.interface_list[i])
        range_list.append(data.range_dict)
        res_list.append(data.request_data())
        print("获取数据中：：：：：：：：："+format((i + 1) / len(config.interface_list), '0.1%'))
    return res_list,config.interface_list,range_list

