# 发送邮件
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

'''
    参考链接地址：https://zhuanlan.zhihu.com/p/318387004   优先参考
    
    参考地址：https://zhuanlan.zhihu.com/p/25718394   其次参考 
    
    参考地址：https://blog.csdn.net/zhangphil/article/details/88578676  第三参考
'''


# 设置smtplib所需的参数
# 下面的发件人，收件人是用于邮件传输的。
HOST = "smtp.qq.com"                 # smtp服务器地址
PORT = '465'                         # smtp服务器端口号
from_addr = "2240607006@qq.com"        # 发送邮件的账号
qqCode = "unzyihmbdkvydijb"          # 登陆授权码
to_addr = ["2240607006@qq.com"]          # 接收邮件的账号 这里可以是一个列表，多个收件邮箱


# 构造邮件对象MIMEMultipart对象
# 下面的主题，发件人，收件人，日期是显示在邮件页面上的。
message = MIMEMultipart('mixed')
subject = 'Python SMTP 邮件测试'                         # 邮件主题/标题
message['Subject'] = Header(subject, 'utf-8')           # 通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息
message['From'] = Header(from_addr, 'utf-8')            # 括号里的对应发件人邮箱昵称（随便起）、发件人邮箱账号
message['To'] = Header(';'.join(to_addr), 'utf-8')      # 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
# message['To'] = Header(to_addr, 'utf-8')              # 括号里的对应收件人邮箱昵称、收件人邮箱账号

# 构造文字内容
msg_text = """
Hi!
How are you?
Here is the link you wanted:
https://www.zhihu.com/
"""
text_file_path = "test1.txt"

def msg_text_attach(plain_text):
    """读取文件或者使用变量传递纯文本"""
    if os.path.isfile(plain_text):
        """如果传递的是路径，则读取文本"""
        with open(plain_text, 'rb') as text_file:
            plain_text = text_file.read()
    msg_text_plain = MIMEText(plain_text, 'plain', 'utf8')
    message.attach(msg_text_plain)


msg_text_attach(msg_text)


# 构造HTML内容
html_content = """
    <html>  
      <head></head>  
      <body>  
         <p>Python 邮件发送测试...<br>  
           How are you?<br>  
           Here is the <a href="http://www.zhihu.com/people/4k8k">link</a> you wanted.<br> 
         </p> 
      </body>  
    </html>  
    """


def html_text_attach(html_text):
    """不需要做替换掉 html构造"""
    html_msg = MIMEText(html_text, 'html', 'utf-8')
    message.attach(html_msg)


# html_text_attach(html_content)


def msg_text_html_attach(html_text_file):
    """构造一个需要替换图片的html"""
    msg_alternative = MIMEMultipart('alternative')
    message.attach(msg_alternative)
    try:
        with open(html_text_file, 'r', encoding='utf8') as html_file:
            html_text_content = html_file.read()
    except Exception as eh:
        print('未找到html文件', eh)
    msg_alternative.attach(MIMEText(html_text_content, 'html', 'utf8'))


def add_image(image_path, cid):
    # 指定图片为当前目录
    with open(image_path, 'rb') as image_file:
        msg_image = MIMEImage(image_file.read())

    # 定义图片id，在html文本中引用
    msg_image.add_header('Content-ID', cid)
    message.attach(msg_image)


# 使用字典保存HTML文件路径
html_file_path = {
    "html1": "使用教程.html",
    "html2": "test_send.html"
}

image_paths = {
    "image1": "./image/主图1.jpg",
    "image2": "./image/主图2.jpg",
    "image3": "./image/主图3.jpg",
    "image4": "./image/场景.jpg"
}

image_cids = {
    "image1": "jpg1",
    "image2": "jpg2",
    "image3": "jpg3",
    "image4": "jpg4"

}

