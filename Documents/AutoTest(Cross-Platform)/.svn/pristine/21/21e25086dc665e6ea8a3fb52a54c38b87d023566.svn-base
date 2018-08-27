import Codes.Tools.judgeOS as judgeOS


class getRelPath:
    ostype = judgeOS.judgeOS().getType()
    L = ''
    W = ''
    path = ''
    relpath = ''

    def __init__(self,filename):
        self.relpath = filename
        self.L='Linux'
        self.W='Windows'

    def getPath(self):
        if (self.ostype==self.L):
            self.path = '/' + self.relpath + '/'
        elif (self.ostype==self.W):
            self.path = '\\' + self.relpath + '\\'
        return self.path

