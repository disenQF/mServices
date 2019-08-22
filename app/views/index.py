#!/usr/bin/python3
# coding: utf-8
from tornado.httputil import HTTPServerRequest
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        data = {
            'msg': 'Hi, Disen!西安欢迎您',
            'error_msg':None,
            'age': 90,
            'menus': ['主页', '最新推荐', '热门话题', '人个中心'],
            'code': "<h3>hi, 我是图片: 8 > 5 </h3>"
        }

        self.render('index.html', **data)

    def post(self):
        # 请求参数读取
        # 1. 读取单个参数
        wd = self.get_argument('wd')
        print(wd)

        # 2. 读取多个参数名相同的参数值
        titles = self.get_arguments('title')

        # 3. 从查询参数中读取url路径参数
        wd2 = self.get_query_argument('wd')
        print(wd2)
        titles2 = self.get_query_arguments('title')
        print(titles2)

        print(titles)

        # 4. 从请求对象中读取参数
        req: HTTPServerRequest = self.request

        # request请求中的数据都是dict字典类型
        wd3 = req.arguments.get('wd')
        print(wd3)  # 字典key对应的value都是bytes字节类型

        wd4 = req.query_arguments.get('wd')
        print(wd4)

        self.write('<h3>我是主页</h3>')

    def put(self):
        # 新增数据
        # 读取表单参数
        # name = self.get_argument('name')
        # city = self.get_argument('city')

        # 建议使用以下方式
        name = self.get_body_argument('name')
        city = self.get_body_argument('city')

        wd = self.get_query_argument('wd')

        self.write('<h3>我是POST请求方式: %s %s, %s </h3>' % (name, city, wd))
