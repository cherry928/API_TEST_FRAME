#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:config.py
# @time:2020/7/5 11:53 上午

import os
from common.config_utils import ConfigUtils

config_path = os.path.join(os.path.dirname(__file__), '..', 'conf/config.ini')
configUtils = ConfigUtils(config_path)
URL = configUtils.read_value('default','URL')
CASE_DATA_PATH = configUtils.read_value('path','CASE_DATA_PATH')
LOG_PATH = configUtils.read_value('path','LOG_PATH')
LOG_LEVEL = int(configUtils.read_value('log','LOG_LEVEL'))
REPORT_PATH = configUtils.read_value('path','REPORT_PATH')
CASE_PATH = configUtils.read_value('path','CASE_PATH')
SMTP_SERVER = configUtils.read_value('email','smtp_server')
SMTP_SENDER = configUtils.read_value('email','smtp_sender')
SMTP_PASSWORD = configUtils.read_value('email','smtp_password')
SMTP_RECEIVER = configUtils.read_value('email','smtp_receiver')
SMTP_CC = configUtils.read_value('email','smtp_cc')
SMTP_SUBJECT = configUtils.read_value('email','smtp_subject')
# print(SMTP_SUBJECT)