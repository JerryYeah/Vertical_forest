# -*- coding: utf-8 -*-

from base import BaseHandler
import json


class EmptyHandler(BaseHandler):

    # print"进入register"
    retjson = {'code': '400', 'contents': 'None'}

    def post(self):
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))
