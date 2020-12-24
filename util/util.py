#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/18 16:51 
# @Author : anning
# @File : util.py 
# @Software: PyCharm


import random
import time


def randomString(length):
    '''生成指定长度的随机字符串'''
    string = '随机字符串'
    char = ''
    for i in range(length):
        char = char+random.choice(string)
    return char

def randomFloat(totalLength,floatLength):
    '''生成指定长度的随机浮点数'''
    string = '0123456789'
    integer = ''
    for i in range(totalLength-floatLength):
        integer = integer+random.choice(string)
    decimal = ''
    for i in range(floatLength):
        decimal = decimal+random.choice(string)

    a = integer +'.'+ decimal

    return float(a)


def getDateTime():

    Time = time.strftime("%Y-%m-%d", time.localtime())
    return Time





