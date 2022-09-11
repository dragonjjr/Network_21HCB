from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import QtGui
from PyQt5.uic import loadUi

class MyDialog(QDialog):
	def __init__(self, title, role, dialog):
		super(MyDialog,self).__init__()
		self.ui = loadUi("ui_CustomDialog.ui",dialog)
		dialog.setWindowTitle(title)
		self.ui.role.setText(role)
		self.ui.btnAddRole.clicked.connect(self.btnAddRole_click)
		self.ui.exec_()

	def btnAddRole_click(self):
		print(self.ui.mail.text())
