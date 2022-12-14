import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow,  QSystemTrayIcon, QMenu, QAction
from PyQt5.uic import loadUi
from UI.configuration import Configuration
from UI.home import Home
from PyQt5.QtCore import QSize
from UI.tray_icon import TrayIcon
import global_variables
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UI/ui_Main.ui', self)
        self.home = Home(self)
        self.stackedWidget.addWidget(self.home)
        self.home.btnConfiguration.clicked.connect(self.go_to_second)
        self.configuration = Configuration(self)
        self.stackedWidget.addWidget(self.configuration)
        self.configuration.btnBack.clicked.connect(self.go_to_first)
        
        

    def go_to_first(self):
        self.stackedWidget.setCurrentIndex(0)

    def go_to_second(self):
        self.stackedWidget.setCurrentIndex(1)
        self.configuration.render_config()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.setFixedSize(window.size())
    window.setWindowIcon(QtGui.QIcon('UI/Assets/Images/logo.png'))
    window.setWindowFlags(QtCore.Qt.WindowCloseButtonHint |
                          QtCore.Qt.WindowMinimizeButtonHint)
    window.setWindowTitle("Remote Control with Email Service")
    if global_variables.app_configs['auto_run'] == False:
        window.show()
    app.exec_()
