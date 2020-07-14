#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:read_excel_03.py
# @time:2020/7/5 10:42 上午

# a = {'one':1,'two':'2','three':3}
# a.setdefault('four',4)
# print(a)
# a.setdefault('one',3.2)
# print(a)

lista = [
    {'one':'case_01','two':1,'three':3},
    {'one':'case_02','two':1,'three':3},
    {'one':'case_02','two':2,'three':3},
    {'one':'case_03','two':1,'three':3},
    {'one':'case_03','two':2,'three':3}]

case_dict = {}
for i in lista:
    case_dict.setdefault(i['one'],[]).append(i)
print(case_dict)

case_list = []
for k,v in case_dict.items():
    case_dict = {}
    case_dict['case_name'] = k
    case_dict['case_info'] = v
    case_list.append(case_dict)

for c in case_list:
    print(c)