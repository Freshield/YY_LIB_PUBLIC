#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: log.py
@Time: 18-7-3 15:29
@Last_update: 18-7-3 15:29
@Desc: None
"""
import sys
import logging
import configparser

import yy_lib as yy
import yy_lib.assert_ops.assertor as assertor
from yy_lib.base.default import get_YMDHMS_time
from yy_lib.io_ops.os_ops import judge_mkdir
from yy_lib.basic.configs.train_configer import TrainConfiger

__all__ = [
    'LOG_LEVEL_DICT',
    'Log'
]

LOG_LEVEL_DICT = {
    'DEBUG' : logging.DEBUG,
    'INFO' : logging.INFO,
    'WARNING' : logging.WARNING,
    'ERROR' : logging.ERROR,
    'FATAL' : logging.FATAL
}

class Log(object):

    _instance = None

    def __new__(cls):
        """
        初始化Log类来获得单件实例
        :return Log
        """
        log_config = TrainConfiger.get_configer()._log
        # 断言保证
        assertor.not_equal_assert(log_config, None)

        # 如果类维护的实例为None就创建一个新的,否则直接返回
        if Log._instance is None:
            Log._instance = object.__new__(cls)
            Log._instance.log_dir = None
            Log._instance.log_sub_dir = None
            Log._instance.log_image_dir = None
            Log._instance.log_tank_dir = None
            Log._instance.log_config = log_config
            Log._instance.save_log = None
            Log._instance.logger = Log._instance._init_log()

        return Log._instance

    @classmethod
    def init(cls):
        cls.__new__(Log)
        return cls._instance

    def _get_dir_with_time_stamp(self) -> str:
        """
        获得把time stamp加入路径的文件夹并辨别创建文件夹
        :return: log_dir: str
        """

        # 得到time stamp
        time_stamp = get_YMDHMS_time()
        # 获得路径并判别创建文件夹
        log_dir = yy.io.join(self.log_config.log_dir, time_stamp + '_log')
        log_sub_dir = yy.io.join(log_dir, 'log')
        log_image_dir = yy.io.join(log_dir, 'image')
        log_tank_dir = yy.io.join(log_dir, 'tank')
        judge_mkdir(log_sub_dir)
        judge_mkdir(log_image_dir)
        judge_mkdir(log_tank_dir)

        # 更新成员
        self.log_sub_dir = log_sub_dir
        self.log_image_dir = log_image_dir
        self.log_tank_dir = log_tank_dir

        return log_sub_dir

    def _init_log(self):
        # 获取logger实例，如果参数为空则返回root logger
        logger = logging.getLogger(self.log_config.log_logger_name)
        # 指定logger输出格式
        formatter = logging.Formatter(self.log_config.log_format)
        self.save_log = self.log_config.save_log
        if self.log_config.save_log:
            # 文件日志
            log_sub_dir = self._get_dir_with_time_stamp()
            log_file_path = yy.io.join(log_sub_dir, self.log_config.log_file_name)
            file_handler = logging.FileHandler(log_file_path)
            # 可以通过setFormatter指定输出格式
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        # 控制台日志
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.formatter = formatter
        # 为logger添加的日志处理器，可以自定义日志处理器让其输出到其他地方
        logger.addHandler(console_handler)
        # 指定日志的最低输出级别，默认为DEBUG级别
        logger.setLevel(LOG_LEVEL_DICT[self.log_config.log_level])

        return logger

    @classmethod
    def get_log(cls):
        """
        得到log唯一的单件
        :return: Log
        """
        assertor.not_None_assert(Log._instance)

        return Log._instance

    @classmethod
    def debug(cls, msg: str) -> None:
        """
        DEGUG信息
        :param msg: str
        :return:
        """
        # 断言保证
        assertor.type_assert(msg, str)

        cls._instance.logger.debug(msg)

    @classmethod
    def info(cls, msg: str) -> None:
        """
        DEGUG信息
        :param msg: str
        :return:
        """
        # 断言保证
        assertor.type_assert(msg, str)

        cls._instance.logger.info(msg)

    @classmethod
    def warning(cls, msg: str) -> None:
        """
        DEGUG信息
        :param msg: str
        :return:
        """
        # 断言保证
        assertor.type_assert(msg, str)

        cls._instance.logger.warning(msg)

    @classmethod
    def error(cls, msg: str) -> None:
        """
        DEGUG信息
        :param msg: str
        :return:
        """
        # 断言保证
        assertor.type_assert(msg, str)

        cls._instance.logger.error(msg)

    @classmethod
    def fatal(cls, msg: str) -> None:
        """
        DEGUG信息
        :param msg: str
        :return:
        """
        # 断言保证
        assertor.type_assert(msg, str)

        cls._instance.logger.fatal(msg)

    @classmethod
    def addHandler(cls, handler: logging.Handler):
        """
        增加handler
        :param handler: logging.Handler
        :return:
        """
        # 断言保证
        assertor.instance_of_assert(handler, logging.Handler)

        cls._instance.logger.addHandler(handler)

    @classmethod
    def removeHandler(cls, handler: logging.Handler):
        """
        去除handler
        :param handler: logging.Handler
        :return:
        """
        # 断言保证
        assertor.instance_of_assert(handler, logging.Handler)

        cls._instance.logger.removeHandler(handler)

    @classmethod
    def addFileHandler(cls, file_name: str, file_dir=None) -> logging.FileHandler:
        """
        直接添加文件的handler
        :param file_name: str
        :param file_dir: None or str
        :return:
        """
        if file_dir is None:
            file_dir = cls._instance.log_sub_dir
        # 断言保证
        assertor.type_assert(file_name, str)

        # 判别并创建文件夹
        judge_mkdir(file_dir)
        # 创建file handler
        formatter = logging.Formatter(cls._instance.log_config.log_format)
        log_file_path = yy.io.join(file_dir, file_name)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        # 设置file handler
        cls.addHandler(file_handler)

        return file_handler


if __name__ == '__main__':
    config = TrainConfiger('/media/freshield/CORSAIR/Linkingmed_HT/Codes_HT/Linkingmed/22_heart_four_organs/04_Wiggle_segment/data/test.ini')
    Log.init()
    Log.debug('debug')
    Log.info('info')
    Log.warning('warning')
    Log.error('error')
    Log.fatal('fatal')

    file_handler = Log.addFileHandler('tester.log')
    Log.debug('debug1')
    Log.info('info1')
    Log.warning('warning1')
    Log.error('error1')
    Log.fatal('fatal1')
    Log.removeHandler(file_handler)


    Log.debug('debug2')
    Log.info('info2')
    Log.warning('warning2')
    Log.error('error2')
    Log.fatal('fatal2')