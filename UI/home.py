from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class Home(QWidget):
	def __init__(self):
		super(Home,self).__init__()
		loadUi("ui_Home.ui",self)
		self.btnRun.clicked.connect(self.btnRun_click)

	def btnRun_click(self):
		print('12')
		
