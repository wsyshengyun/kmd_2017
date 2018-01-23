# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_look_per.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import *
from PyQt4.QtCore import *

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)
HEIGHT_COMBO = 26
FONT = QFont(u'微软雅黑', 10)
FONT_TABLE = QFont(u'微软雅黑', 9)
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.resize(500, 500)
        self.cbox_adr = QComboBox(Dialog)
        self.label = QLabel(Dialog)
        self.label_2 = QLabel(Dialog)
        self.cbox_line = QComboBox(Dialog)
        self.cbox_ty = QComboBox(Dialog)
        self.label_3 = QLabel(Dialog)
        self.cnum = QLabel(Dialog)
        self.csure = QPushButton(Dialog)
        self.ct_view = QTableWidget(Dialog)
        self.ct_view.setColumnCount(0)
        self.ct_view.setRowCount(0)
        self.cfilter = QLineEdit(Dialog)
        self.label_4 = QLabel(Dialog)

        # width, font
        ctr_tup = self.cbox_ty, self.cbox_line, self.cbox_adr, self.csure, \
                self.cfilter, self.label, self.label_2, self.label_3, self.label_4 \
                ,self.cnum

        for i in ctr_tup:
            i.setMinimumHeight(HEIGHT_COMBO)
            i.setFont(FONT)
        self.ct_view.setFont(FONT_TABLE)

        # lay
        grid = QGridLayout()
        self.setLayout(grid)
        grid.setHorizontalSpacing(5)
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setColumnStretch(2, 1)
        grid.setColumnStretch(3, 1)
        grid.setColumnStretch(4, 1)
        grid.addWidget(self.label, 0, 0, 1, 1, Qt.AlignCenter)
        grid.addWidget(self.label_2, 0, 1, 1, 1, Qt.AlignCenter)
        grid.addWidget(self.label_3, 0, 2, 1, 1, Qt.AlignCenter)
        grid.addWidget(self.label_4, 0, 3, 1, 1, Qt.AlignCenter)
        grid.addWidget(self.cnum, 0, 4, 1, 1, Qt.AlignCenter)
        grid.addWidget(self.cbox_adr, 1, 0)
        grid.addWidget(self.cbox_line, 1, 1)
        grid.addWidget(self.cbox_ty, 1, 2)
        grid.addWidget(self.cfilter, 1, 3)
        grid.addWidget(self.csure, 1, 4)
        grid.addWidget(self.ct_view, 2, 0, 1, 5)



        self.retranslateUi(Dialog)
        QObject.connect(self.ct_view, SIGNAL(_fromUtf8("cellChanged(int,int)")), Dialog.slot_cell_changed)
        QObject.connect(self.csure, SIGNAL(_fromUtf8("clicked()")), Dialog.slot_sure)
        QObject.connect(self.cbox_ty, SIGNAL(_fromUtf8("currentIndexChanged(QString)")), Dialog.slot_box_changed)
        QObject.connect(self.cbox_line, SIGNAL(_fromUtf8("currentIndexChanged(QString)")), Dialog.slot_box_changed)
        QObject.connect(self.cbox_adr, SIGNAL(_fromUtf8("currentIndexChanged(QString)")), Dialog.slot_box_changed)
        QObject.connect(self.ct_view, SIGNAL(_fromUtf8("cellDoubleClicked(int,int)")), Dialog.slot_cell_double_clicked)
        QObject.connect(self.cfilter, SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.slot_edit_text_changed)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "地址", None))
        self.label_2.setText(_translate("Dialog", "在线", None))
        self.label_3.setText(_translate("Dialog", "类型", None))
        self.cnum.setText(_translate("Dialog", "-", None))
        self.csure.setText(_translate("Dialog", "确定", None))
        self.label_4.setText(_translate("Dialog", "过滤", None))
