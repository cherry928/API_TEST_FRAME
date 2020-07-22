#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:case_01.py
# @time:2020/7/18 10:14 上午
'''
作业2：获取token -- 新建标签 -- 修改标签
'''
import re
from common.request_uitls import RequestUtils
from common.test_data_utils import TestdataUtils
from common.requests_utils import RequestsUtils

# testdataUtils = TestdataUtils()
# all_cases = testdataUtils.def_testcase_data_list()
# for case in all_cases:
    # print(case)
    # case_info = case['case_info']
    # print(case_info)
    # RequestUtils().request_by_step(case_info)
# case_infos = [{'测试用例编号': 'case01', '测试用例名称': '验证新建标签，再修改标签', '用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx5189359b0e0ddd89","secret":"11d4de7719a2276becf27ab573263061"}', '提交数据（post)': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'},
#               {'测试用例编号': 'case01', '测试用例名称': '验证新建标签，再修改标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '新建标签', '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '提交数据（post)': '{"tag" : {"name" : "testcherry039"}}', '取值方式': 'json取值', '传值变量': 'tagid', '取值代码': '$.tag.id', '期望结果类型': '正则匹配', '期望结果': '{"tag":{"id":(.+?),"name":"(.+?)"}}'},
#               {'测试用例编号': 'case01', '测试用例名称': '验证新建标签，再修改标签', '用例执行': '是', '测试用例步骤': 'step_03', '接口名称': '修改标签', '请求方式': 'post', '请求地址': '/cgi-bin/tags/update', '请求参数(get)': '{"access_token":${token}}', '提交数据（post)': '{"tag":{"id":${tagid},"name":"test__cherry039"}} ', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{ "errcode":0,"errmsg":"ok" } '}]

case_infos = [{'测试用例编号': 'case03', '测试用例名称': '验证新建标签，再删除标签', '用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx5189359b0e0ddd89","secret":"11d4de7719a2276becf27ab573263061"}', '提交数据（post)': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'},
              {'测试用例编号': 'case03', '测试用例名称': '验证新建标签，再删除标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '新建标签', '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '提交数据（post)': '{"tag" : {"name" : "testcherry050"}}', '取值方式': 'json取值', '传值变量': 'tagid', '取值代码': '$.tag.id', '期望结果类型': '正则匹配', '期望结果': '{"tag":{"id":(.+?),"name":"(.+?)"}}'},
              {'测试用例编号': 'case03', '测试用例名称': '验证新建标签，再删除标签', '用例执行': '是', '测试用例步骤': 'step_03', '接口名称': '删除标签', '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}', '提交数据（post)': '{"tag":{"id":${tagid}} } ', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{ "errcode":0,"errmsg":"ok" } '}]
RequestUtils().request_by_step(case_infos)
# RequestsUtils().request_by_step(case_infos)
# test_data3 = [
#     {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'},
#     {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag" : {"name" : "testP1P201"} } ', '取值方式': 'json取值', '传值变量': 'tagid', '取值代码': '$.tag.id', '期望结果类型': '无', '期望结果': ''},
#     {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_03', '接口名称': '获取所有标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/update', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag":{"id":${tagid},"name":"testP1P202"}} ', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{"errcode":0,"errmsg":"ok" }'}
# ]
# RequestsUtils().request_by_step( test_data3 )