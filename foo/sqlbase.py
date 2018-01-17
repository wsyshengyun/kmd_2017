# coding:utf8
from sqlalchemy import Column, String ,Text, Integer, create_engine, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///kmdkmd.db", echo=True)
#engine = create_engine("sqlite:///:memory:", echo=True)
Base = declarative_base(engine)
#Session = sessionmaker(engine)
#session = Session()
print '-'*60
#class User(Base):
#    __tablename__ = 'users'
#    id = Column(Integer, primary_key=True)
#    name = Column(String)
#Base.metadata.create_all(engine)



















