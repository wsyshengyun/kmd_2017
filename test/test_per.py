# coding:utf8

import unittest
from foo.pervj import *
from foo.sqlbase import *

class TestPerson(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(engine)
        cls.session = get_session()
        cls.nper = PersonVj(id = None, name = u'汪生云1', adress=u'谢营', phone='15037711075',bLine=1, crdate='2018-01-16', bz='123')
        cls.per2= PersonVj(id = None, name = u'汪生云2', adress=u'谢营1', phone='1503771107l9',bLine=1, crdate='2018-01-16', bz='123')

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        pass

    # def setUp(self):
        # Base.metadata.create_all(engine)
        # self.session = get_session()
        # pass

    # def tearDown(self):
        # self.session.close()
        # pass

    def test_add_delete(self):
        # add_data(self.nper)
        self.nper.add()
        self.nper.delself()

    def test_mod(self):
        self.per2.add()
        print self.session.query(PersonVj).get(1)
        self.per2.delself()
        print self.session.query(PersonVj).get(4)





