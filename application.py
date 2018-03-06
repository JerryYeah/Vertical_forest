#!/usr/bin/env Python
# coding=utf-8

from url import url
from sqlalchemy.orm import scoped_session, sessionmaker
import tornado.web
from database.build import engine

application = tornado.web.Application(
    handlers=url
    )
application.db = scoped_session(sessionmaker(bind=engine,
                                              autocommit=False, autoflush=True,
                                              expire_on_commit=False))

# session负责执行内存中的对象和数据库表之间的同步工作 Session类有很多参数,使用sessionmaker是为了简化这个过程
