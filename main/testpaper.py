# This Python file uses the following encoding: utf-8
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    sys.path.append("D:\\project\\QT\\Final-assignments")
from func.mysql import Mysql
from main.tools import cardButton
from ui.ui_testpaper import Ui_Testpaper
from PySide6.QtWidgets import (QWidget, QListWidgetItem, QLabel, QPushButton, QSizePolicy
                                , QSpacerItem, QHBoxLayout,QVBoxLayout)
from PySide6.QtCore import Qt, QRect,Slot,QSize
from PySide6.QtGui import QFont, QPixmap,QFont,QIcon
from random import randint
from math import ceil
import rc_resource

class testpaper(QWidget):
        
    def __init__(self,subject: str,cnt: int,parent=None):
        super().__init__(None)

        self.db = Mysql.connect()
        self.subject = subject
        self.cnt = cnt
        self.single = Mysql.max(self.db,subject,False)[0]
        self.mutiple = Mysql.max(self.db,subject,True)[0]
        self.maxIndex = int(self.single+self.mutiple)

        self.ui = Ui_Testpaper()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint | Qt.CustomizeWindowHint)

        self.reason = QLabel(self.ui.questions)
        self.reason.setWordWrap(True)
        self.reason.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        
        font = QFont()
        font.setPointSize(12)
        font.setLetterSpacing(QFont.PercentageSpacing, 105);
        self.reason.setFont(font)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap(":/background/resource/blue.png"))
        self.background.setScaledContents(True)
        self.background.lower()

        self.checked = QPushButton(self)
        self.checked.setGeometry(QRect(700,800,100,60))
        self.checked.raise_()
        self.checked.setText("确认")
        self.checked.clicked.connect(self.check)
        self.checked.clicked.connect(lambda :self.checked.setEnabled(False))

        self.createAnswerCard(cnt)

        self.showMaximized()

        self.ui.question.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        font = QFont()
        font.setPointSize(12)
        font.setLetterSpacing(QFont.PercentageSpacing, 105);
        self.ui.question.setFont(font)

        self.ui.answer.itemClicked.connect(self.chosen)
        self.ui.answer.itemClicked.connect(self.saveAnswer)
        self.createQuestion()

        self.setWindowIcon(QIcon(QPixmap(":/background/resource/open.png")))
        self.setWindowFlag(Qt.WindowType.MSWindowsFixedSizeDialogHint,True)
        
    def createAnswerCard(self,cnt = 25):
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
        label1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        label1.setFixedSize(100,20)
        label1.setFont(font)

        label2.setText("  多选题")
        label2.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        label2.setFixedSize(100,25)
        label2.setFont(font)

        sum = 0

        self.single_options = []
        ButtonVlayout = QVBoxLayout()

        for i in range(0,int(cnt*0.7/row+bool((cnt*0.7)%row))):
            ButtonHlayout  = QHBoxLayout()
            for j in range (0,row):
                if sum >= cnt*0.7:
                    space = QSpacerItem(58,10)
                    ButtonHlayout.addItem(space)
                else:
                    button = cardButton(str(sum+1))
                    button.setMutipleorSingle(False)
                    ButtonHlayout.addWidget(button)
                    sum+=1
                
            ButtonVlayout.addLayout(ButtonHlayout)
            self.single_options.append(ButtonHlayout)
        layout1.addWidget(label1)
        layout1.addLayout(ButtonVlayout)
        layout1.setAlignment(Qt.AlignTop)
        # layout1.setContentsMargins(10,10,10,0)

        self.muti_options = []
        ButtonVlayout = QVBoxLayout()
        for i in range(0,int(cnt*0.3/row+bool((cnt*0.3)%row))):
            ButtonHlayout  = QHBoxLayout()
            for j in range (0,row):
                if sum > cnt-1:
                    space = QSpacerItem(58,10)
                    ButtonHlayout.addItem(space)
                else:
                    button = cardButton(str(sum+1))
                    button.setMutipleorSingle(True)
                    ButtonHlayout.addWidget(button)
                    sum+=1
            ButtonVlayout.addLayout(ButtonHlayout)
            self.muti_options.append(ButtonHlayout)
        layout2.addWidget(label2)
        layout2.addLayout(ButtonVlayout)
        layout2.setAlignment(Qt.AlignTop)
        # layout2.setContentsMargins(10,0,10,0)

        layout.addLayout(layout1)
        layout.addLayout(layout2)
        self.ui.card.setLayout(layout)

        # self.ui.s.setLayout(layout1)
        # self.ui.m.setLayout(layout2)

    def createQuestion(self):
        for i in self.single_options:
            if type(i) == QHBoxLayout:
                for temp in [i.itemAt(index).widget() for index in range (i.count()) ]:
                    if type(temp) == cardButton:
                        goal = randint(1,self.single)
                        temp.setIndex(goal)
                        temp.sendIndex.connect(self.showQuestionandAnswerorReason)
        for i in self.muti_options:
            if type(i) == QHBoxLayout:
                for temp in [i.itemAt(index).widget() for index in range (i.count()) ]:
                    if type(temp) == cardButton:
                        goal = randint(1,self.mutiple)
                        temp.setIndex(goal)
                        temp.sendIndex.connect(self.showQuestionandAnswerorReason)

    @Slot(int,int,bool)
    def showQuestionandAnswerorReason(self,index,id,mutipleorsingle:bool):
        self.id = id
        self.index = index
        self.result = Mysql.select(self.db,self.subject,mutipleorsingle,index=index)
        
        result = self.result
        self.ui.question.setText(result[3])
        print(result)
        if not(self.checked.isEnabled()):
            self.reason.setText(self.result[9])
            #print(self.result[9])

        self.indexs = [Qt.Unchecked,Qt.Unchecked,Qt.Unchecked,Qt.Unchecked]
        
        item = QListWidgetItem()
        item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        item.setSizeHint(QSize(self.ui.answer.width(),86))
        item.setCheckState(Qt.Unchecked)
        
        itemA = QListWidgetItem(item)
        itemA.setText('A '+result[4])

        itemB = QListWidgetItem(item)
        itemB.setText('B '+result[5])

        itemC = QListWidgetItem(item)
        itemC.setText('C '+result[6])

        itemD = QListWidgetItem(item)
        itemD.setText('D '+result[7])

        try:
            if self.result[2] == "单选题":
                for i in self.single_options[int((self.id-1)/5)].itemAt(int((self.id-1)%5)).widget().returnAnswer():
                    if i == 'A':
                        self.indexs[0] = Qt.Checked
                        itemA.setCheckState(Qt.Checked)
                    elif i == 'B':
                        self.indexs[1] = Qt.Checked
                        itemB.setCheckState(Qt.Checked)
                    elif i == 'C':
                        self.indexs[2] = Qt.Checked
                        itemC.setCheckState(Qt.Checked)
                    elif i == 'D':
                        self.indexs[3] = Qt.Checked
                        itemD.setCheckState(Qt.Checked)
            if self.result[2] == "多选题":
                id = self.id - ceil(self.cnt*0.7)
                for i in self.muti_options[int((id-1)/5)].itemAt(int((id-1)%5)).widget().returnAnswer():
                    if i == 'A':
                        self.indexs[0] = Qt.Checked
                        itemA.setCheckState(Qt.Checked)
                    elif i == 'B':
                        self.indexs[1] = Qt.Checked
                        itemB.setCheckState(Qt.Checked)
                    elif i == 'C':
                        self.indexs[2] = Qt.Checked
                        itemC.setCheckState(Qt.Checked)
                    elif i == 'D':
                        self.indexs[3] = Qt.Checked
                        itemD.setCheckState(Qt.Checked)
        except:
            pass
        
        self.ui.answer.clear()
        self.ui.answer.addItem(itemA)
        self.ui.answer.addItem(itemB)
        self.ui.answer.addItem(itemC)
        self.ui.answer.addItem(itemD)
    @Slot(QListWidgetItem)
    def chosen(self,item: QListWidgetItem):
        if not(self.checked.isEnabled()):
            return
        
        if self.result[2] == "多选题":
            if item.checkState() == Qt.Checked:
                self.indexs[self.ui.answer.row(item)] = Qt.Unchecked 
                item.setCheckState(Qt.Unchecked)
            else:
                self.indexs[self.ui.answer.row(item)] = Qt.Checked
                item.setCheckState(Qt.Checked)
        
        if self.result[2] == "单选题":
            item.setCheckState(Qt.Checked)
            self.indexs[self.ui.answer.row(item)] = Qt.Checked
            for i in range(self.ui.answer.count()):
                if i != self.ui.answer.row(item):
                    self.indexs[i] = Qt.Unchecked
                    self.ui.answer.item(i).setCheckState(Qt.Unchecked)
    @Slot()
    def check(self):
        for i in self.single_options+self.muti_options:
            if type(i) == QHBoxLayout:
                for temp in [i.itemAt(index).widget() for index in range (i.count()) ]:
                    if type(temp) == cardButton:
                        temp.checkAll()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.ui.questions.setGeometry(QRect(60,50,1000,350))
        self.ui.question.setGeometry(QRect(0,0,1000,150))
        self.reason.setGeometry(QRect(0,150,1000,200))

        self.ui.answers.setGeometry(QRect(60,420,1000,350))
        self.ui.answer.setGeometry(QRect(0,0,1000,350))

        self.ui.card.setGeometry(QRect(1080,50,300,720))
        self.ui.s.setGeometry(QRect(0,0,300,360))
        self.ui.m.setGeometry(QRect(0,360,300,360))
        
        self.background.setGeometry(0,0,self.width(),self.height())
        #print(event.size())
    @Slot()
    def saveAnswer(self):
        if not(self.checked.isEnabled()):
            return
        options =['A','B','C','D']
        answer = [i for i in range(self.ui.answer.count()) if self.ui.answer.item(i).checkState() == Qt.Checked]
        answer = [options[i] for i in answer]

        if self.result[2] == "单选题":
            self.single_options[int((self.id-1)/5)].itemAt(int((self.id-1)%5)).widget().setAnswer(answer)
        id = self.id - ceil(self.cnt*0.7)
        if self.result[2] == "多选题":
            self.muti_options[int((id-1)/5)].itemAt(int((id-1)%5)).widget().setAnswer(answer)

        
if __name__ == "__main__":
    app = QApplication()
    w = testpaper("mao",60)
    w.show()
    sys.exit(app.exec())

    sys.path.pop()
