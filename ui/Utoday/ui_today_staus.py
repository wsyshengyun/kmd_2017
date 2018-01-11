# -*- coding:utf8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
# sys.path.append('..')
from foo import modlevj

QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))

class TodayStatusUi(QWidget):
    """docstring for TodayStatusUi."""
    def __init__(self, pos=None, arg=None):
        super(TodayStatusUi, self).__init__()
        self.arg = arg
        self.resize(400, 500)
        if pos:
            self.move(pos)
        vlayout = QVBoxLayout()
        hlay = QHBoxLayout()
        self.setLayout(vlayout)
        vlayout.addLayout(hlay)


        # control
        self.lab2 = QLabel(self.tr('类型'))
        self.lab_dis = QLabel('#')
        self.comb_ty = QComboBox()
        self._initCombty()
        self.csure = QPushButton(self.tr('确定'))
        self.table = QTableWidget()
        self.header = [u'日期', u'收货(个)', u'发货(个)',  u'工费']
        self._init_table()


        hlay.addWidget(self.lab2)
        hlay.addWidget(self.comb_ty)
        hlay.addWidget(self.csure)
        hlay.addStretch(1)
        hlay.addWidget(self.lab_dis)

        vlayout.addWidget(self.table)

        self.csure.clicked.connect(self.slot_btn_clicked)
        # self.comb_ty.currentIndexChanged.connect(self.slot_comboTy_changed)

        # connect
        self.table.itemSelectionChanged.connect(self.slot_table_itemSelectChanged)

        # 数据

        self.tmdData = modlevj.TMYData()
        self.dit = self.tmdData.getDaysData()

        # 确定一次
        self.slot_btn_clicked()


    def _initCombty(self):
        tysList = modlevj.many_huos.tys
        word = QStringList()
        for i in tysList[::-1]:
            word<<self.tr(i)
        self.comb_ty.addItems(word)

    def _init_table(self):
        self.table.clear()
        # self.table.setFrameShape(QFrame.NoFrame)  #无边框
        # self.table.setShowGrid(False) #设置不显示格子线
        # self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置选择行为时每次选择一行
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置不可编辑
        # self.table.setSelectionMode(QTableWidget.SingleSelection)  # 只能选择一行

        self.table.verticalHeader().setVisible(False)  # 垂直表头不可见
        # self.table.horizontalHeader().setVisible(False)  # 水平表头不可见
        # self.table.horizontalHeader().setFixedHeight(25) # 设表头高度
        self.table.verticalHeader().setDefaultSectionSize(25)  # 设置行距
        self.table.horizontalHeader().setStretchLastSection(True)  # 设置充满表宽度

        self.table.setColumnCount(len(self.header))
        qstr = QStringList([QString(i) for i in self.header])
        self.table.setHorizontalHeaderLabels(qstr)
        # self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)
        self.table.setFont(QFont(self.tr('微软雅黑'), 10))

    def _table_insert_data(self, datas):
        ilen = len(datas)
        if not ilen: return
        else:
            self.table.setRowCount(ilen)
            for irow in range(ilen):
                for icol in range(len(datas[0])):
                    data = datas[irow][icol]
                    qtext_data = QString(unicode(data))
                    item = QTableWidgetItem(qtext_data)
                    self.table.setItem(irow, icol, item)

    def slot_btn_clicked(self):
        ty = self.comb_ty.currentText()
        ty = unicode(ty)
        lit = self.tmdData.format_dit(self.dit, ty)
        self._table_insert_data(lit)
    #
    # def slot_comboTy_changed(self, index):
    #
    #     pass

    def slot_table_itemSelectChanged(self):
        listitems = self.table.selectedItems()
        val = 0.0
        for item in listitems:
            try:
                if item:
                    val += float(item.text())
            except ValueError:
                break
        ilen = len(listitems)
        tsl = [str(ilen), ' - ', str(int(val))]
        self.lab_dis.setText(''.join(tsl))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dia = TodayStatusUi()
    dia.show()
    sys.exit(app.exec_())
