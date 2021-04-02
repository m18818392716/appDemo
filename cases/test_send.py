import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from smtplib import SMTP_SSL

'''
    参考链接地址：https://zhuanlan.zhihu.com/p/318387004   优先参考
    
    参考地址：https://zhuanlan.zhihu.com/p/25718394   其次参考 
    
    参考地址：https://blog.csdn.net/zhangphil/article/details/88578676  第三参考
'''

'''
说明：

smtplib.SMTP()：实例化SMTP()

connect(host,port):

host:指定连接的邮箱服务器。常用邮箱的smtp服务器地址如下：

QQ邮箱：smtp.qq.com                 端口号：465
新浪邮箱：smtp.sina.com,
新浪VIP：smtp.vip.sina.com,
搜狐邮箱：http://smtp.sohu.com，
126邮箱：smtp.126.com,
139邮箱：smtp.139.com,
163网易邮箱：http://smtp.163.com    端口号：25

port：指定连接服务器的端口号，默认为25. 默认很可能会失败，端口号具体内容需要查询邮件服务提供商

login(user,password):

user:登录邮箱的用户名。

password：登录邮箱的密码，像笔者用的是QQ邮箱，QQ邮箱一般是网页版，需要用到客户端密码，需要在网页版的QQ邮箱中设置授权码，该授权码即为客户端密码。

sendmail(from_addr,to_addrs,msg,...):

from_addr:邮件发送者地址

to_addrs:邮件接收者地址。字符串列表['接收地址1','接收地址2','接收地址3',...]或'接收地址'

msg：发送消息：邮件内容。一般是msg.as_string():as_string()是将msg(MIMEText对象或者MIMEMultipart对象)变为str。

quit():用于结束SMTP会话。

'''

# # smtp = smtplib.SMTP()
# username = '2240607006@qq.com'
# password = 'unzyihmbdkvydijb'
# smtp = SMTP_SSL('smtp.qq.com',465)
# smtp.set_debuglevel(1)
# smtp.login(username, password)
# send_add = '2240607006@qq.com'
# to_add = ['2240607006@qq.com']
# msg = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# subject = 'Python SMTP 邮件测试'
# msg['Subject'] = Header(subject, 'utf-8')
# smtp.sendmail(send_add, to_add, msg.as_string())
# smtp.quit()


# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "2240607006@qq.com"  # 用户名
mail_pass = "unzyihmbdkvydijb"  # 授权码
sender = '2240607006@qq.com'
receivers = ['2240607006@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#使用Python发送HTML格式的邮件
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.zhihu.com">这是一个链接</a></p>
"""

message = MIMEText(mail_msg, 'plain', 'utf-8')
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')

message['From'] = Header("Python SMTP教程", 'utf-8') #括号里的对应发件人邮箱昵称（随便起）、发件人邮箱账号
message['To'] = Header("测试", 'utf-8') #括号里的对应收件人邮箱昵称、收件人邮箱账号
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
try:
    smtpObj = SMTP_SSL('smtp.qq.com',465)
    # smtpObj.connect(mail_host, 465)  # 发件人邮箱中的SMTP服务器，端口是465
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")

