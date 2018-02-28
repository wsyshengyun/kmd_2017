# -*- coding: utf-8 -*-
import unittest
from foo.evvj import EvVj

class TestEvvj(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tu = 1, 1001, 102, 1000, 2000, 10, 500, 100.0,None, u'nihao'
        # cls.evobj = EvVj(*tu)

        cls.evobj = EvVj(id=1, nameId=1001, huoId=102, sh=1000, fa=2000,
                sun=10, numla=500, money=100.0, crdate=u'2016-02-12',
                bz=u'nihao')

    @classmethod
    def tearDown(cls):
       pass

    def test_toStr(self):
        objstr = self.evobj.toStr()
        nowStr = '1|1001|102|1000|2000|10|500|100.0|2016-02-12|nihao'
        self.assertEqual(objstr,  nowStr)


