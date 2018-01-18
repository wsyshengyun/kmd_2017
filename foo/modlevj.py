# coding=utf8
from basevj import BaseMany
from pervj import PersonVj
from huovj import HuoVj
import sun
from evvj import  EvVj, Xev, Xev_expand
import  gcl
from sqlbase import *
__author__ = 'Wsy'
'''
1, 如何添加帮助信息?

'''
import _sql
import datetime
IS_WINDOWS = True
import os
if os.name != 'nt':
    IS_WINDOWS = False

# set sql
class Set1(Base):
    __tablename__ = 'set'
    name = Column(Text, primary_key=True)
    val = Column(Text)



version = 'v1.2'
test_dbpath = "E:\\_Wsy\\kmdkmd.db"
default_db_path = "E:\\kmdkmd.db"
if not IS_WINDOWS:
    test_dbpath = "/home/pi/.data/test_kmdkmd.db"
    default_db_path = "/home/pi/.data/kmdkmd.db"

curpath = default_db_path
testSql = _sql.TestSql(path = curpath)

curper = None
curdate = str(datetime.date.today())


def create_sqlAndTab_ifNotExist():
    testSql.create_many_table( _sql.sqlCreate_tabs_list )

create_sqlAndTab_ifNotExist()

'''new'''
Base.metadata.create_all(engine)


# ***************************************************************设置数据
def new_date_setSql(name, val):
    SQL = _sql.SQL_SET
    datas = [(name, val)]
    testSql.insert(SQL.INSERT, datas=datas)

def update_date_setSql(name, val):
    datas = [(val, name)]
    testSql.update(_sql.SQL_SET.UPDATE, datas)

def find_d1d2_setSql():
    datas = testSql.find_some(_sql.SQL_SET.FIND_DATE_VAL(u'd1'))
    datas2 = testSql.find_some(_sql.SQL_SET.FIND_DATE_VAL(u'd2'))
    if datas and datas2:
        return datas[0][0], datas2[0][0]
    else:
        print 'date not find, will use default'
        tu_ = (u'2015-01-01', u'2100-12-12')
        new_date_setSql(u'd1', tu_[0])
        new_date_setSql(u'd2', tu_[1])
        return tu_



d1 = None
d2 = None

def set_d1_d2(ud1, ud2):
    global d1, d2
    if ud1: d1 = ud1
    if ud2: d2 = ud2

set_d1_d2( * find_d1d2_setSql() )
_sql.SQL_EV.set_d1_d2(d1, d2)

# ***************************************************************per

def new_person(name, address, phone, bLine, crdate, bz=''):
    ''' 需要先检查类型是否正确'''
    datas = [(name, address, phone, bLine, crdate, bz)]
    testSql.insert(_sql.SQL_PERSON.INSERT_AUTO, datas)

def mod_person_obj(perObj):
    datas = [(perObj._name, perObj._adress, perObj._phone, perObj._bLine, perObj._crdate, perObj._bz, perObj._id)]
    testSql.update(_sql.SQL_PERSON.UPDATE, datas)

def mod_person(name, adress, phone, bLine, crdate, bz, id):
    datas = [(name, adress, phone, bLine, crdate, bz, id)]
    testSql.update(_sql.SQL_PERSON.UPDATE, datas)

# ***************************************************************


# ***************************************************************qita
def get_adresss():
    datas = testSql.find_some(_sql.SQL_PERSON.FIND_Lie)
    # print datas
    _datas = [list(tu) for tu in datas]  # 元组元素转化为列表元素
    lit = []
    for el in _datas:

        lit += el
    adr_set = set(lit)
    net_adrs = list(adr_set)
    # 对地址进行按字母排序
    net_adrs.sort(key= lambda x: gcl.getPinyin_first(x))
    # print net_adrs
    return net_adrs


def get_person_all():
    datas = testSql.find_all(_sql.SQL_PERSON.FIND)
    return datas


