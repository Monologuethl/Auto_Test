import xlrd

class ReadExcel:
    interface_list = []

    def __init__(self, filepath):
        self.work_book = xlrd.open_workbook(filepath)

    def load_row(self, ws, row):
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
            elif index_col == 6:    #开始时间偏移量
                item['begin_offset'] = ws.cell(row, index_col).value
            elif index_col == 7:    #结束时间偏移量
                item['end_offset'] = ws.cell(row, index_col).value
            elif index_col == 8:
                range_item = ws.cell(row, index_col).value
                range_dict = {}
                if range_item:
                    range_list = range_item.split(';')
                    for i in range(0, len(range_list)):
                        range_temp = range_list[i].split(':')
                        range_value = range_temp[1].split(',')
                        range_dict[range_temp[0]] = range_value
                item['range_dict'] = range_dict
        if item:
            item['module'] = ws.name
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


if __name__ == '__main__':
    test('InterfaceCase.xls')
