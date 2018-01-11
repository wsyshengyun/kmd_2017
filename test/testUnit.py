# coding:utf8

import unittest

from pervj import PersonVj
from modlevj import ManyPerVj


class TestPersonMany(unittest.TestCase):
    def setUp(self):
        self.per = PersonVj('李冰', '小营', '13513774637', 'nihao', 1)
        self.sourList =   ['李冰', '小营', '13513774637', 'nihao', 1]
        self.memberList = ['汪生云', '大营', '15037711075', 'happy', 0, 1050]

        self.perS = [
            PersonVj('小红',   '官寺', '15636987589', '我是三好学生', 1),
            PersonVj('王利',   '油田', '18023695212', '不知是好', 1, 1050),
            PersonVj('李志川', '尹庄', '17125634212', '一个良民', 1),
            PersonVj('郭智斌', '肖坡', '18639817086', '当时说好的', 1),
            PersonVj('唐春红', '李庄', '15123968216', '明天天气不错哦', 1),
            PersonVj('王中华', '谢营', '13023568745', '好的东西一起分享', 1)
        ]
    def tearDown(self):
        # print self.per
        pass

    def testMember(self):
        self.assertEqual(self.per.name, '李冰')
        self.assertEqual(self.per.adress, '小营')
        self.assertEqual(self.per.phone, '13513774637')
        self.assertEqual(self.per.bz, 'nihao')
        self.assertEqual(self.per.bWork, 1)
        # self.assertEqual(self.per.id, 1003)


    def testAfterSet(self):
        per2 = PersonVj('李冰', '小营', '13513774637', 'nihao', 1)
        self.setMember(per2)
        self.assertEqual(per2.name, self.memberList[0])
        self.assertEqual(per2.adress, self.memberList[1])
        self.assertEqual(per2.phone, self.memberList[2])
        self.assertEqual(per2.bz, self.memberList[3])
        self.assertEqual(per2.bWork, self.memberList[4])
        self.assertEqual(per2.id, self.memberList[5])


    def testManyPerAdd(self):  # not out
        many = ManyPerVj()
        for per in self.perS:
            many.add(per)

    def testManyPerMod(self):
        newPer = PersonVj('王利', '油田', '11111111111', '不知是好', 1, 1050)
        many = ManyPerVj()
        for per in self.perS:
            many.add(per)
        manyLast = many
        firstPer = many.getFromId(1050)

        many.mod(newPer)
        self.assertEqual(str(many), str(manyLast))
        self.assertEqual(str(firstPer), str(newPer))
        # print firstPer




    def setMember(self, per):
        per.name = self.memberList[0]
        per.adress = self.memberList[1]
        per.phone = self.memberList[2]
        per.bz = self.memberList[3]
        per.bWork = self.memberList[4]
        per.id = self.memberList[5]


    # 构造测试集
def suite():
    suite = unittest.TestSuite()
    # suite.addTest(TestPersonMany('testAfterSet'))
    # suite.addTest(TestPersonMany('testMember'))
    suite.addTest(TestPersonMany('testManyPerMod'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
    # dSuite = unittest.TestLoader().loadTestsFromTestCase(TestPersonMany)
    # unittest.TextTestRunner(verbosity=1).run(dSuite)
