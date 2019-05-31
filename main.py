from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2 import QtCore
import sys
from ui.mainwindow import Ui_MainWindow
from ui.cyldialog import Ui_cyldialog
from ui.projdialog import Ui_projdialog
from ui.sphdialog import Ui_sphdialog
from projection import Window


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.projdialog = Window()

        self.cylinderdialog = QDialog()
        self.spheredialog = QDialog()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.cylinderdialog.ui = CylinderDialog()
        self.cylinderdialog.ui.setupUi(self.cylinderdialog)
        self.spheredialog.ui = SphereDialog()
        self.spheredialog.ui.setupUi(self.spheredialog)

        self.projectionbutton.clicked.connect(self.projdialog.show)
        self.cylindersbutton.clicked.connect(self.cylinderdialog.show)
        self.spheres.clicked.connect(self.spheredialog.show)


class CylinderDialog(Ui_cyldialog):
    def __init__(self):
        super(CylinderDialog, self).__init__()


class SphereDialog(Ui_sphdialog):
    def __init__(self):
        super(SphereDialog, self).__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    window = QMainWindow()
    ui = MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
