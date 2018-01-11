# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_set.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(414, 303)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 75, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.cstart_date = QtGui.QDateEdit(Dialog)
        self.cstart_date.setGeometry(QtCore.QRect(135, 60, 110, 22))
        self.cstart_date.setObjectName(_fromUtf8("cstart_date"))
        self.cend_date = QtGui.QDateEdit(Dialog)
        self.cend_date.setGeometry(QtCore.QRect(135, 105, 110, 22))
        self.cend_date.setObjectName(_fromUtf8("cend_date"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 105, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(15, 15, 271, 166))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(285, 225, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox.raise_()
        self.label.raise_()
        self.cstart_date.raise_()
        self.cend_date.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.slot_sure_clicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "开始日期", None))
        self.label_2.setText(_translate("Dialog", "终止日期", None))
        self.groupBox.setTitle(_translate("Dialog", "日期设置", None))
        self.pushButton.setText(_translate("Dialog", "确定", None))

