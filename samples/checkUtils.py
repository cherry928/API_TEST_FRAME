#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:checkUtils.py
# @time:2020/7/15 8:30 下午

import ast
import re

class CheckUtils:
    def __init__(self,check_response=None):
        self.ck_response = check_response
        self.ck_rules = {
            '无':self.no_check,
            'json键是否存在':self.check_key,
            'json键':self.check_keyvalue,
            '正则匹配':self.check_regxp
        }
        self.pass_result = {
            'code': 0,   # 请求是否成功的标志位
            'response_reason': self.ck_response.reason,
            'response_code': self.ck_response.status_code,
            'resonse_header': self.ck_response.headers,
            'response_nody': self.ck_response.text,
            'check_result':True,
            'message':'' # 扩展作为日志输出等
        }
        self.fail_result = {
            'code': 2,  # 请求是否成功的标志位
            'response_reason': self.ck_response.reason,
            'response_code': self.ck_response.status_code,
            'resonse_header': self.ck_response.headers,
            'response_nody': self.ck_response.text,
            'check_result': False,
            'message': ''  # 扩展作为日志输出等
        }

    def no_check(self):
        return self.pass_result

    def check_key(self,check_data=None):
        '''
        是否包含json key
        :param check_data: {"access_token":"hello","expires_in":7200}
        :return:
        '''
        check_data_list = check_data.split(',')
        reslist = []     # 存放每次比较的结果
        wrongkey = []    # 存放比较失败key
        for check_data in check_data_list:
            if check_data in self.ck_response.json().keys():
                reslist.append(self.pass_result)
            else:
                reslist.append(self.fail_result)
                wrongkey.append(check_data)
        print(reslist)
        print(wrongkey)
        if self.fail_result in reslist:
            return self.fail_result
        else:
            return self.pass_result

    def check_keyvalue(self, check_data=None):
        res_list = []     # 存放每次比较的结果
        wrong_items = []    # 存放比较失败 items
        for check_item in ast.literal_eval(check_data).items():
            if check_item in self.ck_response.json().items():
                res_list.append(self.pass_result)
            else:
                res_list.append(self.fail_result)
                wrong_items.append(check_item)
        print(res_list)
        print(wrong_items)
        if self.fail_result in res_list:
            return self.fail_result
        else:
            return self.pass_result

    def check_regxp(self,check_data=None):
        pattern = re.compile(check_data)
        if re.findall(pattern=pattern,string=self.ck_response.text):
            return self.pass_result
        else:
            return self.fail_result

    def run_check(self,check_type=None,check_data=None):
        code = self.ck_response.status_code
        if code == 200:
            if check_type in self.ck_rules.keys():
                result = self.ck_rules[check_type](check_data)
                return result
            else:
                self.fail_result['message'] = '不支持%s判断方法'%check_type
                return self.fail_result
        else:
            self.fail_result['message'] = '请求响应状态码非%s'%str(code)
            return self.fail_result



if __name__=='__main__':
    # CheckUtils({"access_token":"hello","expires_in":7200}).check_data('access_token,expires_in')
    # CheckUtils({"access_token": "hello", "expires_in": 7200}).check_keyvalue('{"expires_in":7200}')
    CheckUtils({"access_token": "hello", "expires_in": 7200}).check_regxp('"access_token": "(.+?)"')
    # s = {"access_token":"hello","expires_in":7200}
    # print(s.items())