class ManyPerVj(BaseMany):
    def __init__(self):
        super(ManyPerVj, self).__init__()
        self.init_data()


    def init_data(self):
        # self.lit = []
        self.names = {}
        self.id_names = {}
        self.real_name_pers = {}
        self.id_perObj = {}

    def getOwnPerNames():
       # TODO
        return []

    def up_data(self):
        self.lit=[]
        datas = get_person_all( )
        for tu in datas:
            # per = PersonVj(tu[0], tu[1], tu[2], tu[3], tu[4], tu[5], tu[6])
            per = PersonVj( *tu )
            self.add( per )


    def __str__(self):
        return ', '.join([str(ele) for ele in self.lit])


    def up_other_from_persLit(self):
        self.init_data( )
        for per in self.lit:
            name = per.name
            if not isinstance(name, unicode): name = unicode(name)
            index_name = gcl.getPinyin(name)
            if not per.bLine:
                index_name = '.' + index_name
            self.names[index_name] = per
            self.id_names[per.id] = per.name
            self.id_perObj[per.id] = per
            self.real_name_pers[per.name] = per

    def get_adrs(self):
        return get_adresss()


def up_manyPers():
    many_pers.up_data( )
    many_pers.up_other_from_persLit( )


many_pers = ManyPerVj()
up_manyPers( )





print '<modlevj>'

# ***************************************************************货物

def new_huoAuto(ty, pay, nums, ibvalid, ibLa, crdate, bz):
    datas = [(ty, pay, nums, ibvalid, ibLa, crdate, bz)]
    testSql.insert(_sql.SQL_HUO.INSERT_AUTO, datas)

def new_huo(id, ty, pay, nums, ibvalid, ibLa, crdate, bz):
    datas = [(id, ty, pay, nums, ibvalid, ibLa, crdate, bz)]
    testSql.insert(_sql.SQL_HUO.INSERT, datas)

def mod_huo(ty, pay, nums, ibvalid, ibLa, crdate, bz, id):
    datas = [(ty, pay, nums, ibvalid, ibLa, crdate, bz, id)]
    testSql.update(_sql.SQL_HUO.UPDATE, datas)

def find_all_huos():
    return testSql.find_some(_sql.SQL_HUO.FIND)

def get_huoTys():
    datas = testSql.find_some(_sql.SQL_HUO.FIND_TYS)
    _datas = [list(tu) for tu in datas]
    lit = []
    for el in _datas:
        lit += el
    tys_set = set(lit)
    return list(tys_set)

def get_huo_valid_ids():
    datas = testSql.find_some(_sql.SQL_HUO.FIND_VALID_IDS)
    _datas = [list(tu) for tu in datas]
    lit = []
    for el in _datas:
        lit += el
    lit.sort(key= lambda strid: int(strid), reverse=True)
    return lit


# ***************************************************************事件
def new_evAuto(nameId, huoId, sh, fa, sun, numla, money, crdate, bz):
    datas = [(nameId, huoId, sh, fa, sun, numla, money, crdate, bz)]
    testSql.insert(_sql.SQL_EV.INSERT_AUTO, datas)


def new_ev(id, nameId, huoId, sh, fa, sun, numla, money, crdate, bz):
    datas = [(id, nameId, huoId, sh, fa, sun, numla, money, crdate, bz)]
    testSql.insert(_sql.SQL_EV.INSERT, datas)


def mod_ev(nameId, huoId, sh, fa, sun, numla, money, crdate, bz, id):
    datas = [(nameId, huoId, sh, fa, sun, numla, money, crdate, bz, id)]
    testSql.update(_sql.SQL_EV.UPDATE, datas)

def find_all_evs():
    return testSql.find_some(_sql.SQL_EV.FIND_FROM_D1_D2())



# ***************************************************************损耗


def new_sunAuto(nameId, evId, c_zhi, c_quan, c_dai, c_la, c_kmd, c_zhu, c_ts, crdate):
    datas = [(nameId, evId,  c_zhi, c_quan, c_dai, c_la, c_kmd, c_zhu, c_ts, crdate)]
    testSql.insert(_sql.SQL_SUN.INSERT_AUTO, datas)


def mod_sun(id, nameId, evId, c_zhi, c_quan, c_dai, c_la, c_kmd, c_zhu, c_ts, crdate):
    datas = [(nameId, evId, c_zhi, c_quan, c_dai, c_la, c_kmd, c_zhu, c_ts, crdate, id)]
    testSql.update(_sql.SQL_SUN.UPDATE, datas)


# ***************************************************************主界面
# 建立在线人物拼音字典  {wsy.汪生云:person}

