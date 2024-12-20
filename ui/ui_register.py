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
        self.tip1.setGeometry(QRect(50, 30, 31, 21))
        self.tip2 = QLabel(Register)
        self.tip2.setObjectName(u"tip2")
        self.tip2.setGeometry(QRect(50, 70, 31, 21))
        self.username = QLineEdit(Register)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(90, 30, 171, 22))
        self.password = QLineEdit(Register)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(90, 70, 171, 22))
        self.regist = QPushButton(Register)
        self.regist.setObjectName(u"regist")
        self.regist.setGeometry(QRect(40, 210, 80, 21))
        self.cancel = QPushButton(Register)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(210, 210, 80, 21))
        self.password_2 = QLineEdit(Register)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setGeometry(QRect(90, 110, 171, 22))
        self.tip3 = QLabel(Register)
        self.tip3.setObjectName(u"tip3")
        self.tip3.setGeometry(QRect(20, 110, 61, 20))
        self.tip4 = QLabel(Register)
        self.tip4.setObjectName(u"tip4")
        self.tip4.setGeometry(QRect(20, 150, 61, 20))
        self.plot = QLineEdit(Register)
        self.plot.setObjectName(u"plot")
        self.plot.setGeometry(QRect(90, 150, 71, 22))
        self.verification_code = QLabel(Register)
        self.verification_code.setObjectName(u"verification_code")
        self.verification_code.setGeometry(QRect(180, 142, 80, 40))

        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Dialog", None))
        self.tip1.setText(QCoreApplication.translate("Register", u"\u767b\u5f55", None))
        self.tip2.setText(QCoreApplication.translate("Register", u"\u5bc6\u7801", None))
        self.username.setText("")
        self.password.setText("")
        self.regist.setText(QCoreApplication.translate("Register", u"\u6ce8\u518c", None))
        self.cancel.setText(QCoreApplication.translate("Register", u"\u53d6\u6d88", None))
        self.password_2.setText("")
        self.tip3.setText(QCoreApplication.translate("Register", u"<html><head/><body><p align=\"center\">\u786e\u8ba4\u5bc6\u7801</p></body></html>", None))
        self.tip4.setText(QCoreApplication.translate("Register", u"<html><head/><body><p align=\"center\">\u9a8c\u8bc1\u7801\n"
"</p></body></html>", None))
        self.plot.setText("")
        self.verification_code.setText("")
    # retranslateUi

