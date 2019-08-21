#!/usr/bin/python3
# coding: utf-8

from unittest import TestCase
import requests


class TestTornadoRequest(TestCase):
    base_url = 'http://10.36.174.2:9000'

    def test_index_post(self):
        url = self.base_url + '/'
        # 发起post请求，表单参数使用data来指定
        resp = requests.post(url, data={
            'name': 'disen',
            'city': '西安'
        })
        print(resp.text)
