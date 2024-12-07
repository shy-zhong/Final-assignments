# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QLabel, QPushButton, QSizePolicy
from PySide6.QtGui import QFont,QPalette,QColor,QPixmap
from PySide6.QtCore import Qt, QSize, Signal, Slot
from random import randint

class loginButton(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.hoverColor = "blue"
        self.leaveColor = "black"

    def setFunction(self,Function):
        self.Function = Function
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:  # 检测鼠标左键按下
            self.Function()
        super().mousePressEvent(event)
        #print(event.button())

    def setHoverColor(self,color):
        self.hoverColor = color

    def setLeaveColor(self,color):
        self.leaveColor = color


    def enterEvent(self,event):
        super().enterEvent(event)

        font = QFont()
        font.setUnderline(True)
        self.setFont(font)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.WindowText,QColor(self.hoverColor))
        self.setPalette(palette)


    def leaveEvent(self,event):
        super().leaveEvent(event)

        font = QFont()
        font.setUnderline(False)
        self.setFont(font)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.WindowText,QColor(self.leaveColor))
        self.setPalette(palette)

class iconButton(QLabel):
    def __init__(self,parent=None):
        self.parent = parent
        super().__init__(parent)
        self.setPixmap(QPixmap(":/tool/resource/avatar.png"))

    def setFunction(self,Function,):
        self.Function = Function
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:  # 检测鼠标左键按下
            self.Function()
        super().mousePressEvent(event)
        #print(event.button())

class cardButton(QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setFixedSize(QSize(50, 50))
        self.setIndex(0)

class QuestionButton(cardButton):

    sendIndex = Signal(int)
    def __init__(self,parent=None):
        self.parent = parent
        super().__init__(parent)
        
        self.clicked.connect(self.IndexofSender)
        self.answer = str(None)
        
    def setResult(self,answer):
        for i in answer:
            pass
        self.answer = answer
        self.setStyleSheet("background-color:rgb(85, 85, 255)")

    def setIndex(self,id):
        self.index = id
    
    def returnIndex(self):
        return self.index
        #return "hello"

    @Slot()
    def IndexofSender(self):
        self.sendIndex.emit(self.index)

class AnswerButton(cardButton):
    def __init__(self,answer,parent=None):
        self.parent = parent
        super().__init__(parent)

        self.clicked.connect(self.IndexofSender)

        self.answer = answer

    def setResult(self,answer):
        self.answer = answer
        self.setStyleSheet("background-color:rgb(85, 85, 255)")

    def setIndex(self,id):
        self.index = id