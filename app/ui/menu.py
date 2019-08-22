#!/usr/bin/python3
# coding: utf-8

from tornado.web import UIModule


class MenuModule(UIModule):
    def render(self):
        # 准备数据（从缓存，从数据库）
        data = {
            'menus': [
                {'title': '百度', 'url': 'https://www.baidu.com'},
                {'title': '京东', 'url': 'https://jd.com'},
                {'title': '阿里', 'url': 'https://www.aliyun.com'}
            ]
        }

        # 渲染ui模块的模板
        return self.render_string('ui/menu.html', **data)