def search_evs(nameid, huoid):
    sql_ev = _sql.SQL_EV
    sql_ev.id_name, sql_ev.id_huo= nameid, huoid
    datas = testSql.find_some(sql_ev.SQL_FIND_NHD())
    return datas

def search_evs_from_huoId(hid):
    return testSql.find_some(_sql.SQL_EV.FIND_EVS_FROM_HUOID(hid))



def search_evs_only(pid):
    SQL = _sql.SQL_EV
    SQL.d1, SQL.d2 = d1, d2
    return testSql.find_some( SQL.SQL_FIND_ONLY( pid ) )

def search_evs_from_date():
    SQL = _sql.SQL_EV
    # todo curdate 是否需要限制
    return testSql.find_some(SQL.SQL_FIND_FROM_DATE(curdate))



def search_sun(nameId=None, d1=d1, d2=d2):
    if None == nameId and curper is not None:
        nameId = curper.id
    SQL = _sql.SQL_SUN
    return testSql.find_some(SQL.FIND_FROM_NAMEID(nameId, d1, d2))


def search_sun_sum(nameId=None):
    if None == nameId and curper is not None: nameId = curper.id
    SQL = _sql.SQL_SUN
    return testSql.find_some(SQL.FIND_SUM_DATA(nameId))




import huovj
class ManyHuos(object):
    def __init__(self):
        self.all_huos = []
        self.id_obj_dict = {}
        self.ty_ids_dict = {}
        self.tys = []
        self.ids = []

    def clear(self):
        self.all_huos = []
        self.id_obj_dict = {}
        self.tys = []
        self.ty_ids_dict = {}
        self.ids = []

    def up_huos(self):
        datas = find_all_huos()
        for tu in datas:
            temp_huo = huovj.HuoVj(*tu)
            ty_temp = temp_huo.ty
            id_temp = temp_huo.id
            self.id_obj_dict[temp_huo.id] = temp_huo
            self.ty_ids_dict[ty_temp] = temp_huo.id
            if ty_temp not in self.tys:
                self.tys.append(ty_temp)
            if id_temp not in self.ids:
                self.ids.append(id_temp)
            self.all_huos.append(temp_huo)

    def get_valid_huos_id(self):
        id_list = []
        if self.all_huos:
            for huo in self.all_huos:
                if huo.bvalid:
                    id_list.append(huo.id)
        return id_list

    # def is_huo_valid(self, huoId):
    #     return  huoId in self.get_valid_huos_id()



    def test_print_huo(self):
        for huo in self.all_huos:
            print huo

    def get_id_ty_dict(self):
        lit = [ (tu[0], tu[1].ty)   for tu in self.id_obj_dict.items() ]
        return dict(lit)

    def get_bla_ids(self):
        bla_list = []
        for huo in self.all_huos:
            if huo.bLa:
                bla_list.append(huo.id)
        return bla_list



many_huos = ManyHuos()
many_huos.up_huos()




# ***************************************************************数据处理

