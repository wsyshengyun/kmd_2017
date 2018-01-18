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

    def __init__(self, id, namdId, evId, zhi, quan, dai, la, kmd, zhu, tiesi, crdate):
        self.id = id
        self.evId = evId
        self.tiesi = tiesi
        self.zhu = zhu
        self.kmd = kmd
        self.la = la
        self.dai = dai
        self.quan = quan
        self.zhi = zhi
        self.namdId = namdId
        self.crdate = crdate

    def __str__(self):
        pass



if __name__ == '__main__':
    pass
