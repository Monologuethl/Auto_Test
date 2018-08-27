import json
import time
import Codes.Tools.writeLog as writeLog

# 统计空结果个数
n1 = 0
# 统计参数问题个数
n2 = 0
# 程序内部执行出错个数
n3 = 0
# 接口正常，传参可能有问题个数
n4 = 0
# 数据为空个数
n5 = 0
# 键值为空
n6 = 0
# 不在范围内
n7 = 0

var = []


# 解析类
class analysisData:
    logger = ''
    errorcode = ''

    def __init__(self, request_info):
        self.info = request_info
        self.errormsg = []
        self.right = True
        self.logger = writeLog.writeLogger(loglevel=4, logger="analysisDate")
        self.errorcode = -2

    def analysisresult(self):
        global n1

        begintime = time.clock()
        self.response = self.info.request_data()
        self.info.clear()
        if self.response == '' or self.response is None:
            self.right = False
            self.errormsg.append('接口请求异常')
            n1 += 1
            self.logger.error(self.errormsg)

            self.errorcode = -1
            self.usedtime = -1
            return
        endtime = time.clock()
        self.usedtime = endtime - begintime  # 耗时

        # 将str类型的数据转换成dict
        try:
            data = json.loads(self.response)
            self.right = True
            self.analysiserrorcode(data)
        except Exception as e:
            self.logger.error(e)

    def analysiserrorcode(self, data):
        global n2
        global n3
        global n4
        if 'errorCode' in data:
            self.errorcode = data['errorCode']  # 错误码
            if self.errorcode == 0:
                self.analysiscontent(data)
            elif self.errorcode == 2:
                self.errormsg.append('参数问题')
                n2 += 1
                self.logger.error(self.errormsg)
                self.right = False
            elif self.errorcode == 3:
                self.errormsg.append('程序内部执行出错')
                n3 += 1
                self.logger.error(self.errormsg)
                self.right = False
            else:
                self.errormsg.append('接口正常，传参可能有问题')
                n4 += 1
                self.logger.error(self.errormsg)
                self.right = False

    def analysisresults(self, data):
        global n5
        for key in data['results']:
            if data['results'][key]:
                for i in range(0, len(data['results'][key])):
                    result_dict = data['results'][key][i]
                    if result_dict:
                        if self.info.range_dict:
                            self.checksubject(result_dict)
                    else:
                        self.right = False
                        self.errormsg.append("Data is null")
                        n5 += 1
                        self.logger.error(self.errormsg)
            else:
                self.right = False
                self.errormsg.append("Data is null")
                self.logger.error(self.errormsg)

    def analysisrows(self, data):
        global n5
        if data['rows']:
            for i in range(0, len(data['rows'])):
                if self.info.range_dict:
                    rowsdata = data['rows'][i]
                    if isinstance(rowsdata, dict):
                        self.checksubject(rowsdata)
                    elif isinstance(rowsdata, list):
                        for j in range(0, len(rowsdata)):
                            self.checksubject(rowsdata[j])
        else:
            self.right = False
            self.errormsg.append("Data is null")
            n5 += 1
            self.logger.error(self.errormsg)

    def analysiscontent(self, data):
        if 'rows' in data:
            self.analysisrows(data)
        elif 'results' in data:
            self.analysisresults(data)

    def checksubject(self, data):
        global n6
        global n7
        for key in data:
            if key in self.info.range_dict:
                if data[key] is None:
                    self.right = False
                    n6 += 1
                    self.errormsg.append("{key} is None".format(key=key))

                elif key in self.info.range_dict:
                    interval_value = self.info.range_dict[key]
                    if data[key] and (data[key] not in interval_value):
                        self.right = False
                        n7 += 1
                        self.errormsg.append("{key} = {value} not in range {section}".format(key=key, value=data[key],

                                                                                             section=interval_value))

        self.logger.error(self.errormsg)

    def getVar(self):
        global var
        var.append(n1)
        var.append(n2)
        var.append(n3)
        var.append(n4)
        var.append(n5)
        var.append(n6)
        var.append(n7)
        return var

    def clear(self):
        self.logger.clear()
