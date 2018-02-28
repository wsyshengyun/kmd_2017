# -*- coding:utf8 -*-

from foo import gcl
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from foo import modlevj
from foo.huovj import HuoVj
import middle_control
QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))


import ui_huo
class Ui_Huo(QDialog, ui_huo.Ui_Dialog):
    def __init__(self, huoObj=None, parent=None):
        super(Ui_Huo, self).__init__(parent)
        self.huoObj = huoObj
        self.setupUi(self)
        self.init()
        self.bwidget = middle_control.B_Widget()
        self.bwidget.add_widget(self.cpay, self.cnums, self.ctext)
        self.bwidget.install_filter( self )


    def init(self):
        # 初始化货物类型
        tys = modlevj.get_huoTys()
        if self.huoObj:
            tys = gcl.insertFistPlace(self.huoObj.ty, tys)

        middle_control.setComBoxValue(self.cty, tys)

        # 初始化日期
        qdate = gcl.strDateToQdate(self.huoObj.crdate) if self.huoObj else middle_control.getCurrentDate()
        self.cdate.setDate(qdate)

        # 其它
        if self.huoObj:
            self.cpay.setText(str(self.huoObj.pay))
            self.cnums.setText(str(self.huoObj.nums))
            self.ctext.setText(self.tr(self.huoObj.bz))
            self.cvalid.setCheckState(Qt.Checked if self.huoObj.bvalid==1 else Qt.Unchecked)
            self.cIsLa.setCheckState(Qt.Checked if self.huoObj.bLa ==1 else Qt.Unchecked)
            # if self.huoObj.bLa == 1:
            #     self.cIsLa.setCheckState(Qt.Checked)
            # else:
            #     self.cIsLa.setCheckState(Qt.Unchecked)
    def eventFilter(self, obj, event):
        self.bwidget.eventFilter(obj, event)
        return super(Ui_Huo, self).eventFilter(obj, event)

    def checkState(self, state):
        return 1 if state==2 else 0

    def slot_sure(self):
        ty = self.cty.currentText().trimmed()
        pay = self.cpay.text().trimmed()
        nums = self.cnums.text().trimmed()
        crdate = self.cdate.date()
        ibvalid = self.cvalid.checkState()
        ibLa = self.cIsLa.checkState()
        bz = self.ctext.toPlainText().trimmed()

        ibvalid = self.checkState(ibvalid)
        ibLa = self.checkState(ibLa)

        ty = unicode(ty)
        bz = unicode(bz)
        crdate = gcl.qdateToSDate(crdate)

        if not nums: nums = 0
        else: nums = int(nums)

        if not pay: return
        else: pay = float(pay)

        newhuo = HuoVj(id=None, ty=ty, pay=pay, nums=nums, bvalid=ibvalid,
                bLa=ibLa, crdate = crdate, bz=bz)
        if not self.huoObj:
            # modlevj.new_huoAuto(ty, pay, nums, ibvalid, ibLa, crdate, bz)
            newhuo.add()
        else:
            newhuo.id = self.huoObj.id
            self.huoObj.mod(newhuo)
            modlevj.logger.info('修改货物: %s' % self.huoObj.toStr())
            # modlevj.mod_huo(ty, pay, nums, ibvalid, ibLa, crdate, bz, self.huoObj.id)


        # check ty
        # write into sql
        # accept

        self.accept()
