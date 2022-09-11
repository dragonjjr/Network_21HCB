import time
from helpers import *
from constants import *

from plyer import notification

from responder import respond
import threading

def show_notification_thread(timeout = 300):
    while True:
        notification.notify (
            title = "Remote Control with Email Service",
            message = "Remote Control is running",
            app_name = 'Remote Control with Email Service',
            app_icon = 'UI/Assets/Images/logo.ico',
            timeout = 5
        )

        time.sleep(timeout)
        
def check_email_thread(host_mail, timeout = 8):
    try:
        while True:
            print('Reading unread mails in primary mail box...')

            mail_list = host_mail.read_email()

            for mail in mail_list:
                mail['subject'] = mail['subject'].replace('\n', '')
                mail['subject'] = mail['subject'].replace('\r', '')
                print('Send from: ' + mail['sender'])
                print('Subject: ' + mail['subject'])
                print('-' * 40)
                process_thread = threading.Thread(target = respond, args = (host_mail, mail, ))
                process_thread.daemon = True
                process_thread.start()
            
            time.sleep(timeout)
    except:
        print('Stop checking mail box')