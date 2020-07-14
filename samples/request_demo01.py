#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:request_demo01.py
# @time:2020/7/5 2:57 下午

import requests

# 创建一个标签
hosts = 'https://api.weixin.qq.com'

get_params_data = {
    'grant_type':'client_credential',
    'appid':'wx5189359b0e0ddd89',
    'secret':'11d4de7719a2276becf27ab573263061'
}

res01 = requests.get(url=hosts+'/cgi-bin/token',
                     params=get_params_data)

token_id = res01.json()['access_token']
# print(token_id)

# 创建一个标签
get_params_data = {'access_token':token_id}
post_params_data = {   "tag" : {     "name" : "cherry1004"  } }
headinfos = {'Content-Type':'application/json'}

response = requests.post(url='https://api.weixin.qq.com/cgi-bin/tags/create',
                         params=get_params_data,
                         # data=json.dumps(post_param_data),
                         json=post_params_data,
                         headers=headinfos)

print(response.content.decode('utf-8'))