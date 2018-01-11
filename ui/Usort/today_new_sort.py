# -*- coding:utf8 -*-
import sys
# sys.path.append('..')

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from foo import modlevj
from foo import gcl
import middle_control
QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))
import ui_sort
class Ui_sort(QDialog, ui_sort.Ui_Dialog):
    box_content_strs = [u'未交数量', u'金钱']
    def __init__(self, pos=None, parent=None):
        super(Ui_sort, self).__init__(parent)
        self.setupUi(self)
        if pos:
            self.move(pos)
        self.from_id = None
        self.from_ty = None
        self.huoid = None
        self.ty = None
        self.content = None
        self.hideRows = []

        self.init()
        self.init_data()

        self.table.itemSelectionChanged.connect(self.slot_table_itemSelectChanged)
        self.symbolCombo.currentIndexChanged.connect(self.slot_symboCom_changed)

    def init(self):
        # radio
        self.cradio_id.setChecked(True)
        self.slot_radio_clicked()
        self.set_huo_box_items( )
        self.set_content_box_items()


    def init_data(self):
        self.all = modlevj.AllEvs()
        self.all.up_all_evs( )
        self.all.get_per_xev_expand( )

    def set_huo_box_items(self):
        self.cbox_huo.clear( )
        if self.from_ty:
            ty_list = modlevj.many_huos.tys
            qstr_list = QStringList([QString(i) for i in ty_list[::-1]])
            self.cbox_huo.addItems(qstr_list)
        elif self.from_id:
            id_list = modlevj.many_huos.get_valid_huos_id()
            if id_list:
                qstr_list = QStringList([QString(str(i)) for i in id_list[::-1]])
                self.cbox_huo.addItems(qstr_list)

    def set_content_box_items(self):
        self.cbox_content.clear( )
        # content_list = [u'未交数量', u'金钱']
        qstr_list = gcl.strList_to_qstrList(Ui_sort.box_content_strs)
        self.cbox_content.addItems(qstr_list)



    def _set_table_header(self, bn=0):
        self.table_init()
        header_num = [u'姓名',  u'数量(个)', u'未交天数(天)']
        header_money = [u'姓名', u'总工费(元)']

        header = header_money
        if bn==0:
            header = header_num

        self.table.setColumnCount(len(header))
        qstr = QStringList([QString(i) for i in header])
        self.table.setHorizontalHeaderLabels(qstr)
        # self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)

        self.table.setFont(QFont(self.tr('微软雅黑'), 10))


    def _table_insert_data(self, datas):
        ilen = len(datas)
        if not ilen: return
        else:
            self.table.setRowCount(ilen)
            for irow in range(ilen):
                for icol in range(len(datas[0])):
                    data = datas[irow][icol]
                    qtext_data = QString(unicode(data))
                    item = QTableWidgetItem(qtext_data)
                    self.table.setItem(irow, icol, item)


    # 计算选中的列总和
    def slot_table_itemSelectChanged(self):
        # self.table.setToolTip('cell changed')
        listitems = self.table.selectedItems()
        val = 0.0
        for item in listitems:
            try:
                if item:
                    val += float(item.text())
            except ValueError:
                break
        ilen = len(listitems)
        tsl = [str(ilen), ' - ', str(int(val))]
        self.lab_calcul.setText(''.join(tsl))







    def slot_sure(self):
        # print 'sure clicked'

        if self.from_id and not self.is_boxContent_money():
            _id = self.cbox_huo.currentText().__str__()
            _id = int(_id)
            datas = self.all.perOwnSorted_keyIs_HuoId(_id)

        if self.from_ty and not self.is_boxContent_money():
            ty = self.cbox_huo.currentText().__str__()
            datas = self.all.perOwnSorted_keyIs_HuoTy(ty)

        if self.is_boxContent_money():
            datas = self.all.perMoney_sorted()

        self._table_insert_data(datas)

    def slot_huoid_box_changed(self):
        pass
        # print 'huoid_box_changed'

    def slot_content_box_changed(self):
        strItem = self.cbox_content.currentText().__str__()
        self.content = strItem
        # print self.is_boxContent_money()
        bn=0
        if strItem == self.box_content_strs[0]:
            self.set_widget_enable(True)
        else:
            self.set_widget_enable(False)
            bn =1
        self._set_table_header(bn)


    def set_widget_enable(self, bol):
        self.cbox_huo.setEnabled(bol)
        self.cradio_id.setEnabled(bol)
        self.cradio_ty.setEnabled(bol)




    def is_boxContent_money(self):
        return  self.content == Ui_sort.box_content_strs[1]

    def slot_radio_clicked(self):
        self.from_ty =  self.cradio_ty.isChecked()
        self.from_id = self.cradio_id.isChecked()
        self.set_huo_box_items( )
        # self.clear_text( )


    def slot_symboCom_changed(self):
        self._show_table_rows()
        self.filterEdit.setText('')




    # 在编辑框里输入过滤的条件对表格第二列进行过滤
    def slot_filter(self, tt):
        # print tt
        self._show_table_rows()
        try:
            val = int(tt)
        except ValueError:
            return

        sym = self.symbolCombo.currentText()
        rownum = self.table.rowCount()
        if rownum:
            if sym == '=':
                for irow in range(rownum):
                    item = self.table.item(irow, 1)
                    tt =  item.text()
                    # print type(tt), float(tt)

                    if val != int( float(tt) ):
                        self.table.hideRow(irow)
                        self.hideRows.append(irow)
            if sym == '>':
                for irow in range(rownum):
                    item = self.table.item(irow, 1)
                    if val >= int( item.text() ):
                        self.table.hideRow(irow)
                        self.hideRows.append(irow)
            if sym == '<':
                for irow in range(rownum):
                    item = self.table.item(irow, 1)
                    if val <= int( item.text() ):
                        self.table.hideRow(irow)
                        self.hideRows.append(irow)



    def _show_table_rows(self):
        for i in self.hideRows:
            self.table.showRow(i)
        self.hideRows = []

    def eventFilter(self, obj, event):
        # if obj == self and event.type()==QEvent.MouseButtonPress:
        #     self.bmousePressed = True
        #     print '123'
        #
        # if obj == self.table and event.type()==QEvent.MouseButtonRelease:
        #     self.bmousePressed = False
        #
        # if obj == self.table and event.type()==QEvent.MouseMove:
        #     if self.bmousePressed:
        #         print '1'

        return super(Ui_sort, self).eventFilter( obj, event)

    # def mouseMoveEvent(self, event):
    #     print 111111111
    #     # return super(Ui_sort, self).mouseMoveEvent(event)
    #     # pass
    #
    # def mousePressEvent(self, event):
    #     pass
    #
    # def mouseReleaseEvent(self, event):
    #     pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Ui_sort()
    dialog.show()
    sys.exit(app.exec_())
