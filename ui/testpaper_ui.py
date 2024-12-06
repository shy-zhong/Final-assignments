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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QListWidget,
    QListWidgetItem, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1020, 628)
        self.questions = QWidget(Form)
        self.questions.setObjectName(u"questions")
        self.questions.setGeometry(QRect(30, 20, 591, 231))
        self.questions.setStyleSheet(u"background-color:white")
        self.question = QLabel(self.questions)
        self.question.setObjectName(u"question")
        self.question.setGeometry(QRect(10, 0, 331, 161))
        self.question.setWordWrap(True)
        self.answers = QWidget(Form)
        self.answers.setObjectName(u"answers")
        self.answers.setGeometry(QRect(30, 310, 591, 231))
        self.answers.setStyleSheet(u"background-color:white")
        self.answer = QListWidget(self.answers)
        self.answer.setObjectName(u"answer")
        self.answer.setGeometry(QRect(0, 20, 591, 231))
        self.answer.setStyleSheet(u"border: none;")
        self.card = QFrame(Form)
        self.card.setObjectName(u"card")
        self.card.setGeometry(QRect(649, 40, 221, 501))
        self.card.setStyleSheet(u"")
        self.card.setFrameShape(QFrame.StyledPanel)
        self.card.setFrameShadow(QFrame.Raised)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8bd5\u5377", None))
        self.question.setText(QCoreApplication.translate("Form", u"\u5728\u4e0a\u8ff0\u793a\u4f8b\u4e2d\uff0c\u521b\u5efa\u4e86\u4e00\u4e2a\u7b80\u5355\u7684 QWidget \u6d3e\u751f\u7c7b MyWidget\uff0c\u5728\u5176\u6784\u9020\u51fd\u6570\u91cc\u901a\u8fc7 self.setWindowFlags(~Qt.WindowMinMaxButtonsHint) \u6b63\u786e\u5730\u8bbe\u7f6e\u4e86\u7a97\u53e3\u6807\u5fd7\uff0c\u4f7f\u5f97\u6700\u7ec8\u663e\u793a\u7684\u7a97\u53e3\u4e0a\u4e0d\u4f1a\u51fa\u73b0\u6700\u5c0f\u5316\u548c\u6700\u5927\u5316\u6309\u94ae\u63d0\u793a\uff08\u5bf9\u5e94\u7684\u6309\u94ae\u4e5f\u5c31\u4e0d\u4f1a\u663e\u793a\u4e86\uff09\u3002\n"
"\u603b\u7684\u6765\u8bf4\uff0c\u539f\u4ee3\u7801\u7684\u76ee\u7684\u662f\u6539\u53d8\u7a97\u53e3\u663e\u793a\u76f8\u5173\u7684\u6807\u5fd7\u5c5e\u6027\uff0c\u4f46\u8bed\u6cd5\u4e0a\u9700\u8981\u6309\u6b63\u786e\u7684\u64cd\u4f5c\u7b26\u6765\u5904\u7406 Qt \u7a97\u53e3\u6807\u5fd7\u5e38\u91cf\uff0c\u4ee5\u8fbe\u5230\u671f\u671b\u7684\u6548\u679c\u3002", None))
    # retranslateUi

