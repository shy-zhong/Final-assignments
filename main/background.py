from PySide6.QtWidgets import QLabel,QWidget
from PySide6.QtGui import QPixmap
import rc_resource
class background(QWidget):
    def __init__(self,parent=None):
        self.parent = parent
        self = QWidget(parent)
        self.label = QLabel(self)

        if parent != None:
            self.setGeometry(0,30,parent.width(),parent.height()-30)
            self.label.resize(self.size())

        self.label.setPixmap(QPixmap(":/background/resource/background.jpg"))
        self.label.setScaledContents(True)