import evvj
class PerWork(object):
    def __init__(self):
        self.init_data()

    def init_data(self):
        self.hid_Xevs = {}
        # self.hid_ownNum = []
        self.hid_ownEvs = {}
        self.hid_evs = {}
        self.allEvs = []
        self.last_ev = None

    def get_ev(self, evid):
        if self.allEvs:
            for ev in self.allEvs:
                if ev.id == evid:
                    return ev

    def set_lastEv(self, ev):
        self.last_ev = ev

    def get_la_own(self):
        bla_list = many_huos.get_bla_ids()
        xev = Xev()
        for huoid in bla_list:
            if huoid in self.hid_evs:
                evs = self.hid_evs[huoid]
                xev.add_evs(evs)
        return xev.get_la_own()

    def up_allEVs_from_sql(self, id=None):
        default_id = id
        if None == default_id:
            default_id = curper.id
        evdatas = search_evs_only(default_id)
        if evdatas:
            for tu in evdatas:
                ev = EvVj(*tu)
                self.add_ev( ev )


    def add_ev(self, ev):
        self.allEvs.append( ev )
        if self.last_ev is None:  # last_ev
            self.last_ev = ev
        else:
            self.last_ev = evvj.get_big_date( ev, self.last_ev )
        h_k = ev.huoId
        evs = self.hid_evs.get( h_k, [] )
        evs.append( ev )
        self.hid_evs[h_k] = evs

    def up_ownEvs(self):
        if self.hid_evs:
            for hid in self.hid_evs:
                xev = Xev()
                evs = self.hid_evs.get(hid)
                xev.add_evs(evs)
                self.hid_Xevs[hid] = xev

            self.hid_ownEvs.update(self.hid_evs)
            for hid in self.hid_evs:
                evs = self.hid_evs.get(hid, None)
                if evs:
                    xev = Xev()
                    xev.add_evs(evs)
                    if xev.is_own_0(): self.hid_ownEvs.pop(hid)
                else:
                    self.hid_ownEvs = {}


    # def test_108(self):
    #     print 'new test ----- ------'
    #     if 108 in self.hid_evs:
    #         for ev in self.hid_evs[108]:
    #             print ev.id, ev.sh, ev.fa


    def get_ownNums(self):
        '''[ [hid, ownNum] ]'''
        hid_nums = {}
        if self.hid_ownEvs:
            for hid in self.hid_ownEvs:
                evs = self.hid_ownEvs.get(hid, None)
                if evs:
                    xev = Xev()
                    xev.add_evs(evs)
                    hid_nums[hid] = xev.get_own()
        return hid_nums.items()

    def get_self_huoIds(self):
        return self.hid_evs.keys()

    def get_last_huoId(self):
        return self.last_ev.huoId if self.last_ev else None


    #---------------------------------date

class DateWork(object):
    def __init__(self):
        self.allEvs = []
        self.h_evs = {}
        self.h_xev = {}

    def clear(self):
        self.allEvs = []
        self.h_evs = {}
        self.h_xev = {}


    def up_date_data(self):
        self.clear()
        evdatas = search_evs_from_date()
        for tu in evdatas:
            ev = EvVj(*tu)
            self.allEvs.append(ev)

            h_k = ev.huoId
            evs = self.h_evs.get(h_k, [])
            evs.append(ev)
            self.h_evs[h_k] = evs

    def get_h_xev(self):
        if self.h_evs:
            for h in self.h_evs:
                xe = Xev()
                xe.add_evs(self.h_evs[h])
                self.h_xev[h] = xe

    def get_names(self):
        lit = []
        if self.allEvs:
            self.allEvs.sort(key=lambda x_ev: x_ev.id)
            print '-----print sorted ev id-------'
            # for ev in self.allEvs:
            #     print ev.id
            id_names = many_pers.id_names
            for ev in self.allEvs:
                # print ev.id
                lit.append(id_names[ev.nameId])
            # lit = set(lit)
            return gcl.uniq_list(lit)
        else:
            return None

    def format_h_xev_to_datedata(self):
        if self.h_xev:
            rlist = []
            for k_hid in self.h_xev:
                xev = self.h_xev[k_hid]
                _list = [k_hid, ':', ' ', xev.sh, ' ', xev.fa, ' ', xev.sun]
                tsr = ''.join([str(i) for i in _list])
                rlist.append(tsr)
            return ' | '.join(rlist)

        else:
            return '-'



perwork = PerWork()
def up_perwork():
    if curper:
        perwork.init_data( )
        perwork.up_allEVs_from_sql( )
        perwork.up_ownEvs( )
        perwork.get_ownNums()
        # for ev in  perwork.hid_evs[108]:
        #     print ev.id, ev.sh, ev.fa



datework = DateWork()
def up_datework():
    datework.up_date_data()
    datework.get_h_xev()








class EvsMethod(object):
    @staticmethod
    def ditEvs_from_huoId( evs, item_str = 'huoId'):
        _dit_huoId_evs = {}
        for ev in evs:
            item_k = getattr(ev, item_str)
            if item_k in _dit_huoId_evs:
                _dit_huoId_evs[item_k].append( ev )
            else:
                _dit_huoId_evs[item_k] = [ev]
        return _dit_huoId_evs


