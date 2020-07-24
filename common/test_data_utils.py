#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:test_data_utils.py
# @time:2020/7/5 11:01 上午

import os
from common.excel_utils import ExcelUtils
from common import config
from common.sql_utils import SqlUtils

test_data_path = os.path.join(os.path.dirname(__file__), config.CASE_DATA_PATH)
# print(test_data_path)

class TestdataUtils:
    def __init__(self, test_data_path=test_data_path):
        self.test_data_path = test_data_path
        self.test_data = ExcelUtils(self.test_data_path,'Sheet1').get_sheet_data_by_dict()
        self.test_data_by_mysql = SqlUtils().get_mysql_test_case_info()

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
        return tuple(testcase_list)

    def get_testcase_data_dict_by_mysql(self):
        test_case_list = {}
        for row_data in self.test_data_by_mysql:
            test_case_list.setdefault(row_data['测试用例编号'],[]).append(row_data)
        return test_case_list

    def def_testcase_data_list_by_mysql(self):
        testcase_list = []
        for k,v in self.get_testcase_data_dict_by_mysql().items():
            one_case_dict = {}
            one_case_dict['case_name'] = k
            one_case_dict['case_info'] = v
            testcase_list.append(one_case_dict)
        return tuple(testcase_list)

    def get_row_num(self,case_id,case_step_name):
        for j in range(len(self.test_data)):
            if self.test_data[j]['测试用例编号'] == case_id and self.test_data[j]['测试用例步骤'] == case_step_name:
                break
        return j+1

if __name__=='__main__':
    testdataUtils = TestdataUtils()
    all = testdataUtils.def_testcase_data_list_by_mysql()
    for i in all:
        print(i)
    # print(testdataUtils.get_row_num('case01','step_01'))
