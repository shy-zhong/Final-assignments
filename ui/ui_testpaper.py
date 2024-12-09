# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testpaper.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QSizePolicy, QWidget)
import resource_rc

class Ui_Testpaper(object):
    def setupUi(self, Testpaper):
        if not Testpaper.objectName():
            Testpaper.setObjectName(u"Testpaper")
        Testpaper.resize(1020, 628)
        icon = QIcon()
        icon.addFile(u":/background/resource/open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Testpaper.setWindowIcon(icon)
        self.questions = QWidget(Testpaper)
        self.questions.setObjectName(u"questions")
        self.questions.setGeometry(QRect(30, 20, 591, 231))
        self.questions.setStyleSheet(u"background-color:white")
        self.question = QLabel(self.questions)
        self.question.setObjectName(u"question")
        self.question.setGeometry(QRect(10, 0, 491, 161))
        self.question.setWordWrap(True)
        self.answers = QWidget(Testpaper)
        self.answers.setObjectName(u"answers")
        self.answers.setGeometry(QRect(30, 310, 591, 231))
        self.answers.setStyleSheet(u"background-color:white")
        self.answer = QListWidget(self.answers)
        self.answer.setObjectName(u"answer")
        self.answer.setGeometry(QRect(0, 20, 591, 231))
        self.answer.setStyleSheet(u"border: none;")
        self.card = QWidget(Testpaper)
        self.card.setObjectName(u"card")
        self.card.setGeometry(QRect(630, 30, 211, 511))
        self.card.setStyleSheet(u"background-color:white;")
        self.s = QWidget(self.card)
        self.s.setObjectName(u"s")
        self.s.setGeometry(QRect(30, 50, 120, 80))
        self.m = QWidget(self.card)
        self.m.setObjectName(u"m")
        self.m.setGeometry(QRect(30, 240, 120, 80))

        self.retranslateUi(Testpaper)

        QMetaObject.connectSlotsByName(Testpaper)
    # setupUi

    def retranslateUi(self, Testpaper):
        Testpaper.setWindowTitle(QCoreApplication.translate("Testpaper", u"\u8bd5\u5377", None))
        self.question.setText("")
    # retranslateUi

