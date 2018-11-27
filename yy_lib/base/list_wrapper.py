#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: list_wrapper.py
@Time: 18-6-30 19:41
@Last_update: 18-6-30 19:41
@Desc: None
"""

__all__ = [
    'ListWrapper'
]

class ListWrapper(list):

    def __init__(self, input_list):
        list.__init__([])
        self += input_list

    def set_list(self, input_list):
        self.clear()
        self += input_list