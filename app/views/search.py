#!/usr/bin/python3
# coding: utf-8
import json

from tornado.web import RequestHandler

class SearchHandler(RequestHandler):
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
