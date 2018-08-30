import xlrd


class readExcel:
    excelfile = ''
    sheet = ''
    def __init__(self, file_path):
        print("[读取数据中]........................]")
        self.excelfile = xlrd.open_workbook(file_path)
        print("[读取数据完毕]......................]")
    def get_sheet(self, sheetname):
        self.sheet = self.excelfile.sheet_by_name(sheetname)
        return self.sheet
