# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QLabel, QPushButton, QSizePolicy
from PySide6.QtGui import QFont,QPalette,QColor,QPixmap
from PySide6.QtCore import Qt, QSize, Signal, Slot
from func.check import Check
class Button(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.login = False
        self.Function = None

    def isLogin(self)->bool:
        return self.login
    def setFunction(self,Function):
        self.Function = Function
        if self.Function == None:
            self.login = True

    def mousePressEvent(self, event):
        if self.Function == None:
            return super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:  # 检测鼠标左键按下
            self.Function()
        return super().mousePressEvent(event)

class loginButton(Button):

    def __init__(self,parent=None):
        super().__init__(parent)

        self.hoverColor = "blue"
        self.leaveColor = "black"

    def setHoverColor(self,color):
        self.hoverColor = color

    def setLeaveColor(self,color):
        self.leaveColor = color

    def mousePressEvent(self, event):
        return super().mousePressEvent(event)

    def enterEvent(self,event):
        super().enterEvent(event)

        if self.isLogin():
            return

        font = QFont()
        font.setUnderline(True)
        self.setFont(font)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.WindowText,QColor(self.hoverColor))
        self.setPalette(palette)

    def leaveEvent(self,event):
        super().leaveEvent(event)

        if self.isLogin():
            return
        
        font = QFont()
        font.setUnderline(False)
        self.setFont(font)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.WindowText,QColor(self.leaveColor))
        self.setPalette(palette)

class iconButton(Button):
    def __init__(self,parent=None):
        self.parent = parent
        super().__init__(parent)
        self.setPixmap(QPixmap(":/tool/resource/avatar.png"))
        self.setScaledContents(False)


    def setPicture(self, arg__1=":/tool/resource/avatar.png" ) -> None:
        picture = QPixmap(arg__1)
        self.setPixmap(picture)
        self.setScaledContents(True)

class cardButton(QPushButton):
    sendIndex = Signal(int,int,bool)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setFixedSize(QSize(50, 50))
        self.clicked.connect(self.IndexofSender)

    @Slot()
    def IndexofSender(self):
        self.sendIndex.emit(self.index,int(self.text()),self.mutipleorsingle)

    def setMutipleorSingle(self,mutipleorsingle:bool):
        self.mutipleorsingle = mutipleorsingle
    
    def returnAnswer(self):
        try:
            return self.answer
        except:
            return list()
        
    def setResult(self,result):
        self.result = result
        
    def setAnswer(self,answer):
        self.answer = answer
        self.setStyleSheet("QPushButton { background-color: #5555ff; } QPushButton:hover { background-color: #5555ff;border-radius:5px;}")
        
    def setIndex(self,id):
        self.index = id
    
    def returnResult(self) -> bool:
        try:
            return Check.checkOption(self.answer,self.result)
        except:
            return False
        
    def checkAll(self):
        #self.setEnabled(False)
        self.answer = self.returnAnswer()
        result = self.returnResult()
        if result:
            self.setStyleSheet("QPushButton { background-color: #55aa00; } QPushButton:hover { background-color: #55aa00;border-radius:5px;}")    
        else:
            self.setStyleSheet("QPushButton { background-color: #ff0000; } QPushButton:hover { background-color: #ff0000;border-radius:5px;}")