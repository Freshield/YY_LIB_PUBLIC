#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: default.py
@Time: 18-6-22 13:05
@Last_update: 18-6-22 13:05
@Desc: 最基础的依赖类
"""
import time

__all__ = [
    'judge_to_list',
    'get_YMD_time',
    'get_YMDHMS_time'
]

def judge_to_list(input_: object) -> list:
    """
    判断输入是否为list,如果不是list则转换为list返回
    :param input_: object
    :return: rst_list
    """
    rst_list = None
    if type(input_) is not list:
        rst_list = [input_]
    else:
        rst_list = input_

    return rst_list

def get_YMD_time():
    return time.strftime("%Y%m%d", time.localtime())

def get_YMDHMS_time():
    return time.strftime("%Y%m%d_%H%M%S", time.localtime())
