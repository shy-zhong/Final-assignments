import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar
from PySide6.QtGui import QIcon, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        file_menu = menu_bar.addMenu("文件")

        action_open = QAction(QIcon("open_icon.png"), "打开", self)
        action_save = QAction(QIcon("save_icon.png"), "保存", self)

        # 设置菜单中QAction悬浮时的背景颜色为浅灰色
        file_menu.setStyleSheet(" QMenu::item:selected {background:rgba(82,130,164,1);border:1px solid rgba(82,130,164,1);}")

        file_menu.addAction(action_open)
        file_menu.addAction(action_save)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())