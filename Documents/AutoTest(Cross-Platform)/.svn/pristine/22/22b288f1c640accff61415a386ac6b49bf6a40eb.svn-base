import Codes.Script.getValues as getValues
import Codes.Script.requestData as requestData
import Codes.Script.analysisData as analysisData
import Codes.Tools.writeExcel as writeExcel
import Codes.Tools.operationMysql as operationMysql
import Codes.Tools.writeLog as writeLog
import Codes.Tools.getTime as getTime


class autoTest:
    config = ''
    conn = ''
    logger = ''
    t = ''
    resl = ''

    def __init__(self, excelconf):
        self.config = getValues.getValues(excelconf)
        self.logger = writeLog.writeLogger(loglevel=4, logger="autoTest")
        self.resl = ''

    def auto_test(self, mysqlconf):
        self.config.load_config()
        report = writeExcel.writeExcel()

        report_head = ['模块名称', '接口名称', '日期', 'URL', '耗时', 'ErrorCode', '错误简介']
        report.initsheet('test report', report_head)

        for i in range(0, len(self.config.interface_list)):
            self.t = getTime.getTime().getToSecond()
            self.logger.info("正在测试接口数据... 已完成：" + format(i / len(self.config.interface_list), '0.1%'))
            data = requestData.requestData(self.config.interface_list[i])
            analysisres = analysisData.analysisData(data)
            analysisres.analysisresult()

            # 清除日志流，避免重复打印日志
            analysisres.clear()

            resultdata = {}
            resultdata['module'] = data.module
            resultdata['name'] = data.name
            resultdata['date'] = self.t
            resultdata['url'] = data.get_request_url()
            resultdata['response'] = analysisres.response

            self.conn = operationMysql.operationMysql(mysqlconf)
            sql = "insert into result(moudle,name,date,url,response) values('%s','%s','%s','%s','%s')" % (
                resultdata['module'], resultdata['name'], resultdata['date'], resultdata['url'], resultdata['response'])
            self.conn.operation(sql)
            self.conn.clear()

            report_row = {}
            report_row['module'] = data.module
            report_row['name'] = data.name
            report_row['date'] = self.t
            report_row['url'] = data.get_request_url()
            report_row['usedtime'] = ("%.3f" % analysisres.usedtime)
            report_row['errorcode'] = analysisres.errorcode
            report_row['errormsg'] = ";".join(analysisres.errormsg)

            if analysisres.right:
                report.write_row(1 + i, report_row)
            else:
                report.write_row(1 + i, report_row, 2)
            if i == len(self.config.interface_list) - 1:
                self.resl = analysisres.getVar()
        self.logger.info("接口测试完成！")
        report.save()
        self.logger.info("保存测试结果报表：%s" % report.reportname)
        self.resl.append(i + 1)
        self.config.clear()
        return self.resl

    def clear(self):
        self.logger.clear()
