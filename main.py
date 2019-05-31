from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore
import sys
from ui.mainwindow import Ui_MainWindow
from ui.cyldialog import Ui_cyldialog
from ui.projdialog import Ui_projdialog
from ui.sphdialog import Ui_sphdialog


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.projdialog = ProjectionDialog()
        self.cylinderdialog = CylinderDialog()
        self.spheredialog = SphereDialog()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)


class ProjectionDialog(Ui_projdialog):
    pass


class CylinderDialog(Ui_cyldialog):
    pass


class SphereDialog(Ui_sphdialog):
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    window = QMainWindow()
    ui = MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
