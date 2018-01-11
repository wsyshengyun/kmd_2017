# coding=utf8

__author__ = 'Administrator'
'''
数据库
'''
import sqlite3




class SQL_PERSON(object):
    name = "person_1"
    @classmethod
    def CRETATE_IF_NOT_EXIST(cls):
        return '''CREATE TABLE if not exists  [person_1] (
            [id] INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
            [name] text  UNIQUE NOT NULL,
            [adress] text  NOT NULL,
            [phone] text   NOT NULL,
            [bLine] INTEGER  NOT NULL,
            [crdate] text  NOT NULL,
            [bz] text  NOT NULL
            )'''
    @classmethod
    def FIND_IDS_FROM_ADR(cls, adr):
        return  '''select id from person_1 WHERE adress='{}' '''.format( adr )

    @classmethod
    def FIND_IDS_FROM_LINE(cls, bline):
        return '''select id from person_1 WHERE bLine={}'''.format(bline)

    FIND_ALL_IDS = '''select id from person_1'''
    FIND = "select * from {name}".format(name = name)
    FIND_ONE = "select * from {name} where id BETWEEN 2 and 20".format(name = name)
    FIND_Lie = "select adress  from {name}".format(name=name)
    FIND_ADRESS = "select * from {name} where adress in ('小刘', '小营')".format(name = name)
    CREATE = '''create table {name}( \
                id INTEGER primary key autoincrement, \
                name text not NULL, \
                adress text not NULL,\
                phone text not NULL,\
                bLine INTEGER  not NULL,\
                crdate text not NULL, \
                bz text not NULL\
            )'''.format(name = name)

    INSERT_AUTO = '''insert into {name}(name, adress, phone, bLine, crdate, bz) values(?,?,?,?,?,?);'''.format(name=name)
    INSERT = '''insert into {name}(ID, name, adress, phone, bLine, crdate, bz) values(?,?,?,?,?,?,?);'''.format(name=name)
    UPDATE = '''update {name} set name=? ,adress=? ,phone=? ,bLine=? ,crdate=? ,bz=? WHERE id=?'''.format(name=name)

    DELETE = '''delete from {name} where name=? and id = ?'''.format(name=name)
    DROP = ''' DROP TABLE IF EXISTS {name}'''.format(name = name)

class SQL_HUO(object):
    name = 'huo'
    find_id = 1
    @classmethod
    def CRETATE_IF_NOT_EXIST(cls):
        return '''CREATE TABLE if not exists huo(
                id INTEGER primary key autoincrement,
                ty text not NULL,
                pay REAL not NULL,
                nums INTEGER not NULL,
                bvalid INTEGER  not NULL,
                bLa INTEGER not NULL,
                crdate text not NULL,
                bz text not NULL
            )'''

    FIND = "select * from {name}".format(name = name)
    FIND_ONE = "select * from {name} where id={id}".format(name = name, id =find_id)
    FIND_TYS = "select ty  from {name}".format(name=name)
    FIND_VALID_IDS = "select id  from {name} where bvalid=1".format(name=name)
    # FIND_ADRESS = "select * from {name} where adress in ('小刘', '小营')".format(name = name)
    CREATE = '''create table {name}(
                id INTEGER primary key autoincrement,
                ty text not NULL,
                pay REAL not NULL,
                nums INTEGER not NULL,
                bvalid INTEGER  not NULL,
                bLa INTEGER not NULL,
                crdate text not NULL,
                bz text not NULL
            )'''.format\
        (name = name)


    INSERT = '''insert into {name}(id, ty, pay, nums, bvalid, bLa, crdate, bz) values(?,?,?,?,?,?,?,?);'''.format(name=name)

    INSERT_AUTO = '''insert into {name}(ty, pay, nums, bvalid, bLa, crdate, bz) values(?,?,?,?,?,?,?);'''.format(name=name)

    UPDATE = '''update {name} set ty=? ,pay=? ,nums=? ,bvalid=? ,bLa=?, crdate=? ,bz=? WHERE id=?'''.format(name=name)

    DELETE = '''delete from {name} where id = ?;'''.format(name=name)
    DROP = ''' DROP TABLE IF EXISTS {name}'''.format(name = name)

