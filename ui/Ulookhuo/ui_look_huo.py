# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_look_huo.ui'
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
        Dialog.resize(824, 510)
        self.ctable = QtGui.QTableWidget(Dialog)
        self.ctable.setGeometry(QtCore.QRect(15, 15, 721, 481))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        self.ctable.setFont(font)
        self.ctable.setObjectName(_fromUtf8("ctable"))
        self.ctable.setColumnCount(0)
        self.ctable.setRowCount(0)
        self.csure_config = QtGui.QPushButton(Dialog)
        self.csure_config.setGeometry(QtCore.QRect(745, 15, 70, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        self.csure_config.setFont(font)
        self.csure_config.setObjectName(_fromUtf8("csure_config"))
        self.cbtn_default = QtGui.QPushButton(Dialog)
        self.cbtn_default.setGeometry(QtCore.QRect(745, 105, 70, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        self.cbtn_default.setFont(font)
        self.cbtn_default.setObjectName(_fromUtf8("cbtn_default"))
        self.cbtn_del_huo = QtGui.QPushButton(Dialog)
        self.cbtn_del_huo.setGeometry(QtCore.QRect(745, 60, 70, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        self.cbtn_del_huo.setFont(font)
        self.cbtn_del_huo.setObjectName(_fromUtf8("cbtn_del_huo"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.csure_config, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.btn_clicked)
        QtCore.QObject.connect(self.cbtn_default, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.btn_clicked)
        QtCore.QObject.connect(self.cbtn_del_huo, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.btn_clicked)
        QtCore.QObject.connect(self.ctable, QtCore.SIGNAL(_fromUtf8("cellClicked(int,int)")), Dialog.slot_cell_clicked)
        QtCore.QObject.connect(self.ctable, QtCore.SIGNAL(_fromUtf8("cellChanged(int,int)")), Dialog.slot_cell_changed)
        QtCore.QObject.connect(self.ctable, QtCore.SIGNAL(_fromUtf8("cellActivated(int,int)")), Dialog.slot_cell_active)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.csure_config.setText(_translate("Dialog", "修改货物", None))
        self.cbtn_default.setText(_translate("Dialog", "恢复", None))
        self.cbtn_del_huo.setText(_translate("Dialog", "删除货物", None))

