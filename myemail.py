# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# sender = 'from@runoob.com'
# receivers = ['@.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# password = ''
#
# try:
#     # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
#     message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
#     message['From'] = Header("菜鸟教程", 'utf-8')
#     message['To'] = Header("测试", 'utf-8')
#
#     subject = 'Python SMTP 邮件测试'
#     message['Subject'] = Header(subject, 'utf-8')
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")
# drzbkulycgbnbefh
# coding:utf-8   #强制使用utf-8编码格式
# import smtplib  # 加载smtplib模块
# from email.mime.text import MIMEText
# from email.utils import formataddr
#
# my_sender = "Felix_Gu@A"  # 发件人邮箱账号，为了后面易于维护，所以写成了变量
# my_user = '@.com'  # 收件人邮箱账号，为了后面易于维护，所以写成了变量
#
# def mail():
#     ret = True
#     try:
#         print(1)
#         msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
#         msg['From'] = formataddr(["发件人邮箱昵称", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
#         msg['To'] = formataddr(["收件人邮箱昵称", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#         msg['Subject'] = "主题"  # 邮件的主题，也可以说是标题
#
#         server = smtplib.SMTP("cn1-..com")  # 发件人邮箱中的SMTP服务器，端口是25
#         server.starttls()
#         server.login(my_sender, "")  # 括号中对应的是发件人邮箱账号、邮箱密码
#         server.sendmail(my_sender, my_user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#         server.quit()
#         print("发送成功")
#     except Exception as e:  # 如果try中的语句没有执行，则会执行下面的ret=False
#         ret = False
#         print(e)
#         print("无法发送")
#     return ret
#
# mail()

#
#
# ret = mail()
# if ret:
#     print("ok")  # 如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
# else:
#     print("filed")  # 如果发送失败则会返回filed



