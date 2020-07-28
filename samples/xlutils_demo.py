#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:xlutils_demo.py
# @time:2020/7/22 8:59 下午

import os
import xlrd
from xlutils.copy import copy
from common import config

test_data_path = os.path.join(os.path.dirname(__file__), config.CASE_DATA_PATH)
# print(test_data_path)
wb = xlrd.open_workbook(test_data_path,formatting_info=True)   # 创建工作薄对象
new_workbook = copy(wb)   # new_workbook 已经变成可写的对象  xlwt对象
# sheet = new_workbook.get_sheet(0)
sheet = new_workbook.get_sheet(wb.sheet_names().index('Sheet1'))
# sheet = new_workbook.sheet_by_name('Sheet1')    # 此方法不支持
sheet.write(1,14,'通过')
new_workbook.save(test_data_path)