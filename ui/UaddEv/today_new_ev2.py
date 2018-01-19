# -*- coding:utf8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from foo import modlevj
from foo import gcl
from foo.evvj import EvVj

from ui import middle_control
QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))
import ui_ev
import mycolor
from myedit import QLineEdit
DEBUG=False
HEIGHT_LINEEDIT = 28
WIDTH_LINEEDIT = 92
WIDTH_LABEL_UNIT = 20

CONTROL_HEIGHT = 28




class MLineEdit(QLineEdit):
    """docstring for MLineEdit."""
    def __init__(self, unit='', bold=False, arg=None):
        super(MLineEdit, self).__init__(arg)

        self.labunit= QLabel()
        self.labunit.setCursor(Qt.PointingHandCursor)
        self.labunit.setFixedSize(WIDTH_LABEL_UNIT,HEIGHT_LINEEDIT)
        self.setFixedSize(WIDTH_LINEEDIT, HEIGHT_LINEEDIT)
        # text base color
        pa = QPalette()
        # pa.setColor(QPalette.Text, Qt.gray)
        self.labunit.setPalette(pa)

        self.setFont(QFont('Arial', 12))

        # font bold
        if bold:
            font = self.font()
            font.setBold(True)
            self.setFont(font)




        margins = self.textMargins()
        self.setTextMargins(margins.left(), margins.top(), self.labunit.width(), margins.bottom())
        # self.setPlaceholderText('0')




        hlay = QHBoxLayout()
        self.setLayout(hlay)

        hlay.addStretch(1)
        hlay.addWidget(self.labunit)
        hlay.setSpacing(0)
        hlay.setContentsMargins(0,0,0,0)

        self.set_unit(unit)
        self.set_input_limit()

    def setBold(self):
        font = self.font()
        font.setBold(True)
        self.setFont(font)
    #
    def set_unit(self, unit):
        uu = self.tr(unit)
        self.labunit.setText(uu)
    #
    def set_unit_base(self):
        self.set_unit('个')


    def set_input_limit(self, reg=r'[-]?[0-9]+[\+|\-|\*|\.]?[0-9]+ '):
        reg = QRegExp(reg)
        validator = QRegExpValidator(reg, self)
        self.setValidator(validator)



    def focusOutEvent(self, event):
        middle_control.set_widget_color(self)
        tsr = self.text().trimmed().__str__()
        if '+'in tsr or '-'in tsr or '*' in tsr:
            val = eval(tsr)
            self.setText(str(val))
        return super(MLineEdit,self).focusOutEvent(event)

    def focusInEvent(self, event):
        middle_control.set_widget_color(self, QColor(31,135,92), Qt.white)
        return super(MLineEdit, self).focusInEvent(event)





