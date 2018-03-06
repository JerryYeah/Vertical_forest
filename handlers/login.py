# coding=utf-8

import json
from sqlalchemy import desc
from tornado import gen
from tornado.web import asynchronous

from base import BaseHandler
from database.tables import User


class LoginHandler(BaseHandler):

    retjson ={'code': '', 'contents': u'未处理'}

    @asynchronous
    @gen.coroutine
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")

        try:
            user = self.db.query(User).filter(User.Uname == username).one()
            if user:  # 存在该用户
                real_pw = user.Upassword
                if password == real_pw:
                    self.retjson['code'] = '10004'
                    self.retjson['contents'] = r'登录成功'
                else:
                    self.retjson['contents'] = u'密码错误'
                    self.retjson['code'] = '10005'  # 密码错误

        except Exception, e:  # 用户不存在
            self.retjson['contents'] = u'该用户不存在'
            self.retjson['code'] = '10006'

        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))



