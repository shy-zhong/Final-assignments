# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFont,QPalette,QColor,QPixmap

class loginButton(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.hoverColor = "blue"
        self.leaveColor = "black"

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
        #self.setScaledContents(True)
        self.setGeometry(640,10,50,35)


