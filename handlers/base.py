# -*- coding: utf-8 -*-

import tornado.web

from database import build
from database.build import redis_engine


class BaseHandler(tornado.web.RequestHandler):

    @property  # python装饰器把一个方法变成属性调用
    def db(self):
        return self.application.db

    # def initialize(self):
    #     self.session = models.DB_Session()

    def on_finish(self):
        self.db.close()

    @property
    def redis(self):
        return redis_engine
