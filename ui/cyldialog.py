# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cyldialog.ui',
# licensing of 'cyldialog.ui' applies.
#
# Created: Fri May 31 11:54:13 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_cyldialog(object):
    def setupUi(self, cyldialog):
        cyldialog.setObjectName("cyldialog")
        cyldialog.resize(400, 300)

        self.retranslateUi(cyldialog)
        QtCore.QMetaObject.connectSlotsByName(cyldialog)

    def retranslateUi(self, cyldialog):
        cyldialog.setWindowTitle(QtWidgets.QApplication.translate("cyldialog", "Qt3D examples - Cylinders", None, -1))

