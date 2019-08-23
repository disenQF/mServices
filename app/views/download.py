#!/usr/bin/python3
# coding: utf-8
from tornado.web import RequestHandler
from tornado.httpclient import HTTPClient, HTTPResponse, HTTPRequest

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