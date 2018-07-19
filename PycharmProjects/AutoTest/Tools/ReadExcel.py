import xlrd


class ReadeExcel(object):

    @staticmethod
    def read_excel(page_index, file_path):
        print("开始加载文件<<<<<<<<<<<<<<<<")
        book = xlrd.open_workbook(file_path)  # 文件名，把文件与py文件放在同一目录下
        sheet_names = book._sheet_names
        sheet_1_name = sheet_names[page_index]
        sheet = book.sheet_by_name(sheet_1_name)
        print("当前页面为[[" + sheet_1_name + "]]")
        print("文件加载结束>>>>>>>>>>>>>>>>")
        return sheet

        # sheet.cell(i,j).value获得数值
        # sheet.nrows获得行数
