# coding=utf8


import sys
# sys.path.append('..')

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from foo import  gcl

__author__ = 'Administrator'
'''


'''

TABLE_DATE_NUMBER = 8



def convert_obj_to_tsrs(evs):
    lit = []
    for ev in evs:
        lit.append(ev.get_tu())
    return lit




class BaseTable(object):
    headList = []
    widthList = []
    width_payList = []
    sum_width = 0
    @classmethod
    def set_head_list(cls, u_list):
        cls.headList = u_list
    @classmethod
    def set_width_list(cls, int_list):
        cls.widthList = int_list

    @classmethod
    def set_widthPay(cls, pay_list):
        s = sum(pay_list)
        cls.width_payList = [float( i ) / s for i in pay_list]

    @classmethod
    def set_sumWidth(cls, sum_width):
        cls.sum_width = sum_width

    @classmethod
    def set_width_list_from_pay(cls):
        if cls.sum_width and cls.width_payList:
            cls.widthList = [int( cls.sum_width * i ) for i in cls.width_payList]


    def __init__(self, table):
        self.table = table
        self.row = 0
        self.col = 0
        # self.tb_data = {}
        self.hided_rows = []

    def init(self):
        self.set_col()
        self.set_head()
        self.set_sumWidth(self.get_table_fixWidth())
        self.set_width_list_from_pay()
        self.set_width()

    def hide_rows_from_qtsr(self, qtsr):
        tsr = qtsr.__str__()
        for ri in range(self.row):
            rowText =''.join( self.get_row_texts(ri) )
            if tsr not in rowText:
                self.hided_rows.append(ri)
                self.table.hideRow(ri)

    def show_rows(self):
        for ri in self.hided_rows:
            self.table.showRow(ri)
        self.hided_rows = []


    def get_table_fixWidth(self):
        return self.table.contentsRect().width()  # todo 实际宽度?

    def set_col(self, col_fixed=None):
        if None == col_fixed:
            col_fixed = len( self.headList )
        self.table.setColumnCount(col_fixed)
        self.col = col_fixed

    def set_column_some_items_color(self, some_list, col=0, color=Qt.red):
        for ri in range(self.row):
            item = self.table.item(ri, col)
            if int(item.text().__str__()) in some_list:
                item.setTextColor(color)
            else:
                item.setTextColor(Qt.black)

    def set_cell_background_color(self, whatColumn):

        pass


    def set_row(self, rowNum=0):
        if rowNum:
            self.table.setRowCount(rowNum)
            self.row = rowNum

    def set_head(self):
        qstrList = QStringList( [QString(ust) for ust in self.headList] )
        self.table.setHorizontalHeaderLabels(qstrList)

    def clear(self):
        self.table.clear( )

    def get_item_text(self, rowNum, columnNum):
        item = self.table.item(rowNum, columnNum)
        return item.text().__str__()

    def get_row0_text(self, rwoNum):
        return self.get_item_text(rwoNum, 0)

    def get_row_texts(self, rowNum):
        return [ self.get_item_text(rowNum, c) for c in range(self.col)]

    def set_width(self):
        if self.widthList and (len( self.widthList ) < len( self.headList )): return
        for i, w in enumerate( self.widthList ):
            self.table.setColumnWidth(i, w)

    # def get_db_data(self):
    #     for ri in range(self.row):


    def geshi_set(self):
        # 设置格式
        self.table.setFrameShape(QFrame.NoFrame)  #无边框
        # self.table.setShowGrid(False) #设置不显示格子线
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置选择行为时每次选择一行
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置不可编辑
        self.table.setSelectionMode(QTableWidget.SingleSelection)  # 只能选择一行

        self.table.verticalHeader().setVisible(False)  # 垂直表头不可见
        # self.table.horizontalHeader().setVisible(False)  # 水平表头不可见
        # self.table.horizontalHeader().setFixedHeight(25) # 设表头高度
        self.table.verticalHeader().setDefaultSectionSize(25)  # 设置行距
        self.table.horizontalHeader().setStretchLastSection(True)  # 设置充满表宽度

    def gs_horizontalHeaderVisible(self, bol):
            self.table.horizontalHeader().setVisible(bol)  # 水平表头不可见

    def gs_setNoVerticalHeader(self):
        self.table.verticalHeader.setVisible(False)

    def insert_data(self, datas):
        ilen = len(datas)
        if not ilen: return
        else:
            self.clear()
            self.set_head()
            self.row = ilen
            self.table.setRowCount(ilen)
            # for irow in range(self.row):
            for irow in range(len(datas)):
                for icol in range(len(datas[0])):
                    data = datas[irow][icol]
                    qtext_data = QString(unicode(data))
                    item = QTableWidgetItem(qtext_data)
                    self.table.setItem(irow, icol, item)

    def insert_evs(self, evs):
        datas = convert_obj_to_tsrs( evs )
        self.insert_data(datas)

    def insert_pers(self, pers):
        datas = convert_obj_to_tsrs(pers)
        self.insert_data(datas)


    def replace_column_data(self, where_column, objective_list):
        pass


