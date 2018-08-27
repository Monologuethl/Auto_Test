import Codes.Script.getRootPath as getRootPath
import Codes.Script.getRelPath as getRelPath
import Codes.Script.globalTime as globalTime

rootpath = getRootPath.getRootPath().getPath()
relpath = getRelPath.getRelPath('Results').getPath() + getRelPath.getRelPath('Mail').getPath()
flag = True


class getMailContent:
    time = ''
    pathName = ''
    file = ''
    str = ''
    line = ''
    var = []

    def __init__(self):
        self.time = globalTime.getGlobalTime()
        self.pathName = rootpath + relpath + self.time + '.txt'
        self.file = open(self.pathName, 'r')
        self.line = self.file.readline()

    def readAndJudge(self):
        global flag
        while self.line:
            value = self.line.split(':')
            if value[1] != '0\n':
                self.var.append(self.line)
                if value[0] != '测试接口数':
                    flag = False
            self.line = self.file.readline()
        if flag:
            self.var.append("Request Success, No Error!")
        return self.var

    def getFlag(self):
        return flag

    def closeRead(self):
        self.file.close()

    def clearVar(self):
        self.var.clear()
