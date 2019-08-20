#!/usr/bin/python3
# coding: utf-8
import tornado.web as web
import tornado.ioloop as ioloop

from tornado.options import define, options, parse_command_line


# 定义命令行的参数
define('port', default=8000, type=int, help='设置Web服务的端口')


class IndexHandler(web.RequestHandler):
    def get(self):
        # 获取请求的查询参数
        word = self.get_argument('wd')

        self.write('Hello, Tornado <p>查询参数wd：%s </p>' % word)

    def post(self):
        # 获取请求的表单参数
        word = self.get_argument('wd')

        self.write('Hello POST <p>查询参数wd：%s </p>' % word)


class LoginHandler(web.RequestHandler):
    def get(self):
        self.write('Login')


class LogoutHandler(web.RequestHandler):
    def get(self):
        self.write('Logout')


if __name__ == '__main__':
    # 解析命令行中参数, 类似于 sys.argv 的数据解析
    parse_command_line()

    # 声明Web服务中请求资源
    app = web.Application([
        ('/', IndexHandler),
        ('/login', LoginHandler),
        ('/logout', LogoutHandler),
    ])

    # 使用命令行中的参数 port
    app.listen(options.port)

    ioloop.IOLoop.current().start()