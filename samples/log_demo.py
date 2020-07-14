#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:log_demo.py
# @time:2020/7/5 2:16 下午

import logging

logger = logging.getLogger('logger')
handler1 = logging.StreamHandler()  # 控制台
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler1.setFormatter(formatter)
logger.addHandler(handler1)
logger.info('hell01')

handler2 = logging.FileHandler('./test.log','a',encoding='utf-8')
logger.setLevel(10)
handler2.setFormatter(formatter)
logger.addHandler(handler2)
logger.info('hello2')