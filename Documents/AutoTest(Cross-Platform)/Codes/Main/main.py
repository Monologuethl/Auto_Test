import sys
import os
path1 = os.path.abspath('..')
path2 = os.path.abspath(path1+os.path.sep+'..')
sys.path.append(path2)



import Codes.Tools.writeLog as writeLog
import Codes.Script.singleThread as singleThread
import time
import Codes.Tools.getTime as getTime
import Codes.Script.globalTime as globalTime
log = writeLog.writeLogger(loglevel=4, logger="main")
while 1:
    try:
        thread = singleThread.singleThread(1, 'Main')
        thread.start()
        log.info("main执行成功！")
        thread.join()
        log.info("测试完成，退出主线程")
    except Exception as e:
        log.error(e)
        log.error("main执行失败！")
    time.sleep(86400)
    globalTime.setGlobalTime(getTime.getTime().getToHour())
