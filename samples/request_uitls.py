#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:request_uitls.py
# @time:2020/7/12 8:50 上午
import ast
import requests
import jsonpath
import re
from common import config
from common.check_utils import CheckUtils

class RequestUtils():
    def __init__(self):
        self.hosts = config.URL
        self.headers = {'Content-Type': 'application/json; charset=utf-8'}
        self.session = requests.session()
        self.temp_variables = {}

    def get(self,get_info):
        url = self.hosts + get_info['请求地址']
        response = self.session.get(url=url,
                                    params= ast.literal_eval(get_info['请求参数(get)']))
        response.encoding = response.apparent_encoding
        if get_info['取值方式'] == 'json取值':
            value = jsonpath.jsonpath(response.json(),get_info["取值代码"])
            self.temp_variables[get_info['传值变量']] = value
            print(self.temp_variables)
        elif get_info ['取值方式'] == "正则取值":
            value = re.findall(get_info['取值代码'], response.text)[0]
            self.temp_variables[get_info['传值变量']] = value
            print(self.temp_variables)
        result = CheckUtils(response).run_check(get_info['期望结果类型'],get_info['期望结果'])
        return result

    def post(self,post_info):
        url = self.hosts + post_info['请求地址']
        response = self.session.post(url=url,
                                     headers = self.headers,
                                     params= ast.literal_eval(post_info['请求参数(get)']),
                                     # data = get_infos['提交数据（post）'],
                                     json= ast.literal_eval(post_info['提交数据（post）']))
        response.encoding = response.apparent_encoding
        if post_info['取值方式'] == 'json取值':
            value = jsonpath.jsonpath(response.json(),post_info["取值代码"])
            self.temp_variables[post_info['传值变量']] = value
            print(self.temp_variables)
        elif post_info ['取值方式'] == "正则取值":
            value = re.findall(post_info['取值代码'], response.text)[0]
            self.temp_variables[post_info['传值变量']] = value
            print(self.temp_variables)
        result = CheckUtils(response).run_check(post_info['期望结果类型'],post_info['期望结果'])
        return result

    def request(self,step_info):
        request_type = step_info["请求方式"]
        print(step_info['请求参数(get)'])
        if request_type == 'get':
            result = self.get(step_info)
            param_variable_list = re.findall('\\${\w+}', step_info['请求参数(get)'])
            if param_variable_list:
                for param_variable in param_variable_list:
                    step_info['请求参数(get)'] = step_info['请求参数(get)'].replace(param_variable, '"%s"' %
                                                                            self.temp_variables.get(param_variable[2:-1]))
        elif request_type == 'post':
            result = self.post(step_info)
            param_variable_list = re.findall('\\${\w+}', step_info['请求参数(get)'])
            if param_variable_list:
                for param_variable in param_variable_list:
                    step_info['请求参数(get)'] = step_info['请求参数(get)'].replace(param_variable, '"%s"' %
                                                                            self.temp_variables.get(param_variable[2:-1]))
        else:
            result = {'code':3, 'reslut':'请求方式不支持'}
            print(result)
        return result

    def request_by_step(self, step_infos):
        for step_info in step_infos:
            temp_result = self.request(step_info)
            if temp_result['code']!=0:
                break
        return temp_result


if __name__=="__main__":
    # get_infos= {'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据（post）': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在', '期望结果': 'access_token,expires_in'}
    # RequestUtils().get(get_infos)
    # get_infos= {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '删除标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag":{"id":408}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{"errcode":0,"errmsg":"ok"}
    # RequestUtils().request({'请求方式':1})
    case_info = {'case_name': 'case03', 'case_info': [{'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'}, {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '删除标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag":{"id":408}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{"errcode":0,"errmsg":"ok"}'}]}
    # print(case_info[2]['case_info'][0])
    # RequestUtils().request(case_info[2]['case_info'][0])
    RequestUtils().request_by_step(case_info)
