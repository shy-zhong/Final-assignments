# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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

class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(330, 265)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        Register.setWindowIcon(icon)
        self.tip1 = QLabel(Register)
        self.tip1.setObjectName(u"tip1")
        self.tip1.setGeometry(QRect(60, 50, 31, 21))
        self.tip2 = QLabel(Register)
        self.tip2.setObjectName(u"tip2")
        self.tip2.setGeometry(QRect(60, 90, 31, 21))
        self.username = QLineEdit(Register)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(100, 50, 171, 22))
        self.password = QLineEdit(Register)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(100, 90, 171, 22))
        self.enter = QPushButton(Register)
        self.enter.setObjectName(u"enter")
        self.enter.setGeometry(QRect(20, 210, 80, 21))
        self.cancel = QPushButton(Register)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(210, 210, 80, 21))
        self.password_2 = QLineEdit(Register)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setGeometry(QRect(100, 130, 171, 22))
        self.tip2_2 = QLabel(Register)
        self.tip2_2.setObjectName(u"tip2_2")
        self.tip2_2.setGeometry(QRect(30, 130, 61, 20))

        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Dialog", None))
        self.tip1.setText(QCoreApplication.translate("Register", u"\u767b\u5f55", None))
        self.tip2.setText(QCoreApplication.translate("Register", u"\u5bc6\u7801", None))
        self.username.setText("")
        self.password.setText("")
        self.enter.setText(QCoreApplication.translate("Register", u"\u767b\u5f55", None))
        self.cancel.setText(QCoreApplication.translate("Register", u"\u53d6\u6d88", None))
        self.password_2.setText("")
        self.tip2_2.setText(QCoreApplication.translate("Register", u"<html><head/><body><p align=\"center\">\u786e\u8ba4\u5bc6\u7801</p></body></html>", None))
    # retranslateUi

