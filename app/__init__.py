#!/usr/bin/python3
# coding: utf-8
from tornado.web import Application

from app.views.cookie import CookieHandler
from app.views.index import IndexHandler
from app.views.order import OrderHandler
from app.views.search import SearchHandler


def make_app(host='localhost'):
    return Application([
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(?P<code>\d+)/(?P<id>\d+)', OrderHandler),

    ], default_host=host)
