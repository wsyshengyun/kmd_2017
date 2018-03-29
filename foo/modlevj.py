# coding=utf8
from basevj import BaseMany
from pervj import PersonVj
from huovj import HuoVj
from sun import Sun
from evvj import  EvVj, Xev, Xev_expand
import  gcl
from sqlbase import *
# import _sql
import datetime
import logging
import sys

logger = logging.getLogger('modlevj_app')
# 指定logger人输出格式
formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d]%(levelname)-8s: %(message)s')
# 文件日志
file_handler = logging.FileHandler("log/file.log")
file_handler.setFormatter(formatter) # 可以通过setFormatter指定输出格式
# file_handler.setLevel(logging.INFO)
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter  #也可以直接给formatter 赋值
console_handler.setLevel(logging.ERROR)

# 为logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.DEBUG)


logger.debug(u'进入modlevj模块')

class Set1(Base):
    __tablename__ = 'set'
    __table_args__ = {"useexisting": True}
    name = Column(Text, primary_key=True)
    val = Column(Text)



'''new'''
Base.metadata.create_all(engine)
version = 'v1.2'
curpath = path
curdate = str(datetime.date.today())
curper = None
# ***************************************************************设置数据
def setD1D2(*tud1d2):
    global d1, d2
    if tud1d2 is None:
        d1, d2  = u'2015-01-01', u'2100-12-12'
        newd1 = Set1(name='d1',val= d1)
        newd2 = Set1(name='d2', val= d2)
        add_data(newd1)
        add_data(newd2)
    else:
        d1,  d2 = tud1d2
        newd1 = Set1(name='d1',val= d1)
        newd2 = Set1(name='d2', val= d2)
        logger.info('设置新的起始日期为{}, 结束日期为{}'.format(newd1, newd2))
        mod_data(newd1)
        mod_data(newd2)
    return d1, d2

def find_d1d2_setSql1():
    try:
        find_d1 = session.query(Set1.val).filter(Set1.name=='d1').first()
        find_d2 = session.query(Set1.val).filter(Set1.name=='d2').first()
        if find_d1 is None or find_d2 is None:
            find_d1, find_d2 = setD1D2()
        else:
            find_d1 = find_d1[0]
            find_d2 = find_d2[0]
        return find_d1, find_d2
    except IndexError:
        return setD1D2()


d1,d2 = find_d1d2_setSql1()

def get_adresss():
    adrs= session.query(PersonVj.adress).all()
    adrs = combain_list(adrs)
    adr_set = set(adrs)
    net_adrs = list(adr_set)
    # 对地址进行按字母排序
    net_adrs.sort(key= lambda x: gcl.getPinyin_first(x))
    return net_adrs



class ManyPerVj(BaseMany):
    def __init__(self):
        super(ManyPerVj, self).__init__()
        self.init_data()


    def init_data(self):
        self.names = {}
        self.id_names = {}
        self.real_name_pers = {}
        self.id_perObj = {}

    def up_data(self):
        self.lit=[]
        datas = session.query(PersonVj).all()
        for per in datas:
            self.add(per)


    def __str__(self):
        return ', '.join([str(ele) for ele in self.lit])


    def up_other_from_persLit(self):
        self.init_data( )
        for per in self.lit:
            name = per.name
            if not isinstance(name, unicode): name = unicode(name)
            index_name = gcl.getPinyin(name)
            if not per.bLine: # 搜索中去掉不在线的人物
                index_name = '.' + index_name
            self.names[index_name] = per
            self.id_names[per.id] = per.name
            self.id_perObj[per.id] = per
            self.real_name_pers[per.name] = per

    # @staticmethod
    # def namesToPinyinNames(nameList):
        # newNames = []
        # if nameList is not None:
            # for name in nameList:
                # newNames.append(gcl.getPinyin(name))
        # return  newNames


def up_manyPers():
    many_pers.up_data( )
    many_pers.up_other_from_persLit( )


many_pers = ManyPerVj()
up_manyPers( )







def find_all_huos():
    return session.query(HuoVj).all()

def get_huoTys():
    _datas = session.query(HuoVj.ty).all()
    tys_set = set(_datas)
    return combain_list(list(tys_set))

def get_huo_valid_ids():
    _datas = session.query(HuoVj.id).filter(HuoVj.bvalid==1).all()
    _datas.sort( reverse=True)
    return combain_list( _datas)


def find_all_evs():
    return session.query(EvVj).filter(and_(EvVj.crdate>d1, EvVj.crdate<d2)).all()


# ***************************************************************主界面
# 建立在线人物拼音字典  {wsy.汪生云:person}

def search_evs(nameid, huoid):
    datas = session.query(EvVj).filter(EvVj.nameId==nameid).filter(EvVj.huoId==huoid).all()
    return datas



def search_evs_from_huoId(hid):
    return session.query(EvVj).filter(EvVj.huoId==hid).all()



