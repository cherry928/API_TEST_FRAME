#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:check_utils.py
# @time:2020/7/12 5:03 下午
import ast
import re
# 正则匹配测试
# 实际结果
str1 = "{'access_token': '35_P1Xh3VfaQPHbh5YCZoTexX1niE512X6vbnhD0kiZxMChZypHyZNoFW7_Ii2R22geGvhG_v2f-YeJKzZxKjQKrjGkKcL7JQJUvslCIDNz207onMO7fwcTV45KoNrcaPcdljd4fwn7vihsV3K7XGVgAEASBQ','expires_in':7200}"

# 期望结果
str2 ='{"access_token":"(.+?)","expires_in":(.+?)}'

if re.findall(str2,str1):
    print(True)
else:
    print(False)

# 是否包含json key
jsondata1 = ast.literal_eval(str1)
str2 ='access_token,expires_in'
check_key_list = str2.split(',')
for check_key in check_key_list:
    result = True
    if check_key in jsondata1.keys():
        result = True
    else:
        result = False
    if result:
        break

# 健值对正确的情况
str2 = '{"expires_in":7200}'
for v in ast.literal_eval(str2).items():
    result = True
    if v in jsondata1.items():
        result = True
    else:
        result = False
    if result:
        break
print(result)