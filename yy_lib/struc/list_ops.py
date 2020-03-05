#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: list_ops.py
@Time: 2020-03-03 13:49
@Last_update: 2020-03-03 13:49
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import random


def split_list_by_ratio(path_dict_list, split_ratio_dict={'train': 0.8, 'val': 0.2},
                        shuffle=True):
    """
    切分路径列表
    返回：split_ratio_dict中的key的且分后的字典
    整体流程：
    1. 根据是否shuffle进行混排
    2. 遍历split ratio dict
    3. 按照相应的比例来对数据进行切分
    """
    # 检测比率是否小于1
    ratio_sum = sum(split_ratio_dict.values())
    assert ratio_sum <= 1, 'The split ratio dict\'s ratio sum larger than 1'

    # 1. 根据是否shuffle进行混排
    if shuffle:
        random.shuffle(path_dict_list)

    rst_dict = dict()
    # 2. 遍历split ratio dict
    data_index = 0
    for dataset_name, ratio in split_ratio_dict.items():
        # 得到相应数据偏移量
        data_size = int(len(path_dict_list) * ratio)
        rst_dict[dataset_name] = path_dict_list[data_index: data_index + data_size]
        data_index += data_size

    return rst_dict


def split_list_by_num(path_list, data_per_file, min_size=0, shuffle=True):
    """
    按照数量来切分路径列表
    整体流程：
    1. 根据是否shuffle进行混排
    2. 首先来把能正整除的部分放进去
    3. 然后把余的部分放进去
    """
    # 1. 根据是否shuffle进行混排
    if shuffle:
        random.shuffle(path_list)

    rst_path_list = []
    path_length = len(path_list)
    # 2. 首先来把能正整除的部分放进去
    for i in range(path_length // data_per_file):
        rst_path_list.append(path_list[i * data_per_file: (i + 1) * data_per_file])

    # 3. 然后把余的部分放进去
    rest_num = path_length % data_per_file
    if rest_num != 0:
        # 如果大于min_size
        if rest_num >= min_size:
            rst_path_list.append(path_list[-rest_num:])
        # 如果小于min_size则补全到min_size
        else:
            last_list = path_list[-rest_num:] + path_list[:(min_size - rest_num)]
            rst_path_list.append(last_list)

    return rst_path_list
