# coding=utf8

__author__ = 'Administrator'
'''

'''

import datetime
import time
from sqlbase import *


# 个人事件情况
class EvVj(Base):
    __tablename__ = 'evs'
    id = Column(Integer, primary_key=True)
    nameId = Column(Integer, ForeignKey('person_1.id'))
    huoId= Column(Integer, ForeignKey('huo.id'))
    sh= Column(Integer)
    fa= Column(Integer)
    sun= Column(Integer)
    numla= Column(Integer)
    money= Column(Float)
    crdate= Column(Text)
    bz = Column(Text)
    huos = relationship('HuoVj', backref='_evs')
    pers = relationship('PersonVj', backref='_evs')

    def __init__(self, id, nameId, huoId, sh, fa, sun, numla, money, crdate=None, bz=''):
        self.id = id
        self.nameId = nameId
        self.huoId = huoId
        self.sh = sh
        self.fa = fa
        self.sun = sun
        self.numla = numla
        self.money = money
        self.crdate = crdate
        self.bz = bz

        if None == crdate:
            # self.crdate = datetime.date.today()
            self.crdate = str(datetime.date.today()) + ' ' + time.strftime("%H:%M:%S") # mok
    def toStr(self):
        return '|'.join([self.id, self,nameId, self.huoId, self.sh, self.fa, self.sun, self.numla, self.money,
        self.crdate, self.bz])

    def toList(self):
        return self.id, self.nameId, self.huoId, self.sh, self.fa, self.sun, self.numla, self.money, self.crdate, self.bz
    def add(self):
            add_data(self)
    def mod(self, new):
        mod_data(new)
    def delself(self):
        del_data(self)


    def get_tu(self):
        return str(self.id), str(self.nameId), str(self.huoId), str(self.sh),\
               str(self.fa), str(self.sun), str(self.numla), str(self.money), self.crdate, self.bz



import datetime
import gcl


def get_big_date(ev, ev2):
    dev = gcl.strdate_to_date_M( ev.crdate )
    dev2 =  gcl.strdate_to_date_M( ev2.crdate )
    return ev if dev>dev2 else ev2




class Xev(object):
    def __init__(self, sh=0, fa=0 ,sun=0, numla = 0, money=0.0, last_ev=None):
        self.sh=sh
        self.fa=fa
        self.sun=sun
        self.numla = numla
        self.money = money
        self.last_ev = last_ev

    def __eq__(self, other):
        if self.sh == other.sh \
            and self.fa == other.fa \
            and self.sun == other.sun \
            and self.money == other.money \
            and self.numla == other.numla:
            return True
        else: return False
    def __str__(self):
        return ' '.join( [str(i) for i in [self.sh, self.fa, self.sun, self.numla, self.money]] )

    def get_own(self):
        return self.fa-self.sh-self.sun

    def is_own_0(self):
        return self.get_own() == 0

    def get_la_own(self):
        return self.numla - self.fa


    def add(self, ev):
        self.sh += ev.sh
        self.fa += ev.fa
        self.sun += ev.sun
        self.numla += ev.numla
        self.money += ev.money
        if  self.last_ev is None:
            self.last_ev = ev
        else:
            # dlast = gcl.strdate_to_date_M(self.last_ev.crdate)
            # dev = gcl.strDateToQdate(ev.crdate)
            # if dev > dlast:
            #     self.last_ev = ev
            self.last_ev = get_big_date(self.last_ev, ev)
            pass


    def add_evs(self, evs):
        for ev in evs:
            self.add(ev)

class Xev_expand(object):
    id_ty_dict = {}
    @classmethod
    def set_dict(cls, id_ty_dict):
        cls.id_ty_dict.update(id_ty_dict)

    def __init__(self):
        self.hid_dict= {}
        self.ty_dict = {}

    def clear(self):
        self.hid_dict= {}
        self.ty_dict = {}

    def add(self, ev):
        hidDict = self.hid_dict
        if ev.huoId not in hidDict:
            xev = Xev()
            xev.add(ev)
            hidDict[ev.huoId] = xev
            # tyDict[ev.]

        else:
            xev = hidDict[ev.huoId]
            xev.add(ev)
            hidDict[ev.huoId] = xev

        # ty_dict
        hid = ev.huoId
        ty = Xev_expand.id_ty_dict[hid]
        tyDict = self.ty_dict
        if ty not in tyDict:
            xev = Xev()
            xev.add(ev)
            tyDict[ty] = xev
        else:
            xev = tyDict[ty]
            xev.add(ev)
            tyDict[ty] = xev


    def add_evs(self, evs):
        for ev in evs:
            self.add(ev)

    def is_ty_in(self, ty):
        return True if ty in self.ty_dict else False

    def get_ty_num(self):
        return len(self.ty_dict)

    def get_all_money(self):
        xev_values = self.hid_dict.values()
        sumMoney = 0.0
        for xev in xev_values:
            sumMoney += xev.money
        return sumMoney


    def get_kid3_dict(self):
        _dict = {}
        for hid in self.hid_dict:
            _dict[hid] = [
                self.hid_dict[hid].fa,
                self.hid_dict[hid].get_own(),
                self.hid_dict[hid].sun,
            ]

        return _dict


# class Yev(object):
#     def __init__(self, sh=0, fa=0 ,sun=0, numla = 0, money=0.0 ):
#         self.sh=sh
#         self.fa=fa
#         self.sun=sun
#         self.numla = numla
#         self.money = money
#         self.huoId = None
#         self.crdate = None







class DateEvs(object):
    def __init__(self):
        pass


    def addev(self, ev):

        pass

    def _get_all_evs(self):
        return None





import unittest
class TestEv(unittest.TestCase):
    def setUp(self):
        self.ev1 = EvVj(12, 1002, 103, 1000, 1000, 20, 2000, 50.0, '2017-01-14', u'我是ev1')
        self.ev2 = EvVj(13, 1003, 103, 1500, 2000, 00, 2000, 75.0, '2017-01-15', u'我是ev2')
        self.ev1.set_ev_from_date(self.ev2)


    def tearDown(self):
        pass

    def testXev(self):
        self.assertEqual(self.ev1, self.ev2)

if __name__ == '__main__':
    unittest.main()
