#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:log_demo_nb.py
# @time:2020/7/26 11:18 上午
import os
from nb_log import LogManager

l_path = os.path.join(os.path.dirname(__file__),'pythonlog')
# print(l_path)

logger = LogManager('lalala').get_logger_and_add_handlers()
logger.info('你好')
logger.warning('!!哈哈哈')
logger.error('报错啦')
