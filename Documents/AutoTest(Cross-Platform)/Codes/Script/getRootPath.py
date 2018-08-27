import os


class getRootPath:
    path1 = ''
    path2=''

    def __init__(self):
        self.path1 = os.path.abspath('..')
        self.path2 = os.path.abspath(self.path1+os.path.sep+'..')

    def getPath(self):
        return self.path2


