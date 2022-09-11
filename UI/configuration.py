from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtCore
from mydialog import MyDialog
class Configuration(QWidget):
	def __init__(self,parent):
		super(Configuration,self).__init__()
		loadUi("ui_Configuration.ui",self)
		self.parent = parent
		self.btnAddBasic.clicked.connect(self.btnAddBasic_click)
		self.btnAddAdvanced.clicked.connect(self.btnAddAdvanced_click)
		self.btnRemoveBasic.clicked.connect(self.btnRemoveBasic_click)
		self.btnRemoveAdvanced.clicked.connect(self.btnRemoveAdvanced_click)
		self.btnSave.clicked.connect(self.btnSave_click)

	def btnAddBasic_click(self):
		dialog = QDialog()
		dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
		dialog.setWindowIcon(QtGui.QIcon('Assets/Images/logo.png'))
		ui = MyDialog("Basic","Basic Controller",dialog)

	def btnAddAdvanced_click(self):
		dialog = QDialog()
		dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
		dialog.setWindowIcon(QtGui.QIcon('Assets/Images/logo.png'))
		ui = MyDialog("Advanced","Advanced Controller",dialog)

	# YOUR CODDE HERE
	def btnSave_click(self):
		print(self.cbAutoRun.isChecked())

	def btnRemoveBasic_click(self):
		#Name listview : lvBasic -> self.lvBasic
		print("Remove Basic")

	def btnRemoveAdvanced_click(self):
		#Name listview : lvAdvanced -> self.lvAdvanced
		print("Remove Advanced")


		
