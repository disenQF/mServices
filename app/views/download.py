#!/usr/bin/python3
# coding: utf-8
from tornado.web import RequestHandler, asynchronous
from tornado.web import gen
from tornado.httpclient import AsyncHTTPClient, HTTPClient, HTTPResponse, HTTPRequest

class DownloadHandler(RequestHandler):
    def get(self):
        # 获取查询参数中的url(下载资源的网址)
        url = self.get_query_argument('url')
        filename = self.get_query_argument('filename', 'index.html')

        # 发起同步请求
        client = HTTPClient()
        # validate_cert  是否验证SSL安全连接的证书
        response: HTTPResponse = client.fetch(url,
                                              validate_cert=False)
        # print(response.body)
        # 保存到 static/downloads
        from app import BASE_DIR, os
        dir = os.path.join(BASE_DIR, 'static/downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)

        self.write('下载成功')

class AsyncDownloadHandler(RequestHandler):

    def save(self, response: HTTPResponse):
        print(response.effective_url, '下载成功')
        self.write('<br>下载完成， 正在保存')

        # 在回调函数中，可以获取请求的查询参数
        filename = self.get_query_argument('filename', 'index.html')

        # 保存到 static/downloads
        from app import BASE_DIR, os
        dir = os.path.join(BASE_DIR, 'static/downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)

        self.write('<br>保存文件成功!')
        self.finish()

    @asynchronous
    def get(self):
        # 获取查询参数中的url(下载资源的网址)
        url = self.get_query_argument('url')

        # 发起异步请求
        client = AsyncHTTPClient()
        # validate_cert  是否验证SSL安全连接的证书
        client.fetch(url,
                     callback=self.save,
                     validate_cert=False)

        self.write('下载中...')
        self.set_status(200)

class Async2DownloadHandler(RequestHandler):

    def save(self, response: HTTPResponse):
        print(response.effective_url, '下载成功')
        self.write('<br>下载完成， 正在保存')

        # 在回调函数中，可以获取请求的查询参数
        filename = self.get_query_argument('filename', 'index.html')

        # 保存到 static/downloads
        from app import BASE_DIR, os
        dir = os.path.join(BASE_DIR, 'static/downloads')
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)

        self.write('<br>保存文件成功!')
        self.finish()

    @asynchronous
    @gen.coroutine
    def get(self):
        # 获取查询参数中的url(下载资源的网址)
        url = self.get_query_argument('url')

        self.write('下载中...')

        # 发起异步请求, 如果使用协程，等于是同步了
        client = AsyncHTTPClient()
        # validate_cert  是否验证SSL安全连接的证书
        response = yield client.fetch(url, validate_cert=False)
        self.save(response)
        print(response.code)
        self.set_status(200)