# coding=utf8

__author__ = 'Administrator'
'''
常用的函数或类
'''
import re
import datetime
import time
from pypinyin import lazy_pinyin
from PyQt4.QtCore import QString, QStringList ,QDate , Qt

def getStime():
    return time.strftime("%H:%M:%S")

def today():
    # return datetime.date.today()
    return  str(datetime.date.today()) + ' ' + time.strftime("%H:%M:%S") # mok

def uniq_list(a_list):
    _list = []
    for ele in a_list:
        if ele not in _list:
            _list.append(ele)
    return _list


def is_phone(tsrPhone):
    p = re.compile('[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$|^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
    match = p.match(tsrPhone)
    return 1 if match else 0

def compare_less_today(qdate):
    today = datetime.date.today()
    inDate = qdateToDate(qdate)
    if inDate < today: return 1
    if inDate == today: return 0
    if inDate > today: return -1


def compare_less_today_str_M(strDate):
    # it = strDate.split()[0]  # mok
    today = datetime.date.today()
    inDate = strdate_to_date_M(strDate)
    if inDate < today: return 1
    if inDate == today: return 0
    if inDate > today: return -1

def qdateToDate(qdate):
    return datetime.date(qdate.year(), qdate.month(), qdate.day())

def qdateToSDate(qdate):
    # return str(qdateToDate(qdate)) + ' ' + getStime()
    return str(qdateToDate(qdate))

def qdateToUdate(qdate):
    return unicode(qdateToDate(qdate))

def qdateToSdate_andTime(qdate):
    idate = qdateToSDate(qdate)
    itime = time.strftime("%H:%M:%S")
    tsr = ' '.join([idate, itime])
    # tsr = da_ti.strftime("%c")   # 日期/时间
    return tsr

def strDateToQdate(sdate):
    return QDate.fromString(sdate, Qt.ISODate)

    # d = sdate.split('-')
    # d = [int(i) for i in d]
    # return QDate(d[0], d[1], d[2])

def strDateTimeToQdate(stida):
    tsr = stida.split()[0]
    return QDate.fromString(tsr, Qt.ISODate)

def dateToQdate(date):
    from PyQt4.QtCore import QDate
    return QDate(date.year, date.month, date.day)

def strdate_to_date_M(str_date):
    only_sdate = str_date.split()[0]
    lit_date_item = only_sdate.split('-')
    lit_date_item_int = map(lambda x: int(x), lit_date_item)
    return datetime.date(*lit_date_item_int)

def days_distance_today_M(str_date):  # mok
    today = datetime.date.today()
    input_date = strdate_to_date_M(str_date)
    return (today-input_date).days


def strList_to_qstrList(str_list):
    return QStringList([QString(i) for i in str_list])

def intList_to_qstrList(int_list):
    str_list = [str(i) for i in int_list]
    return strList_to_qstrList(str_list)

def insertFistPlace(ele, vessel):
    ilit = vessel
    if not isinstance(vessel, list):
        ilit = list(ilit)
    if ele in ilit:
        ilit.remove(ele)
    ilit.insert(0, ele)
    return ilit


def getPinyin(uchine):
    if not isinstance(uchine, unicode): return
    vals = lazy_pinyin(uchine)
    vals = [ut.encode('utf8')[0] for ut in vals]
    pys = ''.join(vals)
    result = ''.join([pys, '.', uchine])
    return result


def getPinyin_first(uchine):
    '''input: u'中心思想'
        return [z, x, s, x]
    '''
    if not isinstance(uchine, unicode): return
    vals = lazy_pinyin(uchine)
    py_list = [ut.encode('utf8')[0] for ut in vals]
    return py_list[0]


def get_name_pyName(pyName):
    lit = pyName.split('.')
    return lit[-1]


# -------------------------------------------@
def log_print(func):
    def _run(*args, **kwargs):
        print '<f: {}>'.format(func.__name__)
    return _run



# 测试
import unittest
class TestDate(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_str_to_date(self):
        self.assertEqual(datetime.date(2017,1,14), strdate_to_date_M('2017-01-14'))

if __name__ == '__main__':
    # unittest.main()
    pass
    utt = '中心思想'
    print getPinyin_first(utt)
