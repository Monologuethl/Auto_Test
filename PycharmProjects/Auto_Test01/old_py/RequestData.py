from old_py.ReadExcel import ReadExcel
import requests
import time
import datetime


class RequestData:
    request_url = ''

    def __init__(self, request_info):
        self.interface_item = request_info

    def get_request_url(self):
        url = self.interface_item['url'] + '?'
        # args = ''
        arg_dict = self.interface_item['arg_dict']
        arg_list = []

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
                    arg_list.append(key + '=' + str(yesterday_start_time))
                else:
                    begintimeArray = time.strptime(arg_dict[key], "%Y-%m-%d %H:%M:%S")
                    # 指定时间格式 "2018-07-20 16:28:54"
                    arg_list.append(key + '=' + str(time.mktime(begintimeArray)))
            elif key.lower() == 'endtime':
                if arg_dict[key] == '':
                    arg_list.append(key + '=' + str(today_start_time))
                else:
                    endtimeArray = time.strptime(arg_dict[key], "%Y-%m-%d %H:%M:%S")
                    # 指定时间格式 "2018-07-20 16:28:54"
                    arg_list.append(key + '=' + str(time.mktime(endtimeArray)))
            else:
                arg_list.append(key + '=' + arg_dict[key])
            self.request_url = url + '&'.join(arg_list)
        return self.request_url

    def request_data(self):
        operation = self.interface_item['operation']
        if operation.lower() == 'get':
            res = requests.get(self.request_url)
            return res.text
        return ''


def test(file_path):
    config = ReadExcel(file_path)
    config.load_config()

    res_list = []

    for i in range(0, len(config.interface_list)):
        data = RequestData(config.interface_list[i])
        data.get_request_url()
        res_list.append(data.request_data())
        print("获取数据中：：：：：：：：："+format((i + 1) / len(config.interface_list), '0.1%'))
        # for i in range(0, len(config.interface_list)):
        #     data = RequestData(config.interface_list[i])
        #     data.get_request_url()
        #     res = data.request_data()
        #     print(res)
    return res_list, config.interface_list


