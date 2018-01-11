# -*- coding:utf8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))

class EVDialog(QDialog):
    def __init__(self, parent=None):
        super(EVDialog, self).__init__(parent)
        self.resize(400, 300)
        self.tab = QTableWidget()
        lay = QVBoxLayout()
        self.setLayout(lay)
        labtable = QLabel(self.tr(u'测试表格'))
        self.btn_addrow = QPushButton(u'add')
        self.btn_addrow.clicked.connect(self.tab_create_row_to_first)
        # self.tab.itemClicked.connect(self.current_item_changedStyle)
        self.connect(self.tab, SIGNAL("itemClicked(QTableWidgetItem)"), self.current_item_changedStyle)


        lay.addWidget(labtable)
        lay.addWidget(self.btn_addrow)
        lay.addWidget(self.tab)
        self.init_table()

    def current_item_changedStyle(curItem):
        print 'current_item_changedStyle:'
        print type(curItem)
        pass

    def init_table(self):
        self.tab.setColumnCount(3)
        self.tab.setRowCount(2)

        world = QStringList()
        world<<u'abc'<<u'122'<<u'33'
        self.tab.setHorizontalHeaderLabels(world)


        item = QTableWidgetItem()
        button = QPushButton(self.tr(u'确定'))
        button.clicked.connect(self.out_text)
        # item.setText('items')
        # self.tab.setItem(0 ,0 , item)

        self.tab.setCellWidget(0, 0, button)

        self.init_style()

    def init_style(self):
        # self.tab.setSelectionMode(QAbstractItemView.SelectItems)
        self.tab.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tab.resizeColumnsToContents()
        self.tab.resizeRowsToContents()

        # self.tab.setShowGrid(True)

        # 设置格式
        self.tab.setFrameShape(QFrame.NoFrame)  #无边框
        # self.tab.setShowGrid(False) #设置不显示格子线
        # self.tab.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置选择行为时每次选择一行
        # self.tab.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置不可编辑
        # self.tab.setSelectionMode(QTableWidget.SingleSelection)  # 只能选择一行

        self.tab.verticalHeader().setVisible(False)  # 垂直表头不可见
        # self.tab.horizontalHeader().setVisible(False)  # 水平表头不可见
        # self.tab.horizontalHeader().setFixedHeight(25) # 设表头高度
        # self.tab.verticalHeader().setDefaultSectionSize(30)  # 设置行距
        # self.tab.horizontalHeader().setStretchLastSection(True)  # 设置充满表宽度

        # 去掉选中虚线
        # self.tab.setAlternatingRowColors(True)
        # self.tab.setFocusPolicy(Qt.NoFocus)
        # self.tab.setItemDelegate(NoFocusDelegate())
        palette = QPalette()
        palette.setColor(QPalette.Base, QColor(255, 255, 255))
        palette.setColor(QPalette.AlternateBase, QColor(233,245,252))
        self.tab.setPalette(palette)


    def out_text(self):
        print 'nihao'
        print '--------------type item'
        print self.tab.itemAt(0, 0)


    def check_first_line_empty(self):
        countColumn = self.tab.columnCount()
        print countColumn
        if countColumn<=0:
            return True
        for i in range(countColumn-1):
            item = self.tab.item(0, i)
            if item is not None and item.text()!='':
                return False
        return True



    def tab_create_row_to_first(self):
        if self.check_first_line_empty():
            return
        else:
            self.tab.insertRow(0)
        pass

class NewEvDialog(QDialog):
    def __init__(self, parent=None):
        super(NewEvDialog, self).__init__(parent)
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.tab = QTableWidget()
        self.btnSure = QPushButton('ok')

        layout.addWidget(self.tab)
        layout.addWidget(self.btnSure)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = NewEvDialog()
    dialog.show()
    sys.exit(app.exec_())
