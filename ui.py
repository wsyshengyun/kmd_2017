# coding=utf8
import sys
sys.path.append("/home/pi/kmdVj/ui")

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui import table
from ui import mycolor
from ui import middle_control
from ui import uiMain

import re
from foo import modlevj
from foo import gcl
from foo.pervj import PersonVj

from UaddEv.today_new_ev import Ui_Ev
from Uhuo.today_new_huo import Ui_Huo
from Uper.today_new_per import Ui_per
from Uset.today_new_set import Ui_set
from Ulooksun.today_new_sun import Ui_sun
from Usort import today_new_sort
from Ulookhuo.today_new_look_huo import Ui_look_huo
from Ulookper.today_new_look_per import Ui_look_per
from Usun.today_new_sunInput import Ui_SunInput
from Utoday import ui_today_staus
from UaddEv.today_new_ev2 import NewEv2Ui
from Usort.today_new_sort import Ui_sort
__author__ = 'Administrator'
'''

'''

QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))
SHOW=False
HIDE_HISTORY_NAME = True   # 隐藏历史名字列表

def show(tsr):
    if SHOW:
        print u"show=======================" + tsr

def set_show(flg=False):
    global SHOW
    SHOW = flg

#import ui_ev
class B_Menu(object):
    def __init__(self, obj, strmenuFunc_dict):
        self.menuDict = strmenuFunc_dict
        self.menu = QMenu()
        self.init(obj)

    def init(self, obj):
        '''

        '''

        for mstr in self.menuDict:
            self.add_menu(mstr, self.menuDict[mstr], obj)
        self.iexec()

    def add_menu(self, mstr, func, selfobj):
        action = QAction( mstr, selfobj )
        self.menu.addAction(action)
        action.triggered.connect(func)

    def iexec(self):
        self.menu.exec_(QCursor.pos())

class UiPoint(object):
    init_pos = QPoint(0,0)
    def __init__(self, main_obj=None):
        self.main_obj = main_obj



pointObj = UiPoint()

class MainUi(QDialog, uiMain.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainUi, self).__init__(parent)
        self.setupUi(self)
        self.btnFuncDit = {u'设置': self.date_set,
                           u'查看货物': self.btn_look_huos,
                           u'新建货物': self.btn_new_huo,
                           u'排序': self.btn_sort,
                           u'查看人物':self.btn_look_per,
                           u'每天':self.btn_today_data,
                           }

        self.row_rect = QRect()
        self.evId_tab_selected = None
        self.flg_leftBtn = False

        self.bwidget = middle_control.B_Widget()
        self.bwidget.add_widget(self.findName)
        self.bwidget.install_filter(self)
        self.init()
        self.move(pointObj.init_pos)
        self.setWindowTitle(modlevj.curpath + ' ' +  modlevj.version)

        self.myConnect()

        #

        self.nametempList = []  # 搜索历史名字列表
        #
        #self.pickle_load()
        self.set_cobName_from_tempNameList()
        # if len(self.nametempList)>=1:
        #     name = self.nametempList[0]
        #     self.findName.setText(name)


        self.findName.installEventFilter(self)
        self.cob_name.installEventFilter(self)  # 历史名字列表
        self.installEventFilter(self)
        self.cob_name.currentIndexChanged.connect(self.set_findName_text_from_cobName)
        # connect
        self.cevTable.itemSelectionChanged.connect(self.slot_cevTable_itemSelectionChanged)

        self.set_search_ico()

        if HIDE_HISTORY_NAME:
            self.cob_name.hide()

    def set_search_ico(self):

        self.findBtn.setText('')
        self.findBtn.setCursor(Qt.PointingHandCursor)
        self.findBtn.setFixedSize(30,30)
        # icon = QPixmap('ui\search.png')
        # self.findBtn.setIcon(icon)
        # self.findBtn.setFixedSize(icon.size())
        self.findBtn.setStyleSheet("QPushButton{border-image:url(./src/isearch.png); background:transparent;} QPushButton:hover{border-image:url(./search.png)}  QPushButton:pressed{border-image:url(./search.png)}");

        margins = self.findName.textMargins()
        self.findName.setTextMargins(margins.left(), margins.top(), self.findBtn.width(), margins.bottom())
        # self.findName.setPlaceholderText(self.tr('姓名?'))
        lay_h = QHBoxLayout()
        self.findName.setLayout(lay_h)

        lay_h.addStretch()
        lay_h.addWidget(self.findBtn)
        lay_h.setSpacing(0)
        lay_h.setMargin(0)



    def set_findName_text_from_cobName(self, text):
        text = self.cob_name.currentText()
        self.findName.setText(text)
        self.findName.setFocus()
        show(u'set findName text')

    def set_cobName_from_tempNameList(self):
        word = QStringList()
        for i in self.nametempList:
            word<<i
        self.cob_name.clear()
        self.cob_name.addItems(word)


    def myConnect(self):
        self.findName.returnPressed.connect(self.findNameReturnPressed)


    def findNameReturnPressed(self):
        self.slotFindNameBtnClicked()
        self.slot_add_ev()

