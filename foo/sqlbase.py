# coding:utf8
from sqlalchemy import Column, String ,Text, Integer, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///~/kmdkmd2.db", echo=True)
Base = declarative_base(engine)
Session = sessionmaker(engine)
session = Session()


















