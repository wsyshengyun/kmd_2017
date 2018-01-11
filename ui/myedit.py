# coding=utf8

__author__ = 'Administrator'
'''

'''
from PyQt4.QtGui import QLineEdit, QPalette
from PyQt4.QtCore import Qt
import mycolor

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
