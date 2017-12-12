#coding:utf-8
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#----------1.跟发件相关的参数-------
smtpserver = "smtp.163.com"    #发件服务器
port = 0
sender = "sara@163.com"
pwd = ""
receiver = "2089910273@qq.com"

#----------2.编辑邮件的内容-------
#读文件
file_path = "result.html"
with open(file_path,"rb") as fp:
    mail_body = fp.read()
msg = MIMEMultipart()

msg['from'] = sender
msg['to'] = "2089910273@qq.com"
msg['subject'] = "这是我的主题"

#正文
body = MIMEText(mail_body,"html","utf-8")
msg.attach(body)

#附件
att = MIMEText(mail_body,"base64","utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Dispositon"] = "attachment;filename=test_report.html"
msg.attach(att)

#----------3.发送邮件-------
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)    #链接服务器
    smtp.login(sender,pwd)      #登录
except:
    smtp = smtplib.SMTP_SSL(smtpserver,port)
    smtp.login(sender,pwd)
smtp.sendmail(sender,receiver,msg.as_string()) #发送
smtp.quit()                 #关闭