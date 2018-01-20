# -*- coding:utf8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from foo import modlevj
import middle_control
QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))
import ui_only
import table
class Ui_sun(QDialog, ui_only.Ui_Dialog):
    def __init__(self, pos=None,  parent=None):
        super(Ui_sun, self).__init__(parent)
        self.setupUi(self)
        self.init()
        if pos:
            self.move(pos)
        self.update()

    def init(self):
        self.btable = table.SunTable(self.table)


    def update(self):
        if modlevj.curper:
            sumdata = modlevj.search_sun_sum()
            sunobjs = modlevj.search_sun()
            datas = []
            for obj in sunobjs:
                datas.append(obj.toList())
            datas = datas[::-1]
            sumdata.extend(datas)
            self.btable.insert_data(sumdata)
            self.btable.gs_first_row_color()
