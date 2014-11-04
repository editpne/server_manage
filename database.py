#coding=utf-8

#数据库定义文件
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config
Base = declarative_base()


class Business(Base):
    __tablename__ = 's_business'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(35))


class Application(Base):
    __tablename__ = 's_application'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(35))


class Servers(Base):
    __tablename__ = 's_servers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(35), default='')
    ip_addr = Column(Integer, default=0)
    isp_id = Column(Integer, default=0)
    idc_id = Column(Integer, default=0)
    environment = Column(Integer, default=0)
    business_id = Column(Integer, default=0)
    application_id = Column(Integer, default=0)
    cluster = Column(String(55), default='')
    role = Column(Integer, default=0)
    head_name = Column(String(35), default='')
    status = Column(Integer, default=0)
    sort_order = Column(Integer, default=100)


class Isp(Base):
    __tablename__ = 's_isp'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(35), default='')


class Idc(Base):
    __tablename__ = 's_idc'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(35), default='')


class Users(Base):
    __tablename__ = 's_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(35), default='')
    passwd = Column(String(32), default='')
    real_name = Column(String(35), default='')


engine = create_engine('mysql+mysqldb://%s:%s@%s:%s/%s?charset=%s' % (config.db['user'], config.db['passwd'], config.db['host'], config.db['port'], config.db['dbname'], config.db['charset']))
DBSession = sessionmaker(bind=engine)
DB = DBSession()