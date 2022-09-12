import sys
from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import QtGui, QtCore
from PyQt5.uic import loadUi
sys.path.append('..')
from helpers import *
from  UI.mymessagebox import MyMessageBox
class MyDialog(QDialog):
	def __init__(self, title, role, dialog, window,is_basic):
		super(MyDialog,self).__init__()
		self.ui = loadUi("UI/ui_CustomDialog.ui",dialog)
		self.is_basic = is_basic
		self.window = window
		dialog.setWindowTitle(title)
		self.ui.role.setText(role)
		self.ui.btnAddRole.clicked.connect(self.btnAddRole_click)
		self.ui.exec_()

	def btnAddRole_click(self):
		if mail_validate(self.ui.mail.text()) != None:
			basic, advanced = [], []

			for i in range(self.window.lvBasic.count()):
				basic.append(self.window.lvBasic.item(i).text())
			for i in range(self.window.lvAdvanced.count()):
				advanced.append(self.window.lvAdvanced.item(i).text())
				
			if self.ui.mail.text() in basic:
				dialog = QDialog()
				dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
				dialog.setWindowIcon(QtGui.QIcon('UI/Assets/Images/logo.png'))
				msg = MyMessageBox(title='Error', message='This controller is already in the basic list!', dialog=dialog)
			elif self.ui.mail.text() in advanced:
				dialog = QDialog()
				dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
				dialog.setWindowIcon(QtGui.QIcon('UI/Assets/Images/logo.png'))
				msg = MyMessageBox(title='Error', message='This controller is already in the advanced list!', dialog=dialog)
			else:
				if self.is_basic:
					self.window.lvBasic.addItem(self.ui.mail.text())
				else:
					self.window.lvAdvanced.addItem(self.ui.mail.text())
		else:
			messagebox = QDialog()
			messagebox.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
			messagebox.setWindowIcon(QtGui.QIcon('UI/Assets/Images/logo.png'))
			uimess = MyMessageBox("Validate Email","Email invalid",messagebox)
