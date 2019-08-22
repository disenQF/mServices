#!/usr/bin/python3
# coding: utf-8
from tornado.web import UIModule


class NavModule(UIModule):
    def render(self, menus):
        return self.render_string('ui/nav.html',
                                  menus=menus)