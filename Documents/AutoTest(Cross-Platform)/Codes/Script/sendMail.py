import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
import configparser
import Codes.Tools.writeLog as writeLog
import Codes.Script.getMailContent as getMailContent
import Codes.Script.getRootPath as getRootPath
import Codes.Script.getRelPath as getRelPath
import Codes.Script.globalTime as globalTime

rootpath = getRootPath.getRootPath().getPath()
relpath = getRelPath.getRelPath('Results').getPath() + getRelPath.getRelPath('Result').getPath()


class sendMail:
    config = ''
    receivers1 = ''
    receivers2 = ''
    host = ''
    user = ''
    pwd = ''
    logger = ''
    content = ''
    mailContent = []
    getClass = ''
    t = ''
    filename = ''
    msg = ''
    flag = ''
    list = []

    def __init__(self, configfile):
        self.time = globalTime.getGlobalTime()
        self.filename = rootpath + relpath + self.time + '.xls'

        self.config = configparser.ConfigParser()
        self.config.read(configfile)
        self.host = self.config.get('MAIL', 'HOST')
        self.user = self.config.get('MAIL', 'USER')
        self.pwd = self.config.get('MAIL', 'PWD')
        self.receivers = self.config.get('MAIL', 'RECEIVERS')
        self.list = self.receivers.split(';')

        self.getClass = getMailContent.getMailContent()
        self.content = self.getClass.readAndJudge()
        self.getClass.closeRead()

        self.logger = writeLog.writeLogger(loglevel=4, logger="sendMail")
        if not self.getClass.getFlag():
            self.mailContent.append("                        测试情况说明如下（具体情况请查看分析文件）\n")
        else:
            self.mailContent.append("                            测试情况说明如下 \n")

        for i in range(0, len(self.content)):
            self.mailContent.append(self.content[i])
        self.msg = '\n'.join(self.mailContent)

        self.mailContent.clear()
        self.getClass.clearVar()

        message = MIMEMultipart('related')
        message['From'] = formataddr(["Search Result", self.user])  # 发送者
        for i in range(0, len(self.list)):
            message['To'] = formataddr(["{receiver}".format(receiver=self.list[i]), self.list[i]])  # 接收者
        if not self.getClass.getFlag():
            self.flag = "Warning"
        else:
            self.flag = "Success"
        message['Subject'] = '{Date}自动测试报告-{state}'.format(Date=self.time, state=self.flag)
        message.attach(MIMEText(self.msg, 'plain', 'utf-8'))
        if not self.getClass.getFlag():
            att = MIMEText(open(self.filename, 'rb').read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att.add_header('Content-Disposition', 'attachment', filename='分析文件.xls')
            message.attach(att)

        try:
            server = smtplib.SMTP_SSL(self.host, 465)
            server.login(self.user, self.pwd)
            server.sendmail(self.user, self.list, message.as_string())
            server.quit()
            self.logger.info("邮件发送成功")
        except Exception as e:
            self.logger.error("{Error}: 无法发送邮件".format(Error=e))

    def clear(self):
        self.logger.clear()
