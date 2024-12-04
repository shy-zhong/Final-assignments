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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1020, 628)
        self.question = QWidget(Form)
        self.question.setObjectName(u"question")
        self.question.setGeometry(QRect(10, 20, 731, 251))
        self.question.setStyleSheet(u"background-color:white")
        self.items = QWidget(Form)
        self.items.setObjectName(u"items")
        self.items.setGeometry(QRect(10, 290, 731, 251))
        self.items.setStyleSheet(u"background-color:white")
        self.anwser = QWidget(Form)
        self.anwser.setObjectName(u"anwser")
        self.anwser.setGeometry(QRect(750, 20, 231, 521))
        self.anwser.setStyleSheet(u"background-color:white")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 570, 80, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

