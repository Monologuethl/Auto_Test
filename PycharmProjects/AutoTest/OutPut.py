import datetime
import json
from Tools.WriteExcel import WriteExcel
from GetContent import GetContent


class OutPutExcel(object):

    @staticmethod
    def output_excel(i, file_path):
        result_list = GetContent().content(i, file_path)
        now_time = datetime.datetime.now()
        yes_time = now_time + datetime.timedelta(days=-1)
        yes_time_nyr = yes_time.strftime('%Y%m%d')

        output_list = []
        for i in range(0, len(result_list)):
            output_dict = (json.loads(result_list[i][2]))
            output_list.append(output_dict)
        # 用dict代替switch
        code = {0: '接口连接正常', 2: '参数问题', 3: '程序内部执行出错'}
        content = {"null": "内容为空"}
        # 接口出问题的日期，所属模块，接口名称,具体的接口打印出来
        InterFaceCode = []
        InterFaceName = []
        ErrorDatetime = []
        Module = []
        Content = []
        ErrorContent = []
        for i in range(0, len(result_list)):
            InterFaceCode.append(code.get((output_list[i])['errorCode'], "接口正常,传参问题"))
            InterFaceName.append(result_list[i][0])
            Module.append(result_list[i][1])
            ErrorDatetime.append(yes_time_nyr)
            if output_list[i].__contains__('rows'):
                Content.append(content.get(str((output_list[i])['rows']), "有值"))
                for d in output_list[i]['rows']:
                    for j in range(0, len(output_list[i]['rows'])):
                        if output_list[i]['rows'][j] == "":
                            ErrorContent.append(d + 'NO Values')
                        else:
                            ErrorContent.append("接口工作正常")
            if output_list[i].__contains__('results'):  # 进入第二层dict0
                Content.append(content.get((output_list[i])['results'], "有值"))  # results:"xxx"
                for d in output_list[i]['results']:  # results下的次级dict1
                    if (output_list[i]['results'])[d] == "":
                        ErrorContent.append(d + 'NO Values')
                        for j in ((output_list[i]['results'])[d])[0]:  # dict1下的dict2
                            if ((((output_list[i])['results'])[d])[0])[j] == "":
                                ErrorContent.append(j + 'NO Values')
                            else:
                                ErrorContent.append("接口工作正常")
            print('解析数据中，请稍等：：：：：：：：：' + format((i + 1) / len(result_list), '0.1%'))
        output_list = [ErrorDatetime, InterFaceCode, InterFaceName, Module, Content, ErrorContent]
        return output_list

    @staticmethod
    def save_result(files, path, page_index):
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
        print()