class HuoTable(BaseTable):
    headList = [u'编号', u'类型', u'比率', u'标称数量',
            u'有效', u'带腊', u'日期', u'备注',
            u'发数量', u'未交数量', u'损耗数量']
    # width = [30, 50, 50, 60, 30, 30, 80, 120, 80, 80, 80]

    def __init__(self, table):
        super(HuoTable, self).__init__(table)
        self.init()


    def init(self):

        paynums = [3,4.5,3.5,6,3,3,8.5,10,8,8,6]
        self.set_widthPay(paynums)

        BaseTable.init(self)
        self.set_width_list_from_pay( )
        self.set_width()

        self.geshi_set()


class EvTable(BaseTable):
    headList = [u'编号', u'姓名', u'货物', u'收货', u'发货', u'损耗', u'蜡', u'付钱', u'创建日期', u'备注']
    widthList = [40, 40, 40, 80, 80, 30, 40, 40, 125, 200]
    def __init__(self, table):
        super(EvTable, self).__init__(table)
        self.init()
        # self.geshi_set()
        self.table.setFrameShape(QFrame.NoFrame)  #无边框
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置不可编辑
        self.table.verticalHeader().setVisible(False)  # 垂直表头不可见
        self.table.verticalHeader().setDefaultSectionSize(22)  # 设置行距
        self.table.horizontalHeader().setStretchLastSection(True)  # 设置充满表宽度


    def is_cellDate_less_today(self, irow):
        tsr = self.get_item_text(irow, TABLE_DATE_NUMBER)
        if tsr:
            bVal = gcl.compare_less_today_str_M(tsr)
            return bVal

    def set_cellDate_color(self):
        if self.row:   # 表格的总行数不为0
            for irow in range(self.row):
                bval = self.is_cellDate_less_today(irow)
                item = self.table.item(irow, TABLE_DATE_NUMBER)
                if bval==0:
                    # item.setTextColor(Qt.blue)
                    item.setBackgroundColor(QColor(int('0xB0E0E6', 16)))
                else:
                    # item.setTextColor (Qt.black)
                    item.setBackgroundColor(Qt.white)

    def insert_evs(self, evs):
        super(EvTable, self).insert_evs(evs)
        self.set_cellDate_color()



class OwnTable(BaseTable):
    headList = [u'货物编号', u'未交数量']
    # widthList = [80,30]

    def __init__(self, table):
        super(OwnTable, self).__init__(table)
        self.init()
        self.geshi_set()


class SunTable(BaseTable):
    headList = [u'编号', u'姓名', u'事件id', u'半纸', u'圈', u'袋子', u'蜡', u'灯', u'竹子', u'铁丝', u'日期']
    widthList = [30,50,50, 40, 40,40, 40,40,40,50,100]
    pay_list = widthList

    def __init__(self, table):
        super(SunTable, self).__init__(table)
        self.init()
        self.geshi_set()

    def gs_first_row_color(self, row=0, color=Qt.red):
        if self.col > 0:
            for i in range( self.col ):
                iwidgetItem = self.table.item( row, i )
                iwidgetItem.setTextColor( color )

    def is_cellDate_less_today(self, irow):
        tsr = self.get_item_text(irow, 10)
        if tsr and tsr != QString('0'):
            bVal = gcl.compare_less_today_str_M(tsr)
            return bVal

    def set_cellDate_color(self):
        if self.row:   # 表格的总行数不为0          ``
            for irow in range(self.row):
                bval = self.is_cellDate_less_today(irow)
                item = self.table.item(irow, 10)
                if bval==0:
                    # item.setTextColor(Qt.blue)
                    item.setBackgroundColor(QColor(int('0xB0E0E6', 16)))
                else:
                    # item.setTextColor (Qt.black)
                    item.setBackgroundColor(Qt.white)

    def insert_data(self, datas):
        super(SunTable, self).insert_data(datas)
        self.set_cellDate_color()

class LookPerTable(BaseTable):
    headList = [u'编号', u'姓名', u'地址', u'电话', u'在线', u'日期', u'备注']
    # width_payList = [2,4,4,6,2,4,6]

    def __init__(self, table):
        super(LookPerTable, self).__init__(table)
        # self.set_widthPay([2,4,4,6,1,4,6])
        # self.init()
        self.set_col()
        self.set_head()

        self.table.setColumnWidth(0, 35)
        self.table.setColumnWidth(1, 50)
        self.table.setColumnWidth(2, 40)
        self.table.setColumnWidth(3, 90)
        self.table.setColumnWidth(4, 20)
        self.table.setColumnWidth(5, 75)
        self.geshi_set()



class TestTable(QTableWidget):
    """docstring for TestTable."""
    def __init__(self, arg=None):
        super(TestTable, self).__init__()
        self.arg = arg




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = TestTable()
    dialog.show()
    sys.exit(app.exec_())

    pass
