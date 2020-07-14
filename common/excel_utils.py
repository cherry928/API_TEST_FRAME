#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:excel_utils.py
# @time:2020/7/5 8:57 上午

import os
import xlrd

excel_path = os.path.join(os.path.dirname(__file__), '../test_data/test_data_01.xlsx')

class ExcelUtils():
    def  __init__(self, file_path, sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()

    def get_sheet(self):
        wb = xlrd.open_workbook(self.file_path)
        sheet = wb.sheet_by_name(self.sheet_name)
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

if __name__=='__main__':
    excelutil = ExcelUtils(excel_path,'Sheet1')
    # print(excelutil.get_cell_merged_value(4,0))
    print(excelutil.get_sheet_data_by_dict())