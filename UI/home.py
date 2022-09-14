import global_variables
from remote_control import *
from PyQt5.QtWidgets import QWidget, QDialog, QSystemTrayIcon, QMenu, QAction
from PyQt5.uic import loadUi
import UI.logo
import sys
from PyQt5 import QtCore, QtGui
from UI.mymessagebox import MyMessageBox
sys.path.append('..')


class Home(QWidget):
    def __init__(self, window):
        super(Home, self).__init__()
        loadUi("UI/ui_Home.ui", self)
        self.window = window
        self.setup()
        self.remote_control_is_running = False
        if global_variables.app_configs['auto_run']:
            RemoteControl(self.window).start()
            self.window.hide()
            self.btnRun.setText('Hide')
            self.remote_control_is_running = True
        if global_variables.app_configs['auto_run'] == False:
            self.btnRun.setText('Run')
        self.btnRun.clicked.connect(self.btnRun_click)
        self.btnExit.clicked.connect(self.btnExit_click)


    def setup(self):
        cfg = load_config('app_configs.yaml')

        global_variables.app_configs['white_list'] = cfg['white_list']
        global_variables.app_configs['auto_run'] = cfg['auto_run']

    def btnRun_click(self):
        if(self.remote_control_is_running == False):
            self.btnRun.setText('Hide')
            self.remote_control_is_running = True
            RemoteControl(self.window).start()
        else:
            self.window.hide()
        

    def btnExit_click(self):
        RemoteControl(self).exit()
