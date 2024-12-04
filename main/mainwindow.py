# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow, QLabel, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt,QRect
from ui.mainwindow import Ui_MainWindow
from main.tools import loginButton,iconButton
from main.login import Login
#from main.background import background
import rc_resource
import variable as va

class MainWindow(QMainWindow):
    def addWidget(self):
        pass

    def __init__(self, parent=None):
        super().__init__(parent)

        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setStyleSheet("background-color:white;");

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap(":/background/resource/background.jpg"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0,50,self.width(),self.height()-30)

        self.login = loginButton(self)
        self.icon = iconButton(self)

        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(680, 20, 80, 20))
        self.login.setStyleSheet(u"font: 12pt;")
        self.login.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.login.setText("登录")

        self.login.setSizePolicy(size_policy)



    def resizeEvent(self, event):
        super().resizeEvent(event)
        #print(self.size())
        self.background.resize(self.size())

    def mousePressEvent(self,event):
        super().mousePressEvent(event)
        x, y = event.pos().x(), event.pos().y()
        if x>=640 and x <=680 and y>=10 and y <= 60:
            login = Login()
            login.exec()
        if x>=700 and x <=750 and y>=20 and y <= 40:
            login = Login()
            login.exec()





