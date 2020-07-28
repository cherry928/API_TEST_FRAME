#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:request_uitls.py
# @time:2020/7/12 8:50 上午
import ast
import requests
import jsonpath
import re
from requests.exceptions import RequestException
from requests.exceptions import ProxyError
from requests.exceptions import ConnectionError
from common import config
from common.check_utils import CheckUtils
from common.test_data_utils import TestdataUtils
from nb_log import LogManager

logger = LogManager(__file__).get_logger_and_add_handlers()


class RequestUtils():
    def __init__(self):
        self.hosts = config.URL
        self.headers = {'ContentType':'application/json;charset=utf-8'}
        self.session = requests.session()
        self.temp_variables = {}

    def __get(self,get_info):
        try:
            url = self.hosts + get_info['请求地址']
            # print('get请求url为%s'%url)
            response = self.session.get(url=url,
                                        params= ast.literal_eval(get_info['请求参数(get)']))
            response.encoding = response.apparent_encoding
            if get_info['取值方式'] == 'json取值':
                value = jsonpath.jsonpath(response.json(),get_info["取值代码"])[0]
                self.temp_variables[get_info['传值变量']] = value
            elif get_info ['取值方式'] == "正则取值":
                value = re.findall(get_info['取值代码'], response.text)[0]
                self.temp_variables[get_info['传值变量']] = value
            # print('check_type为%s'%get_info['期望结果类型'])
            # print('check_data为%s'%get_info['期望结果'])
            # print(response.status_code)
            result = CheckUtils(response).run_check(get_info['期望结果类型'],get_info['期望结果'])
        except ProxyError as e:
            result = {'code': 4, 'result': '[%s]请求：代理错误异常' % get_info['接口名称']}
        except ConnectionError as e:
            result = {'code':4, 'result':'[%s]请求：连接超时'%get_info['接口名称']}
        except RequestException as e:
            result = {'code':4, 'result':'[%s]请求：报Request异常，原因是%s'%(get_info['接口名称'],e.__str__())}
        except Exception as e:
            result = {'code':4, 'result':'[%s]请求：报错，原因是%s'%(get_info['接口名称'],e.__str__())}
        return result

    def __post(self,post_info):
        try:
            url = self.hosts + post_info['请求地址']
            # print('post请求url为%s' % url)
            # print('post请求参数为%s'%ast.literal_eval(post_info['请求参数(get)']))
            # print('post请求json为%s'%post_info['提交数据（post)'])
            response = self.session.post(url=url,
                                         headers=self.headers,
                                         params=ast.literal_eval(post_info['请求参数(get)']),
                                         # data=post_info['提交数据（post)'],
                                         json= ast.literal_eval(post_info['提交数据（post)'])
                                         )
            response.encoding = response.apparent_encoding
            # print('post请求取值方式为：%s'%post_info['取值方式'])
            if post_info['取值方式'] == 'json取值':
                value = jsonpath.jsonpath(response.json(),post_info["取值代码"])[0]
                self.temp_variables[post_info['传值变量']] = value
                # print('value为%s'%self.temp_variables)
            elif post_info ['取值方式'] == "正则取值":
                value = re.findall(post_info['取值代码'], response.text)[0]
                self.temp_variables[post_info['传值变量']] = value
                # print('value为%s'%self.temp_variables)
            # print('post请求返回的值为：%s'%response.content.decode('utf-8'))
            # print('check_type为%s' % post_info['期望结果类型'])
            # print('check_data为%s' % post_info['期望结果'])
            result = CheckUtils(response).run_check(post_info['期望结果类型'],post_info['期望结果'])
        except ProxyError as e:
            result = {'code': 4, 'result': '[%s]请求：代理错误异常' % post_info['接口名称']}
        except ConnectionError as e:
            result = {'code':4, 'result':'[%s]请求：连接超时'%post_info['接口名称']}
        except RequestException as e:
            result = {'code':4, 'result':'[%s]请求：报Request异常，原因是%s'%(post_info['接口名称'],e.__str__())}
        except Exception as e:
            result = {'code':4, 'result':'[%s]请求：报错，原因是%s'%(post_info['接口名称'],e.__str__())}
        return result

    def request(self,step_info):
        try:
            request_type = step_info["请求方式"]
            param_variable_list = re.findall('\\${\w+}', step_info['请求参数(get)'])
            if param_variable_list:
                for param_variable in param_variable_list:
                    step_info["请求参数(get)"] = step_info["请求参数(get)"] \
                        .replace(param_variable, '"%s"' % self.temp_variables.get(param_variable[2:-1]))
            if request_type == 'get':
                result = self.__get(step_info)
            elif request_type == 'post':
                data_variable_list = re.findall('\\${\w+}', step_info['提交数据（post)'])
                if data_variable_list:
                    for param_variable in data_variable_list:
                        step_info['提交数据（post)'] = step_info['提交数据（post)'].replace(param_variable, '"%s"' %
                                                                                self.temp_variables.get(param_variable[2:-1]))
                result = self.__post(step_info)
            else:
                result = {'code':1, 'reslut':'请求方式不支持'}
                logger.error('请求方式不支持')
        except Exception as e:
            result = {'code':4, 'reslut':'用例编号[%s]的[%s]步出现系统异常，原因：%s'%(step_info['用例编号'],step_info['测试用例步骤'],e.__str__())}
            logger.error('用例编号[%s]的[%s]步骤出现系统异常，原因：%s'%(step_info['测试用例编号'],step_info["测试用例步骤"],e.__str__()))
        return result

    def request_by_step(self,step_infos):
        self.temp_variables = {}
        for step_info in step_infos:
            temp_result = self.request(step_info)
            if temp_result['code'] != 0:
                TestdataUtils().write_result_to_excel(step_info['测试用例编号'], step_info['测试用例步骤'], '失败')
                break
            else:
                TestdataUtils().write_result_to_excel(step_info['测试用例编号'], step_info['测试用例步骤'])
        return temp_result


if __name__=="__main__":
    case_info = [
        {'请求方式': 'get', '请求地址': '/cgi-bin/token',
         '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}',
         '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token'},
        {'请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}',
         '提交数据（post）': '{"tag":{"id":459}}', '取值方式': '无', '传值变量': '', '取值代码': ''}
    ]
    RequestUtils().request_by_step(case_info)
