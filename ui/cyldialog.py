# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cyldialog.ui',
# licensing of 'cyldialog.ui' applies.
#
# Created: Fri May 31 14:34:42 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_cyldialog(object):
    def setupUi(self, cyldialog):
        cyldialog.setObjectName("cyldialog")
        cyldialog.resize(976, 581)
        self.horizontalLayout = QtWidgets.QHBoxLayout(cyldialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(cyldialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.groupBox = QtWidgets.QGroupBox(cyldialog)
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
        self.radiusLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.radiusLineEdit.setObjectName("radiusLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.radiusLineEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lengthLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lengthLineEdit.setObjectName("lengthLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lengthLineEdit)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.xLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.xLineEdit.setObjectName("xLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.xLineEdit)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.yLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.yLineEdit.setObjectName("yLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.yLineEdit)
        self.zLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.zLineEdit.setObjectName("zLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.zLineEdit)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(cyldialog)
        QtCore.QMetaObject.connectSlotsByName(cyldialog)

    def retranslateUi(self, cyldialog):
        cyldialog.setWindowTitle(QtWidgets.QApplication.translate("cyldialog", "Qt3D examples - Cylinders", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("cyldialog", "Geometry", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("cyldialog", "Radius", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("cyldialog", "Length", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("cyldialog", "add cylinder", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("cyldialog", "X", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("cyldialog", "Y", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("cyldialog", "Z", None, -1))

