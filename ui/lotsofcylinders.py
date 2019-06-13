# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lotsofcylinders.ui',
# licensing of 'lotsofcylinders.ui' applies.
#
# Created: Thu Jun 13 12:30:19 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1031, 780)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 26, 141, 74))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.ringslineedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.ringslineedit.setObjectName("ringslineedit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ringslineedit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.sliceslineedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.sliceslineedit.setObjectName("sliceslineedit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sliceslineedit)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Dialog", "rings and slices", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "rings", None, -1))
        self.ringslineedit.setText(QtWidgets.QApplication.translate("Dialog", "10", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "slices", None, -1))
        self.sliceslineedit.setText(QtWidgets.QApplication.translate("Dialog", "10", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Dialog", "Add lots of cylinders", None, -1))

