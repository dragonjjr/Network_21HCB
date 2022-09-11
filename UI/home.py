from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
import UI.logo
import sys
sys.path.append('..')

from remote_control import *
import global_variables 

class Home(QWidget):
	def __init__(self):
		super(Home,self).__init__()
		loadUi("UI/ui_Home.ui",self)
		self.btnRun.clicked.connect(self.btnRun_click)

	def setup(self):
	    cfg = load_config('app_configs.yaml')

	    global_variables.app_configs['white_list'] = cfg['white_list']
	    global_variables.app_configs['auto_run'] = cfg['auto_run']

	def btnRun_click(self):
		self.setup()
		RemoteControl().start()


	
		
		
