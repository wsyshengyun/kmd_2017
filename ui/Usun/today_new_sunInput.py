# -*- coding:utf8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from foo import modlevj
from foo import gcl
import middle_control
import mycolor
import ui_sunInput
from foo.sun import Sun
QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))
class Ui_SunInput(QDialog, ui_sunInput.Ui_Dialog):
    def __init__(self, sunObj=None, evId=None,  parent=None):
        super(Ui_SunInput, self).__init__(parent)
        self.setupUi(self)
        self.sunObj = sunObj
        self.evId = evId
        self.Init()
        self.bwidget = middle_control.B_Widget()
        self.bwidget.add_widget(self.cb_zhi, self.cb_quan, self.cb_dai, self.cb_la,
                                self.cb_kmd, self.cq_zhu, self.cq_tiesi)
        self.bwidget.install_filter(self)
        self.set_date_background_color()


    def slot_date_changed(self):
        self.set_date_background_color()


    def eventFilter(self, obj, event):
        self.bwidget.eventFilter(obj, event)
        return super(Ui_SunInput, self).eventFilter(obj, event)


    def set_date_background_color(self):
        displayed_date = self.dateEdit.date()
        val = gcl.compare_less_today(displayed_date)
        if val==0: b_color = mycolor.date_today
        if val<0: b_color = mycolor.date_tommorrow
        if val>0: b_color = mycolor.date_last
        middle_control.set_widget_color(self.dateEdit, b_color)



    def Init(self):

        tem_date = None
        obj = self.sunObj
        if obj:
            self.cid.setText(str(obj.id))
            tem_date = gcl.strDateTimeToQdate(obj.crdate)
            self.cb_zhi.setText(str(obj.c_zhi))
            self.cb_quan.setText(str(obj.c_quan))
            self.cb_dai.setText(str(obj.c_dai))
            self.cb_la.setText(str(obj.c_la))
            self.cb_kmd.setText(str(obj.c_kmd))
            self.cq_zhu.setText(str(obj.c_zhu))
            self.cq_tiesi.setText(str(obj.c_ts))

        else:
            tem_date = middle_control.getCurrentDate()

        self.cname.setText(QString(modlevj.curper.name))
        self.cev_id.setText(str(self.evId))
        # set date
        self.dateEdit.setDate(tem_date)


    def set_0(self, who):
        who.setText(str(0))

    def get_editText_int_val(self, who):
        text = who.text().trimmed().__str__()
        try:
            intVal = int(text)
        except ValueError:
            if text == '':
                intVal = 0
            else:
                middle_control.message( u'请输入数字！' )
                intVal =  None
        return intVal

    def get_editText_float_val(self, who):
        text = who.text().trimmed().__str__()
        try:
            intVal = float(text)
        except ValueError:
            if text == '':
                intVal = 0.0
            else:
                middle_control.message( u'请输入数字！' )
                intVal =  None
        return intVal

    def slot_btn_sure(self):
        val_lit = [None]*11

        val_lit[1] =modlevj.curper.id if modlevj.curper else None
        val_lit[2] = self.evId
        val_lit[3] = self.get_editText_int_val( self.cb_zhi )
        val_lit[4] = self.get_editText_int_val( self.cb_quan )
        val_lit[5] = self.get_editText_int_val( self.cb_dai )
        val_lit[6] = self.get_editText_int_val( self.cb_la )
        val_lit[7] = self.get_editText_int_val( self.cb_kmd )
        val_lit[8] = self.get_editText_int_val( self.cq_zhu )
        val_lit[9] = self.get_editText_float_val( self.cq_tiesi )
        val_lit[10] = val_date = gcl.qdateToUdate( self.dateEdit.date() )

        if None in val_lit[1:]:
            return
        newsun = Sun(*val_lit)
        # 保存
        if self.sunObj:  # 修改
            # val_lit.insert(0, self.sunObj.id)
            # modlevj.mod_sun(*val_lit)
            newsun.id = self.sunObj.id
            self.sunObj.mod(newsun)
        else:  # 新建obj
            # modlevj.new_sunAuto(*val_lit)
            newsun.add()

        self.accept()
        # self.close()
