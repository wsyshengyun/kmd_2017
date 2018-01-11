# coding=utf8

__author__ = 'Administrator'
'''

'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import test_ui


class TestUi(QDialog, test_ui.Ui_Dialog):
    def __init__(self, parent=None):
        super(TestUi, self).__init__(parent)
        self.setupUi(self)
        self.init()

    def init(self):
        # QPalette.Base  将要对编辑框背景色设置
        # QPalette.Text  将要对编辑框前景色（文字）进行设置

        # self.lineEdit.setDisabled(True)
        self.lineEdit.setAutoFillBackground(True)
        paltte = QPalette()
        paltte.setColor(
            # QPalette.Active,
            QPalette.Text, Qt.red)
        self.lineEdit.setPalette(paltte)


        paltte = QPalette()
        paltte.setColor(
            # QPalette.Active,
            QPalette.Text, Qt.red)
        self.lineEdit.setPalette(paltte)


        # self.pushButton.setAutoFillBackground(True)
        # paltte = QPalette()
        # paltte.setColor(QPalette.ButtonText, Qt.red)
        # paltte.setColor(QPalette.Active, QPalette.Button, Qt.green)
        # self.pushButton.setPalette(paltte)




    def slot_finished(self):
        self.lineEdit.setAutoFillBackground(True)
        paltte = QPalette()
        paltte.setColor(
            # QPalette.Active,
            QPalette.Base, Qt.white)
        self.lineEdit.setPalette(paltte)

        pass

    def slot_text_changed(self):
        pass

    def slot_sure(self):
        pass

    def slot_date_changed(self):
        pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = TestUi()
    dialog.show()
    sys.exit(app.exec_())
