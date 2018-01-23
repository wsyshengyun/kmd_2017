# coding:utf8
from sqlalchemy import Column, String ,Text, Integer, create_engine, Float, ForeignKey
from sqlalchemy import or_, and_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base



import os
path = ''
if os.name == 'nt':
    #windows 系统
    path = "E://kmdkmd.db"
else:
    # linux 系统
    path = "/home/pi/kmdkmd.db"

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


















