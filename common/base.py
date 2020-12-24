#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/22 16:24 
# @Author : anning
# @File : base.py 
# @Software: PyCharm

from copy import deepcopy
from public_login.login import getToken
from util.util import getDateTime, randomString, randomFloat


class base:


    def __init__(self):
        self.bodyList = []
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": getToken()
        }
        self.successCount = 0
        self.failCount = 0
        self.body = {}
        self.field_length = {}
        self.resource = ''
        self.host = ''




    def body_refactor(self,key,value):
        '''重新构建请求体,对原有的键重新赋值
            key：原有的键，value：新值
        '''
        body = deepcopy(self.body)
        body.pop(key)
        body.setdefault(key, value)
        return body

    def body_list(self):

        '''根据需要循环创建请求体'''

        for key, value in self.field_length.items():

            if isinstance(self.get_field_length(key), bool):
                for field in value:
                    self.bodyList.append(self.body_refactor(field, getDateTime()))

            elif isinstance(self.get_field_length(key),int):
                integer = self.get_field_length(key)
                for field in value:
                    self.bodyList.append(self.body_refactor(field, randomString(integer)))

            elif isinstance(self.get_field_length(key),tuple):
                totalLength,floatLength = self.get_field_length(key)
                for field in value:
                    self.bodyList.append(self.body_refactor(field, randomFloat(totalLength,floatLength)))
        return self.bodyList


    def get_field_length(self,key):

        '''获取字段长度'''
        if key.startswith('string'):
            integer = int(key.split('_')[1])
            return integer
        elif key.startswith('decimal'):
            totalLength = int(key.split('_')[1])
            floatLength = int(key.split('_')[2])
            return totalLength, floatLength
        elif key.startswith('date'):
            return True
        else:
            return False
