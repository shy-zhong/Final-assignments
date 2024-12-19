# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QComboBox, QMessageBox
from PySide6.QtGui import QPixmap, QShortcut
from PySide6.QtCore import Qt,Slot,QSize
from ui.ui_mainwindow import Ui_MainWindow
from main.tools import loginButton,iconButton
from main.login import Login
from main.background import information
from main.testpaper import testpaper
from func.mysql import Mysql
import rc_resource
class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.username = str()

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap(":/background/resource/background.jpg"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0,50,self.width(),self.height()-30)
        
        self.pushButton = QPushButton(self)
        self.pushButton.clicked.connect(self.open)
        self.pushButton.setStyleSheet("border-radius:50px;background-color:#fffae0")
        self.pushButton.setText("clicked me")
        self.pushButton.resize(100,100)
        
        self.subject = QComboBox(self)
        self.subject.setObjectName(u"subject")
        self.subject.resize(QSize(240, 30))
        self.subject.setStyleSheet("background-color:#aaffff")

        self.count = QComboBox(self)
        self.count.setObjectName(u"count")
        self.count.resize(QSize(240, 30))
        self.count.setStyleSheet("background-color:#aaffff")
        self.count.addItems([str(i*10) for i in range(1,10)])

        self.setStyleSheet("background-color:white;");
        
        self.login = loginButton(self)
        self.icon = iconButton(self)
        
        self.login.setStyleSheet(u"font: 12pt;")
        self.login.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.login.setText("用户")
        self.login.setFunction(self.enterLogin)
        self.login.resize(QSize(50,50))

        self.icon.setFunction(self.enterLogin)
        self.icon.resize(QSize(50,50))

        self.shutcut = QShortcut(Qt.Modifier.CTRL | Qt.Key.Key_S, self)
        self.shutcut.activated.connect(lambda:information().show())

    @Slot()
    def enterLogin(self):
        login = Login()
        login.LoginOver.connect(self.setProperty)
        login.exec()
        login.LoginOver.disconnect(self.setProperty)

    @Slot()
    def open(self):
        dictionary = {'语文':'chinese',
                      '计算机基础':'basic_computer',
                      '数据库':'database',
                      '毛泽东思想和中国特色社会主义理论体系概论':'mao',
                      '计算机组成原理':'computer_organization',
                      '市场营销学':'marketing_studies',
                      '马克思基本主义原理':'marketing_studies'}
        try:
            self.a=testpaper(dictionary[self.subject.currentText()],int(self.count.currentText()))
        except:
            QMessageBox.critical(self,"提示","请先登录！",QMessageBox.Ok)
        self.a.show()
    @Slot(str)
    def setProperty(self,username):
        #print(":/ico/resource/zyy.ico")
        self.username = username
        self.icon.setPicture(":/ico/resource/"+username+".ico")
        self.icon.setFunction(None)
        self.login.setFunction(None)
        self.login.setText(username)

        db = Mysql.connect()
        self.subject.addItems(( j for i in Mysql.execute(db,"SELECT subjectName FROM subject") for j in i))
        db.close()

    def resizeEvent(self,event):
        self.count.move(self.width()*0.35,self.height()*0.45)
        self.subject.move(self.width()*0.35,self.height()*0.35)
        self.pushButton.move(self.width()*0.42,self.height()*2/3)
        self.login.move(self.width()-100,0)
        self.icon.move(self.width()-150,0)
        self.background.resize(self.size())
        return super().resizeEvent(event)
