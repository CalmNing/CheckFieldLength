#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/24 16:56 
# @Author : anning
# @File : demo.py 
# @Software: PyCharm
from common.RequestAndAssertion import RequestAndAssertion
from common.base import base


class demo(base):

    def test_one(self):
        super().__init__()
        # 请求参数
        self.body={}
        # 请求头
        self.headers={}
        # 请求的域名或者ip
        self.host= ''
        # 请求具体地址(接口路径)
        self.resource=''
        # 需要验证长度的字段
        self.field_length={
            '''
            目前支持的字符类型：string、decimal、date。
            后续还需要支持，请到base中修改get_field_length方法。
            使用方法
                {
                "string_32":["字段a","字段b"],
                "decimal_18_2":["字段a","字段b"],
                "date_date":["字段a","字段b"],
            }
            
            解析：
                string_32，代表字段类型为string，长度限制为32，我们可以传string_33，验证超长后是否报错
                decimal_18_2，代码字段类型为decimal，字段长度为18，小数位占2位。测试：decimal_19_2、decimal_18_3，长度19两位小数和长度18三位小数
                date_date，代码字段类型为date，目前获取的是系统的当前日期
            '''
        }

if __name__ == '__main__':
    execute = demo()
    RequestAndAssertion().execute(execute)