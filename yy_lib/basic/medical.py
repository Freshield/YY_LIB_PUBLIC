#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: medical.py
@Time: 18-7-4 11:08
@Last_update: 18-7-4 11:08
@Desc: None
"""
from yy_lib.base.window_dict import WINDOW_DICT

__all__ = [
    'get_window'
]

def get_window(name, window_dict=WINDOW_DICT):
    ww = window_dict[name]['ww']
    wl = window_dict[name]['wl']
    min = wl - (ww/2)
    max = wl + (ww/2)
    return min, max
