import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton
from PySide6.QtCore import Slot


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        button_ok = QPushButton("确定")
        button_ok.clicked.connect(self.accept)
        layout.addWidget(button_ok)


class MainWidget:
    def __init__(self):
        app = QApplication(sys.argv)
        dialog = MyDialog()
        dialog.accepted.connect(self.on_dialog_accepted)
        dialog.exec()
        sys.exit(app.exec())

    @Slot()
    def on_dialog_accepted(self):
        print("对话框已被接受")

if __name__ == '__main__':
    app = QApplication([])
    window = MyDialog()
    window.show()

    sys.exit(app.exec())