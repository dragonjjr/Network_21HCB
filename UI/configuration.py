from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtCore
class Configuration(QWidget):
	def __init__(self,parent):
		super(Configuration,self).__init__()
		loadUi("ui_Configuration.ui",self)
		self.parent = parent
		self.btnAddBasic.clicked.connect(self.btnAddBasic_click)

	def btnAddBasic_click(self):
		dialog = QDialog()
		dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
		ui = loadUi("ui_CustomDialog.ui",dialog)
		ui.exec_()


		
