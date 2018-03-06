#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""
from handlers.register import RegisterHandler
from handlers.login import LoginHandler
from  handlers.empty import EmptyHandler
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


url = [
    (r'/', EmptyHandler ),
    (r'/register', RegisterHandler),
    (r'/login', LoginHandler),
]