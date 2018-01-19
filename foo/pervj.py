# encoding: utf-8
from sqlbase import *

import datetime as dt
import sys

import _sql
#import unit

reload(sys)
sys.setdefaultencoding('utf8')
class PersonVj(Base):
    __tablename__ = 'person_1'
    id = Column(Integer, primary_key = True )
    name = Column(Text)
    adress = Column(Text)
    phone = Column(Text)
    bLine = Column(Integer)
    crdate = Column(Text)
    bz = Column(Text)


    def __init__(self, id, name, adress, phone, bLine=1, crdate=None, bz=''):

        self.id = id
        self.name = name
        self.adress = adress
        self.phone = phone
        self.bz = bz
        self.bLine = bLine
        if None == crdate:
            self.crdate = dt.date.today()
        else:
            self.crdate = crdate

    def add(self):
        add_data(self)
    def mod(self, new):
        mod_data(new)
    def delself(self):
        del_data(self)


    def __str__(self):
        temList = ['[',  str(self.id),
                    self.name,
                    self.phone,
                    self.adress,
                    str(self.bLine),
                    self.crdate,
                    self.bz,  ']'
                    ]
        return ' '.join(temList)

    def get_tu(self):
        return str(self.id), self.name, self.adress, self.phone, str(self.bLine), self.crdate, self.bz

    def get_per_list_to_tooltip(self):
        return [
            u'编号:' + str( self.id ),
            u'地址:' + self.adress,
            u'电话:' + self.phone,
            u'是否在线:' + str(self.bLine),
            u'登记日期:' + self.crdate,
            u'备注:' + self.bz,
        ]


i=0
def get_Per():
    global i
    i = i+1
    name = unit.get_name().decode('utf8')
    adress = unit.get_address().decode('utf8')
    phone = unit.get_phone().decode('utf8')
    bz = "".decode('utf8')
    crdate = unit.get_date()
    bLine =  unit.rd.choice([1,0,1,1,1])
    id = None
    return (name, adress, phone, bLine, str(crdate), bz)

def printPers(pers, lit=None):
    for tuPer in pers:
        newPer = PersonVj(tuPer[0], tuPer[1], tuPer[2], tuPer[3], tuPer[4], tuPer[5], tuPer[6])
        if lit is not None:
            lit.append(newPer)
        # print newPer

if __name__ == '__main__':

    pass
    #testSql = _sql.TestSql()
    '''把人物数据插入到数据库中'''
    lit = [get_Per() for i  in range(10)]
    # for i in lit:
    #     print str(i)
    testSql.insert(_sql.SQL_PERSON.INSERT_AUTO, lit)
    #
    ''' 读取人物数据'''
    lit = []
    # pers = testSql.find_all(_sql.SQL_PERSON.FIND)
    #
    # if pers:
    #     print len(pers)
    #     printPers(pers, lit)




    ''' 有条件的读取人物数据'''
    # pers = testSql.find_some(_sql.SQL_PERSON.FIND_ADRESS)
    # printPers(pers, lit)





