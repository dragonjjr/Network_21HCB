import sys
from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtCore
from UI.mydialog import MyDialog
from UI.mymessagebox import MyMessageBox
sys.path.append('..')
from helpers import *
import global_variables  

class Configuration(QWidget):
	def __init__(self,parent):
		super(Configuration,self).__init__()
		loadUi("UI/ui_Configuration.ui",self)
		self.render_config()
		self.parent = self
		self.btnAddBasic.clicked.connect(self.btnAddBasic_click)
		self.btnAddAdvanced.clicked.connect(self.btnAddAdvanced_click)
		self.btnRemoveBasic.clicked.connect(self.btnRemoveBasic_click)
		self.btnRemoveAdvanced.clicked.connect(self.btnRemoveAdvanced_click)
		self.btnSave.clicked.connect(self.btnSave_click)
		

	def btnAddBasic_click(self):
		dialog = QDialog()
		dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
		dialog.setWindowIcon(QtGui.QIcon('UI/Assets/Images/logo.png'))
		ui = MyDialog("Basic","Basic Controller",dialog, self.parent ,True)

	def btnAddAdvanced_click(self):
		dialog = QDialog()
		dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
		dialog.setWindowIcon(QtGui.QIcon('UI/Assets/Images/logo.png'))
		ui = MyDialog("Advanced","Advanced Controller",dialog, self.parent, False)

	
	def btnSave_click(self):
		new_configs = {
			'white_list': {},
			'auto_run': False
		}
		basic, advanced = [], []
		
		for i in range(self.lvBasic.count()):
			basic.append(self.lvBasic.item(i).text())
		for i in range(self.lvAdvanced.count()):
			advanced.append(self.lvAdvanced.item(i).text())

		new_configs['white_list']['basic'] = basic
		new_configs['white_list']['advanced'] = advanced
		new_configs['auto_run'] = self.cbAutoRun.isChecked()

		global_variables.app_configs = new_configs

		save_config(new_configs, 'app_configs.yaml')
		dialog = QDialog()
		dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
		dialog.setWindowIcon(QtGui.QIcon('UI/Assets/Images/logo.png'))
		msg = MyMessageBox(title='Success', message='Save configs successfully', dialog=dialog)

	def btnRemoveBasic_click(self):
		selected = self.lvBasic.selectedItems()
		if len(selected) == 0:
			dialog = QDialog()
			dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
			dialog.setWindowIcon(QtGui.QIcon('UI/Assets/Images/logo.png'))
			msg = MyMessageBox(title='Error', message='Please select controllers to remove!', dialog=dialog)
		for item in selected: 
			self.lvBasic.takeItem(self.lvBasic.row(item))

	def btnRemoveAdvanced_click(self):
		selected = self.lvAdvanced.selectedItems()
		if len(selected) == 0:
			dialog = QDialog()
			dialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
			dialog.setWindowIcon(QtGui.QIcon('UI/Assets/Images/logo.png'))
			msg = MyMessageBox(title='Error', message='Please select controllers to remove!', dialog=dialog)
		for item in selected: 
			self.lvAdvanced.takeItem(self.lvAdvanced.row(item))

	def render_config(self):
		cfg = load_config('app_configs.yaml')
		global_variables.app_configs['white_list'] = cfg['white_list']
		global_variables.app_configs['auto_run'] = cfg['auto_run']
		self.lvBasic.clear()
		self.lvAdvanced.clear()

		for mail in global_variables.app_configs['white_list']['basic']:
			self.lvBasic.addItem(mail)
		for mail in global_variables.app_configs['white_list']['advanced']:
			self.lvAdvanced.addItem(mail)
		self.cbAutoRun.setChecked(global_variables.app_configs['auto_run'])


		
