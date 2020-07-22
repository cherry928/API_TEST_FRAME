#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:unittest_demo01.py
# @time:2020/7/19 11:09 上午

import unittest
import paramunittest

# # 元组列表类型
# @paramunittest.parametrized(
#     (8,5),
#     (10,20)
# )
# # 列表列表类型
# @paramunittest.parametrized(
#     [8,5],
#     [10,20]
# )
# 字典列表类型
# @paramunittest.parametrized(
#     {'numa1':8,'numb1':5},
#     {'numa1':10,'numb1':520}
# )
# 函数或者数据对象传入进去
# testdata = [{'numa1':8,'numb1':5},{'numa1':10,'numb1':520}]
def get_data():
    return [{'numa1':8,'numb1':5},{'numa1':10,'numb1':520}]
@paramunittest.parametrized(
    *get_data()
)
class UnittstDemo01(paramunittest.ParametrizedTestCase):
    def setParameters(self, numa1, numb1):
        self.numa = numa1
        self.numb = numb1

    def test_case(self):
        print('numa=%d,numb=%d'%(self.numa,self.numb))
        self.assertGreater(self.numa,self.numb)

if __name__=='__main__':
    unittest.main()