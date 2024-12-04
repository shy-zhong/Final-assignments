# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow, QLabel, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt,QRect,Slot
from ui.mainwindow import Ui_MainWindow
from main.tools import loginButton,iconButton
from main.login import Login
from main.testpaper import testpaper
#from main.background import background
import rc_resource
class MainWindow(QMainWindow):


    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open)

        self.a=testpaper()
        #self.a.close()

        self.setStyleSheet("background-color:white;");

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap(":/background/resource/background.jpg"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0,50,self.width(),self.height()-30)


        self.login = loginButton(self)
        self.icon = iconButton(self)

        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"font: 12pt;")
        self.login.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.login.setText("登录")
        self.login.setFunction(self.enterLogin)

        self.icon.setFunction(self.enterLogin)


    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.background.resize(self.size())
        self.login.setGeometry(QRect(self.width()-120,20, 80, 20))
        self.icon.setGeometry(QRect(self.width()-150,10,50,35))

    def enterLogin(self):
        login = Login()
        login.exec()

    @Slot()
    def open(self):
        self.a.show()




