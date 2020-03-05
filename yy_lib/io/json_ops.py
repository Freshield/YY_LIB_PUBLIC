#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: json_ops.py
@Time: 2019-11-13 16:25
@Last_update: 2019-11-13 16:25
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import os
import json
import yy_lib.base.assertor as assertor


def save_dict_as_json(
        save_file_path: str, input_dict: dict, 
        save_file_name=None, indent=4, ensure_ascii=False):
    """
    保存dict为json文件
    """
    if save_file_name is not None:
        save_file_path = os.path.join(save_file_path, save_file_name)

    with open(save_file_path, 'w') as f:
        f.write(json.dumps(input_dict, indent=indent, ensure_ascii=ensure_ascii))


def get_json_as_dict(file_path: str, file_name=None):
    """
    通过json文件读取,返回dict
    """
    if file_name is not None:
        file_path = os.path.join(file_path, file_name)

    # 断言保证
    assertor.file_exist_assert(file_path)

    with open(file_path, 'r') as f:
        json_data = f.read()
    json_data = json.loads(json_data)
    data_dict = dict(json_data)

    return data_dict


def read_add_log_json(file_path, add_dict, file_name=None):
    """
    读取log的json文件，并且添加新的log并保存
    """
    log_dict = get_json_as_dict(file_path, file_name)

    for key, value in add_dict.items():
        log_dict[key] = value

    save_dict_as_json(file_path, log_dict, file_name)

