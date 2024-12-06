# This Python file uses the following encoding: utf-8
from func.mysql import Mysql
from func.check import Check
from PySide6.QtWidgets import QWidget, QListWidgetItem, QLabel, QPushButton
from PySide6.QtCore import Qt, QRect,Slot, QSize
from PySide6.QtGui import QFont, QPixmap
from ui.testpaper import Ui_Form
import rc_resource
from random import randrange
class testpaper(QWidget):
    def __init__(self,parent=None):
        super().__init__(None)

        self.index = randrange(1,31)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint | Qt.CustomizeWindowHint)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap(":/background/resource/blue.png"))
        self.background.setScaledContents(True)
        self.background.lower()

        self.checked = QPushButton(self)
        self.checked.setGeometry(QRect(700,800,100,60))
        self.checked.raise_()
        self.checked.setText("确认")
        self.checked.clicked.connect(self.check)

        self.showMaximized()

        self.ui.question.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        font = QFont()
        font.setPointSize(12)
        font.setLetterSpacing(QFont.PercentageSpacing, 105);
        self.ui.question.setFont(font)

        self.db = Mysql.connect()
        self.show_question_and_answer()
        self.maxIndex = Mysql.max(self.db,'question','id')

        self.ui.answer.setGeometry(QRect(0,0,1000,350))
        self.ui.answer.itemClicked.connect(self.chosen)


    def show_question_and_answer(self):

        self.result = Mysql.select(self.db,"question",self.index)
        print(self.result)
        self.ui.question.setText(self.result[3])

        self.indexs = [Qt.Unchecked,Qt.Unchecked,Qt.Unchecked,Qt.Unchecked]

        item = QListWidgetItem()
        item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        item.setCheckState(Qt.Unchecked)
        item.setSizeHint(QSize(self.ui.answer.width(),86))

        itemA = QListWidgetItem(item)
        itemA.setText('A '+self.result[4])

        itemB = QListWidgetItem(item)
        itemB.setText('B '+self.result[5])

        itemC = QListWidgetItem(item)
        itemC.setText('C '+self.result[6])

        itemD = QListWidgetItem(item)
        itemD.setText('D '+self.result[7])

        self.ui.answer.addItem(itemA)
        self.ui.answer.addItem(itemB)
        self.ui.answer.addItem(itemC)
        self.ui.answer.addItem(itemD)
        #print()
        #self.ui.answer.item(0).setSelected(True)

    @Slot(QListWidgetItem)
    def chosen(self,item):
        item.setCheckState(Qt.Checked)
        if self.result[2] == "多选题":
            return
        for i in range(self.ui.answer.count()):
            if i != self.ui.answer.row(item):
                self.indexs[i] = Qt.Unchecked
                self.ui.answer.item(i).setCheckState(Qt.Unchecked)
        self.indexs[self.ui.answer.row(item)] = Qt.Checked

    @Slot()
    def check(self):
        options =['A','B','C','D']
        answer = [i for i in range(self.ui.answer.count()) if self.ui.answer.item(i).checkState() == Qt.Checked]
        answer = [options[i] for i in answer]
        Check.checkOption(answer,self.result[8])


    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.ui.questions.setGeometry(QRect(60,50,1000,350))
        self.ui.answers.setGeometry(QRect(60,420,1000,350))
        self.ui.card.setGeometry(QRect(1080,50,300,720))
        self.ui.question.setGeometry(QRect(0,0,1000,350))
        self.background.setGeometry(0,0,self.width(),self.height())
        #print(event.size())
