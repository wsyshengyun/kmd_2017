# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

# from PyQt4.QtGui import *
# from PyQt4.QtCore import *
from middle_control import *
from myedit import AutoCompleteEdit

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
HEIGHT_FINDNAME = 28
HEIGHT_NAME_DISPLAY = 30
HEIGHT_BTN = 25
HEIGHT_COMMON = 25
FONT_DISNAME = QFont(u'微软雅黑', 20)
FONT_INPUT = QFont(u'黑体', 10)
FONT_LA = QFont(u'黑体', 10, QFont.Bold)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.resize(500, 500)
        self.move(0, 0)
        Dialog.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint |
            Qt.CustomizeWindowHint)
        # self.findName = QLineEdit(Dialog)
        self.findName = AutoCompleteEdit(Dialog)
        self.findName.setMinimumHeight(HEIGHT_FINDNAME)
        self.findName.setText(_fromUtf8(""))
        self.findName.setFont(FONT_INPUT)
        self.ccheck_find_allNames = QCheckBox(u'全部')
        self.ccheck_find_allNames.setMinimumHeight(HEIGHT_FINDNAME)
        self.cevTable = QTableWidget(Dialog)
        self.cevTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.cevTable.setFrameShape(QFrame.WinPanel)
        self.cevTable.setColumnCount(0)
        self.cevTable.setRowCount(0)
        self.findBtn = QPushButton(Dialog)
        self.modPerBtn = QPushButton(Dialog)
        self.disNameLab = QLabel(Dialog)
        self.disNameLab.setFont(FONT_DISNAME)
        self.disNameLab.setMinimumHeight(HEIGHT_NAME_DISPLAY)
        # self.disNameLab.setEnabled(True)
        # self.disNameLab.setAutoFillBackground(False)
        # self.disNameLab.setFrameShape(QFrame.Box)  # 带边框
        # self.disNameLab.setFrameShadow(QFrame.Plain)
        # self.disNameLab.setLineWidth(0)
        # self.disNameLab.setMidLineWidth(0)
        self.disNameLab.setAlignment(Qt.AlignTop)

        self.newPerBtn = QPushButton(Dialog)
        self.cAddev = QPushButton(Dialog)
        self.chuobox = QComboBox(Dialog)
        self.cdate = MDateEdit(Dialog)
        self.cdate.setContextMenuPolicy(Qt.CustomContextMenu)
        self.cdate.setAutoFillBackground(False)
        self.cdate.setCurrentSection(QDateTimeEdit.DaySection)
        self.cdate.setCalendarPopup(True)
        self.cownTable = QTableWidget(Dialog)
        self.cownTable.setEnabled(True)
        self.cownTable.setAutoFillBackground(False)
        self.cownTable.setFrameShape(QFrame.Box)
        self.cownTable.setFrameShadow(QFrame.Plain)
        self.cownTable.setMidLineWidth(0)
        self.cownTable.setAlternatingRowColors(True)
        self.cownTable.setRowCount(0)
        self.cownTable.setColumnCount(0)
        self.nameListWidget = QListWidget(Dialog)
        # width
        # self.nameListWidget.setMaximumWidth(60)
        self.cnew_h = QPushButton(Dialog)
        self.cset = QPushButton(Dialog)
        self.csort = QPushButton(Dialog)
        self.clook_h = QPushButton(Dialog)
        self.clook_per = QPushButton(Dialog)
        self.cook_sun = QPushButton(Dialog)
        self.cdatedata = QLabel(Dialog)
        self.cdatedata.setText(_fromUtf8(""))
        self.ctodoBtn = QPushButton(Dialog)
        # cdatedata
        self.cdatedata.setFrameShape(QFrame.Panel)
        self.cdatedata.setFrameShadow(QFrame.Sunken)
        self.cdatedata.setMinimumHeight(HEIGHT_COMMON)
        self.cdatedata.setFont(FONT_INPUT)

        self.cla_own = QLabel(Dialog)
        # self.cob_name = QComboBox(Dialog)
        self.retranslateUi(Dialog)

        self.ctodayData = QPushButton(u'每天')

        # HEIGHT
        self.cdate.setMinimumHeight(HEIGHT_BTN)
        self.chuobox.setMinimumHeight(HEIGHT_BTN)
        self.cAddev.setMinimumHeight(HEIGHT_BTN)
        self.cook_sun.setMinimumHeight(HEIGHT_BTN)
        self.cla_own.setMinimumHeight(HEIGHT_BTN)

        # FONT
        self.cla_own.setFont(FONT_LA)

        # ------------------------
        vlayout = QVBoxLayout()
        self.setLayout(vlayout)
        grid1 = QGridLayout()
        h1 = QHBoxLayout()
        h_btn = QHBoxLayout()
        h_di = QHBoxLayout()

        vlayout.addLayout(grid1)
        vlayout.addLayout(h_btn)
        vlayout.addLayout(h_di)

        # 上层
        grid1.setHorizontalSpacing(10) # 设置水平间距
        grid1.setVerticalSpacing(10)  # 设置垂直间距
        grid1.setColumnMinimumWidth(0, 60)
        grid1.setContentsMargins(1, 1, 1, 1) # 设置外间距
        grid1.setColumnStretch(0, 1)
        grid1.setColumnStretch(1, 1)
        grid1.setColumnStretch(2, 1)
        grid1.setColumnStretch(3, 1)
        grid1.setColumnStretch(4, 1)
        grid1.setColumnStretch(5, 4)
        grid1.addWidget(self.disNameLab, 0, 0, 2, 2)
        grid1.addWidget(self.findName, 0, 2, 1, 2)
        grid1.addWidget(self.ccheck_find_allNames, 0, 4, 1, 1)
        grid1.addWidget(self.cdate, 1, 0)
        grid1.addWidget(self.chuobox,       1, 1, 1, 1)
        grid1.addWidget(self.cook_sun,      1, 2, 1, 1)
        grid1.addWidget(self.cAddev,        1, 3, 1, 1)
        grid1.addWidget(self.cla_own,       1, 4, 1, 1, Qt.AlignCenter)
        grid1.addWidget(self.cownTable,     0, 5, 2, 1)
        grid1.addWidget(self.nameListWidget, 2,0)
        grid1.addWidget(self.cevTable,2,1,2,5)



        # 按钮 横层
        h_btn.addWidget(self.newPerBtn)
        h_btn.addWidget(self.modPerBtn)
        h_btn.addWidget(self.cnew_h)
        h_btn.addWidget(self.cset)
        h_btn.addWidget(self.clook_h)
        h_btn.addWidget(self.clook_per)
        h_btn.addWidget(self.csort)
        h_btn.addWidget(self.ctodayData)
        h_btn.addWidget(self.ctodoBtn)

        # 最后一 横层
        h_di.addWidget(self.cdatedata)


        # ------------------------
        QObject.connect(self.newPerBtn, SIGNAL(_fromUtf8("clicked()")), Dialog.slot_new_per)
        QObject.connect(self.modPerBtn, SIGNAL(_fromUtf8("clicked()")), Dialog.slot_modPer)
        QObject.connect(self.findBtn, SIGNAL(_fromUtf8("clicked()")), Dialog.slot_find_name)
        QObject.connect(self.cAddev, SIGNAL(_fromUtf8("clicked()")), Dialog.slot_add_ev)
        QObject.connect(self.chuobox, SIGNAL(_fromUtf8("activated(QString)")), Dialog.slot_huoBox_changed)
        QObject.connect(self.cdate, SIGNAL(_fromUtf8("editingFinished()")), Dialog.slot_date_finished)
        QObject.connect(self.nameListWidget, SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), Dialog.slot_nameList_doubleClicked)
        QObject.connect(self.nameListWidget, SIGNAL(_fromUtf8("currentTextChanged(QString)")), Dialog.slot_nameList_currText_changed)
        QObject.connect(self.cook_sun, SIGNAL(_fromUtf8("clicked()")), Dialog.slot_sun_clicked)
        QObject.connect(self.clook_h, SIGNAL(_fromUtf8("clicked()")), Dialog.slot_btn_clicked)
        QObject.connect(self.clook_per, SIGNAL(_fromUtf8("clicked()")), Dialog.slot_btn_clicked)
        QObject.connect(self.ctodoBtn, SIGNAL(_fromUtf8("clicked()")), Dialog.slot_btn_clicked)
        QObject.connect(self.csort, SIGNAL(_fromUtf8("clicked()")), Dialog.slot_btn_clicked)
        QObject.connect(self.cset, SIGNAL(_fromUtf8("clicked()")), Dialog.slot_btn_clicked)
        QObject.connect(self.ctodayData, SIGNAL(_fromUtf8("clicked()")), Dialog.slot_btn_clicked)
        QObject.connect(self.cnew_h, SIGNAL(_fromUtf8("clicked()")), Dialog.slot_btn_clicked)
        QObject.connect(self.cevTable, SIGNAL(_fromUtf8("cellDoubleClicked(int,int)")), Dialog.slot_cell_double_clicked)
        QObject.connect(self.cdate, SIGNAL(_fromUtf8("dateChanged(QDate)")), Dialog.slot_date_changed)
        QObject.connect(self.cevTable, SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), Dialog.slot_mytable_context)
        QObject.connect(self.cownTable, SIGNAL(_fromUtf8("cellDoubleClicked(int, int)")), Dialog.slot_cownTable_DoubleClicked)
        # QObject.connect(self.cownTable, SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), Dialog.slot_mytable_context)
        QObject.connect(self.cdate, SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), Dialog.slot_mytable_context)
        QObject.connect(self.cevTable, SIGNAL(_fromUtf8("cellClicked(int,int)")), Dialog.slot_cell_clicked)
        QMetaObject.connectSlotsByName(Dialog)


    def _init_table(self):
        self.cevTable.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.cevTable.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.findBtn.setText(_translate("Dialog", "查找姓名", None))
        self.modPerBtn.setText(_translate("Dialog", "修改人物", None))
        self.disNameLab.setText(_translate("Dialog", " ...", None))
        self.newPerBtn.setText(_translate("Dialog", "新建人物", None))
        self.cAddev.setText(_translate("Dialog", "添加事件", None))
        self.cnew_h.setText(_translate("Dialog", "新建货物", None))
        self.cset.setText(_translate("Dialog", "设置", None))
        self.csort.setText(_translate("Dialog", "排序", None))
        self.clook_h.setText(_translate("Dialog", "查看货物", None))
        self.clook_per.setText(_translate("Dialog", "查看人物", None))
        self.cook_sun.setText(_translate("Dialog", "个人损耗", None))
        self.cla_own.setText(_translate("Dialog", "-", None))
        self.ctodoBtn.setText(_translate("Dialog", '待办', None))
