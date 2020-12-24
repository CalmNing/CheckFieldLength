#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/18 16:02 
# @Author : anning
# @File : login.py 
# @Software: PyCharm


import requests


host = ''


def getToken(userName='',passWorld=''):
    '''获取token'''
    resource = f'/请求地址?password={passWorld}&username={userName}'
    response = requests.post(host+resource)
    return response.json().get('data')

