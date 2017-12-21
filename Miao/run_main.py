#coding=utf-8
import os
import unittest
import time
import HTMLTestRunner
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#当前脚本所在的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))

def add_case(caseName="case", rule="test*.py"):
    '''加载所有的用例'''
    case_path = os.path.join(cur_path,caseName)
    #如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    print ("test case path:%s"%case_path)

    #定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)

    print (discover)
    return discover

def run_case(all_case,reportName="report"):
    '''执行所有的用例，并把结果写入HTML测试报告'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path,reportName)
    if not os.path.exists(report_path):os.mkdir(report_path)
    # report_abspath = os.path.join(report_path,now+"result.html")
    report_abspath = os.path.join(report_path,"result.html")
    print ("report path:%s"%report_abspath)
    fp = open(report_abspath,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u"自动化测试报告",
                                           description=u"用例执行情况")
    runner.run(all_case)
    fp.close()
def get_report_file(report_path):
    '''获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda  fn:os.path.getctime(os.path.join(report_path,fn)))
    print (u"最新测试生成的报告："+lists[-1])
    #找到最新生成的报告文件
    report_file = os.path.join(report_path,lists[-1])
    return report_file

def send_mail(sender,pwd,receiver,smtpserver,report_file,port):
    '''发送最新的测试报告'''
    with open(report_file,"rb") as f:
        mail_body = f.read()
    #定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText( mail_body,_subtype="html",_charset="utf-8")
    msg['subject'] = u"自动化测试报告"
    msg['from'] = sender
    msg['to'] = "2089910273@qq.com"

    #添加附件
    # att = MIMEText(mail_body,"base64","utf-8")
    # att["Content-Type"] = "application/octet-stream"
    # att["Content-Dispositon"] = 'attachment;filename="test_report.html"'
    # msg.attach(att)
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)

    #----------3.发送邮件-------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)    #链接服务器
    except:
        smtp = smtplib.SMTP_SSL(smtpserver,port)

    smtp.login(sender,pwd)      #登录
    smtp.sendmail(sender,receiver,msg.as_string()) #发送
    smtp.quit()
    print ("test report email has send out!")

if __name__ == "__main__":
    all_case = add_case()
    run_case(all_case)
    #获取最新测试报告
    report_path = os.path.join(cur_path,"report")
    report_file = get_report_file(report_path)
    #邮箱配置
    from config import readConfig
    sender = readConfig.sender
    pwd = readConfig.pwd
    smtp_server = readConfig.smtp_server
    port  =readConfig.port
    receiver = readConfig.receiver
    send_mail(sender,pwd,receiver,smtp_server,report_file,port)

