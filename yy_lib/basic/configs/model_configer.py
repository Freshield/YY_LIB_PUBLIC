#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: model_configer.py
@Time: 18-7-5 11:29
@Last_update: 18-7-5 11:29
@Desc: None
"""
import json
import configparser

import yy_lib.assert_ops.assertor as assertor

__all__ = [
    'ModelConfiger'
]

class ModelConfiger(object):

    def __init__(self, config: configparser.ConfigParser):
        self._model_name = config.get('model', 'model_name')
        self._batch_size = config.getint('model','batch_size')
        self._input_shape = json.loads(config.get('model','input_shape'))
        self._label_shape = json.loads(config.get('model','label_shape'))
        self._device = config.get('model', 'device')
        self._classes_num = config.getint('model', 'classes_num')
        self._learning_rate_value = config.getfloat('model', 'learning_rate_value')
        self._lr_decay = config.getfloat('model', 'lr_decay')
        self._up_method = config.get('model', 'up_method')
        self._first_layer_diff = config.getboolean('model', 'first_layer_diff')
        self._epoch = config.getint('model', 'epoch')
        self._gpu_allow_growth = config.getboolean('model', 'gpu_allow_growth')
        self._best_tank_num = config.getint('model', 'best_tank_num')
        self._threshold_value = config.getfloat('model', 'threshold_value')

        self._inputer_list = config.get('model','inputer_list').strip('[]').split(',')
        self._preder_list = config.get('model','preder_list').strip('[]').split(',')
        self._acter_list = config.get('model','acter_list').strip('[]').split(',')
        self._losser_list = config.get('model','losser_list').strip('[]').split(',')
        self._accier_list = config.get('model','accier_list').strip('[]').split(',')
        self._optimizer_list = config.get('model','optimizer_list').strip('[]').split(',')

    @property
    def model_name(self):
        return self._model_name
    @model_name.setter
    def model_name(self, value):
        self._model_name = value

    @property
    def batch_size(self):
        return self._batch_size
    @batch_size.setter
    def batch_size(self, value):
        self._batch_size = value

    @property
    def input_shape(self):
        return self._input_shape
    @input_shape.setter
    def input_shape(self, value):
        self._input_shape = value

    @property
    def label_shape(self):
        return self._label_shape
    @label_shape.setter
    def label_shape(self, value):
        self._label_shape = value

    @property
    def device(self):
        return self._device
    @device.setter
    def device(self, value):
        self._device = value

    @property
    def classes_num(self):
        return self._classes_num
    @classes_num.setter
    def classes_num(self, value):
        self._classes_num = value

    @property
    def learning_rate_value(self):
        return self._learning_rate_value
    @learning_rate_value.setter
    def learning_rate_value(self, value):
        self._learning_rate_value = value

    @property
    def lr_decay(self):
        return self._lr_decay
    @lr_decay.setter
    def lr_decay(self, value):
        self._lr_decay = value

    @property
    def up_method(self):
        return self._up_method
    @up_method.setter
    def up_method(self, value):
        self._up_method = value

    @property
    def first_layer_diff(self):
        return self._first_layer_diff
    @first_layer_diff.setter
    def first_layer_diff(self, value):
        self._first_layer_diff = value

    @property
    def epoch(self):
        return self._epoch
    @epoch.setter
    def epoch(self, value):
        self._epoch = value

    @property
    def gpu_allow_growth(self):
        return self._gpu_allow_growth
    @gpu_allow_growth.setter
    def gpu_allow_growth(self, value):
        self._gpu_allow_growth = value

    @property
    def best_tank_num(self):
        return self._best_tank_num
    @best_tank_num.setter
    def best_tank_num(self, value):
        self._best_tank_num = value

    @property
    def threshold_value(self):
        return self._threshold_value
    @threshold_value.setter
    def threshold_value(self, value):
        self._threshold_value = value

    @property
    def inputer_list(self):
        return self._inputer_list
    @inputer_list.setter
    def inputer_list(self, value):
        self._inputer_list = value

    @property
    def preder_list(self):
        return self._preder_list
    @preder_list.setter
    def preder_list(self, value):
        self._preder_list = value

    @property
    def acter_list(self):
        return self._acter_list
    @acter_list.setter
    def acter_list(self, value):
        self._acter_list = value

    @property
    def losser_list(self):
        return self._losser_list
    @losser_list.setter
    def losser_list(self, value):
        self._losser_list = value

    @property
    def accier_list(self):
        return self._accier_list
    @accier_list.setter
    def accier_list(self, value):
        self._accier_list = value

    @property
    def optimizer_list(self):
        return self._optimizer_list
    @optimizer_list.setter
    def optimizer_list(self, value):
        self._optimizer_list = value
