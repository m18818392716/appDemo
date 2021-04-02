import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

'''
    参考链接地址：https://zhuanlan.zhihu.com/p/318387004   优先参考
    
    参考地址：https://zhuanlan.zhihu.com/p/25718394   其次参考 
    
    参考地址：https://blog.csdn.net/zhangphil/article/details/88578676  第三参考
'''


# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "2240607006@qq.com"  # 用户名
mail_pass = "unzyihmbdkvydijb"  # 授权码
sender = '2240607006@qq.com'
receivers = ['2240607006@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("发送者", 'utf-8')
msgRoot['To'] = Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
msgRoot['Subject'] = Header(subject, 'utf-8')
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
mail_msg = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Send mail Tets</title>
</head>
<body>
<img src="cid:jpg1" width="400" height="400" alt="">  <br><br>
</body>
</html>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
# 指定图片为当前目录
with open('12.png', 'rb') as image_file:
    msgImage = MIMEImage(image_file.read())
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', 'jpg1')
msgRoot.attach(msgImage)
try:
    smtpObj = SMTP_SSL('smtp.qq.com', 465)
    # smtpObj.connect(mail_host, 465)  # 发件人邮箱中的SMTP服务器，端口是465
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, msgRoot.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")