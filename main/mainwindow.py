# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow
from ui.mainwindow import Ui_MainWindow
from main.login import Login

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(start)
def start():
    login = Login()
    login.exec()



