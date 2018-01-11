# coding=utf8

__author__ = 'Administrator'
'''

'''
import pickle
import sys
import modlevj

def linkImport(modStr):
    if not modStr in sys.modules:
        mod = __import__(modStr)
    else:
        eval('import' + modStr)
        mod = eval('reload({})'.format(modStr))
    return mod


path2 = u"E:\\_python\\pycharmFile\\kmdIj2017年2月20日"
mod_huo = 'huoIj'
mod_ev = 'evIj'
mod_per = 'personIj'

if not path2 in sys.path:
    sys.path.append(path2)

# if not mod_huo in sys.modules:
#     huoIj = __import__(mod_huo)  # todo ???__import__(imod)
# else:
#     eval('import huoIj')
#     huoIj = eval('reload(huoIj)')

# import 模块
huoIj = linkImport(mod_huo)
perIj = linkImport(mod_per)
evIj = linkImport(mod_ev)

# start
path = "e:\\kmdIj.txt"
all_thing = None
huos = None
pers = None
evs = None

# todo 关于生成器的使用
def load():
    global all_thing
    with open(path) as f:  # todo 关于with的使用
        all_thing = pickle.load(f)

def get_3():
    global huos, pers, evs
    huos = all_thing['chuo']
    pers = all_thing['cper']
    evs = all_thing['cev']

def get_huo_data():
    datas = []
    for huo in huos:
        tu = huo.idd, unicode(huo.ty),\
             huo.payRate, huo.num, 1, 0, unicode(huo.crDate), unicode(huo.bz)
        datas.append(tu)
    return datas

def get_ev_data():
    datas = []
    for ev in evs:
        tu = ev.idd, ev.nameId, ev.huoId, ev.sh, ev.fa, ev.sun, 0, ev.money, \
                unicode(ev.crDate), unicode(ev.bz)
        datas.append(tu)
    return datas


def get_per_data():
    datas = []
    for per in pers:
        name = per.name
        if '.' in name:
            name = name.split('.')[-1]
        # st = per.st
        # st = 1 if st=='在线' else 0
        st = 1
        tu = per.idd, unicode(name), unicode(per.adr), \
             unicode(per.phone), st, unicode(per.crDate), unicode(per.bz)
        datas.append(tu)
    return datas





if __name__ == '__main__':
    load()
    get_3()
    import _sql
    tsql = _sql.TestSql()
    print '---------------------------------------------start insert pers---------------------------'
    tsql.insert(_sql.SQL_PERSON.INSERT, get_per_data())


    print '---------------------------------------------start insert huos---------------------------'
    tsql.insert(_sql.SQL_HUO.INSERT, get_huo_data())

    print '---------------------------------------------start insert evs---------------------------'
    tsql.insert(_sql.SQL_EV.INSERT, get_ev_data())

    print '--------end-------'
