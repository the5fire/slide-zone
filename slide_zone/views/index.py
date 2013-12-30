#coding:utf-8
from __future__ import absolute_import, unicode_literals

from config import lookup


class IndexHandler:
    def GET(self):
        t = lookup.get_template('index.html')
        return t.render()

