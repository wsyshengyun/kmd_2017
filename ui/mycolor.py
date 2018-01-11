# coding=utf8

__author__ = 'Administrator'
'''
color
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import QColor

def int_hex(h):
    return int( h, 16 )

date_last = Qt.gray
date_tommorrow = Qt.white
date_today = QColor(int_hex('0xB0E0E6'))

money_f = Qt.red
lab_date_sum = QColor(int_hex('0x808a87'))

edit_background = QColor(int_hex('0x4169E1'))
sh_edit_b = QColor(int_hex('0xFFD700'))
fa_edit_b = QColor(int_hex('0x308014'))
money_edit_b = QColor(int_hex('0xFF6100'))




if __name__ == '__main__':
    pass
