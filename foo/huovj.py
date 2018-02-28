#coding=utf8

from sqlbase import *
import datetime

__author__ = 'Administrator'
'''

'''

tys = ['包装', '竹圈', '粘纸' ,'包装(无蜡)' ]

class HuoVj(Base):
    __tablename__ = 'huo'
    id = Column(Integer, primary_key=True)
    ty = Column(Text)
    pay= Column(Float)
    nums = Column(Integer)
    bvalid= Column(Integer)
    bLa= Column(Integer)
    crdate= Column(Text)
    bz= Column(Text)
    def __init__(self, id, ty, pay, nums, bvalid=1, bLa = 0, crdate=None, bz=""):
        self.id = id
        self.ty = ty
        self.pay = pay
        self.nums = nums
        self.bvalid = bvalid
        self.bLa = bLa
        self.bz = bz
        self.crdate = crdate
        if None == crdate:
            self.crdate = datetime.date.today()
    def toList(self):
        return self.id, self.ty, self.pay, self.nums, self.bvalid, self.bLa, self.crdate, self.bz

    def add(self):
            add_data(self)
    def mod(self, new):
        mod_data(new)
    def delself(self):
        del_data(self)

    def __str__(self):
        return '.'.join(str(i) for i in [
            self.id,
            self.ty,
            self.pay,
            self.nums,
            self.bvalid,
            self.bLa,
            self.bz,
            self.crdate
        ])

    def toStr(self):
        return '|'.join(str(i) for i in [
            self.id,
            self.ty,
            self.pay,
            self.nums,
            self.bvalid,
            self.bLa,
            self.bz,
            self.crdate
        ])






class Csun(object):
    def __init__(self, id, c_zhi, c_quan, c_dai, c_la, c_zhu, c_ts, crdate=None):
        self.id = id
        self.c_zhi = c_zhi
        self.c_quan = c_quan
        self.c_dai = c_dai
        self.c_la = c_la
        self.c_zhu = c_zhu
        self.c_ts = c_ts
        self.crdate = crdate

        if None == crdate:
            self.crdate = datetime.date.today()

if __name__ == '__main__':
    pass
