# -*- coding: utf-8 -*-



from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
# sys.path.append('..')
# from foo import modlevj
import pickle
TODOPATH = './ui/todo.txt'

QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))

class TodoUi(QWidget):
    def __init__(self, pos=None, arg=None):
        super(TodoUi, self).__init__()
        self.resize(400, 400)
        if pos:
            self.move(pos)

        self.listdata = []
        self.listWidget= QListWidget()
        # self.listWidget.verticalHeader().setDefaultSectionSize(20)
        # self.listWidget.verticalHeader().setMinimumSectionSize(20)
        self.cadd = QPushButton(self.tr(u"增加一条"))
        self.cdel = QPushButton(self.tr(u"删除一条"))
        self.csave = QPushButton(self.tr(u"保存"))
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.listWidget, 0, 0, 8, 1)
        layout.addWidget(self.cadd, 0, 1)
        layout.addWidget(self.cdel, 1, 1)
        layout.addWidget(self.csave, 2, 1)


        data = self._getData()
        if data is not None:
            self.listdata = data
            for i in self.listdata:
                item = QListWidgetItem(i)
                self.listWidget.addItem(item)
                self._setItemHeight(item)


        self.listWidget.itemDoubleClicked.connect(self.list_itemDoubleClicked)
        self.connect(self.cadd, SIGNAL("clicked()"), self.clicked_addItem)
        self.connect(self.cdel, SIGNAL("clicked()"), self.clicked_delItem)
        self.connect(self.csave, SIGNAL("clicked()"), self.clicked_save)
    def _getData(self):
        with open(TODOPATH, 'r') as file:
            try:
               data =  pickle.load(file)
            except :
                print 'EOFERROR'
            else:
                return data


    def _dumpData(self, data):
        with open(TODOPATH, 'w+') as file:
            pickle.dump(data, file)

    def _setItemHeight(self, item):
        item.setSizeHint(QSize(self.listWidget.width(), 30))
        font = item.font()
        font.setPointSize(16)
        item.setFont(font)

    def clicked_save(self):
        # curitem = self.listWidget.currentItem()
        count = self.listWidget.count()
        lit_item_text = []
        for i in range(count):
            text = self.listWidget.item(i).text()
            lit_item_text.append(text)
        self._dumpData(lit_item_text)

        pass


    def _setItemEnableEdit(self, item):
        item.setFlags(item.flags()|Qt.ItemIsEditable)
        self.listWidget.editItem(item)

    def list_itemDoubleClicked(self, curItem):
        self._setItemEnableEdit(curItem)

    def clicked_addItem(self):
        count = self.listWidget.count()
        newItem = QListWidgetItem('')
        self.listWidget.addItem(newItem)
        self._setItemHeight(newItem)
        self._setItemEnableEdit(newItem)

    def clicked_delItem(self):
        count = self.listWidget.count()
        if count>0:
            curow = self.listWidget.currentRow()
            self.listWidget.takeItem(curow)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    dia = TodoUi()
    dia.show()
    sys.exit(app.exec_())

