# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lotsofspheres.ui',
# licensing of 'lotsofspheres.ui' applies.
#
# Created: Fri May 31 15:44:38 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_LotsOfSpheresDialog(object):
    def setupUi(self, LotsOfSpheresDialog):
        LotsOfSpheresDialog.setObjectName("LotsOfSpheresDialog")
        LotsOfSpheresDialog.resize(936, 680)
        self.horizontalLayout = QtWidgets.QHBoxLayout(LotsOfSpheresDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(LotsOfSpheresDialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.pushButton = QtWidgets.QPushButton(LotsOfSpheresDialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(LotsOfSpheresDialog)
        QtCore.QMetaObject.connectSlotsByName(LotsOfSpheresDialog)

    def retranslateUi(self, LotsOfSpheresDialog):
        LotsOfSpheresDialog.setWindowTitle(QtWidgets.QApplication.translate("LotsOfSpheresDialog", "0", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("LotsOfSpheresDialog", "Add lots of spheres", None, -1))

