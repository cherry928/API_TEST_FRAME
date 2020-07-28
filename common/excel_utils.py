#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:excel_utils.py
# @time:2020/7/5 8:57 上午

import os
import xlrd
from xlutils.copy import copy

excel_path = os.path.join(os.path.dirname(__file__), '../test_data/test_case.xls')

class ExcelUtils():
    def  __init__(self, file_path, sheet_name):
        self.file_path = file_path
        self.wb = xlrd.open_workbook(self.file_path, formatting_info=True)
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()

    def get_sheet(self):
        # wb = xlrd.open_workbook(self.file_path)
        sheet = self.wb.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        row_count = self.sheet.nrows
        return row_count

    def get_col_count(self):
        col_count = self.sheet.ncols
        return col_count

    def get_cell_value(self, row_index, col_index):
        cell_value = self.sheet.cell_value(row_index,col_index)
        return cell_value

    def get_merged_info(self):
        merged_info = self.sheet.merged_cells
        return merged_info

    def get_cell_merged_value(self, row_index, col_index):
        '''既能获取合并单元格又能获取普通单元格'''
        for (rlow, rhigh, clow, chigh) in self.get_merged_info():
            if (row_index >= rlow and row_index < rhigh):
                if (col_index >= clow and col_index < chigh):
                    return self.get_cell_value(rlow, clow)
        else:
            return self.get_cell_value(row_index, col_index)

    def get_sheet_data_by_dict(self):
        alldata_list = []
        first_row = self.sheet.row(0)
        for row in range(1, self.get_row_count()):
            row_dict = {}
            for col in range(0, self.get_col_count()):
                row_dict[first_row[col].value] = self.get_cell_merged_value(row, col)
            alldata_list.append(row_dict)
        return alldata_list

    def update_excel_data(self,row_id,col_id,content):
        new_wb = copy(self.wb)
        sheet = new_wb.get_sheet(self.wb.sheet_names().index(self.sheet_name))
        sheet.write(row_id, col_id, content)
        new_wb.save(self.file_path)

    def clear_excel_column(self,start_id,end_id,col_id):
        new_wb = copy(self.wb)
        sheet = new_wb.get_sheet(self.wb.sheet_names().index(self.sheet_name))
        for rowd_id in range(start_id,end_id):
            sheet.write(rowd_id, col_id, "")
        new_wb.save(self.file_path)


if __name__=='__main__':
    excelutil = ExcelUtils(excel_path,'Sheet1')
    # print(excelutil.sheet.row(0)[0].value)
    for i in range(len(excelutil.sheet.row(0))):
        if excelutil.sheet.row(0)[i].value == '测试结果':
            break
    print(i)
    # print(excelutil.get_cell_merged_value(4,0))
    # print(excelutil.update_excel_data(1,14,'失败'))