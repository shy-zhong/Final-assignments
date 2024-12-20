# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(330, 265)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        Login.setWindowIcon(icon)
        self.tip1 = QLabel(Login)
        self.tip1.setObjectName(u"tip1")
        self.tip1.setGeometry(QRect(50, 60, 31, 21))
        self.tip2 = QLabel(Login)
        self.tip2.setObjectName(u"tip2")
        self.tip2.setGeometry(QRect(50, 100, 31, 21))
        self.username = QLineEdit(Login)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(90, 60, 171, 22))
        self.password = QLineEdit(Login)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(90, 100, 171, 22))
        self.enter = QPushButton(Login)
        self.enter.setObjectName(u"enter")
        self.enter.setGeometry(QRect(30, 180, 80, 21))
        self.cancel = QPushButton(Login)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(210, 180, 80, 21))

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Dialog", None))
        self.tip1.setText(QCoreApplication.translate("Login", u"\u767b\u5f55", None))
        self.tip2.setText(QCoreApplication.translate("Login", u"\u5bc6\u7801", None))
        self.username.setText(QCoreApplication.translate("Login", u"zyy", None))
        self.password.setText(QCoreApplication.translate("Login", u"123456", None))
        self.enter.setText(QCoreApplication.translate("Login", u"\u767b\u5f55", None))
        self.cancel.setText(QCoreApplication.translate("Login", u"\u53d6\u6d88", None))
    # retranslateUi

