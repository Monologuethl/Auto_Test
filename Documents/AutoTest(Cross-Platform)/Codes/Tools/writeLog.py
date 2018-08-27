import logging
import Codes.Script.getRootPath as getRootPath
import Codes.Script.getRelPath as getRelPath
import Codes.Script.globalTime as globalTime

rootpath = getRootPath.getRootPath().getPath()
relpath = getRelPath.getRelPath('Results').getPath() + getRelPath.getRelPath('Log').getPath()


class writeLogger():
    logger = ''
    ch = ''
    fh = ''
    time = ''
    logname = ''

    def __init__(self, loglevel, logger):
        self.logger = logger
        self.time = globalTime.getGlobalTime()
        self.logname = rootpath + relpath + self.time + '.log'
        # logger 输出格式
        format_dict = \
            {
                1: logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s'),
                2: logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(message)s'),
                3: logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s'),
                4: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            }
        # 这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志

        # 创建一个logger,默认级别是DEBUG
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        self.fh = logging.FileHandler(self.logname)
        self.fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = format_dict[int(loglevel)]
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    # 以下皆为重写方法 并且每次记录后清除logger
    def info(self, message=None):
        self.logger.info(message)

    def debug(self, message=None):
        self.logger.debug(message)

    def warning(self, message=None):
        self.logger.warning(message)

    def error(self, message=None):
        self.logger.error(message)

    def critical(self, message=None):
        self.logger.critical(message)

    def clear(self):
        self.logger.removeHandler(self.fh)
        self.logger.removeHandler(self.ch)
