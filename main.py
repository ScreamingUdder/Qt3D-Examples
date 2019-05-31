from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore
import sys


class MainWindow:
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    window = QMainWindow()
    ui = MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
