# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_per.ui'
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
        Dialog.resize(495, 259)
        self.cSave = QtGui.QPushButton(Dialog)
        self.cSave.setGeometry(QtCore.QRect(405, 78, 75, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.cSave.setFont(font)
        self.cSave.setObjectName(_fromUtf8("cSave"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 38, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.cName = QtGui.QLineEdit(Dialog)
        self.cName.setGeometry(QtCore.QRect(54, 10, 151, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.cName.setFont(font)
        self.cName.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.cName.setObjectName(_fromUtf8("cName"))
        self.cPhone = QtGui.QLineEdit(Dialog)
        self.cPhone.setGeometry(QtCore.QRect(316, 10, 166, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.cPhone.setFont(font)
        self.cPhone.setObjectName(_fromUtf8("cPhone"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 10, 57, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 44, 38, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.cAdress = QtGui.QComboBox(Dialog)
        self.cAdress.setGeometry(QtCore.QRect(54, 44, 151, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.cAdress.setFont(font)
        self.cAdress.setEditable(True)
        self.cAdress.setObjectName(_fromUtf8("cAdress"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 78, 38, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.cDate = QtGui.QDateEdit(Dialog)
        self.cDate.setGeometry(QtCore.QRect(54, 79, 121, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.cDate.setFont(font)
        self.cDate.setObjectName(_fromUtf8("cDate"))
        self.cText = QtGui.QTextEdit(Dialog)
        self.cText.setGeometry(QtCore.QRect(10, 114, 466, 134))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.cText.setFont(font)
        self.cText.setObjectName(_fromUtf8("cText"))
        self.cOnLine = QtGui.QCheckBox(Dialog)
        self.cOnLine.setGeometry(QtCore.QRect(230, 45, 80, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.cOnLine.setFont(font)
        self.cOnLine.setObjectName(_fromUtf8("cOnLine"))
        self.cCancel = QtGui.QPushButton(Dialog)
        self.cCancel.setGeometry(QtCore.QRect(316, 78, 75, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.cCancel.setFont(font)
        self.cCancel.setObjectName(_fromUtf8("cCancel"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.cCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QObject.connect(self.cSave, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.slotSave)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.cName, self.cPhone)
        Dialog.setTabOrder(self.cPhone, self.cAdress)
        Dialog.setTabOrder(self.cAdress, self.cText)
        Dialog.setTabOrder(self.cText, self.cSave)
        Dialog.setTabOrder(self.cSave, self.cDate)
        Dialog.setTabOrder(self.cDate, self.cOnLine)
        Dialog.setTabOrder(self.cOnLine, self.cCancel)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.cSave.setText(_translate("Dialog", "保存", None))
        self.label.setText(_translate("Dialog", "姓名", None))
        self.label_2.setText(_translate("Dialog", "手机号", None))
        self.label_3.setText(_translate("Dialog", "地址", None))
        self.label_4.setText(_translate("Dialog", "日期", None))
        self.cOnLine.setText(_translate("Dialog", "不在线", None))
        self.cCancel.setText(_translate("Dialog", "取消", None))

