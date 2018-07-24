import xlrd
import time


class ReadExcel:
    interface_list = []

    def __init__(self, filepath):
        self.work_book = xlrd.open_workbook(filepath)

    def load_row(self, ws, row):
        start = time.clock()
        item = {}
        for index_col in range(0, ws.ncols):
            if index_col == 0:      #id
                item['id'] = ws.cell(row, index_col).value
            elif index_col == 1:    #接口名称
                item['name'] = ws.cell(row, index_col).value
            elif index_col == 2:    #调用方法
                item['operation'] = ws.cell(row, index_col).value
            elif index_col == 3:    #接口URL
                item['url'] = ws.cell(row, index_col).value
            elif index_col == 5:    #参数
                arg_dict = {}
                arg_list = ws.cell(row, index_col).value.split(',')
                for i in range(0, len(arg_list)):
                    temp_list = arg_list[i].split('=')
                    if len(temp_list) > 1:
                        arg_dict[temp_list[0]] = temp_list[1]
                    else:
                        arg_dict[temp_list[0]] = ''
                item['arg_dict'] = arg_dict
            elif index_col == 6:
                item['begin_offset'] = ws.cell(row, index_col).value
            elif index_col == 7:
                item['end_offset'] = ws.cell(row, index_col).value
        if item:
            item['module'] = ws.name
        elapsed = (time.clock() - start)
        return item

    def load_config(self):
        for sheetname in self.work_book.sheet_names():
            ws = self.work_book.sheet_by_name(sheetname)
            for index_row in range(1, ws.nrows):
                item = self.load_row(ws, index_row)
                if item:
                    self.interface_list.append(item)


def test(filepath):
    config = ReadExcel(filepath)
    config.load_config()

