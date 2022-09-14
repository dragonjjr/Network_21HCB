from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QObject

class TrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon_path, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, QtGui.QIcon(icon_path), parent)
        self.__set_menu()

        self.activated.connect(self.__systemIcon)
        self.window = parent

    def __systemIcon(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.show_window()

    def __set_menu(self):
        menu = QtWidgets.QMenu()
        self.setContextMenu(menu)
        menu.addAction("Open Window", self.show_window)
        menu.addAction("Exit", self.exit)

    def show_window(self):
        self.window.show()
    def exit(self):
        self.window.close()
