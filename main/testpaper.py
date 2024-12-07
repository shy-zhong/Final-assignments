# This Python file uses the following encoding: utf-8
from func.mysql import Mysql
from func.check import Check
from main.tools import QuestionButton
from PySide6.QtWidgets import (QWidget, QListWidgetItem, QLabel, QPushButton, QSizePolicy
                            , QSpacerItem, QHBoxLayout,QVBoxLayout)
from PySide6.QtCore import Qt, QRect,Slot,QSize
from PySide6.QtGui import QFont, QPixmap,QFont
from ui.ui_testpaper import Ui_Testpaper
import rc_resource
from random import randrange
class testpaper(QWidget):
    def __init__(self,parent=None):
        super().__init__(None)

        #self.index = randrange(1,31)

        self.ui = Ui_Testpaper()
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

        self.createAnswerCard()

        self.showMaximized()

        self.ui.question.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        font = QFont()
        font.setPointSize(12)
        font.setLetterSpacing(QFont.PercentageSpacing, 105);
        self.ui.question.setFont(font)

        self.db = Mysql.connect()
        #self.showQuestionandAnswer()
        self.maxIndex = Mysql.max(self.db,'question','id')

        self.ui.answer.setGeometry(QRect(0,0,1000,350))
        self.ui.answer.itemClicked.connect(self.chosen)
        self.ui.answer.itemClicked.connect(self.saveAnswer)
        self.createQuestion()
    
    def createAnswerCard(self,cnt = 22):
        row = 5
        layout = QVBoxLayout()
        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()

        label1 = QLabel(self.ui.card)
        label2 = QLabel(self.ui.card)
        
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)

        label1.setText("  单选题")
        label1.setFont(font)

        label2.setText("  多选题")
        label2.setFont(font)
        #self.single_option = []
        ButtonVlayout = QVBoxLayout()
        sum = 0
        for i in range(0,row):
            ButtonHlayout  = QHBoxLayout()
            for j in range (0,row):
                if sum > 22:
                    pass
                else:
                    button = QuestionButton(str(sum+1))
                    ButtonHlayout.addWidget(button)
                sum+=1
            if i == row-1:
                space = QSpacerItem(22%row*60,1)
                ButtonHlayout.addItem(space)
            ButtonVlayout.addLayout(ButtonHlayout)
            #self.single_option.append(ButtonHlayout)
        layout1.addWidget(label1)
        layout1.addLayout(ButtonVlayout)

        sum = 0
        ButtonVlayout = QVBoxLayout()
        for i in range(0,row):
            ButtonHlayout  = QHBoxLayout()
            for j in range (0,row):
                if sum > cnt:
                    pass
                else:
                    button = QuestionButton(str(i*4+j + 1))
                    ButtonHlayout.addWidget(button)
                sum+=1
            if i == row-1:
                space = QSpacerItem(22%row*60,1)
                ButtonHlayout.addItem(space)
            ButtonVlayout.addLayout(ButtonHlayout)
        layout2.addWidget(label2)
        layout2.addLayout(ButtonVlayout)

        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.setContentsMargins(0,0,0,80)
        self.ui.card.setLayout(layout)
        self.ui.card.layout().setSpacing(0)

    def createQuestion(self):
        layout = self.ui.card.layout()
        for i in range(layout.count()):
            temp1 = layout.itemAt(i)
            for j in range(temp1.count()):
                if type(temp1.itemAt(j)) == QVBoxLayout:
                    temp2 = temp1.itemAt(j)
                    for k in range(temp1.count()):
                        temp3 = temp1.itemAt(k)
                        if type(temp3) == QVBoxLayout:
                            for l in range(temp3.count()):
                                temp4 = temp3.itemAt(l)
                                for m in range(temp4.count()):
                                    temp5 = temp4.itemAt(m).widget()
                                    if type(temp5) == QuestionButton: 
                                        goal = int(temp5.text())
                                        temp5.setIndex(goal)
                                        temp5.sendIndex.connect(self.showQuestionandAnswer)
    @Slot(int)
    def showQuestionandAnswer(self,index = 1):

        self.result = Mysql.select(self.db,"question",index)
        result = self.result
        print(index)
        print(result)
        self.ui.question.setText(result[3])

        self.indexs = [Qt.Unchecked,Qt.Unchecked,Qt.Unchecked,Qt.Unchecked]

        item = QListWidgetItem()
        item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        item.setCheckState(Qt.Unchecked)
        item.setSizeHint(QSize(self.ui.answer.width(),86))

        itemA = QListWidgetItem(item)
        itemA.setText('A '+result[4])

        itemB = QListWidgetItem(item)
        itemB.setText('B '+result[5])

        itemC = QListWidgetItem(item)
        itemC.setText('C '+result[6])

        itemD = QListWidgetItem(item)
        itemD.setText('D '+result[7])

        self.ui.answer.clear()
        self.ui.answer.addItem(itemA)
        self.ui.answer.addItem(itemB)
        self.ui.answer.addItem(itemC)
        self.ui.answer.addItem(itemD)

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

    def saveAnswer(self):
        options =['A','B','C','D']
        answer = [i for i in range(self.ui.answer.count()) if self.ui.answer.item(i).checkState() == Qt.Checked]
        answer = [options[i] for i in answer]
        #Check.saveAnswer(answer,self.result[0])