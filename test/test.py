# coding=utf8

__author__ = 'Administrator'
'''

'''


class EvMethod(object):
    def __init__(self):
        pass


class A(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return '|'.join(map(lambda x:str(x), [self.a, self.b]))

    def func(self):
        print self.a, self.b

def main():
    abc = A(1, 2)
    print dir(abc)






if __name__ == '__main__':
    main()
