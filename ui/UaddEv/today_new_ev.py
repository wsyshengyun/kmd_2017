# -*- coding:utf8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from foo import modlevj
from foo import gcl
import middle_control
QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))
import ui_ev
import mycolor

class Ui_Ev(QDialog, ui_ev.Ui_Dialog):
    def __init__(self, evObj=None,  parent=None):
        super(Ui_Ev, self).__init__(parent)
        self.setupUi(self)
        self.evObj = evObj
        self.huoObj = None
        self.perObj = None
        self.init()
        self.set_b_widget()
        self.cFa.editingFinished.connect(self.slot_cfa_finished)


    def set_b_widget(self):
        self.b_widget_edit = middle_control.B_Widget_expand( )
        # self.cSh.installEventFilter(self)
        col_list = [self.cSh, self.cFa, self.cMoney, self.cSun, self.cLa, self.cText]
        color_list = [mycolor.sh_edit_b, mycolor.fa_edit_b, mycolor.money_edit_b,
                      mycolor.edit_background,
                      mycolor.edit_background,
                      mycolor.edit_background,

                      ]
        # self.b_widget_edit.add_widget( self.cSh, self.cFa, self.cMoney, self.cSun, self.cLa, self.cText )
        self.b_widget_edit.add_widget(wids=col_list, colors=color_list )
        self.b_widget_edit.install_filter( self )

    def init(self):
        # date

        temp_id = None
        evObj = self.evObj
        if evObj:
            temp_id = evObj.huoId
            self.cSh.setText(str(evObj.sh))
            self.cFa.setText(str(evObj.fa))
            self.cSun.setText(str(evObj.sun))
            self.cLa.setText(str(evObj.numla))
            self.cMoney.setText(str(evObj.money))
            temd_date = gcl.strDateTimeToQdate(evObj.crdate)
            self.cText.setPlainText(QString(evObj.bz))

            self.perObj = modlevj.many_pers.getFromId(evObj.nameId)

        else:
            last_ev_huoId = modlevj.perwork.get_last_huoId()
            temp_id = last_ev_huoId
            self.perObj = modlevj.curper
            temd_date = middle_control.getCurrentDate()

        # set date
        self.cDate.setDate(temd_date)

        # set-huo-box-items
        huo_ids = modlevj.get_huo_valid_ids()
        huo_ids = gcl.insertFistPlace(temp_id, huo_ids ) if temp_id else huo_ids  # 插入列表0位置 huo_ids = [str(i) for i in huo_ids]
        middle_control.setComBoxValue(self.cHuoBox, huo_ids)
        self.get_huo_obj()

        # nameLab
        if self.perObj:
            self.cName.setText(self.tr(self.perObj._name))

        # set cla-enable or no
        self.set_cLa_state_from_huoId_bLa()

        # pale_foreground_red = QPalette()
        # pale_foreground_red.setColor(QPalette.Text, Qt.red)
        # self.cMoney.setAutoFillBackground(True)
        # self.cMoney.setPalette(pale_foreground_red)


    def eventFilter(self, obj, event):
        self.b_widget_edit.eventFilter(obj, event)
        return super(Ui_Ev, self).eventFilter(obj, event)

    def slot_state_changed(self, a):
        # st = self.ccheck.checkState()
        if a == 2:
            self.add_mark_to_bzCol()
        else:
            self.remove_mark_to_bzCol()


    def add_mark_to_bzCol(self, umark=u'<检>'):
        origin = self.cText.toPlainText().__str__()
        self.cText.setText(QString(''.join([origin, umark])))

    def remove_mark_to_bzCol(self, umark = u'<检>'):
        origin = unicode(self.cText.toPlainText().trimmed().__str__())
        info = re.compile(umark)
        newtsr = info.sub(u'', origin)
        self.cText.setText(QString(newtsr))

    def slot_chuobox_index_changed(self):
        self.get_huo_obj()
        self.set_cLa_state_from_huoId_bLa()

    def slot_cfa_finished(self):
        faNum = self.get_editText_num_val(self.cFa)
        self.cFa.setText(str(faNum))

    def slot_csh_finished(self):
        shNum = self.get_editText_num_val(self.cSh)   # todo error   'NoneType' object has no attribute 'pay'
        self.cSh.setText(str(shNum))
        try:
            money = self.huoObj.pay * shNum
        except TypeError:
            return

        self.cMoney.setText(str(money))

    def get_huo_obj(self):
        temp = self.cHuoBox.currentText().trimmed().__str__()
        try:
            huoId = int(temp)
        except ValueError:
            self.huoObj = None
        else:
            self.huoObj = modlevj.many_huos.id_obj_dict[huoId]

    def set_cLa_state_from_huoId_bLa(self):
        if self.huoObj and self.huoObj.bLa == 0:
            self.cLa.setDisabled(True)
            self.lab_la.setDisabled(True)
        else:
            self.cLa.setEnabled(True)
            self.lab_la.setEnabled(True)

    def slot_date_changed(self):
        self.set_date_background_color()

    def set_date_background_color(self):
        displayed_date = self.cDate.date()
        val = gcl.compare_less_today(displayed_date)
        if val==0: b_color = mycolor.date_today
        if val<0: b_color = mycolor.date_tommorrow
        if val>0: b_color = mycolor.date_last
        # setWidgetBackground(self.cDate, b_color)
        middle_control.set_widget_color(self.cDate, b_color)

    def get_editText_num_val(self, who, typ=int):
        text = who.text().trimmed().__str__()
        intVal = None
        try:
            intVal = typ(text)
        except ValueError:
            if text == '':
                intVal = typ(0)
            elif '+' in text or '-' in text or '*' in text:
                try:
                    intVal = eval(text)
                except SystemError:
                    middle_control.message( u'输入格式不正确！' )
            else:
                middle_control.message( u'输入格式不正确！' )
        return intVal




    def slot_add(self):
        val_lit = [None]*9
        val_lit[0] = self.perObj.id
        val_lit[1] = int( self.cHuoBox.currentText().__str__())
        val_lit[2] = self.get_editText_num_val(self.cSh)
        val_lit[3] = self.get_editText_num_val(self.cFa)
        val_lit[4] = self.get_editText_num_val(self.cSun)
        val_lit[5] = self.get_editText_num_val(self.cLa)
        val_lit[6] = self.get_editText_num_val(self.cMoney, float)
        val_lit[7] = gcl.qdateToSdate_andTime( self.cDate.date() )
        val_lit[8] = self.cText.toPlainText().trimmed().__str__()

        if None in val_lit:
            return

        # save to sql
        if self.evObj:  # 修改事件
            val_lit.append(self.evObj.id)
            modlevj.mod_ev(*val_lit)
        else:  # 新建事件
            modlevj.new_evAuto(*val_lit)

        self.accept()
