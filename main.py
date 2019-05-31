from PySide2.QtGui import QWindow
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QPushButton
from PySide2 import QtCore
import sys
from ui.mainwindow import Ui_MainWindow
from cylinderwindow import CylinderWindow
from spherewindow import SphereWindow
from ui.cyldialog import Ui_cyldialog
from ui.sphdialog import Ui_sphdialog


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.cylinderdialog = QDialog()
        self.spheredialog = QDialog()

        self.cylinderdialog.ui = CylinderDialog()
        self.cylinderdialog.ui.setupUi(self.cylinderdialog)

        self.spheredialog.ui = SphereDialog()
        self.spheredialog.ui.setupUi(self.spheredialog)

        self.cylindersbutton.clicked.connect(self.cylinderdialog.show)
        self.spheres.clicked.connect(self.spheredialog.show)


class CylinderDialog(Ui_cyldialog):
    def __init__(self):
        super().__init__()
        self.window = CylinderWindow()

    def setupUi(self, CylinderDialog):
        super().setupUi(CylinderDialog)
        self.horizontalLayout.replaceWidget(
            self.widget, QWidget.createWindowContainer(self.window)
        )


class SphereDialog(Ui_sphdialog):
    def __init__(self):
        super().__init__()
        self.window = SphereWindow()

    def setupUi(self, SphereDialog):
        super().setupUi(SphereDialog)
        self.horizontalLayout.replaceWidget(
            self.widget, QWidget.createWindowContainer(self.window)
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    window = QMainWindow()
    ui = MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
