#coding:utf8
import sys
sys.path.append('/home/pi/kmdVj/')
import unittest
from test_per import *
from test_ev import *


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # tests = [TestPerson.test_add, TestPerson.test_mod]
    # suite.addTest(tests)
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPerson))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestEvvj))
    runer = unittest.TextTestRunner(verbosity=2)
    runer.run(suite)
    pass

