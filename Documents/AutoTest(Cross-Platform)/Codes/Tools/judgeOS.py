import platform

class judgeOS:
    type=''
    def __init__(self):
        self.type=platform.system()
    def getType(self):
        return self.type