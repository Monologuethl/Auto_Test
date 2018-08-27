import Codes.Script.getRootPath as getRootPath
import Codes.Script.getRelPath as getRelPath
import Codes.Script.globalTime as globalTime

rootpath = getRootPath.getRootPath().getPath()
relpath = getRelPath.getRelPath('Results').getPath() + getRelPath.getRelPath('Mail').getPath()


class writeTxt:
    time = ''
    pathName = ''
    file = ''
    str = ''

    def __init__(self):
        self.time = globalTime.getGlobalTime()
        self.pathName = rootpath + relpath + self.time + '.txt'
        self.file = open(self.pathName, 'w')

    def writeTxt(self, str):
        self.str = str
        self.file.writelines(self.str+'\n')

    def closeWrite(self):
        self.file.close()
