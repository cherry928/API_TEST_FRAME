#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:read_excel_02.py
# @time:2020/7/5 9:23 上午

import os
import xlrd
from common.excel_utils import ExcelUtils
excel_path = os.path.join(os.path.dirname(__file__), 'data/test_data_01.xlsx')

excelUtils = ExcelUtils(excel_path,'Sheet1')
# print(excelUtils.get_cell_merged_value(4,0))
# 方式一
# sheet_list = []
# for row in range(1,excelUtils.get_row_count()):
#     row_dict = {}
#     row_dict["事件"] = excelUtils.get_cell_merged_value(row,0)
#     row_dict["步骤序号"] = excelUtils.get_cell_merged_value(row, 1)
#     row_dict["步骤操作"] = excelUtils.get_cell_merged_value(row, 2)
#     row_dict["完成情况"] = excelUtils.get_cell_merged_value(row, 3)
#     sheet_list.append(row_dict)
#
# for row in sheet_list:
#     print(row)

# 方式二
alldata_list = []
first_row = excelUtils.sheet.row(0)
print(first_row)
for row in range(1, excelUtils.get_row_count()):
    row_dict = {}
    for col in range(0, excelUtils.get_col_count()):
        row_dict[first_row[col].value] = excelUtils.get_cell_merged_value(row,col)
    alldata_list.append(row_dict)

for row in alldata_list:
    print(row)