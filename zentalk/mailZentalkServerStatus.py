# coding=utf8
import email
import smtplib
from email.mime.text import MIMEText
from zentalk.zenDB import mail_host
from zentalk.zenDB import mail_user
from zentalk.zenDB import mail_pass

#邮件发送


class SendMail(object):
    mailto_list = [
        "Bruce_zhou@asus.com",
        "felix_gu@asus.com",
        "jerry_qiu@asus.com",
    ]
    mail_host = mail_host
    mail_user = mail_user
    mail_pass = mail_pass

    def sendTestMail(self, sub, content):
        me = self.mail_user + "@asus.com"
        msg = MIMEText(content, _subtype='plain', _charset='gb2312')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(self.mailto_list)
        try:
            server = smtplib.SMTP()
            server.connect(self.mail_host)
            server.starttls()
            server.login(self.mail_user, self.mail_pass)
            server.sendmail(me, self.mailto_list, msg.as_string())
            server.close()
            return True
        except Exception as e:
            print(str(e))
            return False


if __name__ == "__main__":
    # pass
    send = SendMail();
    send.sendTestMail("hello", "test");
