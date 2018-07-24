import xlrd
from xlutils.copy import copy


class WriteExcel(object):

    @staticmethod
    def write(path, page_index):
        rb = xlrd.open_workbook(path)
        r_sheet = rb.sheet_by_index(page_index)
        r = r_sheet.nrows
        wb = copy(rb)
        sheet = wb.get_sheet(page_index)
        return sheet, r, wb

        # r表格的行数
        # sheet.write(i, j, values)设置数值
        # wb.save(path)追加写入
