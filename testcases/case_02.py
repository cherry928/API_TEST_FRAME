#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:case_01.py
# @time:2020/7/18 10:14 上午
'''
作业2：获取token -- 新建标签 -- 修改标签
'''
import re
from common.request_uitls import RequestUtils
from common.test_data_utils import TestdataUtils

testdataUtils = TestdataUtils()
all_cases = testdataUtils.def_testcase_data_list()
for case in all_cases:
    # print(case)
    case_info = case['case_info']
    print(case_info)
    RequestUtils().request_by_step(case_info)