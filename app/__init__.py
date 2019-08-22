#!/usr/bin/python3
# coding: utf-8
import os

from tornado.web import Application

from app.ui.nav import NavModule
from app.views.cookie import CookieHandler
from app.views.index import IndexHandler
from app.views.order import OrderHandler
from app.views.search import SearchHandler


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # /Users/apple/PycharmProjects/mircoServer

settings = {
    'debug': True,
    'template_path': os.path.join(BASE_DIR, 'templates'),
    'static_path': os.path.join(BASE_DIR, 'static'),
    'static_url_prefix': '/s/',
    'ui_modules': {
        'Nav': NavModule
    }
}

def make_app(host='localhost'):
    return Application(handlers=[
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(?P<code>\d+)/(?P<id>\d+)', OrderHandler),

    ], default_host=host, **settings)
