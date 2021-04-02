import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from smtplib import SMTP_SSL

'''
    参考链接地址：https://zhuanlan.zhihu.com/p/318387004   优先参考
    
    参考地址：https://zhuanlan.zhihu.com/p/25718394   其次参考 
    
    参考地址：https://blog.csdn.net/zhangphil/article/details/88578676  第三参考
'''

mail_user = "2240607006@qq.com"  # 用户名
mail_pass = "unzyihmbdkvydijb"  # 授权码
sender = '2240607006@qq.com'
receivers = ['2240607006@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("Python SMTP教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
#邮件正文内容
message.attach(MIMEText('这是Python 邮件发送测试……', 'plain', 'utf-8'))
# 构造附件1，传送当前目录下的 test.txt 文件
att_annex1 = MIMEText(open('a.txt', 'rb').read(), 'base64', 'utf-8')
att_annex1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att_annex1["Content-Disposition"] = 'attachment; filename="aaa.txt"'
message.attach(att_annex1)
# 构造附件2，传送当前目录下的 test2.txt 文件
att_annex2 = MIMEText(open('b.txt', 'rb').read(), 'base64', 'utf-8')
att_annex2["Content-Type"] = 'application/octet-stream'
att_annex2["Content-Disposition"] = 'attachment; filename="bbb.txt"'
message.attach(att_annex2)
try:
    smtpObj = SMTP_SSL('smtp.qq.com', 465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")