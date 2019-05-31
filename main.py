from PySide2.QtGui import QWindow
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QPushButton
from PySide2 import QtCore
import sys
from ui.mainwindow import Ui_MainWindow
from cylinderwindow import CylinderWindow
from spherewindow import SphereWindow
from ui.cyldialog import Ui_cyldialog
from ui.sphdialog import Ui_sphdialog
from ui.lotsofspheres import Ui_LotsOfSpheresDialog
from ui.lotsofcylinders import Ui_Dialog


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.cylinderdialog = QDialog()
        self.spheredialog = QDialog()
        self.lotsofcylindersdialog = QDialog()
        self.lotsofspheresdialog = QDialog()

        self.cylinderdialog.ui = CylinderDialog()
        self.cylinderdialog.ui.setupUi(self.cylinderdialog)

        self.lotsofcylindersdialog.ui = LotsOfCylindersDialog()
        self.lotsofcylindersdialog.ui.setupUi(self.lotsofcylindersdialog)

        self.spheredialog.ui = SphereDialog()
        self.spheredialog.ui.setupUi(self.spheredialog)

        self.lotsofspheresdialog.ui = LotsOfSpheresDialog()
        self.lotsofspheresdialog.ui.setupUi(self.lotsofspheresdialog)

        self.cylindersbutton.clicked.connect(self.cylinderdialog.show)
        self.spheres.clicked.connect(self.spheredialog.show)
        self.lotsofcylindersbutton.clicked.connect(self.lotsofcylindersdialog.show)
        self.lotsofspheresButton.clicked.connect(self.lotsofspheresdialog.show)


class CylinderDialog(Ui_cyldialog):
    def __init__(self):
        super().__init__()
        self.window = CylinderWindow()

    def setupUi(self, CylinderDialog):
        super().setupUi(CylinderDialog)
        self.horizontalLayout.replaceWidget(
            self.widget, QWidget.createWindowContainer(self.window)
        )
        self.pushButton.clicked.connect(self.add_cylinder)

    def add_cylinder(self):
        self.window.add_cylinder(
            int(self.radiusLineEdit.text()),
            int(self.radiusLineEdit.text()),
            int(self.xLineEdit.text()),
            int(self.yLineEdit.text()),
            int(self.zLineEdit.text()),
        )
        print("Cylinder added.")


class SphereDialog(Ui_sphdialog):
    def __init__(self):
        super().__init__()
        self.window = SphereWindow()

    def setupUi(self, SphereDialog):
        super().setupUi(SphereDialog)
        self.horizontalLayout.replaceWidget(
            self.widget, QWidget.createWindowContainer(self.window)
        )
        self.pushButton.clicked.connect(self.add_sphere)

    def add_sphere(self):

        self.window.add_sphere(
            int(self.radiusLineEdit.text()),
            int(self.xLineEdit.text()),
            int(self.yLineEdit.text()),
            int(self.zLineEdit.text()),
        )


class LotsOfCylindersDialog(Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.window = CylinderWindow()

    def setupUi(self, CylinderDialog):
        super().setupUi(CylinderDialog)
        self.horizontalLayout.replaceWidget(
            self.widget, QWidget.createWindowContainer(self.window)
        )
        self.pushButton.clicked.connect(self.add_cylinder)

    def add_cylinder(self):
        x = 20
        y = 256

        radius = 0.5
        length = 0.5
        translation_distance = 1

        for i in range(x):
            for j in range(y):
                self.window.add_cylinder(
                    radius,
                    length,
                    i * translation_distance * 2,
                    j * translation_distance,
                    0,
                )

        # self.window.add_cylinder()
        print("Cylinder added.")


class LotsOfSpheresDialog(Ui_LotsOfSpheresDialog):
    def __init__(self):
        super().__init__()
        self.window = SphereWindow()

    def setupUi(self, LotsOfSpheresDialog):
        super().setupUi(LotsOfSpheresDialog)
        self.horizontalLayout.replaceWidget(
            self.widget, QWidget.createWindowContainer(self.window)
        )
        self.pushButton.clicked.connect(self.add_spheres)

    def add_spheres(self):
        x = 64
        y = 256

        radius = 0.5
        translation_distance = 1

        for i in range(x):
            for j in range(y):
                self.window.add_sphere(
                    radius, i * translation_distance * 2, j * translation_distance, 0
                )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    window = QMainWindow()
    ui = MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
