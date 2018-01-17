uthor__ = 'Administrator'
'''

'''

class BaseMany(object):
    def __init__(self):
        self.lit = []

    def add(self, element):
        for iele in self.lit:
            if iele.id == element.id:
                iele.__dict__.update(element.__dict__)
                return 1
        self.lit.append(element)

    def mod(self, element):
        self.add(element)

    def delElement(self, element):
        self.lit.remove(element)

    def getFromId(self, id):
        for ele in self.lit:
            if ele.id == id:
                return ele

    def getFormTy(self):
        pass





if __name__ == '__main__':
    pass