class SQL_EV(object):
    tab_name = 'evs'
    find_id = 1
    id_name, id_huo, d1, d2 = None, None, None, None
    FIND = "select * from {name}".format(name = tab_name)

    @classmethod
    def set_d1_d2(cls, d1, d2):
        cls.d1, cls.d2 = d1, d2

    @classmethod
    def CRETATE_IF_NOT_EXIST(cls):
        return '''CREATE TABLE if not exists evs(
                id INTEGER primary key autoincrement,
                nameId INTEGER not NULL ,
                huoId INTEGER not NULL,
                sh INTEGER not NULL,
                fa INTEGER not NULL,
                sun INTEGER not NULL,
                numla INTEGER  not NULL,
                money REAL not NULL,
                crdate text not NULL,
                bz text not NULL
            )'''

    @classmethod
    def FIND_EVS_FROM_HUOID(cls, hid):
        return ''' select * from evs WHERE huoId={} and crdate between '{}' and '{} '''.format( hid , cls.d1, cls.d2)

    @classmethod
    def FIND_FROM_D1_D2(cls):
        return '''select * from evs WHERE  crdate BETWEEN  '{}' and '{}' ; '''.format(cls.d1, cls.d2)

    @classmethod
    def SQL_FIND_ONLY(cls, pid):
        return '''select * from evs WHERE nameId={} and crdate between '{}' and '{}';''' \
                .format(pid, cls.d1, cls.d2)

    @classmethod
    def SQL_FIND_NHD(cls):
        return '''select * from {} where nameId ={} and huoId={} and crdate between '{}' and '{}' ;\
                                 '''.format(cls.tab_name, cls.id_name, cls.id_huo, cls.d1, cls.d2)

    @classmethod
    def SQL_FIND_FROM_DATE(cls, date):  # todo 对参数限制
        # select * from evs where crdate = '2016-10-29';
        # only_date = date.split()[0]
        # return '''select * from {} where crdate='{}' '''.format(cls.tab_name, only_date)
        dt1 = date
        dt2 = date + ' ' + '23:59:59'
        return '''select * from {} where crdate between'{}' and '{}' '''.format(cls.tab_name, dt1, dt2)

    FIND_ONE = "select * from {name} where id={id}".format(name = tab_name, id =find_id)
    # FIND_TYS = "select ty  from name".format(name=name)
    # FIND_ADRESS = "select * from {name} where adress in ('小刘', '小营')".format(name = name)
    CREATE = '''create table {name}(
                id INTEGER primary key autoincrement,
                nameId INTEGER not NULL ,
                huoId INTEGER not NULL,
                sh INTEGER not NULL,
                fa INTEGER not NULL,
                sun INTEGER not NULL,
                numla INTEGER  not NULL,
                money REAL not NULL,
                crdate text not NULL,
                bz text not NULL
            )'''.format(name = tab_name)


    INSERT = '''insert into {name}(id, nameId, huoId, sh, fa, sun, numla, money, crdate, bz) values(?,?,?,?,?,?,?,?,?,?);'''.format(name=tab_name)

    INSERT_AUTO = '''insert into {name}(nameId, huoId, sh, fa, sun, numla, money, crdate, bz) values(?,?,?,?,?,?,?,?,?);'''.format(name=tab_name)

    UPDATE = '''update {name} set nameId=?, huoId=? ,sh=?, fa=?, sun=?, numla=?, money=?, crdate=?, bz=? WHERE id=?'''.format(name=tab_name)

    DELETE = '''delete from {name} where id = ?;'''.format(name=tab_name)
    DROP = ''' DROP TABLE IF EXISTS {name}'''.format(name = tab_name)

class SQL_SUN(object):
    name = 'sunc'
    find_id = 1

    @classmethod
    def CRETATE_IF_NOT_EXIST(cls):
        return '''CREATE TABLE IF NOT EXISTS [sunc] (
        [id] INTEGER  PRIMARY KEY AUTOINCREMENT NULL,
        [nameId] INTEGER  NOT NULL,
        [evId] INTEGER  UNIQUE NOT NULL,
        [c_zhi] INTEGER  NOT NULL,
        [c_quan] INTEGER  NOT NULL,
        [c_dai] INTEGER  NOT NULL,
        [c_la] INTEGER  NOT NULL,
        [c_kmd] INTEGER  NOT NULL,
        [c_zhu] INTEGER  NOT NULL,
        [c_ts] REAL  NOT NULL,
        [crdate] text  NOT NULL
        )'''


    FIND = "select * from {name}".format(name = name)
    FIND_ONE = "select * from {name} where id={id}".format(name = name, id =find_id)
    # FIND_TYS = "select ty  from name".format(name=name)
    # FIND_ADRESS = "select * from {name} where adress in ('小刘', '小营')".format(name = name)

    @classmethod
    def FIND_EVIDS_FROM_PERID(cls, nameId):
        return '''select evId from sunc where nameId={}'''.format(nameId)

    @ classmethod
    def FIND_FROM_EVID(cls, evid):
        return '''select * from sunc where evId={}'''.format(evid)

    @classmethod
    def FIND_FROM_NAMEID(cls, nameId, d1, d2):
        return '''select * from {} where nameId={} and crdate between '{}' and '{}' '''.format(cls.name, nameId, d1, d2)
    @classmethod
    def FIND_SUM_DATA(cls, nameId):
        return '''select count(id), 0, 0, sum(c_zhi), sum(c_quan), sum(c_dai), sum(c_la), sum(c_kmd), sum(c_zhu),
                    sum(c_ts), 0 from {} where nameId={}'''.format(cls.name, nameId)

    CREATE = '''CREATE TABLE [sunc] (
                [id] INTEGER  PRIMARY KEY AUTOINCREMENT NULL,
                [nameId] INTEGER  NOT NULL,
                [evId] INTEGER  UNIQUE NOT NULL,
                [c_zhi] INTEGER  NOT NULL,
                [c_quan] INTEGER  NOT NULL,
                [c_dai] INTEGER  NOT NULL,
                [c_la] INTEGER  NOT NULL,
                [c_kmd] INTEGER  NOT NULL,
                [c_zhu] INTEGER  NOT NULL,
                [c_ts] REAL  NOT NULL,
                [crdate] text  NOT NULL
                )'''

    INSERT = '''insert into {name}(id, nameId, evId, c_zhi, c_quan, c_dai, c_la, c_kmd, c_zhu, c_ts, crdate) values(?,?,?,?,?,?,?,?,?,?,?);'''.format(name=name)

    INSERT_AUTO = '''insert into {name}(nameId, evId, c_zhi, c_quan, c_dai, c_la, c_kmd, c_zhu, c_ts, crdate) values(?,?,?,?,?,?,?,?,?,?);'''.format(name=name)

    UPDATE = '''update {name} set nameId=?, evId=?, c_zhi=?, c_quan=?, c_dai=?, c_la=?, c_kmd=?, c_zhu=?, c_ts=?, crdate=? WHERE id=?'''.format(name=name)

    DELETE = '''delete from {name} where id = ?;'''.format(name=name)
    DROP = ''' DROP TABLE IF EXISTS {name}'''.format(name = name)