import gcl
class AllEvs(object):
    def __init__(self):
        # self.allevs = []
        # self.pid_xevExpand_Dict = {}
        # self.xevEXpand = Xev_expand()
        self.init_data()

        Xev_expand.set_dict(
                many_huos.get_id_ty_dict()
            )

    def init_data(self):
        self.allevs = []
        self.pid_xevExpand_Dict = {}
        self.xevEXpand = Xev_expand()


    def up_all_evs(self):
        for tu in find_all_evs():
            self.allevs.append(EvVj(*tu))

    def get_xevExpand(self):
        if self.allevs:
            self.xevEXpand.clear()
            self.xevEXpand.add_evs(self.allevs)

    def is_huoId_inEvs(self, hid):
        datas = search_evs_from_huoId(hid)
        return datas != None


    def get_per_xev_expand(self):
        pid_xevExpand_Dict = self.pid_xevExpand_Dict
        for ev in self.allevs:
            if ev.nameId not in pid_xevExpand_Dict:
                xev_expand = Xev_expand()
                xev_expand.add(ev)
                pid_xevExpand_Dict[ev.nameId] = xev_expand
            else:
                xev_expand = pid_xevExpand_Dict[ev.nameId]
                xev_expand.add(ev)
                pid_xevExpand_Dict[ev.nameId] = xev_expand

    def perMoney_sorted(self):
        id_names = many_pers.id_names
        tup_list = self.pid_xevExpand_Dict.items()
        tup_pidAndMoney = [( id_names[tu[0]], tu[1].get_all_money() ) for tu in tup_list]
        tup_pidAndMoney.sort(key=lambda x: x[1], reverse=True)
        # return self.format_perMoney(tup_pidAndMoney)
        return tup_pidAndMoney

    def format_perMoney(self, list_tup):
        return '\n'.join([
            u'{:>12} 元, {:>12}'.format(tu[1], tu[0]) for tu in list_tup
        ])


    def perOwnSorted_keyIs_HuoTy(self, ty):
        id_names = many_pers.id_names
        tup_list = self.pid_xevExpand_Dict.items( )
        own_list = filter(lambda x: x[1].ty_dict[ty].is_own_0() == False
                if ty in x[1].ty_dict else False, tup_list)

        own_list.sort(key=lambda x:gcl.strdate_to_date_M(
            x[1].ty_dict[ty].last_ev.crdate) )  # mok

        result_list = [[id_names[tu[0]],
                        tu[1].ty_dict[ty].get_own(),
                        gcl.days_distance_today_M(tu[1].ty_dict[ty].
                        last_ev.crdate)] for tu in own_list]  # mok
        # return self.format_own_days_names(result_list)
        return result_list


    def perOwnSorted_keyIs_HuoId(self, huoId):
        '''
        {perId:Xev_expand}
                {huoId:xev}

        :return:
        '''
        id_names = many_pers.id_names
        tup_list = self.pid_xevExpand_Dict.items( )
        own_list = filter(lambda x: x[1].hid_dict[huoId].is_own_0() == False
                if huoId in x[1].hid_dict else False, tup_list)

        own_list.sort(key=lambda x:gcl.strdate_to_date_M(
            x[1].hid_dict[  huoId].last_ev.crdate) )  #mok

        result_list = [[id_names[tu[0]],
                        tu[1].hid_dict[huoId].get_own(),
                        gcl.days_distance_today_M(tu[1].hid_dict[huoId].
                        last_ev.crdate)] for tu in own_list] # mok
        # return self.format_own_days_names(result_list)
        return result_list


    def format_own_days_names(self, mat_list):
        return  '\n'.join([
            u'{:>12}个 {:>12}天  {:>12}'.format(
                _list[1], _list[2], _list[0] ) for _list in mat_list]
            )


