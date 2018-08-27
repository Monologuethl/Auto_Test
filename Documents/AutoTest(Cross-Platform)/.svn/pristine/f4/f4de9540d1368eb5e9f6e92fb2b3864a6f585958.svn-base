import requests
import time
import datetime
import Codes.Tools.writeLog as writeLog


class requestData:
    logger = ''

    def __init__(self, request_info):
        self.logger = writeLog.writeLogger(loglevel=4, logger="requestData")
        # 模块名称
        self.module = request_info['module']
        # 接口名称
        self.name = request_info['name']
        # 接口英文名称
        self.name_en = request_info['name_en']
        # 超时
        if request_info['overtime'] and request_info['overtime'] != 0:
            self.overtime = int(request_info['overtime'])
        else:
            self.overtime = 30
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
            if key.lower() == 'begintime' or key.lower() == 'starttime':
                if arg_dict[key] == '':
                    if 'begin_offset' in request_info:
                        if request_info['begin_offset'] == '':
                            beginoffset = 0
                        else:
                            beginoffset = request_info['begin_offset']
                        yesterday_start_time = int(yesterday_start_time + beginoffset * 3600)

                    self.arg_list.append(key + '=' + str(yesterday_start_time))
                else:
                    if arg_dict[key].isdigit():
                        self.arg_list.append(key + '=' + arg_dict[key])
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
                        today_start_time = int(today_start_time + endoffset * 3600)

                    self.arg_list.append(key + '=' + str(today_start_time))
                else:
                    if arg_dict[key].isdigit():
                        self.arg_list.append(key + '=' + arg_dict[key])
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
            try:
                # request url(timeout=30): http://www.baidu.com
                self.logger.info("request url(timeout = {:.0f}): {}".format(self.overtime, self.get_request_url()))
                res = requests.get(self.get_request_url(), timeout=self.overtime)
                res.close()
                return res.text
            except Exception as e:
                self.logger.error("Interface Connect Error - %s" % e)
        return ''

    def clear(self):
        self.logger.clear()
