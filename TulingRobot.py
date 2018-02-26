#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Newton_apple time:2018-02-26
# 调用图灵机器人API

import urllib.request
import urllib.parse
import json

def autochat(input_data, userid=None):
    api_url = 'http://www.tuling123.com/openapi/api'
    post_data = {
        'key': 'b69556533e7b412382f34d7cb7136e0a',
        'info': input_data,
        'loc': '北京市中关村',
        'userid': userid
    }
    # 对post_data进行编码
    data = urllib.parse.urlencode(post_data).encode('utf-8')
    response = urllib.request.Request(url=api_url, data=data)
    json_content = urllib.request.urlopen(response).read().decode('utf-8')     # 得到的是json格式
    content = json.loads(json_content)['text']           # 转换成字典类型
    return content


if __name__ == '__main__':
    inputdata = input('请输入内容：')
    print(autochat(inputdata))
