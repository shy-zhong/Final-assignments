from ui.login import Ui_Dialog
from PySide6.QtWidgets import QDialog

class Login(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