class SQL_SET:
    name = 'set'
    INSERT = '''insert into [set](name,val)values(?,?);'''
    UPDATE = '''update [set] set val=? where name=? ;'''
    @classmethod
    def FIND_DATE_VAL(cls,dx):
        return '''select val from '{}' where name='{}'; '''.format(cls.name, dx)

    @classmethod
    def CRETATE_IF_NOT_EXIST(cls):
        return '''CREATE TABLE if not exists [set] (
        [name] TEXT  NOT NULL,
        [val] TEXT  NOT NULL
        )'''

sqlCreate_tabs_list = [
        SQL_EV.CRETATE_IF_NOT_EXIST(),
        SQL_HUO.CRETATE_IF_NOT_EXIST(),
        SQL_PERSON.CRETATE_IF_NOT_EXIST(),
        SQL_SET.CRETATE_IF_NOT_EXIST(),
        SQL_SUN.CRETATE_IF_NOT_EXIST(),
    ]



class TestSql(object):
    def __init__(self, path = "e:\\kmdkmd.db"):
        self.set_path(path)
        self.conn = None
        self.cursor = None

    def set_path(self, path):
        self.path = path
        print u'数据库路径为设置为: ', self.path

    def execute_sql(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.conn.commit()
        self.close()

    def drop_table(self, sql):
        self.execute_sql(sql)

    def create_table(self, sql):
        self.execute_sql(sql)

    def create_many_table(self, sql_list):
        self.connect()
        for sql in sql_list:
            self.cursor.execute(sql)
        self.conn.commit()
        self.close()

    def connect(self):
        if self.path in (None, ''): return

        if None == self.conn:
            self.conn = sqlite3.connect(self.path)
        if None == self.cursor:
            self.cursor = self.conn.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None

        if self.conn:
            self.conn.close()
            self.conn = None

    def insert(self, sql, datas):
        self.connect()
        for i,d in enumerate(datas):
            print u'数据库新插入第 {} 个数据'.format(i+1)
            self.cursor.execute(sql, d)
        self.conn.commit()
        self.close()
        print u'插入数据结束'


    def find_all(self, sql):
        self.connect()
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        return datas

    def find_one(self, sql, data):
        d = (data, )
        self.connect()
        self.cursor.execute(sql, d)
        r = self.cursor.fetchall()
        return r

    def find_some(self, sql):
        self.connect()
        self.cursor.execute(sql)
        r = self.cursor.fetchall()
        return r

    def update(self, sql, datas):
        self.insert(sql, datas=datas)


    def delete_data(self, sql, datas):
        self.insert(sql, datas)


if __name__ == '__main__':
    # test = TestSql()
    # test.create_table(SQL_PERSON.CREATE)
    # datas = [
    #     (10, u'汪生云', u'小营', u'13513774637', 1, u'开始新的历程'),
    #     (20, u'刘瑞飞', u'大营', u'13513774637', 0, u'长长长长得工'),
    #     (30, u'蒋春林', u'小蒋庄', u'13513774637', 1, u'桌子椅子厨房')
    # ]


    # test.drop_table('person')
    # for j in data2:
    #     print j


    # test.insert(SQL_PERSON.INSERT, datas)

    # da2 = test.find_all(SQL_PERSON.FIND)
    # for d in da2:
    #     for i in d:
    #         print i,
    #     print
    # test.drop_table(SQL_EV.DROP)
    # test.create_table(SQL_EV.CREATE)   # 3、30



    pass
