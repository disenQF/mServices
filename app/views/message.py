#!/usr/bin/python3
# coding: utf-8
import random
import time
from tornado.websocket import WebSocketHandler
from tornado.web import RequestHandler


class RobbitHandler(RequestHandler):
    def get(self):
        self.render('msg/robbit.html')



class MessageOldHandler(WebSocketHandler):
    # 当前处理器是一个长连接

    def open(self):  # 表示客户请求连接
        ip = self.request.remote_ip

        # 向客户端发送消息
        self.write_message('您好, %s' % ip)

        # 每间隔一秒发送一个数字
        self.write_message('starting')
        for i in range(10):
            time.sleep(1)
            number = random.randint(100, 1000)
            self.write_message('%s' % number)
        self.write_message('end')


class MessageHandler(WebSocketHandler):
    # 当前处理器是一个长连接
    online_clients = []

    def send_all(self, msg):
        for client in self.online_clients:
            # 向客户端发送消息
            client.write_message(msg)

    def open(self):  # 表示客户请求连接
        ip = self.request.remote_ip
        self.online_clients.append(self)
        username = self.get_secure_cookie('username').decode()
        self.send_all('%s 进入聊天室' % username)

    def on_message(self, message):
        # ip = self.request.remote_ip
        username = self.get_secure_cookie('username').decode()
        msg = '%s 说了: %s' % (username, message)
        self.send_all(msg)

    def on_connection_close(self):
        self.online_clients.remove(self)