#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:importdata_demo.py
# @time:2020/7/19 9:25 上午
'''
使用excel的数据去驱动 request_uitls
'''

from common.request_uitls import RequestUtils
from common.test_data_utils import TestdataUtils

testdataUtils = TestdataUtils()
all_case_info = testdataUtils.def_testcase_data_list()
for case in all_case_info:
    print(case)
    case_info = case['case_info']
    print(case_info)
    # RequestUtils().request_by_step(case_info)