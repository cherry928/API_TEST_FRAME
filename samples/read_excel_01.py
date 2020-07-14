#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:read_excel.py
# @time:2020/7/1 9:13 下午

import os
import xlrd

# excel路径
excel_path = os.path.join(os.path.dirname(__file__), 'data/test_data_01.xlsx')

# 使用xlrd创建一个工作薄对象
workbook = xlrd.open_workbook(excel_path)
# 根据工作表的名称创建表格对象
sheet = workbook.sheet_by_name('sheet1')
# 获取总行数
print(sheet.nrows)      # 结果：4
# 获取总列数
print(sheet.ncols)      # 结果：4
# 以列表的方式返回一行数据
print(sheet.row_values(1))      # 结果：[1.0, '陈浩', '男', 18.0]
# 以列表的方式返回一列数据
print(sheet.col_values(1))      # 结果：['姓名', '陈浩', '小明', '小黑']
# 以列表的方式返回一列数据，指定从行开始
print(sheet.col_values(3,1))     # 结果：[18.0, 20.0, 19.0]
# 获取某个单元格的数据
cell_value = sheet.cell_value(2,1)      # 结果：小明
print(cell_value)