class NewEv2Ui(QDialog):
    """docstring for NewEv2Ui."""
    def __init__(self, evobj=None, pos=None, arg=None):
        super(NewEv2Ui, self).__init__(arg)

        self.evObj = evobj
        self.huoObj = None
        self.perObj = None

        self.resize(340,300)
        if pos:
            self.move(pos)
        vlay = QVBoxLayout()
        self.setLayout(vlay)



        groupBoxSh = QGroupBox(self.tr('收货发货'))

        lab_date = QLabel(self.tr('时间'))
        lab_huo = QLabel(self.tr('货物'))
        lab_fa = QLabel(self.tr('发货'))
        lab_sh = QLabel(self.tr('收货'))
        lab_money = QLabel(self.tr('付钱'))
        lab_sun = QLabel(self.tr('损耗'))
        self.lab_la = QLabel(self.tr('蜡'))
        self.cdate = QDateEdit()
        self.cdate.setCalendarPopup(True)
        self.cdate.setFixedHeight(CONTROL_HEIGHT)
        self.cdate.setFont(QFont('Arial', 12, QFont.Bold))

        self.chuobox = QComboBox()
        self.chuobox.setFixedHeight(CONTROL_HEIGHT)
        self.chuobox.setFont(QFont('Arial', 12, QFont.Bold))

        self.csh = MLineEdit('个', False)
        self.cfa = MLineEdit('个', False)
        # self.cfa = QLineEdit()
        self.cmoney = MLineEdit('元', True)
        self.csun = MLineEdit('个')
        self.cla = MLineEdit('块')


        self.check_money = QCheckBox(self.tr('付钱'))
        self.check_money.setChecked(True)
        # =================================================================时间货物
        gb_date = QGroupBox()
        lay_gb_date = QHBoxLayout()
        lay_gb_date.setSpacing(20)
        gb_date.setLayout(lay_gb_date)
        vlay.addWidget(gb_date)

        lay_gb_date.addWidget(lab_date, 0, Qt.AlignLeft|Qt.AlignCenter)
        lay_gb_date.addWidget(self.cdate, 0, Qt.AlignLeft|Qt.AlignCenter)
        lay_gb_date.addWidget(lab_huo, 0, Qt.AlignRight|Qt.AlignCenter)
        lay_gb_date.addWidget(self.chuobox, 0, Qt.AlignRight|Qt.AlignCenter)
        lay_gb_date.addStretch(1)
        # =================================================================收, 发


        # 收货
        self.check_fa_1000 = QRadioButton('1000')
        self.check_fa_2000 = QRadioButton('2000')
        self.check_fa_500 = QRadioButton('500')
        self.check_fa_200 = QRadioButton('200')
        self.fa_nums_control_list = [self.check_fa_1000, self.check_fa_2000, self.check_fa_500, self.check_fa_200 ]


        self.check_sh_1000 = QRadioButton('1000')
        self.check_sh_2000 = QRadioButton('2000')
        self.check_sh_500 = QRadioButton('500')
        self.check_sh_200 = QRadioButton('200')
        self.sh_nums_control_list = [self.check_sh_1000, self.check_sh_2000, self.check_sh_500, self.check_sh_200 ]


        gb_sh = QGroupBox()
        lay_sh = QGridLayout()
        lay_sh.setHorizontalSpacing(25)
        gb_sh.setLayout(lay_sh)
        # 收货
        lay_sh.addWidget(lab_sh, 0, 0)
        lay_sh.addWidget(self.csh, 0, 1)
        sncLayout = self._setHorizontalLayout(self.sh_nums_control_list)
        lay_sh.addLayout(sncLayout, 0, 2, 1, 2)

        # lay_sh.addWidget(lab_money, 1, 0)
        # 付钱 损耗
        lay_sh.addWidget(self.check_money, 1, 0)
        lay_sh.addWidget(self.cmoney, 1, 1)
        lay_sh.addWidget(lab_sun, 1, 2)
        lay_sh.addWidget(self.csun, 1, 3)

        # 发货
        lay_sh.addWidget(lab_fa, 2, 0)
        lay_sh.addWidget(self.cfa, 2, 1)
        sncLayout = self._setHorizontalLayout(self.fa_nums_control_list)
        lay_sh.addLayout(sncLayout, 2, 2, 1, 2)

        self.radio_la2000= QRadioButton(self.tr('2000'))
        self.radio_la1000= QRadioButton(self.tr('1000'))
        self.radio_la500 = QRadioButton(self.tr('500'))
        self.radio_la200 = QRadioButton(self.tr('200'))
        self.la_num_list = [self.radio_la2000, self.radio_la1000, self.radio_la500, self.radio_la200]
        lay_sh.addWidget(self.lab_la, 3, 0)
        lay_sh.addWidget(self.cla, 3, 1)
        laNumsLayout = self._setHorizontalLayout(self.la_num_list)
        lay_sh.addLayout(laNumsLayout, 3, 2, 1, 2)



        vlay.addWidget(gb_sh)




        # =================================================================层 text
        self.ctext = QTextEdit()
        bzsize = self.ctext.sizeHint()
        # self.ctext.setFixedSize(bzsize.width(), bzsize.height()/4)
        vlay.addWidget(self.ctext)


        # =================================================================ok, cancel
        self.cok = QPushButton('ok')
        self.ccancel = QPushButton('cancel')

        self.cok.clicked.connect(self.clicked_ok)
        self.ccancel.clicked.connect(self.reject)

        lay_ok = QHBoxLayout()
        vlay.addLayout(lay_ok)
        lay_ok.addStretch(1)
        lay_ok.addWidget(self.ccancel)
        lay_ok.addWidget(self.cok)

        # ....
        vlay.addStretch(1)
        # =================================================================singal
        self.csh.installEventFilter(self)
        self.chuobox.installEventFilter(self)
        # self.cfa.installEventFilter(self)
        self.cdate.dateChanged.connect(self.auto_set_date_background_color)

        self.check_money.stateChanged.connect(self.checkMoneyChanged)

        self.chuobox.currentIndexChanged.connect(self.slot_chuobox_index_changed)
        # =================================================================init
        self.csh.setFocus()
        self.setTabOrder(self.csh, self.cfa)
        self.setTabOrder(self.cfa, self.csun)
        self.setTabOrder(self.csun, self.cla)
        self.setTabOrder(self.cla, self.cok)

        # check connect
        _allradio = self.fa_nums_control_list + self.sh_nums_control_list + self.la_num_list
        for i in _allradio:
            i.setFont(QFont('Arial', 10))
            self.connect(i, SIGNAL('clicked()'), self.slot_radios_clicked)
        self.init()


    # @staticmethod
    # def eval_input(tsr):
    #     if '+'in tsr or '-'in tsr or '*' in tsr:
    #         return str(eval(tsr))
    #     else:
    #         return None
    #
    # def sh_finished(self):
    #     tt = self.csh.text().trimmed().__str__()
    #     result = self.eval_input(tt)
    #     if result:
    #         self.csh.setText(result)
    #
    # def fa_finished(self):
    #     tt = self.cfa.text().trimmed().__str__()
    #     result =  self.eval_input(tt)
    #     if result:
    #         self.cfa.setText(result)
    def init(self):
        tempId = None
        tempDate= None
        evobj = self.evObj
        if evobj:
            tempId = evobj.huoId
            self.csh.setText(str(evobj.sh))
            self.cfa.setText(str(evobj.fa))
            self.csun.setText(str(evobj.sun))
            self.cla.setText(str(evobj.numla))
            self.cmoney.setText(str(evobj.money))
            self.ctext.setPlainText(self.tr(evobj.bz))
            tempDate = gcl.strDateTimeToQdate(evobj.crdate)
            self.perObj = modlevj.many_pers.getFromId(evobj.nameId)
        else:
            last_ev_huoId = modlevj.perwork.get_last_huoId()
            tempId = last_ev_huoId
            self.perObj = modlevj.curper
            tempDate = middle_control.getCurrentDate()
        self.cdate.setDate(tempDate)
        # set huobox items
        huo_ids = modlevj.get_huo_valid_ids()
        huo_ids = gcl.insertFistPlace(tempId, huo_ids) if tempId else huo_ids
        middle_control.setComBoxValue(self.chuobox, huo_ids)



        self.set_cLa_state_from_huoId_bLa()

        # text backgroung

        # 设置备注对话框的颜色
        # middle_control.set_widget_color(self.ctext, QColor(156,228,235))

    def slot_radios_clicked(self):
        focus = self.focusWidget()
        if focus in self.sh_nums_control_list:
            self.csh.setText(focus.text())
            self.set_cmoney()
        if focus in self.fa_nums_control_list:
            self.cfa.setText(focus.text())
        if focus in self.la_num_list:
            self.cla.setText(focus.text())





    @staticmethod
    def _setHorizontalLayout(control_list):
        hlay = QHBoxLayout()
        if control_list:
            for ic in control_list:
                hlay.addWidget(ic)
        return hlay

    def checkMoneyChanged(self):
        if self.check_money.checkState() == Qt.Checked:
            print 'checked'
        else: # Unchecked
            self.set_cmoney(0.0)

            tt = self.ctext.toPlainText().trimmed().__str__()
            tt = tt + u'[未付钱 元]'
            self.ctext.setPlainText(self.tr(tt))

    def get_huo_obj(self):
        temp = self.chuobox.currentText().trimmed().__str__()
        try:
            huoId = int(temp)
        except ValueError:
            self.huoObj = None
        else:
            self.huoObj = modlevj.many_huos.id_obj_dict[huoId]

    def slot_chuobox_index_changed(self):
        self.get_huo_obj()
        self.set_cLa_state_from_huoId_bLa()

    def set_cLa_state_from_huoId_bLa(self):
        # print self.huoObj.bLa
        if self.huoObj and self.huoObj.bLa == 0:
            self.cla.hide()
            self.lab_la.hide()
            for i in self.la_num_list:
                i.hide()
            self.cla.setText('')
        else:
            self.cla.show()
            self.lab_la.show()
            for i in self.la_num_list:
                i.show()

    # def set_sh_fa_money(self, ish, ifa):
    #     self.csh.setText(str(ish))
    #     self.cfa.setText(str(ifa))
    #     self.set_cmoney()




    def auto_set_date_background_color(self):
        displayed_date = self.cdate.date()
        val = gcl.compare_less_today(displayed_date)
        if val==0: b_color = mycolor.date_today
        if val<0: b_color = mycolor.date_tommorrow
        if val>0: b_color = mycolor.date_last
        # setWidgetBackground(self.cdate, b_color)
        middle_control.set_widget_color(self.cdate, b_color)

    def set_cmoney(self, ival=None):
        ish = self.get_widget_numVal(self.csh)
        if  DEBUG:
            imoney = 0.0
        else:
            imoney = ish * self.huoObj.pay if self.huoObj else 0.0
        if ival != None:
            imoney = ival
        self.cmoney.setText(str(imoney))

    # Filter
    def eventFilter(self, obj, event):
        if obj ==self.csh and event.type()==QEvent.FocusOut:
            tsr = self.csh.text().trimmed().__str__()
            if '+'in tsr or '-'in tsr or '*' in tsr:
                val = eval(tsr)
                self.csh.setText(str(val))
            # money
            self.set_cmoney()

        # if obj ==self.chuobox and event.type()==QEvent.HoverEnter:
        #     self.chuobox.showPopup()

        return super(NewEv2Ui, self).eventFilter(obj, event)

    @staticmethod
    def get_widget_numVal(who, typ=int):
        tt = who.text()
        try:
            val = typ(who.text())
        except ValueError:
            val = 0.0 if typ==float else 0
        return val

    def clicked_ok(self):
        val_lit = [None]*10
        val_lit[1] = self.perObj.id
        val_lit[2] = int( self.chuobox.currentText().__str__())
        val_lit[3] = self.get_widget_numVal(self.csh)
        val_lit[4] = self.get_widget_numVal(self.cfa)
        val_lit[5] = self.get_widget_numVal(self.csun)
        val_lit[6] = self.get_widget_numVal(self.cla)
        val_lit[7] = self.get_widget_numVal(self.cmoney, float)
        val_lit[8] = gcl.qdateToSdate_andTime( self.cdate.date() )
        val_lit[9] = self.ctext.toPlainText().trimmed().__str__()

        if None in val_lit[1:]:
            return

        newev = EvVj(*val_lit)
        if self.evObj:  # 修改事件
            newev.id = self.evObj.id
            self.evObj.mod(newev)
        else:  # 新建事件
            newev.add()
        self.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = NewEv2Ui()
    dlg.show()
    sys.exit(app.exec_())
