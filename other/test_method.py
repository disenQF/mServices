#!/usr/bin/python3
# coding: utf-8

from unittest import TestCase
import requests


class TestTornadoRequest(TestCase):
    base_url = 'http://10.36.174.2:9000'

    def test_index_get(self):
        url = self.base_url+'/'

        # 查询参数
        resp = requests.get(url, params={
            'wd': 'disen',
            'title': 20
        })

        # 可能会出现400 错误：  原因是查询参数没有给对
        print(resp.text)

    def test_index_post(self):
        url = self.base_url + '/?wd=python'
        # 发起post请求，表单参数使用data来指定
        resp = requests.post(url, data={
            'name': '高超',
            'city': '北京'
        })
        print(resp.text)

class TestCookieRequest(TestCase):
    url = 'http://10.36.174.2:9000/cookie'

    def test_search(self):
        resp = requests.get('http://10.36.174.2:9000/search',params={
            'wd': 'python'
        })

        print(resp.text)
        print(resp.cookies)
        for key, cookie in resp.cookies.items():
            print(key, resp.cookies.get(key))

    def test_get(self):
        resp = requests.get(self.url)
        print(resp.text)

    def test_delete(self):
        resp = requests.delete(self.url, params={
            'name': 'token'
        })
        print(resp.text)

class TestOrderRequest(TestCase):
    url = 'http://10.36.174.2:9000/order/3/1'

    def test_get(self):
        resp = requests.get(self.url)
        print(resp.text)

    def test_post(self):
        resp = requests.post(self.url)
        print(resp.text)

class TestUserRequest(TestCase):
    url = 'http://10.36.174.2:8000/user'

    def test_login(self):
        # 上传json数据
        resp = requests.get(self.url,
                            json={
                                'name': 'jack',
                                'pwd': '123'
                            })

        # 读取响应的json数据
        if resp.headers.get('Content-Type').startswith('application/json'):
            print(resp.json())
        else:
            print(resp.text)


