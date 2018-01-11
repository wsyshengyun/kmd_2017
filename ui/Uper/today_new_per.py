# -*- coding:utf8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from foo import modlevj
from foo import gcl
import middle_control
import per
from foo.pervj import PersonVj

QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))
class Ui_per(QDialog, per.Ui_Dialog):
    def __init__(self, person=None, parent=None):
        super(Ui_per, self).__init__(parent)
        self.setupUi(self)
        if isinstance(person, PersonVj):
            self.per = person
        else:
            self.per = None
        self.init()

        self.bwidget = middle_control.B_Widget()
        self.bwidget.add_widget(self.cName, self.cAdress, self.cPhone, self.cText)
        self.bwidget.install_filter(self)

    def eventFilter(self, obj, event):
        self.bwidget.eventFilter(obj, event)
        return super(Ui_per, self).eventFilter(obj, event)

    def init(self):
        qdate = QDate().currentDate()
        adrs = modlevj.get_adresss()
        adress = None
        QITA = u'其它'
        if self.per:
            adress = self.per.adress
            phone = self.per.phone
            name = self.per.name
            bz = self.per.bz
            bLine = self.per.bLine
            idate = self.per.crdate.split()[0]

            gcl.insertFistPlace(adress, adrs)

            i_date = idate.split('-')   # 处理date
            ii_date = [int(i) for i in i_date]
            qdate = QDate(ii_date[0], ii_date[1], ii_date[2])


            self.cName.setText(self.tr(str(name.encode('utf8'))))
            self.cPhone.setText(self.tr(str(phone.encode('utf8'))))
            self.cText.setText(self.tr(str(bz.encode('utf8'))))
            self.cOnLine.setCheckState(Qt.Unchecked if bLine else Qt.Checked)
        else:
            if QITA in adrs:
                qita = QITA
                gcl.insertFistPlace( qita, adrs )
            else:
                adrs.insert(0, QITA)



        # address
        middle_control.setComBoxValue(self.cAdress, adrs)

        # date
        self.cDate.setDate(qdate)

    def slotSave(self):
        name = unicode(self.cName.text().trimmed())
        adress = unicode(self.cAdress.currentText().trimmed())
        phone = unicode(self.cPhone.text().trimmed())
        i_state =  self.cOnLine.checkState()

        onLine = 1 if i_state==0 else 0

        bz = unicode(self.cText.toPlainText())
        i_qcrdate = self.cDate.date()
        crdate = gcl.qdateToSDate(i_qcrdate)

        if '' == name: return

        if phone and not gcl.is_phone(phone): return
        if '' == adress: return

        # save
        if self.per:  # 修改人物， 下面保存修改
            modlevj.mod_person(name,adress, phone,onLine, crdate, bz, self.per._id)
            self.per.name = name
            self.per.adress = adress
            self.per.phone = phone
            self.per.crdate = crdate
            self.per.bz = bz
            self.per.bLine = onLine
        else:  # 新建的人物
            modlevj.new_person(name, adress, phone, onLine, crdate, bz)
        self.accept()
