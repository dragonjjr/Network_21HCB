from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
import logo
import sys
sys.path.append('..')

from remote_control import *
class Home(QWidget):
	def __init__(self):
		super(Home,self).__init__()
		loadUi("ui_Home.ui",self)
		self.btnRun.clicked.connect(self.btnRun_click)

	def btnRun_click(self):
		remotecontrol = RemoteControl()
		remotecontrol.start()
		
		
