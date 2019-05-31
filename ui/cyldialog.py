# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cyldialog.ui',
# licensing of 'cyldialog.ui' applies.
#
# Created: Fri May 31 12:46:52 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_cyldialog(object):
    def setupUi(self, cyldialog):
        cyldialog.setObjectName("cyldialog")
        cyldialog.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(cyldialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(cyldialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.pushButton = QtWidgets.QPushButton(cyldialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(cyldialog)
        QtCore.QMetaObject.connectSlotsByName(cyldialog)

    def retranslateUi(self, cyldialog):
        cyldialog.setWindowTitle(QtWidgets.QApplication.translate("cyldialog", "Qt3D examples - Cylinders", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("cyldialog", "add cylinder", None, -1))

