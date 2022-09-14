import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from UI.mymessagebox import MyMessageBox
from mail_service import MailService
from PyQt5.QtWidgets import QWidget, QDialog
from UI.tray_icon import TrayIcon
import global_variables
import time
from helpers import *
from thread_targets import *
import app_logging as logging


class LoginThread(QObject):
    ok = pyqtSignal(MailService)
    fail = pyqtSignal()
    finished = pyqtSignal()

    def __init__(self, host_mail: MailService):
        super(LoginThread, self).__init__()
        self.host_mail = host_mail

    def start(self):
        print('Login to mail server...')
        logging.log('Login to mail server...')
        status = self.host_mail.login(REMOTE_MAIL, REMOTE_PWD)

        if status:
            print('Login successfully')
            logging.log('Login successfully')
            self.ok.emit(self.host_mail)
        else:
            print('Failed to login with login with name: ' + REMOTE_MAIL)
            logging.log(f'Failed to login with login with name: {REMOTE_MAIL}')
            self.fail.emit()
        logging.save()
        self.finished.emit()


class RemoteControl():
    def __init__(self, window):
        self.host_mail = MailService()
        self.window = window
        
    def auto_run_check(self):
        #if global_variables.app_configs['auto_run']:
        self.__run(close_window=False)

    def start(self):
        tray_icon = TrayIcon(QtGui.QIcon('UI/Assets/Images/logo.png'),parent=self.window)
        tray_icon.show()
        self.auto_run_check()
        

    def __run_thread(self, status, close_window):
        '''
            Run threads for app if status is True
            After that, the Run button will become Hide button, the config window will closed or not based on close_window
        '''
        # self.__dialog.close()
        if status == True:
            # Start checking mail box and show notifications
            self.checking_thread = threading.Thread(
                target=check_email_thread, args=(self.host_mail, ))
            self.checking_thread.daemon = True
            self.checking_thread.start()
            self.noti_thread = threading.Thread(
                target=show_notification_thread, args=())
            self.noti_thread.daemon = True
            self.noti_thread.start()
            # self.config_window.background_setup(close_window)
        else:
            dialog = QDialog()
            dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
            dialog.setWindowIcon(QtGui.QIcon('UI/Assets/Images/logo.png'))
            msg = MyMessageBox(
                title='Error', message='Cannot login to mail server. Please try again later.', dialog=dialog)

    def __run(self, close_window):
        '''
            Run the app (first run button click or auto-run)
        '''
        # dialog = QDialog()
        # dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        # dialog.setWindowIcon(QtGui.QIcon('UI/Assets/Images/logo.png'))
        # msg = MyMessageBox(
        #    title='Message', message='Remote control is running', dialog=dialog)

        # create thread and start
        self.__thread = QThread()
        self.__target = LoginThread(self.host_mail)
        self.__target.moveToThread(self.__thread)

        self.__thread.started.connect(self.__target.start)

        self.__target.finished.connect(self.__thread.quit)
        self.__target.ok.connect(lambda: self.__run_thread(True, close_window))
        self.__target.fail.connect(
            lambda: self.__run_thread(False, close_window))

        self.__thread.start()

    def __show_msg(self, msg):
        msg.exec_()

    def exit(self):
        if self.host_mail:
            try:
                print('Logout successfully')
                logging.log('Logout mail server...')
                self.host_mail.logout()
            except:
                print('Exception raised while loging out')
                logging.log('Exception raised while loging out')
                pass

        logging.log('App closed')
        logging.save()
        sys.exit()
