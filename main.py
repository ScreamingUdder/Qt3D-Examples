from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2 import QtCore
import sys
from ui.mainwindow import Ui_MainWindow
from cylinderwindow import CylinderWindow
from spherewindow import SphereWindow


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.cylinderdialog = CylinderWindow()
        self.spheredialog = SphereWindow()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        self.cylindersbutton.clicked.connect(self.cylinderdialog.show)
        self.spheres.clicked.connect(self.spheredialog.show)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    window = QMainWindow()
    ui = MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
