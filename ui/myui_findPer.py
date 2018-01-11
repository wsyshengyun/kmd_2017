# -*- coding:utf8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import middle_control
QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))

class FindPerUi(QDialog):
    """docstring for FindPerUi."""
    def __init__(self, parent=None):
        super(FindPerUi, self).__init__(parent)
        vlayout = QVBoxLayout()
        self.setLayout(vlayout)
        lab = QLabel(u'Wang Sheng Yun')

        vlayout.addWidget(lab)

class MLineEdit(QLineEdit):
    """docstring for MLineEdit."""
    def __init__(self, arg=None):
        super(MLineEdit, self).__init__(arg)
        # self.setInputMask('nihao')

    # def mousePressEvent(self, event):
    #     self.originX = event.globalX()
    #     self.originY = event.globalY()
        # dialog = FindPerUi()
        # # if dialog.exec_(): pass
        # dialog.move(self.originX, self.originY)
        # dialog.show()
        # qe = QEventLoop()
        # qe.exec_()



    # def focusInEvent(self, event):
    #     # print event.gotFocus()
    #     print 'gotFoucus3333'
    #
    #     print  '============= '


class FloatDialog(QDialog):
    """docstring for FloatDialog."""
    def __init__(self, arg=None):
        super(FloatDialog, self).__init__(arg)
        self.arg = arg
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        vlayout = QVBoxLayout()
        self.setLayout(vlayout)

        lab1 = QLabel(u'wo shi wang sheng yun')
        self.btn = QPushButton(u'sure')
        vlayout.addWidget(lab1)
        vlayout.addWidget(self.btn)
        self.resize(300,100)



class MyDialog(QDialog):
    """docstring for MyDialog."""
    def __init__(self, arg=None):
        super(MyDialog, self).__init__(arg)

        self.resize(300, 200)

        self.testcombo = QComboBox()
        self.testcombo.setCursor(Qt.PointingHandCursor)
        self.testcombo.setFixedSize(60,22)
        self.testcombo.setToolTip(u'serach')
        word = QStringList()
        word<<'1'<<'2'<<'ssssss'
        self.testcombo.addItems(word)
        self.testcombo.currentIndexChanged.connect(self.box_index_changed)

        # testBtn.setStyleSheet("QPushButton{border-image:url(:/images/icon_search_normal); background:transparent;} QPushButton:hover{border-image:url(:/images/icon_search_hover)}                                      QPushButton:pressed{border-image:url(:/images/icon_search_press)} ")
        self.testEdit = QLineEdit()
        margins = self.testEdit.textMargins()
        self.testEdit.setTextMargins(margins.left(), margins.top(), self.testcombo.width(), margins.bottom())
        self.testEdit.setPlaceholderText('please input text')
        testlayout = QHBoxLayout()
        self.testEdit.setLayout(testlayout)
        reg = QRegExp(r'[-]?[0-9]+[\+|\-|\*]?[0-9]+ ')
        validator = QRegExpValidator(reg, self.testEdit)
        self.testEdit.setValidator(validator)

        testlayout.addStretch()
        testlayout.addWidget(self.testcombo)
        testlayout.setSpacing(0)
        testlayout.setContentsMargins(0,0,0,0)

        # ========================================================
        hlayout = QHBoxLayout()
        self.setLayout(hlayout)
        # self.input = MLineEdit()
        self.btn = QPushButton('ok')
        self.btn.clicked.connect(self.ok_clicked)
        self.btn.installEventFilter(self)

        # hlayout.addWidget(self.input)
        hlayout.addWidget(self.testEdit)
        hlayout.addWidget(self.btn)
        self.testEdit.installEventFilter(self)
        self.testcombo.installEventFilter(self)

    def ok_clicked(self):
        self.dialog = FloatDialog()
        # self.dialog.move(0,0)
        self.dialog.show()
        qe = QEventLoop()
        qe.exec_()

        print 'clicked ok btn'

    def leave_okBtn(self):
        if self.dialog:
            self.dialog.close()
            self.dialog=None

        print 'leave ok btn'

    def test_print(self):
        print 'test1111'

    def box_index_changed(self, index):
        print index
        self.testEdit.setText(self.testcombo.currentText())


    def eventFilter(self, obj, event):
        # print obj
        # if obj==self.testcombo and event.type()==QEvent.HoverEnter:
        #     print 1111
        #     self.testcombo.showPopup()

        if obj==self.btn and event.type() == QEvent.FocusOut:
            # self.leave_okBtn()
            pass


        return super(MyDialog, self).eventFilter(obj, event)

    # def mouseMoveEvent(self, event):
    #     print '111'
    #     pass


    # def mousePressEvent(self, event):
    #     originX = event.globalX()
    #     originY = event.globalY()
    #     print originX, originY

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = MyDialog()

    # dialog = FloatDialog()
    dialog.show()
    sys.exit(app.exec_())
