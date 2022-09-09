from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class Configuration(QWidget):
	def __init__(self):
		super(Configuration,self).__init__()
		loadUi("ui_Configuration.ui",self)
		
