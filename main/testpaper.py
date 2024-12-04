# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt

from ui.testpaper import Ui_Form

class testpaper(QWidget):
    def __init__(self,parent=None):
        super().__init__(None)
        myWidget = parent
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.CustomizeWindowHint)
        self.showMaximized()

    def resizeEvent(self, event):
        super().resizeEvent(event)
