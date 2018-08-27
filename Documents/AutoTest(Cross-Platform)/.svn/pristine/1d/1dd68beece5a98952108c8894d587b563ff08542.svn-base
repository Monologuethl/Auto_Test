import xlrd


class readExcel:
    excelfile = ''
    sheet = ''

    def __init__(self, file_path):
        self.excelfile = xlrd.open_workbook(file_path)

    def get_sheet(self, sheetname):
        self.sheet = self.excelfile.sheet_by_name(sheetname)
        return self.sheet
