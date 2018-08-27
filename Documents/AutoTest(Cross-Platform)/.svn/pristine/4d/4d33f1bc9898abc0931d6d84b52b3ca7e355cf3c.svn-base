import Codes.Script.autoTest as autoTest


class Main:
    excelconf = ''
    sqlconf = ''

    def __init__(self, excelconf, sqlconf):
        self.excelconf = excelconf
        self.sqlconf = sqlconf

    def main(self):
        m = autoTest.autoTest(self.excelconf)
        r = m.auto_test(self.sqlconf)
        m.clear()
        return r
