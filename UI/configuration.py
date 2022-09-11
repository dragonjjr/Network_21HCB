import sys
from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtCore
from mydialog import MyDialog

sys.path.append('..')
from helpers import *
import global_variables  

class Configuration(QWidget):
	def __init__(self,parent):
		super(Configuration,self).__init__()
		loadUi("ui_Configuration.ui",self)
		self.render_config()
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

	def render_config(self):
		cfg = load_config('../app_configs.yaml')
		global_variables.app_configs['white_list'] = cfg['white_list']
		global_variables.app_configs['auto_run'] = cfg['auto_run']
		self.lvBasic.clear()
		self.lvAdvanced.clear()

		for mail in global_variables.app_configs['white_list']['basic']:
			self.lvBasic.addItem(mail)
		for mail in global_variables.app_configs['white_list']['advanced']:
			self.lvAdvanced.addItem(mail)
		self.cbAutoRun.setChecked(global_variables.app_configs['auto_run'])


		
