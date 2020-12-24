#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/22 17:41 
# @Author : anning
# @File : RequestAndAssertion.py 
# @Software: PyCharm
import json

import requests


class RequestAndAssertion:

    def execute(self,execute):

        try:
            for i in execute.body_list():
                try:
                    body = json.dumps(i)
                    # print(i)
                    response = requests.post(execute.host + execute.resource, data=body, headers=execute.headers).json()
                    assert response.get('msg') == '操作成功'
                    assert response.get('code') == 200
                    execute.successCount = execute.successCount + 1
                except AssertionError as a:
                    execute.failCount = execute.failCount + 1
                    print('#' * 180)
                    print(a, '请求失败,请求体:{0}'.format(i))
                    print('=' * 180)
                    # body = json.loads(i)
                    print('响应信息：{0}'.format(response))
                    print()
                    print()
        except Exception as e:
            print(e)
        finally:
            total = execute.successCount + execute.failCount
            print('共计执行了{0}条用例，成功了{1},失败了{2}'.format(total, execute.successCount, execute.failCount))