# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.types import CHAR, Integer, VARCHAR, Boolean, Float, Text
from sqlalchemy.sql.functions import func
from build import Base


# 每个类对应一个表
class User(Base):  # 用户表
    __tablename__ = 'user'

    Uid = Column(Integer, nullable=False, primary_key=True)  # 主键
    Upassword = Column(VARCHAR(16), nullable=False)
    Uname = Column(VARCHAR(24), nullable=False)


class Wetland(Base):  # 湿地表
    __tablename__ = 'wetland'

    Lid = Column(Integer, nullable=False, primary_key=True)  # 主键
    temp = Column(Float, nullable=True)
    humi = Column(Float, nullable=True)
    illum = Column(Float, nullable=True)
    adminId = Column(Integer, ForeignKey('user.Uid', onupdate='CASCADE'))