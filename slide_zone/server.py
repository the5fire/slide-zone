#!/usr/bin/env python
#coding:utf-8
from __future__ import unicode_literals

import os

import web
from web.httpserver import StaticMiddleware

from views.index import IndexHandler

urls = (
    '/', 'IndexHandler',  #返回首页
)

app = web.application(urls, globals())
application = app.wsgifunc(StaticMiddleware)

def main():
    app.run()

if __name__ == "__main__":
    main()
