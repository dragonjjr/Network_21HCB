import sys
from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import QtGui, QtCore
from PyQt5.uic import loadUi
sys.path.append('..')
from helpers import *
class MyMessageBox(QDialog):
	def __init__(self, title, message, dialog):
		super(MyMessageBox,self).__init__()
		self.ui = loadUi("UI/ui_CustomMessageBox.ui",dialog)
		dialog.setWindowTitle(title)
		self.ui.lbMessage.setText(message)
		self.ui.btnOK.clicked.connect(self.btnOK_click)
		self.ui.exec_()

	def btnOK_click(self):
		self.ui.close()
		