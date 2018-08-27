import xlwt
import Codes.Tools.writeLog as writeLog
import Codes.Script.getRootPath as getRootPath
import Codes.Script.getRelPath as getRelPath
import Codes.Script.globalTime as globalTime

rootpath = getRootPath.getRootPath().getPath()
relpath = getRelPath.getRelPath('Results').getPath() + getRelPath.getRelPath('Result').getPath()


class writeExcel:
    reportname = ''
    workbook = ''
    logger = ''
    time = ''

    def __init__(self):
        self.workbook = xlwt.Workbook()
        self.time = globalTime.getGlobalTime()
        self.reportname = rootpath + relpath + self.time + '.xls'
        self.logger = writeLog.writeLogger(loglevel=4, logger="writeExcel")

    def initsheet(self, sheetname, rowhead):
        self.worksheet = self.workbook.add_sheet(sheetname)
        for i in range(0, len(rowhead)):
            self.worksheet.write(0, i, rowhead[i])

    @staticmethod
    def set_font_style(name='Arial', color=0, height=200):
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = name
        font.colour_index = color
        font.height = height
        style.font = font
        return style

    def write_row(self, row_index, rowdata, color_index=0):
        style = self.set_font_style(color=color_index)
        col_index = 0
        for key in rowdata:
            try:
                self.worksheet.write(row_index, col_index, rowdata[key], style)
                col_index += 1
            except Exception as e:
                self.logger.error(e)

    def save(self):
        try:
            self.workbook.save(self.reportname)
        except Exception as e:
            self.logger.error(e)

    def clear(self):
        self.logger.clear()
