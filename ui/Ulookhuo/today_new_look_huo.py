# -*- coding:utf8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from foo import modlevj
import middle_control
import table
from Uhuo import today_new_huo
QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))



import ui_look_huo
class Ui_look_huo(QDialog, ui_look_huo.Ui_Dialog):
    def __init__(self, parent=None):
        super(Ui_look_huo, self).__init__(parent)
        self.setupUi(self)
        self.table = table.HuoTable(self.ctable)
        # print self.ctable.size
        self.btn_func_dict = {
            u'修改货物': self.mod_huo,
            u'删除货物': self.del_huo,
            u'恢复': self.regain_huo,
        }
        self.currHuo = None
        self.init()
        self.init_data()
        self.display_huos_to_table()
        if self.allEvs:
            self.display_evsData()

    def init(self):
        self.cbtn_default.hide()

    def init_data(self):
        self.allEvs = modlevj.AllEvs()
        self.allEvs.up_all_evs()
        self.allEvs.get_xevExpand()

    def display_evsData(self):
        hidXevDict = self.allEvs.xevEXpand
        _dict = hidXevDict.get_kid3_dict()

        for row in range(self.ctable.rowCount()):
            # print row
            hid = self.get_itemText(row, 0)
            hid = int(hid)
            if hid in _dict:
                self.set_itemText(row, 8, str(_dict[hid][0]))
                self.set_itemText(row, 9, str(_dict[hid][1]))
                self.set_itemText(row, 10, str(_dict[hid][2]))

    def display_huos_to_table(self):
        self.table.clear()
        self.table.init()
        datas = modlevj.find_all_huos()
        self.table.insert_obj(datas)

    def btn_clicked(self):
        btnText = self.focusWidget().text().__str__()
        self.btn_func_dict[btnText]()

    def slot_cell_clicked(self, a,b):
        # print self.ctable.item(a,b)
        # row = a
        idItem = self.ctable.item(a, 0)
        huoId = int( idItem.text().__str__() )
        self.currHuo = modlevj.many_huos.id_obj_dict[huoId]

    def get_itemText(self, a, b):
        item = self.ctable.item(a,b)
        return item.text().__str__()

    def set_itemText(self, a, b, text):
        item = QTableWidgetItem(QString(text))
        self.ctable.setItem(a,b, item)

    def slot_cell_changed(self, a, b):
        # print 'slot_cell_changed  ', a, b
        pass

    def slot_cell_active(self, a, b):
        # print 'slot_cell_active  ',a, b
        pass

    def mod_huo(self):
        dialog  = today_new_huo.Ui_Huo(huoObj=self.currHuo)
        if dialog.exec_():
            pass
        self.display_huos_to_table()

    def del_huo(self):
        hid = self.currHuo.id
        # datas =
        # print  'del huo'

    def regain_huo(self):
        # print  'regain huo'
        pass
