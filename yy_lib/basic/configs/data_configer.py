#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: data_driver_configer.py
@Time: 18-6-26 17:56
@Last_update: 18-6-26 17:56
@Desc: data driver的configer
"""
import json
import configparser

import yy_lib.assert_ops.assertor as assertor

__all__ = [
    'DataConfiger'
]

class DataConfiger(object):

    def __init__(self, config: configparser.ConfigParser):
        self._train_data_driver = config.get('data', 'train_data_driver')
        self._predict_data_driver = config.get('data', 'predict_data_driver')
        self._save_test_path_list = config.getboolean('data','save_test_path_list')
        self._image_file_name = config.get('data', 'image_file_name')
        self._label_file_name = config.get('data', 'label_file_name')
        self._image_data_key = config.get('data', 'image_data_key')
        self._label_data_key = config.get('data', 'label_data_key')
        self._batch_size = config.getint('model','batch_size')
        self._file_size = config.getint('data', 'file_size')
        self._split_ratio = config.getfloat('data', 'split_ratio')
        self._file_dir = config.get('data', 'file_dir')
        self._tank_dir = config.get('data', 'tank_dir')

        self._image_data_shape = json.loads(config.get('data','image_data_shape'))
        self._label_data_shape = json.loads(config.get('data','label_data_shape'))

    @property
    def train_data_driver(self):
        return self._train_data_driver
    @train_data_driver.setter
    def train_data_driver(self, value):
        self._train_data_driver = value

    @property
    def predict_data_driver(self):
        return self._predict_data_driver
    @predict_data_driver.setter
    def predict_data_driver(self, value):
        self._predict_data_driver = value

    @property
    def save_test_path_list(self):
        return self._save_test_path_list
    @save_test_path_list.setter
    def save_test_path_list(self, value):
        self._save_test_path_list = value

    @property
    def image_file_name(self):
        return self._image_file_name
    @image_file_name.setter
    def image_file_name(self, value):
        self._image_file_name = value

    @property
    def label_file_name(self):
        return self._label_file_name
    @label_file_name.setter
    def label_file_name(self, value):
        self._label_file_name = value

    @property
    def image_data_key(self):
        return self._image_data_key
    @image_data_key.setter
    def image_data_key(self, value):
        self._image_data_key = value

    @property
    def label_data_key(self):
        return self._label_data_key
    @label_data_key.setter
    def label_data_key(self, value):
        self._label_data_key = value

    @property
    def batch_size(self):
        return self._batch_size
    @batch_size.setter
    def batch_size(self, value):
        self._batch_size = value

    @property
    def file_size(self):
        return self._file_size
    @file_size.setter
    def file_size(self, value):
        self._file_size = value

    @property
    def split_ratio(self):
        return self._split_ratio
    @split_ratio.setter
    def split_ratio(self, value):
        self._split_ratio = value

    @property
    def file_dir(self) -> str:
        """
        判别file_dir是否存在,并返回file_dir
        :return: str
        """
        # 断言保证
        assertor.path_exist_assert(self._file_dir)

        return self._file_dir
    @file_dir.setter
    def file_dir(self, value: str):
        """
        判别value的path是否存在,若存在则设置file_dir为value
        :param value: str
        :return:
        """
        # 断言保证
        assertor.path_exist_assert(value)

        self._file_dir = value

    @property
    def tank_dir(self):
        # 断言保证
        assertor.path_exist_assert(self._tank_dir)

        return self._tank_dir
    @tank_dir.setter
    def tank_dir(self, value):
        # 断言保证
        assertor.path_exist_assert(value)

        self._tank_dir = value

    @property
    def image_data_shape(self):
        return self._image_data_shape
    @image_data_shape.setter
    def image_data_shape(self, value):
        self._image_data_shape = value

    @property
    def label_data_shape(self):
        return self._label_data_shape

    @label_data_shape.setter
    def label_data_shape(self, value):
        self._label_data_shape = value

