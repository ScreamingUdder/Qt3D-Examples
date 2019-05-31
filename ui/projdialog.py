# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projdialog.ui',
# licensing of 'projdialog.ui' applies.
#
# Created: Fri May 31 11:53:13 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_projdialog(object):
    def setupUi(self, projdialog):
        projdialog.setObjectName("projdialog")
        projdialog.resize(400, 300)

        self.retranslateUi(projdialog)
        QtCore.QMetaObject.connectSlotsByName(projdialog)

    def retranslateUi(self, projdialog):
        projdialog.setWindowTitle(QtWidgets.QApplication.translate("projdialog", "Qt3D examples - 2D projection", None, -1))

