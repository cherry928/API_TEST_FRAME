#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:read_excel.py
# @time:2020/7/1 9:13 下午

import os
import xlrd

excel_path = os.path.join(os.path.dirname(__file__), 'data/test_data_01.xlsx')

workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_name('Sheet1')
cell_value = sheet.cell_value(2,0)  # 合并的单元格不输出值
print(cell_value)

# 处理方式
merged = sheet.merged_cells
print(sheet.merged_cells)  # 返回一个列表  起始行 结束行 起始列 结束列

# 逻辑：凡是在merged_cells属性范围内的单元格 它的值都要等于左上角首个单元格的值

# row_index = 2; col_index = 0
# for (rlow, rhigh, clow, chigh) in merged:  # 遍历表格中所有合并单元格位置信息
#     if (row_index >= rlow and row_index < rhigh):  # 行坐标判断
#         if (col_index >= clow and col_index < chigh):  # 列坐标判断
#             # 如果满足条件，就把合并单元格第一个位置的值赋给其它合并单元格
#             cell_value = sheet.cell_value(rlow,clow)
# print( cell_value )

def get_merged_cell_value(row_index,col_index):
    cell_value = None
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value = sheet.cell_value(rlow, clow)
    return cell_value

# print(get_merged_cell_value(0,0))
# print(sheet.cell_value(0,0))

# 获取第二列所有值
# print(sheet.col_values(1))

# 编写一个方法，方法参数为单元格的坐标（x,y），如果给的坐标是合并的单元格，输出此单元格是合并的，否则，输出普通单元格
def get_cell_value(row_index,col_index):
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                return sheet.cell_value(rlow, clow)
    else:
        return sheet.cell_value(row_index, col_index)

print(get_cell_value(4,0))
# print(get_cell_value(2,0))
# for i in range(1,9):
#     print(get_cell_value(i, 0))


# 获取第四列所有值
# print(sorted(sheet.col_values(3,1), reverse=True))