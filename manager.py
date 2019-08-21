#!/usr/bin/python3
# coding: utf-8
import json

import tornado.web
import tornado.ioloop
import tornado.options
from tornado.httputil import HTTPServerRequest


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
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

    def post(self):
        # 新增数据
        # 读取表单参数
        # name = self.get_argument('name')
        # city = self.get_argument('city')

        # 建议使用以下方式
        name = self.get_body_argument('name')
        city = self.get_body_argument('city')

        wd = self.get_query_argument('wd')

        self.write('<h3>我是POST请求方式: %s %s, %s </h3>' %(name, city, wd))

    def put(self):
        self.write('<h3>我是PUT请求方式</h3>')

    def delete(self):
        self.write('<h3>我是Delete请求方式</h3>')

class SearchHandler(tornado.web.RequestHandler):
    mapper = {
        'python': 'Python是目前世界最流行的AI语言',
        'java': 'Java已经是20多年企业级应用开发语言',
        'H5': 'H5全称是HTML5, 于2014流程的前端WEB标签语言'
    }

    def get(self):
        html = """
            <h3>搜索%s结果</h3>
            <p>
                %s
            </p>
        """

        wd = self.get_query_argument('wd')
        result = self.mapper.get(wd)

        # self.write(html % (wd, result))
        resp_data = {
            'wd': wd,
            'result': result
        }
        self.write(json.dumps(resp_data))
        self.set_status(200)  # 设置响应状态码
        # 设置响应头的数据类型
        self.set_header('Content-Type', 'application/json;charset=utf-8')

        # cookie操作
        self.set_cookie('wd', wd)

class CookieHandler(tornado.web.RequestHandler):
    def get(self):
        # 验证参数中是否存在 name ?
        if self.request.arguments.get('name'):
            # 从查询参数中读取Cookie的名称
            name = self.get_query_argument('name')

            # 从cookies中获取name的对象或值
            value = self.get_cookie(name)
            print(type(value))
            self.write(value)
        else:
            # 查看所有的cookie
            cookies: dict = self.request.cookies
            html = '<ul>%s</ul>'
            lis = []
            for key in cookies:

                lis.append('<li>%s: %s</li>' % (key, self.get_cookie(key)))

            html = '显示所有cookie' + html % ''.join(lis)
            html += """
                <form method="post">
                    <input name="name" placeholder="请输入cookie的名称">
                    <button>提交</button>
                </form>
            """
            self.write(html)

    def post(self):
        name = self.get_argument('name')
        if self.request.cookies.get(name, None):
            # 存在的
            self.clear_cookie(name)
            self.write('<h3 style="color:green;">删除 %s 成功</h3>' % name)
        else:
            self.write('<h3 style="color:red;">删除 %s 失败， 不存在!</h3>' % name)

        # 重定向操作时，不需要再调用self.write()
        self.redirect('/cookie')  # 重定向

class OrderHandler(tornado.web.RequestHandler):
    goods = [
        {
            'id': 1,
            'name': 'Python高级开发',
            'author': 'disen',
            'price': 190
        },
        {
            'id': 2,
            'name': 'Python3 Vs Python2',
            'author': 'disen',
            'price': 290
        }
    ]

    action_map = {
        1: '取消订单',
        2: '再次购买',
        3: '评价'
    }

    def query(self, order_id):
        for item in self.goods:
            if item.get('id') == order_id:
                return item

    def initialize(self):
        # 所有的请求方法在调用之前，都会进行初始化操作
        print('-----initialize----')

    def prepare(self):
        # 在初始化之后，调用行为方法之前，
        # 调用此方法进行预处理
        print('-----prepare----')

    def get(self, id, code):
        print('---get-----')
        self.write('订单查询')
        html = """
            <p>
                商品编号 ： %s
            </p>
            <p>
                商品名称 ： %s
            </p>
            <p>
                商品价格 ： %s
            </p>
        """
        goods = self.query(int(id))
        self.write(html % (goods.get('id'), goods.get('name'), goods.get('price')))
        self.write(self.action_map.get(int(code)))

    def post(self, code, id):
        print('---post-----')
        self.write('---post-----')

    def on_finish(self):
        print('---on_finish-----')


def make_app():
    return tornado.web.Application([
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(?P<code>\d+)/(?P<id>\d+)', OrderHandler),

    ], default_host=tornado.options.options.host)


if __name__ == '__main__':
    # 定义命令行参数
    tornado.options.define('port',
                           default=8000,
                           type=int,
                           help='bind socket port')
    tornado.options.define('host',
                           default='localhost',
                           type=str,
                           help='设置host name')

    # 解析命令行参数的
    tornado.options.parse_command_line()

    app = make_app()
    app.listen(tornado.options.options.port)  # 使用命令行参数

    print('starting Web Server http://%s:%s' % (
        tornado.options.options.host,
        tornado.options.options.port
    ))
    # 启动服务
    tornado.ioloop.IOLoop.current().start()