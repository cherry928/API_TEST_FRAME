#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:test_01.py
# @time:2020/7/18 11:39 上午

import jsonpath

s = {   "tag":{ "id":134, "name":"广东"   } }

value = jsonpath.jsonpath(s,'$.tag.id')
print(value)