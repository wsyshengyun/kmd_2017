# coding:utf8
from sqlalchemy import Column, String ,Text, Integer, create_engine, Float, ForeignKey
from sqlalchemy import or_, and_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

LINUXNAME = 'posix'
WINDOWSNAME = 'nt'
SQLDATA_PATH_ON_LINUX =  "/home/pi/kmdkmd.db"
SQLDATA_PATH_ON_WINDOW = "E://kmdkmd.db"
import os
def getOsName():
    return os.name

path = ''
if os.name ==WINDOWSNAME:
    #windows 系统
    path = SQLDATA_PATH_ON_WINDOW
elif getOsName() == LINUXNAME:
    # linux 系统
    path = SQLDATA_PATH_ON_LINUX
else:
    # 添加异常
    pass

engine = create_engine("sqlite:///%s"%path, echo=False)
#engine = create_engine("sqlite:///:memory:", echo=True)
Base = declarative_base(engine)
Session = sessionmaker(engine)
session = Session()
print '-'*60

def add_data(data):
    session = Session()
    try:
        try:
            ilen = len(data)
            session.add_all(data)
        except TypeError:
            session.add(data)
    except:
        session.rollback()
    session.commit()
    session.close()

def mod_data(new):
    session = get_session()
    session.merge(new)
    session.commit()
    session.close()
    pass

def del_data(obj):
    session =get_session()
    session.delete(obj)
    session.commit()
    session.close()

def get_session():
    return Session()


def combain_list(datalist):
    lit = []
    for tu in datalist:
        lit += list(tu)
    return lit


















