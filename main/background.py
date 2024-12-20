from PySide6.QtWidgets import QLabel,QWidget, QVBoxLayout, QLineEdit, QSizePolicy, QPushButton, QHBoxLayout
from PySide6.QtGui import QPixmap,QIcon,QShortcut
from PySide6.QtCore import Qt
from func.mysql import Mysql
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

class information(QWidget):
    def __init__(self,w: int = 150,h: int = 50):
        super().__init__()

        self.label = QLabel()
        self.host = QLineEdit()
        self.password = QLineEdit()
        self.button1 = QPushButton()
        self.button2 = QPushButton()
        layout = QVBoxLayout()
        layoutB = QHBoxLayout()

        self.label.setText("请输入数据库地址")
        self.label.setFixedSize(120,20)
        self.label.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.host.setFixedSize(120,30)
        self.host.setStyleSheet("background-color:white")
        self.host.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.host.setPlaceholderText("127.0.0.1")
        self.host.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.host)

        self.password.setFixedSize(120,30)
        self.password.setStyleSheet("background-color:white")
        self.password.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.password.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.password)

        self.button1.clicked.connect(lambda : Mysql.setHost(self.host.text()))
        self.button1.clicked.connect(lambda : Mysql.setPassword(self.password.text()))
        self.button1.clicked.connect(lambda : self.close())
        self.button1.setFixedSize(55,20)
        self.button1.setText("确认")

        self.button2.clicked.connect(lambda : self.close())
        self.button2.setFixedSize(55,20)
        self.button2.setText("返回")

        layoutB.addWidget(self.button1)
        layoutB.addWidget(self.button2)
        layoutB.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addLayout(layoutB)

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
        self.resize(w, h)
        self.setWindowTitle("host设置")
        self.setWindowIcon(QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave)))
        self.setWindowFlags(self.windowFlags() 
                            & ~Qt.WindowType.WindowMinMaxButtonsHint
                            | Qt.WindowType.WindowCloseButtonHint
                            | Qt.WindowType.WindowStaysOnTopHint
                            | Qt.WindowType.MSWindowsFixedSizeDialogHint
                            )
        QShortcut(Qt.Key.Key_Enter,self).activated.connect(lambda : self.button1.clicked.emit())