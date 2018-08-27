import Codes.Tools.getTime as getTime

globaltime = ''


def setGlobalTime(value):
    global globaltime
    globaltime = value


def getGlobalTime(defaultvalue=getTime.getTime().getToHour()):
    if globaltime == '':
        return defaultvalue
    else:
        return globaltime
