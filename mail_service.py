import imaplib
import email
from helpers import *
import email.message
from smtplib import SMTP_SSL, SMTP_SSL_PORT

from constants import SMTP_HOST, IMAP_HOST, APP_REQ

class MailService:
    def __init__(self):
        self.imap_server = imaplib.IMAP4_SSL(IMAP_HOST)
        self.smtp_server = SMTP_SSL(SMTP_HOST, port = SMTP_SSL_PORT)

    def login(self, username, password):        
        try:
            self.imap_server.login(username, password)
            self.smtp_server.login(username, password)
        except:
            return False
        
        return True

    def logout(self):
        self.imap_server.logout()
        self.smtp_server.quit()

    def read_email (self, category = 'primary', box = 'inbox'):  
        mail_list = []
        
        try:
            self.imap_server.select(box)

            status, mail_ids = self.imap_server.search(None, f'X-GM-RAW "category:{category} in:unread"')
            
            id_list = mail_ids[0].split()
            if len(id_list) == 0:
                print('All mails are read')
                return []
            
            first_email_id = int(id_list[0])
            latest_email_id = int(id_list[-1])

            for i in range(latest_email_id, first_email_id - 1, -1):
                #Đọc những mail có header có chứa lệnh  RFC822
                status, data = self.imap_server.fetch(str(i), '(RFC822)')
                
                mail = email.message_from_bytes(data[0][1])
                date = email.utils.parsedate_to_datetime(mail['date'])
                
                sender = email.utils.parseaddr(mail['from'])[1]
                subject = mail['subject']
                subject, encoding = email.header.decode_header(subject)[0]
                if encoding:
                    subject = str(subject, encoding)

                if not subject.upper().startswith(APP_REQ):
                    continue

                mail_list.append({
                    'sender': sender, 
                    'subject': subject,
                })

        except Exception as e:
            print('Error while reading the mail inbox as below:')
            print(str(e), level = 1)
            
        return mail_list
#Gửi mail trả lời cho người điều khiển
    def send_mail(self, mail):
        try:
            self.smtp_server.sendmail(mail['From'], mail['To'], str(mail).encode())
        except Exception as e:
            print(e)
            return False
        return True
