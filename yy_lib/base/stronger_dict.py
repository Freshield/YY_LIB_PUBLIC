#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: stronger_dict.py
@Time: 18-6-19 14:45
@Last_update: 18-6-19 14:45
@Desc: 可以使用点来get set的dict
"""

__all__ = [
    'StrongerDict'
]

class StrongerDict(dict):

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def __call__(self, key):
        return self[key]