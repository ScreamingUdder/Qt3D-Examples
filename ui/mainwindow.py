# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Fri May 31 15:20:03 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(583, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cylindersbutton = QtWidgets.QPushButton(self.centralwidget)
        self.cylindersbutton.setObjectName("cylindersbutton")
        self.verticalLayout.addWidget(self.cylindersbutton)
        self.lotsofcylindersbutton = QtWidgets.QPushButton(self.centralwidget)
        self.lotsofcylindersbutton.setObjectName("lotsofcylindersbutton")
        self.verticalLayout.addWidget(self.lotsofcylindersbutton)
        self.spheres = QtWidgets.QPushButton(self.centralwidget)
        self.spheres.setObjectName("spheres")
        self.verticalLayout.addWidget(self.spheres)
        self.lotsofspheresButton = QtWidgets.QPushButton(self.centralwidget)
        self.lotsofspheresButton.setObjectName("lotsofspheresButton")
        self.verticalLayout.addWidget(self.lotsofspheresButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 583, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Qt3D examples", None, -1))
        self.cylindersbutton.setText(QtWidgets.QApplication.translate("MainWindow", "Cylinders", None, -1))
        self.lotsofcylindersbutton.setText(QtWidgets.QApplication.translate("MainWindow", "Lots of cylinders", None, -1))
        self.spheres.setText(QtWidgets.QApplication.translate("MainWindow", "Spheres", None, -1))
        self.lotsofspheresButton.setText(QtWidgets.QApplication.translate("MainWindow", "Lots of spheres", None, -1))

