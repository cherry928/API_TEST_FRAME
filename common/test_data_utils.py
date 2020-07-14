#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:test_data_utils.py
# @time:2020/7/5 11:01 上午

import os
from common.excel_utils import ExcelUtils
from common import config

test_data_path = os.path.join(os.path.dirname(__file__), config.CASE_DATA_PATH)
print(test_data_path)

class TestdataUtils:
    def __init__(self, test_data_path=test_data_path):
        self.test_data_path = test_data_path
        self.test_data = ExcelUtils(self.test_data_path,'Sheet1').get_sheet_data_by_dict()

    def get_testcase_data_dict(self):
        test_case_list = {}
        for row_data in self.test_data:
            test_case_list.setdefault(row_data['测试用例编号'],[]).append(row_data)
        return test_case_list

    def def_testcase_data_list(self):
        testcase_list = []
        for k,v in self.get_testcase_data_dict().items():
            one_case_dict = {}
            one_case_dict['case_name'] = k
            one_case_dict['case_info'] = v
            testcase_list.append(one_case_dict)
        return testcase_list

if __name__=='__main__':
    testdataUtils = TestdataUtils()
    all = testdataUtils.def_testcase_data_list()
    for i in all:
        print(i)