#    def save_findnameText_to_pickle(self):
#        nameQstr = self.findName.text()
#        self.nametempList = self.nametempList[:9] # 只保存有限个元素
#
#        show(nameQstr)
#        if nameQstr in self.nametempList:
#            self.nametempList.remove(nameQstr)
#        self.nametempList.insert(0, nameQstr)
#        self.pickle_dump()
#        self.set_cobName_from_tempNameList()


    # 查找名字历史缓存
#    def pickle_dump(self):
#        with open(pickle_file_path, 'w') as f:
#            pickle.dump(self.nametempList, f)
#        pass

#    def pickle_load(self):
#        with open(pickle_file_path, 'r') as f:
#            self.nametempList = pickle.load(f)
#            if not isinstance(self.nametempList, list):
#                self.nametempList = []
#        pass
    # 初始化
    def init(self):
        # nameLine
        self.set_findName_edit_completer( )

        self.bt_evTable = table.EvTable( self.cevTable )
        self.bt_evTable.init( )
        # self.cevTable.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        # self.cevTable.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)


        self.bt_ownTable = table.OwnTable( self.cownTable )
        self.bt_ownTable.gs_horizontalHeaderVisible( False )
        self.cownTable.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.cownTable.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)

        # date`
        self.cdate.setDate(QDate().currentDate())

        # lit
        self.init_list_widget()
        self.slot_date_finished()

        # hid
        # self.cmod_h.hide()
        self.clook_sum.hide()
        # lab color
        middle_control.set_widget_color(self.cdatedata, fcolor=mycolor.lab_date_sum)

    def keyPressEvent(self, ekey):
        pass
        # if ekey.key() == Qt.Key_F3:   # 按下F3键, 添加事件
        #     print 'F3 is down'
        #     self.slot_add_ev()


    def eventFilter(self, obj, event):
        if obj==self.findName and  event.type() == QEvent.KeyPress:
            # if event.key() == Qt.Key_1 and event.modifiers()==Qt.AltModifier:
            if event.key() == Qt.Key_F3:
                self.slot_add_ev()

        # if obj==self.cob_name and event.type() == QEvent.HoverEnter:
        #     self.cob_name.showPopup()
        #     show(u'cob_name:HoverEnter')

        return super(MainUi, self).eventFilter(obj, event)



    # def mousePressEvent(self, e):
    #     if self.flg_Rbtn == False and e.button() == Qt.RightButton:
    #         self.flg_Rbtn = True

    # def mouseDoubleClickEvent(self,  qmouse_event):
    #     if qmouse_event.button() == Qt.LeftButton:
    #         self.flg_leftBtn = True
    #     else:
    #         self.flg_leftBtn = False


    # def mouseReleaseEvent(self, e):
    #     if self.flg_Rbtn:
    #         self.flg_Rbtn = False

    # 日期控件跳转到表格指定的日期
    def set_date_from_table_cell(self):
        cell_date = None


        self.cdate.setDate(cell_date)
        pass

    # 设置名字标签的tip显示
    def set_curper_tip_at_nameLab(self):
        curper = modlevj.curper
        if curper:
            tsr = '\n'.join(curper.get_per_list_to_tooltip())
            qtsr = QString(tsr)
        else:
            qtsr = ''
        self.disNameLab.setToolTip(qtsr)

    # 初始化今日人物的列表
    def init_list_widget(self):
        self.nameListWidget.clear( )
        names = modlevj.datework.get_names()


        if names:
            names = [self.tr(i) for i in names]
            qstrList = QStringList(names)
            self.nameListWidget.addItems(qstrList)
            self.nameListWidget.setToolTip(u'人数:' + str(len(names)))

    def set_date_background_color(self):
        displayed_date = self.cdate.date()
        val = gcl.compare_less_today(displayed_date)
        _dit = {
            -1: mycolor.date_tommorrow,
            0: mycolor.date_today,
            1: mycolor.date_last,
        }
        middle_control.set_widget_color(self.cdate, _dit[val])
        # middle_control.set_widget_color(self.cdate, fcolor=_dit[val])

    def set_findName_edit_completer(self):
        qlist = [QString(utser) for utser in modlevj.many_pers.names.keys()]
        self.icompleter = QCompleter(qlist)
        self.findName.setCompleter(self.icompleter)

    def update_display_per(self):
        if modlevj.curper:
            self.bt_ownTable.clear( )
            self.bt_evTable.clear()
            # lab-diaplay name
            self.disNameLab.setText( self.tr( modlevj.curper.name ) )
            self.set_curper_tip_at_nameLab( )

            # diaplay huo-ty-box
            self.init_huoBox_items( )

            # OneTable show data  from now huo-box-items
            box_t = self.chuobox.currentText( ).__str__( )
            # evs = modlevj.perwork.hid_evs.get(int(box_t), modlevj.perwork.allEvs)
            try:
                evs = modlevj.perwork.hid_evs.get( int( box_t ) )
            except ValueError:
                evs = modlevj.perwork.allEvs
            if evs:
                # print u"个人ev数: %d" % len(evs)
                evs.sort( key=lambda x_ev: x_ev.id, reverse=True )
                # print len(evs)
                self.bt_evTable.insert_evs( evs )
                self.set_evTable_textcolor_from_sunInfo( )

            self.bt_ownTable.insert_data( modlevj.perwork.get_ownNums( ) )  # own 表格

            #
            self.cla_own.setText( str( modlevj.perwork.get_la_own( ) ) )

    # 设置有损耗时,事件的编号颜色为红色
    def set_evTable_textcolor_from_sunInfo(self):
        allsun = modlevj.AllSun( )
        sun_ev_ids = allsun.get_per_sun_evIds( )
        if sun_ev_ids:
            self.bt_evTable.set_column_some_items_color( sun_ev_ids )


    # 初始化货物列表
    def init_huoBox_items(self):
        self.chuobox.clear( )
        modlevj.up_perwork( )
        terms = modlevj.perwork.get_self_huoIds( )
        last_ev = modlevj.perwork.last_ev
        if last_ev:  # set box first items
            if last_ev.huoId in terms:
                terms = gcl.insertFistPlace( last_ev.huoId, terms )
        terms = [str( i ) for i in terms]
        terms.append( self.tr( u'全部' ) )
        qslist = QStringList( terms )
        self.chuobox.addItems( qslist )

    def slot_mytable_context(self, point):
        now_widget = self.focusWidget()
        if now_widget == self.cevTable:
            range_table = self.row_rect
            if point in range_table:
                popMenu = QMenu()
                self.q_action = QAction( u'添加/修改(损耗)', self )
                popMenu.addAction( self.q_action )
                self.q_action.triggered.connect(self.action_add_sunHao)
                popMenu.exec_(QCursor.pos())
        elif now_widget == self.cdate:
            _dict = {
                u'回到今天': self.qdateedit_goto_today,
                u'上一天': self.qdateedit_goto_lastDay,
                u'下一天': self.qdateedit_goto_tomorrow,
            }
            B_Menu(self, _dict)

    def qdateedit_goto_lastDay(self):
        now_day = self.cdate.date()
        self.cdate.setDate(now_day.addDays(-1))

    def qdateedit_goto_today(self):
        self.cdate.setDate(middle_control.getCurrentDate())

    def qdateedit_goto_tomorrow(self):
        now_day = self.cdate.date()
        self.cdate.setDate(now_day.addDays(1))

    # 添加损耗
    def action_add_sunHao(self):

        sunObj = modlevj.find_sun_data(self.evId_tab_selected)
        # print self.evId_tab_selected
        dialog = Ui_SunInput(sunObj=sunObj, evId=self.evId_tab_selected)
        if dialog.exec_()==QDialog.Accepted:
            self.set_evTable_textcolor_from_sunInfo()

    # 表格双击
    def slot_cell_double_clicked(self,ri, ci):
        # if  not self.flg_leftBtn: return
        evid = int( self.bt_evTable.get_row0_text( ri ) )
        evobj = modlevj.perwork.get_ev(evid)
        if evobj:
            dialog = NewEv2Ui(evobj=evobj, pos=self._getMainFrameRightPos())
            if dialog.exec_()==QDialog.Accepted:
                self.update_display_per()
                self.slot_date_finished()


    # 表格单击
    def slot_cell_clicked(self, ri, ci):
        self.get_evTable_rect()
        self.evId_tab_selected = int( self.bt_evTable.get_row0_text( ri ) )

    # 表格选择变化
    def slot_cevTable_itemSelectionChanged(self):
        listitems = self.cevTable.selectedItems()
        val = 0.0
        for item in listitems:
            try:
                if item:
                    val += float(item.text())
            except ValueError:
                break
        ilen = len(listitems)
        tsl = [str(ilen), ' - ', str(int(val))]
        # self.lab_calcul.setText(''.join(tsl))
        print tsl

    # 事件表格的 范围
    def get_evTable_rect(self):
        items = self.cevTable.selectedItems( )
        item0 = items[0]
        item1 = items[-1]
        rect0 = self.cevTable.visualItemRect( item0 )
        rect1 = self.cevTable.visualItemRect( item1 )
        newrect = QRect(rect0.topLeft(), rect1.bottomRight())
        self.row_rect =  newrect

    def slot_date_finished(self):
        modlevj.curdate = gcl.qdateToSDate(self.cdate.date())
        # modlevj.datework.up_date_data()
        modlevj.up_datework()
        self.init_list_widget()
        # self.set_date_background_color()
        self.cdatedata.setText(QString(modlevj.datework.format_h_xev_to_datedata()))

    # 日期改变 事件
    def slot_date_changed(self, qdate):
        self.set_date_background_color()

    def slot_nameList_currText_changed(self, qstr):
        pass


    # 点击损耗按钮后 事件
    def slot_sun_clicked(self):
        if not modlevj.curper: return
        dialog = Ui_sun(pos=self._getMainFrameRightPos())
        dialog.show()
        qe = QEventLoop()
        qe.exec_()
        # if dialog.exec_():
            # pass

    # 双击表格一行后 事件
    def slot_nameList_doubleClicked(self):
        nameText = self.nameListWidget.currentItem().text().trimmed()
        nameText = unicode(nameText)
        pers = modlevj.many_pers.real_name_pers
        if nameText in pers:
            self.findName.setText('')
            modlevj.curper = pers[nameText]
            self.update_display_per()


    # 按下查找按钮后 事件
    def slotFindNameBtnClicked(self):
        self.slot_find_name()


    # 查找人物 事件
    def slot_find_name(self):  # btn find
        editTxt = self.findName.text().trimmed()
        editTxt = unicode(editTxt)


        names = modlevj.many_pers.names
        if editTxt in names:
            modlevj.curper = names[editTxt]
            self.update_display_per()

            #self.save_findnameText_to_pickle()
            self.findName.setText('')


    # 货物列表变化 事件
    def slot_huoBox_changed(self, qstr):
        # 跟据box项目显示数据
        box_t = self.chuobox.currentText()
        try:
            evs = modlevj.perwork.hid_evs.get(int(box_t))
        except ValueError:
            evs = modlevj.perwork.allEvs
        if evs:
            evs.sort(key=lambda x_ev: x_ev.id, reverse=True)
            self.bt_evTable.insert_evs( evs )
            self.set_evTable_textcolor_from_sunInfo( )
            # allsun = modlevj.AllSun( )
            # evids = allsun.get_per_sun_evIds( )
            # if evids:
            #     self.tabOne.set_column_some_items_color( evids )

    # 新建人物 事件
    def slot_new_per(self):
        newPerDialog = Ui_per()
        if newPerDialog.exec_()== QDialog.Accepted:
            modlevj.up_manyPers()
            self.set_findName_edit_completer( )

    # 修改人物 事件
    def slot_modPer(self):
        # print modlevj.curper
        if modlevj.curper:
            dialog = Ui_per(person=modlevj.curper)
            if dialog.exec_():
                modlevj.many_pers.mod(modlevj.curper)
                modlevj.many_pers.up_other_from_persLit( )
                self.set_findName_edit_completer( )

    # 添加新事件  事件
    def slot_add_ev(self):
        if modlevj.curper:
            dialog = NewEv2Ui(pos=self._getMainFrameRightPos())
            if dialog.exec_() == QDialog.Accepted:
                self.update_display_per()
                self.slot_date_finished()



    # 所有按钮点击后产物事件, 根据按钮的文本响应对应的事件
    def slot_btn_clicked(self):
        btnText =  self.focusWidget().text().trimmed()
        btnText = unicode(btnText)
        self.btnFuncDit[btnText]()

    # def slot_btn_add_sun(self):
    #     pass

    # 日期范围设置  事件
    def date_set(self):
        dialog = Ui_set()
        if dialog.exec_(): pass


    # 查看货物事件
    def btn_look_huos(self):
        dialog = Ui_look_huo()
        # if dialog.exec_() == QDialog.Rejected:
        #     print 'end look huo'
        dialog.show()
        qe = QEventLoop()
        qe.exec_()

    # 新建货物事件
    def btn_new_huo(self):
        # print 'new huo'
        dialog = Ui_Huo()
        if dialog.exec_()==QDialog.Accepted:
            modlevj.many_huos.up_huos()

    # 点击排序按钮对应事件
    def btn_sort(self):
        dialog = Ui_sort(pos=self._getMainFrameRightPos())
        # if dialog.exec_(): pass
        dialog.show()
        qe = QEventLoop()
        qe.exec_()
    # 点击 查看人物按钮 后的事件
    def btn_look_per(self):
        dialog = Ui_look_per(pos= self._getMainFrameRightPos())
        # if dialog.exec_(): pass
        dialog.show()
        qe = QEventLoop()
        qe.exec_()

    # 每天的收发情况
    def btn_today_data(self):
        dialog = ui_today_staus.TodayStatusUi(pos=self._getMainFrameRightPos())
        dialog.show()
        qe = QEventLoop()
        qe.exec_()

    def _getMainFrameRightPos(self):
        rect = self.frameGeometry()
        return QPoint(rect.x()+rect.width(), rect.y())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    # per = PersonVj(57, u'王中王', u'官庄', u'13676342309', bLine=0, crdate='2013-12-23',bz=u'在main中创建的')
    # dialog = Ui_per(person=per)
    # dialog = Ui_SunInput()
    # dialog = Ui_look_per()
    dialog = MainUi()
    dialog.show()
    sys.exit(app.exec_())
