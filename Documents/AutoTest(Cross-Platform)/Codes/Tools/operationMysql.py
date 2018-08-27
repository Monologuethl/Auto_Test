import pymysql
import configparser
import Codes.Tools.writeLog as writeLog



class operationMysql:
    config = ''
    ip = ''
    user = ''
    pwd = ''
    dbname = ''
    db = ''
    logger=''

    def __init__(self, configfile):
        self.config = configparser.ConfigParser()
        self.config.read(configfile)
        self.ip = self.config.get('MYSQL', 'IP')
        self.user = self.config.get("MYSQL", "UserName")
        self.pwd = self.config.get("MYSQL", "PassWord")
        self.dbname = self.config.get("MYSQL", "DBName")
        self.logger = writeLog.writeLogger(loglevel=4, logger="operationMysql")
        try:
            self.db = pymysql.connect(self.ip, self.user, self.pwd, self.dbname)
            self.logger.info("Mysql connect success!")
        except:
            self.logger.info("Mysql connect failure!")

    def operation(self, sql):
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            self.db.commit()
            self.logger.info("Sql operation success!")
        except:
            self.logger.info("Sql operation failure!")
            self.db.rollback()
        finally:
            if cursor:
                cursor.close()
                self.logger.info("Mysql connect close!")

    def clear(self):
        self.logger.clear()
