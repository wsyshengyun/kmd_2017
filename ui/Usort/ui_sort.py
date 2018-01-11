# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_sort.ui'
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
        Dialog.resize(400, 500)
        self.cradio_ty = QtGui.QRadioButton(Dialog)
        # self.cradio_ty.setGeometry(QtCore.QRect(30, 30, 89, 16))
        self.cradio_ty.setObjectName(_fromUtf8("cradio_ty"))
        self.cradio_id = QtGui.QRadioButton(Dialog)
        # self.cradio_id.setGeometry(QtCore.QRect(30, 60, 89, 16))
        self.cradio_id.setObjectName(_fromUtf8("cradio_id"))
        self.cbox_huo = QtGui.QComboBox(Dialog)
        # self.cbox_huo.setGeometry(QtCore.QRect(120, 60, 69, 22))
        self.cbox_huo.setObjectName(_fromUtf8("cbox_huo"))
        self.csure = QtGui.QPushButton(Dialog)
        # self.csure.setGeometry(QtCore.QRect(300, 60, 75, 23))
        self.csure.setObjectName(_fromUtf8("csure"))
        self.cbox_content = QtGui.QComboBox(Dialog)
        # self.cbox_content.setGeometry(QtCore.QRect(210, 60, 76, 22))
        self.cbox_content.setObjectName(_fromUtf8("cbox_content"))
        # self.label = QtGui.QLabel(Dialog)
        # self.label.setGeometry(QtCore.QRect(135, 45, 54, 12))
        # self.label.setText(_fromUtf8(""))
        # self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(225, 45, 54, 12))
        # self.label_2.setObjectName(_fromUtf8("label_2"))
        # self.ctext = QtGui.QTextEdit(Dialog)
        # self.ctext.setGeometry(QtCore.QRect(30, 120, 541, 331))
        # self.ctext.setObjectName(_fromUtf8("ctext"))

        self.table = QtGui.QTableWidget()
        self.lab_filter = QtGui.QLabel(self.tr('过滤 '))
        self.filterEdit = QtGui.QLineEdit()
        self.lab_calcul = QtGui.QLabel(u'')
        self.lab_calcul.setFont(QtGui.QFont(self.tr('微软雅黑'), 10))
        self.symbolCombo = QtGui.QComboBox()

        hlayout = QtGui.QHBoxLayout()
        hlayout.addWidget(self.lab_filter)
        hlayout.addWidget(self.symbolCombo)
        hlayout.addWidget(self.filterEdit)
        hlayout.addStretch(1)
        hlayout.addWidget(self.lab_calcul)
        word = QtCore.QStringList(['=', '>', '<'])
        self.symbolCombo.addItems(word)


        # sum Layout
        vlayout = QtGui.QVBoxLayout()
        grid = QtGui.QGridLayout()
        self.setLayout(vlayout)
        groupbox = QtGui.QGroupBox(self.tr('排序方法'))
        groupbox.setLayout(grid)
        vlayout.addWidget(groupbox)
        grid.setSpacing(10)
        grid.addWidget(self.cradio_ty, 0, 0)
        grid.addWidget(self.cradio_id, 1, 0)
        grid.addWidget(self.cbox_huo, 1, 1)
        grid.addWidget(self.label_2, 2, 0)
        grid.addWidget(self.cbox_content, 2, 1)
        grid.addWidget(self.csure, 2, 2)

        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.table)



        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.cradio_ty, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.slot_radio_clicked)
        QtCore.QObject.connect(self.cradio_id, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.slot_radio_clicked)
        QtCore.QObject.connect(self.cbox_huo, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), Dialog.slot_huoid_box_changed)
        QtCore.QObject.connect(self.cbox_content, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), Dialog.slot_content_box_changed)
        QtCore.QObject.connect(self.csure, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.slot_sure)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        QtCore.QObject.connect(self.filterEdit, QtCore.SIGNAL('textChanged(QString)'), Dialog.slot_filter)

        self.table_init()

    def table_init(self):
        self.table.clear()
        # 初始化表格
        # self.table.setFrameShape(QFrame.NoFrame)  #无边框
        # self.table.setShowGrid(False) #设置不显示格子线
        # self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置选择行为时每次选择一行
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)  # 设置不可编辑
        # self.table.setSelectionMode(QTableWidget.SingleSelection)  # 只能选择一行

        self.table.verticalHeader().setVisible(False)  # 垂直表头不可见
        # self.table.horizontalHeader().setVisible(False)  # 水平表头不可见
        # self.table.horizontalHeader().setFixedHeight(25) # 设表头高度
        self.table.verticalHeader().setDefaultSectionSize(25)  # 设置行距
        self.table.horizontalHeader().setStretchLastSection(True)  # 设置充满表宽度


    def _clear_lab_calcul(self):
        self.lab_calcul.setText('')



    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.cradio_ty.setText(_translate("Dialog", "按货物类型", None))
        self.cradio_id.setText(_translate("Dialog", "按货物ID", None))
        self.csure.setText(_translate("Dialog", "确定", None))
        self.label_2.setText(_translate("Dialog", "排序内容", None))
