# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(322, 247)
        self.tip1 = QLabel(Dialog)
        self.tip1.setObjectName(u"tip1")
        self.tip1.setGeometry(QRect(60, 60, 31, 21))
        self.tip2 = QLabel(Dialog)
        self.tip2.setObjectName(u"tip2")
        self.tip2.setGeometry(QRect(60, 100, 31, 21))
        self.username = QLineEdit(Dialog)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(100, 60, 161, 22))
        self.password = QLineEdit(Dialog)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(100, 100, 161, 22))
        self.enter = QPushButton(Dialog)
        self.enter.setObjectName(u"enter")
        self.enter.setGeometry(QRect(30, 190, 80, 21))
        self.cancel = QPushButton(Dialog)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(220, 190, 80, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.tip1.setText(QCoreApplication.translate("Dialog", u"\u767b\u5f55", None))
        self.tip2.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801", None))
        self.enter.setText(QCoreApplication.translate("Dialog", u"\u767b\u5f55", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

