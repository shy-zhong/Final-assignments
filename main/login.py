from ui.ui_login import Ui_Login
from PySide6.QtWidgets import QDialog,QLabel,QMessageBox
from PySide6.QtCore import QRect,QCoreApplication,Slot,Signal
from PySide6.QtGui import QPixmap
from func.mysql import Mysql
from main.tools import loginButton
from main.register import Register
import rc_resource

class Login(QDialog):

    LoginOver = Signal(str)
    registerOver = Signal()

    def __init__(self,parent=None):
        self.parent=parent
        super().__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.setWindowTitle("登录")
        self.register = loginButton(self)
        self.background = QLabel(self)

        self.register.setObjectName(u"register")
        self.register.setGeometry(QRect(170, 130, 110, 25))
        self.register.setText(QCoreApplication.translate("Dialog", u"\u6ca1\u6709\u8d26\u53f7\uff1f\u70b9\u51fb\u6ce8\u518c", None))
        self.register.setHoverColor("white")
        self.register.setFunction(self.__tramsmit__)

        self.background.setPixmap(QPixmap(":/background/resource/blue.png"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0,0,self.width(),self.height())
        self.background.lower()

        self.ui.enter.clicked.connect(self.Check)
        self.ui.cancel.clicked.connect(self.reject)

    def login(self,username:str,password:str)->bool:
        if username == None or password == None:
            return False
        result = Mysql.select(Mysql.connect(),"login",username=username)
        if result == None:
            return False
        else:
            return password == result[1]
    
    def __tramsmit__(self):
        u_p = ("","")
        register = Register(self.parent,self.pos().x(),self.pos().y())
        self.hide()
        register.exec()
        if register.isRegist():
            u_p = register.returnU_P()
        self.ui.username.setText(u_p[0])
        self.ui.password.setText(u_p[1])
        self.show()

    @Slot()
    def Check(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        if self.login(username,password):
            message =  QMessageBox()
            message.setIcon(QMessageBox.Information)
            message.setText("登录成功")
            message.exec()
            self.LoginOver.emit(username)
            self.close()
        else:
            message =  QMessageBox()
            message.setIcon(QMessageBox.Critical)
            message.setText("登录失败")
            message.exec()