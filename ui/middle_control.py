# -*- coding:utf8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import myedit

QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))

def setComBoxValue(box, values):
    values = [QString(unicode(i)) for i in values]
    word = QStringList(values)
    box.addItems(word)

def getCurrentDate():
    return QDate().currentDate()


   # 设置控件的背景色和前景色
def set_widget_color(who, bcolor=Qt.white, fcolor=Qt.black):
    pale = QPalette()
    pale.setColor(QPalette.Text, fcolor)
    who.setAutoFillBackground(True)
    pale.setColor(QPalette.Base, bcolor)
    who.setPalette(pale)


def message(text, title=u'警告'):
    msg_box = QMessageBox( QMessageBox.Warning, QString(title), QString(text) )
    msg_box.exec_( )


class B_Widget(object):
    def __init__(self):
        self.widlist = []

    def add_widget(self, *wids):
        for wid in wids:
            self.widlist.append(myedit.MyEdit(wid))

    def install_filter(self, mainObj):
        for w in self.widlist:
            w.installEventFilter(mainObj)

    def eventFilter(self, obj, event):
        for bw in self.widlist:
            if bw.edit == obj:
                if event.type() == QEvent.FocusIn:
                    # bw.set_fColor(Qt.white)
                    bw.set_focusIn_color()
                if event.type() == QEvent.FocusOut:
                    # bw.set_fColor()
                    bw.set_focusOut_color()

class B_Widget_expand(B_Widget):
    def __init__(self):
        super(B_Widget_expand, self).__init__()
        self.color_list = []

    def add_widget(self, wids, colors):
        if len(wids) != len(colors): return
        # B_Widget.add_widget(wids)
        for d in wids:
            self.widlist.append(myedit.MyEdit(d))

        for icolor in colors:
            self.color_list.append(icolor)

    def eventFilter(self, obj, event):
        for bw in self.widlist:
            if bw.edit == obj:
                if event.type() == QEvent.FocusIn:
                    # bw.set_focusIn_color()
                    idx = self.widlist.index(bw)
                    icolor = self.color_list[idx] if self.color_list else mycolor.edit_background
                    bw.set_color(b_color=icolor, f_color= Qt.black)

                if event.type() == QEvent.FocusOut:
                    bw.set_focusOut_color()
