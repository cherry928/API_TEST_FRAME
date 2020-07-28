#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:api_test.py
# @time:2020/7/19 11:34 上午

import warnings
import unittest
import paramunittest
from common.test_data_utils import TestdataUtils
from common.request_uitls import RequestUtils
from nb_log import LogManager

case_infos = TestdataUtils().def_testcase_data_list()
logger = LogManager(__file__).get_logger_and_add_handlers()

print(case_infos)
@paramunittest.parametrized(
    *case_infos
)

class APITest(paramunittest.ParametrizedTestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore',ResourceWarning)
        logger.info('测试初始化操作')

    def setParameters(self, case_name, case_info):
        logger.info('测试数据加载')
        self.case_id = case_name
        self.case_info = case_info

    # def test_demo(self):
    #     print(self.case_id[0] + ':' + self.case_info[0].get('测试用例名称'))
    #     self.assertTrue(True)

    def test_api_commom_function(self):
        logger.info("测试用例[ %s ]开始执行" % (self.case_info[0].get("测试用例编号") + self.case_info[0].get("测试用例名称")))
        self._testMethodName = self.case_info[0].get('测试用例编号')
        self._testMethodDoc = self.case_info[0].get('测试用例名称')
        actual_result = RequestUtils().request_by_step(self.case_info)
        self.assertTrue(actual_result.get('check_result'),actual_result.get('message'))

if __name__ == '__main__':
    unittest.main()