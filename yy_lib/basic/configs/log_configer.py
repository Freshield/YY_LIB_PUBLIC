#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: log_configer.py
@Time: 18-7-3 15:34
@Last_update: 18-7-3 15:34
@Desc: None
"""
import configparser

import yy_lib.assert_ops.assertor as assertor
from yy_lib.io_ops.os_ops import judge_mkdir

__all__ = [
    'LogConfiger'
]

class LogConfiger(object):

    def __init__(self, config: configparser.ConfigParser):
        self._save_log = config.getboolean('log', 'save_log')
        self._log_dir = config.get('log', 'log_dir')
        self._log_file_name = config.get('log', 'log_file_name')
        self._log_logger_name = config.get('log', 'log_logger_name')
        self._log_format = config.get('log', 'log_format', raw=True)
        self._log_level = config.get('log', 'log_level')

    @property
    def save_log(self):
        return self._save_log
    @save_log.setter
    def save_log(self, value):
        self._save_log = value

    @property
    def log_dir(self) -> str:
        """
        判别log_dir是否存在,如果不存在则创建log_dir
        :return:
        """
        judge_mkdir(self._log_dir)

        return self._log_dir
    @log_dir.setter
    def log_dir(self, value: str):
        """
        判别传入的value文件是否存在,若不存在则创建
        :param value: str
        :return:
        """
        # 断言保证
        assertor.type_assert(value, str)

        judge_mkdir(value)
        self._log_dir = value

    @property
    def log_file_name(self):
        return self._log_file_name
    @log_file_name.setter
    def log_file_name(self, value):
        self._log_file_name = value

    @property
    def log_logger_name(self):
        return self._log_logger_name
    @log_logger_name.setter
    def log_logger_name(self, value):
        self._log_logger_name = value

    @property
    def log_format(self):
        return self._log_format
    @log_format.setter
    def log_format(self, value):
        self._log_format = value

    @property
    def log_level(self):
        return self._log_level
    @log_level.setter
    def log_level(self, value):
        self._log_level = value
