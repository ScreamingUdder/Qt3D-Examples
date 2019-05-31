# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sphdialog.ui',
# licensing of 'sphdialog.ui' applies.
#
# Created: Fri May 31 12:46:51 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_sphdialog(object):
    def setupUi(self, sphdialog):
        sphdialog.setObjectName("sphdialog")
        sphdialog.resize(426, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(sphdialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(sphdialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.pushButton = QtWidgets.QPushButton(sphdialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(sphdialog)
        QtCore.QMetaObject.connectSlotsByName(sphdialog)

    def retranslateUi(self, sphdialog):
        sphdialog.setWindowTitle(QtWidgets.QApplication.translate("sphdialog", "Qt3D examples - Spheres", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("sphdialog", "add sphere", None, -1))

