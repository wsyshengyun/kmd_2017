# coding=utf8

__author__ = 'Administrator'
'''

'''
# from PyQt4.QtGui import QLineEdit, QPalette
# from PyQt4.QtCore import Qt
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import mycolor

# -*- coding:utf8 -*-



class AutoCompleteEdit(QLineEdit):
    def __init__(self, parent=None):
        super(AutoCompleteEdit, self).__init__(parent)
        self.words = QStringList()
        self.words<<'wangshengyun'<<'liuruifei'<<'wangjing'<<'wangjing'<<'lihang'
        self.listView = QListView()
        # self.setTabOrder(self, self.listView)
        self.listView.setWindowFlags(Qt.ToolTip)
        self.model = QStringListModel()
        self.connect(self, SIGNAL("textChanged(QString)"), self.setCompleter)

        #self.connect(self.listView, SIGNAL("clicked()", self.completeText)
        self.listView.clicked.connect(self.completeText)

    def set_words(self, words):
        self.words = words

    def keyPressEvent(self, e):
        if not self.listView.isHidden():
            key = e.key()
            count = self.listView.model().rowCount()
            currentIndex = self.listView.currentIndex()
            self.listView.setFocus()

            if Qt.Key_Down == key or Qt.Key_Tab == key:
                row = currentIndex.row() + 1
                if row >= count:
                    row = 0
                index = self.listView.model().index(row, 0)
                self.listView.setCurrentIndex(index)

            elif Qt.Key_Up == key:
                row = currentIndex.row() - 1
                if row < 0:
                    row = count - 1
                index = self.listView.model().index(row, 0)
                self.listView.setCurrentIndex(index)

            elif Qt.Key_Escape == key:
                self.listView.hide()
            elif Qt.Key_Enter == key or Qt.Key_Return == key:
                if currentIndex.isValid():
                    text = self.listView.currentIndex().data().toString()
                    self.setText(text)
                self.listView.hide()
            else:
                self.listView.hide()
                QLineEdit.keyPressEvent(self, e)
        else:
            QLineEdit.keyPressEvent(self, e)

    def focusOutEvent(self, e): # QFocusEvent e
        # self.listView.hide()
        pass


    def setCompleter(self, text):
        if text.isEmpty():
            self.listView.hide()
            return
        if text.length() >1 and  not self.listView.isHidden():
            return

        s1 = QStringList()
        for word in self.words:
            if word.contains(text):
                s1 << word

        self.model.setStringList(s1)
        self.listView.setModel(self.model)
        if self.model.rowCount() == 0:
            return

        self.listView.setMinimumWidth(self.width())
        self.listView.setMinimumHeight(self.height())

        p = QPoint(0, self.height())
        x = self.mapToGlobal(p).x()
        y = self.mapToGlobal(p).y() + 1
        self.listView.move(x,y)
        self.listView.show()



    def completeText(self, index):
        text = index.data().toString()
        self.setText(text)
        self.listView.hide()






class MyEdit(object):
    def __init__(self, edit):
        self.edit = edit



    def set_color(self, b_color=Qt.white, f_color= Qt.black):
        pale_foreground_red = QPalette()
        pale_foreground_red.setColor(QPalette.Text, f_color)
        self.edit.setAutoFillBackground(True)
        pale_foreground_red.setColor(QPalette.Base, b_color)
        self.edit.setPalette(pale_foreground_red)

    # def set_bfocus_color(self):
    #     self.set_bColor(Qt.blue)

    def set_focusIn_color(self):
        self.set_color(mycolor.edit_background, Qt.white)

    def set_focusOut_color(self):
        self.set_color()

    def setText(self, text):
        self.edit.setText(text)
    def text(self):
        return self.edit.text()

    def installEventFilter(self, obj):
        self.edit.installEventFilter(obj)


if __name__ == '__main__':
    pass
