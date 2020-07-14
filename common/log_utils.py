#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:log_utils.py
# @time:2020/7/5 2:24 下午

import os,time
import logging
from common import config

current_path = os.path.dirname(__file__)
log_path = os.path.join(current_path,config.LOG_PATH)

class LogUtils():
    def __init__(self,log_path=log_path):
        self.log_name = os.path.join(log_path,'ApiTest_%s.log'%time.strftime('%Y-%m-%d'))
        self.logger = logging.getLogger('ApiTest')
        self.logger.setLevel(config.LOG_LEVEL)
        # 控制台输出
        console_handler = logging.StreamHandler()
        # 文件输出
        file_handle = logging.FileHandler(self.log_name,'a',encoding='utf-8')
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
        console_handler.setFormatter(formatter)
        file_handle.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handle)

        console_handler.close()   # 防止日志打印重复
        file_handle.close()

    def get_logger(self):
        return self.logger

logger = LogUtils().get_logger()  # 防止日志打印重复

if __name__=='__main__':
    logger.info('hello')