msg_text_html_attach(html_file_path.get("html2"))
add_image(image_paths.get('image1'), image_cids.get('image1'))  # 替换cid1
add_image(image_paths.get('image2'), image_cids.get('image2'))  # 替换cid2
add_image(image_paths.get('image3'), image_cids.get('image3'))  # 替换cid3
add_image(image_paths.get('image4'), image_cids.get('image4'))  # 替换cid4


"""
html2即 test_send.html内容如下
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Send mail Tets</title>
</head>
<body>
<img src="cid:jpg1" width="400" height="400" alt="">  <br><br>
<img src="cid:jpg2" width="400" height="400" alt="">  <br><br>
<img src="cid:jpg3" width="400" height="400" alt="">  <br><br>
<img src="cid:jpg4" width="400" height="400" alt="">
</body>
</html>

"""


# 构造图片链接


def image_attach(image_file_path, imgid, filename=None):
    if filename is None:
        """如果不重命名文件，则默认使用源文件名"""
        filename = image_file_path
    try:
        with open(image_file_path, 'rb') as image_file:
            image_content = image_file.read()
    except Exception as ei:
        print('未找到图片文件', ei)
    image = MIMEImage(image_content)
    image.add_header('Content-ID', imgid)   # image1是照片别名，可以在HTML代码中引用
    image['Content-Disposition'] = f'attachment; filename={filename}'
    message.attach(image)


image_attach('test.jpg', 'image1', 'test_image.jpg')

# 构造附件


def send_annex_file(annex_file_path, annex_filename=None):
    """传入附加文件路径和文件名(重命名附件，可以省略，默认为源文件名)"""
    if annex_filename is None:
        annex_filename = annex_file_path
    try:
        with open(annex_file_path, 'rb') as annex_file:
            send_file = annex_file.read()
    except Exception as es:
        print('未找到附件', es)

    text_appendix = MIMEText(send_file, 'base64', 'utf-8')
    text_appendix["Content-Type"] = 'application/octet-stream'
    # 以下附件可以重命名成：核心数据.xlsx
    # text_appendix["Content-Disposition"] = 'attachment; filename="核心数据.xlsx"'
    # 另一种附件重命名实现方式
    text_appendix.add_header('Content-Disposition', 'attachment', filename=annex_filename)
    message.attach(text_appendix)


# 使用字典保存文件路径
annex_path = {
    "file1": "核心数据.xlsx",
    "file2": "test1.txt",
    "file3": "使用教程.html"
}
send_annex_file(annex_path["file1"], '核心数据报表.xlsx')
send_annex_file(annex_path["file2"])
send_annex_file(annex_path.get('file3'))

"""
邮件类型为"multipart/alternative"的邮件包括纯文本正文（text/plain）
和超文本正文（text/html）。
邮件类型为"multipart/related"的邮件正文中包括图片，声音等内嵌资源。
邮件类型为"multipart/mixed"的邮件包含附件。向上兼容，
如果一个邮件有纯文本正文，超文本正文，内嵌资源，附件，则选择mixed类型。
"""

# 配置服务器 发送邮件
try:
    # 配置服务器

    # smtp = smtplib.SMTP()                    # 1 创建SMTP实例
    # smtp.connect('smtp.qq.com', PORT)        # 2 连接SMTP服务器
    server = smtplib.SMTP_SSL(HOST, PORT)     # 本例这里直接一步到位
    # #打印出和SMTP服务器交互的所有信息
    # server.set_debuglevel(1)    # python里打印出来的内容是红色的，有点像报错，这里屏蔽了，可以正常发邮件
    # 登录SMTP服务器
    server.login(from_addr, qqCode)
    # 发送邮件，由于可以一次发给多个人，所以传入一个list,邮件正文是一个str，as_string()把MIMEText对象变成str
    server.sendmail(from_addr, to_addr, message.as_string())
    server.quit()
    print('--邮件发送成功--')
except Exception as e:
    print('--邮件发送失败--' + str(e))