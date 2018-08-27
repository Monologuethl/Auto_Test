import threading
import Codes.Tools.writeLog as writeLog
import Codes.Script.getRootPath as getRootPath
import Codes.Script.getRelPath as getRelPath
import Codes.Tools.mainClass as mainClass
import Codes.Tools.writeTxt as writeTxt
import Codes.Script.sendMail as sendMail
import Codes.Script.globalTime as globalTime
import Codes.Tools.getTime as getTime

globalTime.setGlobalTime(getTime.getTime().getToHour())
rootpath = getRootPath.getRootPath().getPath()
logger = writeLog.writeLogger(loglevel=4, logger="singleThread")
relpath = getRelPath.getRelPath('Codes').getPath() + getRelPath.getRelPath('Config').getPath()
mailconf = rootpath + relpath + 'mailInfo.conf'
threadLock = threading.Lock()


class singleThread(threading.Thread):
    threadID = ''
    name = ''
    logger = ''

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        logger.info("开启线程： " + self.name)
        timing_query()


def timing_query():
    writeMail = writeTxt.writeTxt()
    Main = mainClass.Main(rootpath + relpath + 'InterfaceCase.xls',
                          rootpath + relpath + 'mysqlInfo.conf')
    dic = Main.main()
    writeMail.writeTxt('空结果' + ':' + str(dic[0]))
    writeMail.writeTxt('参数问题' + ':' + str(dic[1]))
    writeMail.writeTxt('内部执行出错' + ':' + str(dic[2]))
    writeMail.writeTxt('传参可能有问题' + ':' + str(dic[3]))
    writeMail.writeTxt('数据为空' + ':' + str(dic[4]))
    writeMail.writeTxt('键值为空' + ':' + str(dic[5]))
    writeMail.writeTxt('不在范围内' + ':' + str(dic[6]))
    writeMail.writeTxt('测试接口数' + ':' + str(dic[7]))
    writeMail.closeWrite()
    try:
        sendMail.sendMail(mailconf).clear()
    except Exception as e:
        logger.error(e)
