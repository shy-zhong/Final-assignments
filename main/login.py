from ui.login import Ui_Dialog
from PySide6.QtWidgets import QDialog,QLabel
from PySide6.QtCore import QRect,QCoreApplication,Slot
from PySide6.QtGui import QPixmap

from main.tools import loginButton

import rc_resource

class Login(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("登录")
        self.register = loginButton(self)
        self.background = QLabel(self)

        self.register.setObjectName(u"register_2")
        self.register.setGeometry(QRect(170, 130, 110, 25))
        self.register.setText(QCoreApplication.translate("Dialog", u"\u6ca1\u6709\u8d26\u53f7\uff1f\u70b9\u51fb\u6ce8\u518c", None))
        self.register.setHoverColor("white")

        self.background.setPixmap(QPixmap(":/background/resource/blue.png"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0,0,self.width(),self.height())
        self.background.lower()

        self.ui.enter.clicked.connect(self.Check)
        self.ui.cancel.clicked.connect(self.reject)

    @Slot()
    def Check(self):
        pass
