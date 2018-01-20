# -*- coding:utf8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from foo import modlevj
from foo import gcl
import middle_control
import ui_set
QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))

class Ui_set(QDialog, ui_set.Ui_Dialog):
    def __init__(self, parent=None):
        super(Ui_set, self).__init__(parent)
        self.setupUi(self)
        self.setQDateEdit( )

    def setQDateEdit(self):
        d1, d2 = modlevj.d1, modlevj.d2
        qd1 = gcl.strDateToQdate(d1)
        qd2 = gcl.strDateToQdate(d2)

        self.cstart_date.setDate(qd1)
        self.cend_date.setDate(qd2)


    def slot_sure_clicked(self):
        qd1 = self.cstart_date.date()
        qd2 = self.cend_date.date()
        if qd1>qd2:
            # print u'设置错误，起始日期不能超过终止日期！'
            middle_control.message(u'起始日期不能超过终止日期')
            return
        d1 = gcl.qdateToUdate(qd1)
        d2 = gcl.qdateToUdate(qd2)
        modlevj.setD1D2((d1, d2))
        self.accept()
