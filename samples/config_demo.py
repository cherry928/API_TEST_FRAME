#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:config_demo.py
# @time:2020/7/5 11:47 上午

import os
import configparser

config_path = os.path.join(os.path.dirname(__file__), '..', 'conf/config.ini')

cfg = configparser.ConfigParser()
cfg.read(config_path)
