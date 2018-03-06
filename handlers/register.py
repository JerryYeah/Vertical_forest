# -*- coding: utf-8 -*-

from base import BaseHandler
from database.tables import User
import json


class RegisterHandler(BaseHandler):

    # print"进入register"
    retjson = {'code': '400', 'contents': 'None'}

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")

        try:
            same_name = self.db.query(User).filter(User.Uname == username).one()
            if same_name:  # 该昵称已被使用
                self.retjson['code'] = '10001'
                self.retjson['contents'] = r'该昵称已被使用'

        except:
            new_user = User(
                Uname=username,
                Upassword=password
            )
            try:
                self.db.merge(new_user)
                self.db.commit()
                self.retjson['code'] = '10003'  # success
                self.retjson['contents'] = r'创建成功'

            except Exception, e:
                print e
                self.db.rollback()
                self.retjson['code'] = '10002'
                self.retjson['contents'] = '新建用户失败'

        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))
