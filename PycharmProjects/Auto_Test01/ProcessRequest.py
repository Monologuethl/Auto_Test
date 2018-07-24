import datetime
import json
from Request_Data import test
from Tools.WriteExcel import WriteExcel
from JsonProcess import json_process


class OutPutExcel(object):

    @staticmethod
    def output_excel(file_path):
        result_list, interface_list, range_list = test(file_path)
        print(range_list)
        check = []
        for ran in range_list:
            if ran:
                check.append(range_list.index(ran))
        now_time = datetime.datetime.now()
        yes_time = now_time + datetime.timedelta(days=-1)
        yes_time_nyr = yes_time.strftime('%Y%m%d')
        output_list = []
        for i in range(0, len(result_list)):
            output_list.append(json.loads(result_list[i]))
        # 用dict代替switch
        code = {0: '接口连接正常', 2: '参数问题', 3: '程序内部执行出错'}
        InterFaceCode = []
        InterFaceName = []
        ErrorDatetime = []
        Module = []
        Content = []
        ErrorContent = []

        for i in range(0, len(output_list)):
            if 'errorCode' in output_list[i]:
                InterFaceCode.append(code.get(output_list[i].get('errorCode'), "接口正常,传参问题"))
            else:
                InterFaceCode.append("无errorCode字段")
            if output_list[i].__contains__('rows'):
                List = output_list[i].get('rows')
                print(List)
                if List[0]:
                    Content.append("有返回值")
                    flag, Error = json_process(List, range_list, i, check)
                    if flag == 1:
                        ErrorContent.append("接口工作正常")
                    else:
                        ErrorContent.append(Error)
                else:
                    Content.append("无返回值")
                    ErrorContent.append("接口工作异常")

            InterFaceName.append(interface_list[i]['name'])
            Module.append(interface_list[i]['module'])
            ErrorDatetime.append(yes_time_nyr)
            print('解析数据中，请稍等：：：：：：：：：' + format((i + 1) / len(result_list), '0.1%'))

        output_list = [ErrorDatetime, InterFaceCode, InterFaceName, Module, Content, ErrorContent]
        return output_list

    @staticmethod
    def save_result(files, path, page_index):
        print(len(files[0]), len(files[1]), len(files[2]), len(files[3]), len(files[4]), len(files[5]))
        column = ['Date', 'Status', 'Interface', 'Module', 'Content', 'ErrorContent']
        sheet, r, wb = WriteExcel().write(path, page_index)
        if r == 0:
            for i in range(0, len(column)):
                sheet.write(0, i, column[i])
            for i in range(0, len(files[0])):
                for j in range(0, len(files)):
                    sheet.write(r + i + 1, j, files[j][i])
        else:
            for i in range(0, len(files[0])):
                for j in range(0, len(files)):
                    sheet.write(r + i, j, files[j][i])
        wb.save(path)