def search_evs_only(pid):
    return session.query(EvVj).filter(EvVj.nameId==pid).all()

def search_evs_from_date():
    return session.query(EvVj).filter( EvVj.crdate.like('%{}%'.format(curdate))).all()
    # return session.query(EvVj).filter(EvVj.crdate<d2).filter(EvVj.crdate>d1).all()




def search_sun(nameId=None, d1=d1, d2=d2):
    if None == nameId and curper is not None:
        nameId = curper.id
    objs = session.query(Sun).filter(and_(Sun.nameId==nameId, Sun.crdate>d1, Sun.crdate<d2)).all()
    return objs

def search_sun_sum(nameId=None):
    if None == nameId and curper is not None: nameId = curper.id
    sql = '''select count(id), 0, 0, sum(c_zhi), sum(c_quan), sum(c_dai), sum(c_la), sum(c_kmd), sum(c_zhu),
                    sum(c_ts), 0 from sunc where nameId={}'''.format(nameId)
    return session.execute(sql).fetchall()



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
        for huo in find_all_huos():
            huo_ty = huo.ty
            id_temp = huo.id
            self.id_obj_dict[huo.id] = huo
            self.ty_ids_dict[huo_ty] = huo.id
            if huo_ty not in self.tys:
                self.tys.append(huo_ty)
            if id_temp not in self.ids:
                self.ids.append(id_temp)
            self.all_huos.append(huo)

    def get_valid_huos_id(self):
        id_list = []
        if self.all_huos:
            for huo in self.all_huos:
                if huo.bvalid:
                    id_list.append(huo.id)
        return id_list





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
        for ev in search_evs_only(default_id):
            self.add_ev(ev)


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
        for ev in evdatas:
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
            id_names = many_pers.id_names
            for ev in self.allEvs:
                lit.append(id_names[ev.nameId])
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
        self.init_data()

        Xev_expand.set_dict(
                many_huos.get_id_ty_dict()
            )

    def init_data(self):
        self.allevs = []
        self.pid_xevExpand_Dict = {}
        self.xevEXpand = Xev_expand()

    def getOwnPerPids(self):
        ownedPids = []
        for pid in self.pid_xevExpand_Dict:
            if self.pid_xevExpand_Dict[pid].is_own():
                ownedPids.append(pid)
        return ownedPids


    def up_all_evs(self):
        for evobj in find_all_evs():
            self.allevs.append(evobj)

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
        return result_list


    def format_own_days_names(self, mat_list):
        return  '\n'.join([
            u'{:>12}个 {:>12}天  {:>12}'.format(
                _list[1], _list[2], _list[0] ) for _list in mat_list]
            )


class LookPers(object):
    def __init__(self):
        self.init_data()

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
            ids = session.query(PersonVj.id).filter(PersonVj.adress==adr)
        else:
            ids = session.query(PersonVj.id).all()
        return combain_list(ids)

    def get_ids_from_bLine(self, bline=None):
        if bline != None:
            ids = session.query(PersonVj.id).filter(PersonVj.bLine==1)
        else:
            ids = session.query(PersonVj.id).all()
        return combain_list(ids)

    def get_all_ids(self):
        return combain_list(session.query(PersonVj.id).all())


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
    sunobj = session.query(Sun).filter(Sun.evId==evid).first()
    return sunobj if sunobj else None

class AllSun(object):
    def __init__(self):
        pass

    def init_data(self):
        pass

    def get_per_sun_evIds(self):
        if curper:
            perid = curper.id
            evids = session.query(Sun.evId).filter(Sun.nameId==perid).all()
            return combain_list(evids)



class TMYData(object):
    '''每天,每月,每年的收货情况'''
    def __init__(self):
        self.huoDit = many_huos.get_id_ty_dict() # id:ty


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
            _evs = find_all_evs()
            evs = []
            for ev in _evs:
                evs.append(ev)
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
        return _dit


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

def get_last_ev():
    return get_end_obj(EvVj)

def get_end_obj(className):
    if hasattr(className, 'id'):
        _query = session.query(className)
        endobj = _query.order_by(className.id.desc()).first()
        return endobj
    else:
        ui_log.error('%s has not attr id' % className)
        return None

def get_last_per():
    return get_end_obj(PersonVj)

def get_last_huo():
    return get_end_obj(HuoVj)


def getOwnPerABCNames():
    allevs = AllEvs()
    allevs.up_all_evs()
    allevs.get_per_xev_expand()

    ownedPids = allevs.getOwnPerPids()
    id_namesDit = many_pers.id_names
    ownedABCNames = []
    if ownedPids:
        for pid in ownedPids:
            name = id_namesDit[pid]
            ABCname = gcl.getPinyin(name)
            ownedABCNames.append(ABCname)
    return ownedABCNames




if __name__ == '__main__':
    # Session = sessionmaker(engine)
    # session = Session()
    pass



