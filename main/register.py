if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    sys.path.append("D:\zyy\oneDrive\Desktop\Final-assignments")

from PySide6.QtWidgets import QDialog, QPushButton
from ui.ui_register import Ui_Register
class Register(QDialog):
    def __init__(self, parent=None,x = 0,y = 0):
        super().__init__(parent)
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.setWindowTitle("Register")
        self.setFixedSize(self.size())
        self.move(x,y)
        # Add your registration logic here

        # Example: Create a button to close the dialog
        self.close_button = QPushButton("Close", self)


if __name__ == "__main__":
    app = QApplication([])
    d = Register()
    d.show()
    sys.exit(app.exec())