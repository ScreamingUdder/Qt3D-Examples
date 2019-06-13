# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sphdialog.ui',
# licensing of 'sphdialog.ui' applies.
#
# Created: Thu Jun 13 12:44:54 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_sphdialog(object):
    def setupUi(self, sphdialog):
        sphdialog.setObjectName("sphdialog")
        sphdialog.resize(866, 607)
        self.horizontalLayout = QtWidgets.QHBoxLayout(sphdialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(sphdialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.groupBox = QtWidgets.QGroupBox(sphdialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.radiusLineEdit = QtWidgets.QSpinBox(self.groupBox)
        self.radiusLineEdit.setObjectName("radiusLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.radiusLineEdit)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.xLineEdit = QtWidgets.QSpinBox(self.groupBox)
        self.xLineEdit.setObjectName("xLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.xLineEdit)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.yLineEdit = QtWidgets.QSpinBox(self.groupBox)
        self.yLineEdit.setObjectName("yLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.yLineEdit)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.zLineEdit = QtWidgets.QSpinBox(self.groupBox)
        self.zLineEdit.setObjectName("zLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.zLineEdit)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(sphdialog)
        QtCore.QMetaObject.connectSlotsByName(sphdialog)

    def retranslateUi(self, sphdialog):
        sphdialog.setWindowTitle(QtWidgets.QApplication.translate("sphdialog", "Qt3D examples - Spheres", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("sphdialog", "Geometry", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("sphdialog", "Radius", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("sphdialog", "X", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("sphdialog", "Y", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("sphdialog", "Z", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("sphdialog", "add sphere", None, -1))

