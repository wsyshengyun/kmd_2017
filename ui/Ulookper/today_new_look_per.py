# -*- coding:utf8 -*-

import sys
# sys.path.append('..')
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from foo import modlevj
import middle_control
import table
from Uper.today_new_per import Ui_per
QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))

import ui_look_per
class Ui_look_per(QDialog, ui_look_per.Ui_Dialog):
    def __init__(self, pos=None,main=None,  parent=None):
        '''
        main: 主窗口对象
        '''
        super(Ui_look_per, self).__init__(parent)
        self.main = main
        self.setupUi(self)
        self.init_data()
        self.init()
        self.bwidget = middle_control.B_Widget()
        self.bwidget.add_widget(self.cfilter)
        self.bwidget.install_filter(self)
        if pos:
            self.move(pos)

        self.ct_view.customContextMenuRequested.connect(self.slot_table_menu)

    def init_data(self):
        self.val_ty = None
        self.val_line = None
        self.val_adr = None
        self.all = modlevj.AllEvs()
        self.look = modlevj.LookPers()
        # self.tb_data = {}

    def slot_table_menu(self, pos):
        print 'ok'
        # now_widget = self.focusWidget()
        # if now_widget == self.cevTable:
        #     range_table = self.row_rect
        #     if point in range_table:
        #         popMenu = QMenu()
        #         self.q_action = QAction( u'添加/修改(损耗)', self )
        #         popMenu.addAction( self.q_action )
        #         self.q_action.triggered.connect(self.action_add_sunHao)
        #         popMenu.exec_(QCursor.pos())

    def init(self):
        table.LookPerTable.set_sumWidth( self.contentsRect().width() )
        self.table = table.LookPerTable(self.ct_view)

        # self.ct_view.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        # self.ct_view.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)
        self.ct_view.horizontalHeader().setStretchLastSection(True)
        # box-ty
        tys_list = self.look.get_tys( )
        # 什么是错误的 tys_list = self.look.get_tys( ).insert(0, u'') # todo
        tys_list.insert(0, u'')
        middle_control.setComBoxValue( self.cbox_ty, tys_list )

        # box-adr
        adr_list = self.look.get_adrs( )
        adr_list.insert(0, u'')
        middle_control.setComBoxValue( self.cbox_adr, adr_list )

        # box-line
        middle_control.setComBoxValue(self.cbox_line, [u'', u'在线', u'不在线',])

        #
        self.set_lab_rowNums( )

        # 运行一次
        self.slot_sure()


    def eventFilter(self, obj, event):
        self.bwidget.eventFilter(obj, event)
        return super(Ui_look_per, self).eventFilter(obj, event)


    def get_box_val(self):
        self.val_adr = self.cbox_adr.currentText().__str__()
        self.val_ty = self.cbox_ty.currentText().__str__()

        str_line = self.cbox_line.currentText().__str__()
        if str_line == u'在线': self.val_line = 1
        elif str_line == u'不在线' : self.val_line = 0
        else: self.val_line = None

    def set_lab_rowNums(self):
        self.cnum.setText(str(self.ct_view.rowCount()))

    def btn_finded(self, icontext):
        will_remove_row = []
        pass


    def slot_sure(self):
        text = self.cfilter.text().__str__()
        if text:
            pass
        else:
            # 表格显示数据
            self.table.clear()

            self.get_box_val()
            ids_adr = self.look.get_ids_from_adr(self.val_adr)
            ids_ty = self.look.get_ids_from_ty(self.val_ty)
            ids_line = self.look.get_ids_from_bLine(self.val_line)
            ids_somed = self.look.get_samed_ids(ids_adr, ids_ty, ids_line)
            if ids_somed:
                ids_somed.sort(reverse=True)
                self.table.insert_data( self.look.get_pers_from_ids(ids_somed) )

            self.set_lab_rowNums( )

    def slot_cell_changed(self):
        pass

    def slot_cell_double_clicked(self, ri, ci):
        pid_text = self.table.get_row0_text(ri)
        pObj = modlevj.many_pers.id_perObj[int(pid_text)]
        dialog = Ui_per(person=pObj)
        if dialog.exec_(): pass

    def slot_box_changed(self):
        pass

    def slot_edit_text_changed(self, qtsr):
        self.table.show_rows()
        self.table.hide_rows_from_qtsr( qtsr )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Ui_look_per()
    dlg.show()
    sys.exit(app.exec_())
