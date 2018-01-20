# coding=utf8
from sqlbase import *

__author__ = 'Administrator'
'''

'''
class Sun(Base):
    __tablename__ = 'sunc'
    id = Column(Integer, primary_key=True)
    nameId = Column(Integer)
    evId= Column(Integer)
    c_zhi= Column(Integer)
    c_quan = Column(Integer)
    c_dai= Column(Integer)
    c_la= Column(Integer)
    c_kmd= Column(Integer)
    c_zhu= Column(Integer)
    c_ts= Column(Float)
    crdate= Column(Text)

    def __init__(self, id, namdId, evId, c_zhi, c_quan, c_dai, c_la, c_kmd, c_zhu, c_ts, crdate):
        self.id = id
        self.namdId = namdId
        self.evId = evId
        self.c_zhi = c_zhi
        self.c_quan = c_quan
        self.c_dai = c_dai
        self.c_la = c_la
        self.c_kmd = c_kmd
        self.c_zhu = c_zhu
        self.c_ts = c_ts
        self.crdate = crdate
    def toList(self):
        return self.id, self.nameId, self.evId, self.c_zhi, self.c_quan, \
                self.c_dai, self.c_la, self.c_kmd, self.c_zhu, self.c_ts, \
                self.crdate
    def add(self):
        add_data(self)
    def mod(self, new):
        mod_data(new)
    def delself(self):
        del_data(self)
    def __str__(self):
        pass



if __name__ == '__main__':
    pass
