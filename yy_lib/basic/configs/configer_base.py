#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: configer_base.py
@Time: 18-6-29 16:22
@Last_update: 18-6-29 16:22
@Desc: 定义Configer的基础类,定义为单件模式
"""
import configparser
import yy_lib as yy
from yy_lib.base.stronger_dict import StrongerDict
import yy_lib.assert_ops.assertor as assertor

__all__ = [
    'Configer'
]

class Configer(object):

    _instance = None

    def __new__(cls, *config_path: tuple):
        """
        接受config path来new一个单件configer,
        不应该直接实例化configer而应该使用init_configer方法
        :param config_path: tuple
        :return Configer
        """
        # 断言保证
        assertor.type_assert(config_path, tuple)
        
        # 如果类维护的实例为None就创建一个新的,否则直接返回
        if Configer._instance is None:
            Configer._instance = object.__new__(cls)
            Configer._instance.config = Configer._instance._get_config_parser(*config_path)
            
        return Configer._instance

    @classmethod
    def get_configer(cls):
        """
        获取单件configer类
        :return: Configer
        """
        # 断言保证
        assertor.not_None_assert(Configer._instance)

        return Configer._instance
    

    def _get_config_parser(self, *config_path_tuple: tuple):
        """
        得到config parser
        :param config_path_tuple: tuple
        :return: config
        """
        file_path = yy.io.join(*config_path_tuple)
        # 断言保证
        assertor.file_exist_assert(file_path)

        config = configparser.ConfigParser()
        config.read(file_path)

        return config
