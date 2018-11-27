#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: train_configer.py
@Time: 18-6-26 17:55
@Last_update: 18-6-26 17:55
@Desc: 训练使用的config, 
"""
import configparser
import yy_lib as yy
import yy_lib.assert_ops.assertor as assertor
from yy_lib.basic.configs import Configer, DataConfiger, LogConfiger, ModelConfiger

__all__ = [
    'TrainConfiger'
]

class TrainConfiger(Configer):

    def __new__(cls, *config_path: tuple):
        """
        Train的Configer的初始化
        :param config_path: tuple
        :return: TrainConfiger
        """
        # 断言保证
        assertor.type_assert(config_path, tuple)

        # 调基类的new方法
        instance = Configer.__new__(cls, *config_path)
        instance._data = DataConfiger(instance.config)
        instance._log = LogConfiger(instance.config)
        instance._model = ModelConfiger(instance.config)

        instance._version = instance.config.get('basic', 'version')
        return instance

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        self._data = value

    @property
    def log(self):
        return self._log
    @log.setter
    def log(self, value):
        self._log = value

    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, value):
        self._model = value

    @property
    def version(self):
        return self._version
    @version.setter
    def version(self, value):
        self._version = value

    @property
    def config_info(self):
        _config_info = '\n'
        for section in self.config.sections():
            _config_info += '[%s]\n\n' % str(section)
            for item in self.config.items(section, raw=True):
                key, value = item
                _config_info += '%s = %s\n' % (str(key), str(value))
            _config_info += '\n'

        return _config_info


if __name__ == '__main__':
    configer = TrainConfiger('/media/freshield/CORSAIR/Linkingmed_HT/Codes_HT/Linkingmed/22_heart_four_organs/04_Wiggle_segment/data','test.ini')
    print(configer.config.sections())
    print(type(configer.config))
    print(configer.data.batch_size)

    configer = TrainConfiger('','test.ini')
    print(configer.config.sections())
    print(type(configer.config))
    print(configer.data.batch_size)

    configer = TrainConfiger.get_configer()
    print(configer.log.log_dir)
    print(configer.log.log_file_name)
    print(configer.log.log_logger_name)
    print(configer.log.log_format)
    print(configer.log.log_level)