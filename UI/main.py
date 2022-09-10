import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication,QMainWindow
from PyQt5.uic import loadUi
from configuration import Configuration
from home import Home


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('ui_Main.ui', self)
        self.home = Home()
        self.stackedWidget.addWidget(self.home)
        self.home.btnConfiguration.clicked.connect(self.go_to_second)
        self.configuration = Configuration(self)
        self.stackedWidget.addWidget(self.configuration)
        self.configuration.btnBack.clicked.connect(self.go_to_first)

    def go_to_first(self):
        self.stackedWidget.setCurrentIndex(0)

    def go_to_second(self):
        self.stackedWidget.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.setWindowIcon(QtGui.QIcon('Assets/Images/logo.png'))
    window.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
    window.setWindowTitle("Remote Control with Email Service")
    window.show()
    app.exec_()