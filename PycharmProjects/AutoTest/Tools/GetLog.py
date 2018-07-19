import logging


class Log(object):
    def __init__(self, path):
        logging.basicConfig(filename=path,
                            format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S %p',
                            level=10)
        # path存放日志的路径