class LookPers(object):
    def __init__(self):
        self.init_data()
        # self.manyPer = many_pers

    def init_data(self):
        self.allevs = AllEvs()
        self.allevs.up_all_evs()
        self.allevs.get_per_xev_expand()


    def get_adrs(self):
        return get_adresss()

    def get_tys(self):
        return get_huoTys()

    def get_ids_from_adr(self, adr=None):
        if adr != '':
            find_sql = _sql.SQL_PERSON.FIND_IDS_FROM_ADR(adr)
        else:
            find_sql = _sql.SQL_PERSON.FIND_ALL_IDS
        ids = testSql.find_some( find_sql )
        # print len(ids)
        id_list = [None]*len(ids)
        for i, tu in enumerate(ids):
            id_list[i] = tu[0]
        return id_list


    def get_ids_from_bLine(self, bline=None):
        if bline != None:
            find_sql = _sql.SQL_PERSON.FIND_IDS_FROM_LINE(bline)
        else:
            find_sql = _sql.SQL_PERSON.FIND_ALL_IDS
        ids = testSql.find_some(find_sql)
        id_list = [None]*len(ids)
        for i, tu in enumerate(ids):
            id_list[i] = tu[0]
        return id_list

    def get_all_ids(self):
        findSql = _sql.SQL_PERSON.FIND_ALL_IDS
        ids = testSql.find_some(findSql)
        id_list = [None] * len( ids )
        for i, tu in enumerate( ids ):
            id_list[i] = tu[0]
        return id_list


    def get_ids_from_ty(self, ty):
        if ty != '':
            id_list = []
            expand_dict = self.allevs.pid_xevExpand_Dict
            for pid in expand_dict:
                if expand_dict[pid].is_ty_in(ty):
                    id_list.append(pid)
            return id_list
        else:
            return self.get_all_ids()

    # todo 求出两种中种的人物

    def get_samed_ids(self, idlist1, idlist2, idlist3):
        samed_list1 = list( set(idlist1).intersection(set(idlist2)))
        samed_list = list( set(samed_list1).intersection(set(idlist3)))
        return samed_list


    def get_pers_from_ids(self, idList):
        id_obj = many_pers.id_perObj
        perobjs = [ id_obj[pid] for pid in idList]
        return perobjs


def find_sun_data(evid):
    sql = _sql.SQL_SUN.FIND_FROM_EVID(evid)
    datas = testSql.find_some(sql)
    if datas:
        data1 = datas[0]
    else:
        data1 = None
    return  sun.Sun(*data1) if data1 else None

class AllSun(object):
    def __init__(self):
        pass

    def init_data(self):
        pass

    def get_per_sun_evIds(self):
        if curper:
            perid = curper.id
            datas = testSql.find_some(_sql.SQL_SUN.FIND_EVIDS_FROM_PERID(perid))
            evids = None
            if datas:
                evids = [ tu[0] for tu in datas]
            return evids



class TMYData(object):
    '''每天,每月,每年的收货情况'''
    def __init__(self):
        self.huoDit = many_huos.get_id_ty_dict() # id:ty

    # def initData(self):
    #     self.huoDit = many_huos.get_id_ty_dict()

    def _getSomeDay(self, nday):
        today = datetime.date.today()
        litDays = [None]*nday
        for i in range(nday):
            litDays[i] = str( today - datetime.timedelta(i) )
        return litDays


    def _getTy(self, ev):
        return self.huoDit[ev.huoId]

    def test(self, dit):
        if not dit:
            return None
        ilen = len(dit)
        sdayList = self._getSomeDay(ilen)
        # TODO: some


    def getDaysData(self, evs=None):
        if evs is None:
            tus = find_all_evs()
            evs = []
            for i in tus:
                evs.append(EvVj(*i))
        _dit = {}
        for ev in evs:
            idate = ev.crdate.split()[0]  # mok
            ity = self._getTy(ev)
            if idate in _dit:
                if ity in _dit[idate]:
                    gxev = _dit[idate][ity]
                    # if gxev is not None:
                    gxev.add(ev)
                else:
                   xev = Xev()
                   _dit[idate][ity]=xev.add(ev)
                   _dit[idate][ity] = xev
            else:
                xev = Xev()
                xev.add(ev)
                _dit[idate] = {}
                _dit[idate][ity] = xev
                # print xev
        return _dit
        # '2017-01-01':'包装':xev


    def format_dit(self, xevDit, ty):
        _lit = []
        for kd in xevDit:
            if ty in xevDit[kd]:
                xev = xevDit[kd][ty]
                tu = kd, str(xev.sh), str(xev.fa), str(xev.money)
                _lit.append(tu)
        if _lit:
            _lit.sort(key=lambda x: gcl.strdate_to_date_M(x[0]), reverse=True )

        return _lit

# 可能不用
class Test(object):
    def __init__(self, parent=None):
        self.persOwn = []
        self.perAll = []
        self.perAdressAll = []
        self.huoAll = []
        self.huoTys = []
        self.todayEvIds = []











if __name__ == '__main__':
    Session = sessionmaker(engine)
    session = Session()
    #print session.query(PersonVj).count()
    pass



