#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: formatter.py
@Time: 18-6-19 15:54
@Last_update: 18-6-19 15:54
@Desc: 各个格式转换
"""
import h5py
import json
import numpy as np

import yy_lib as yy
import yy_lib.assert_ops.assertor as assertor

__all__ = [
    'save_dict_as_hdf5',
    'get_hdf5_as_dict',
    'transfer_npy_to_hdf5',
    'save_list_to_str',
    'get_json_as_dict',
    'save_dict_as_json'
]

def save_dict_as_hdf5(
        save_file_dir: str, save_file_name: str,
        input_dict: dict, useCompression=False) -> None:
    """
    保存dict为hdf5文件
    :param save_file_dir: str
    :param save_file_name: str
    :param input_dict: dict
    :param useCompression: bool
    :return: None
    """
    # 断言保证
    assertor.path_exist_assert(save_file_dir)

    with h5py.File(yy.io.join(save_file_dir, save_file_name), 'w') as f:
        for key, value in input_dict.items():
            if useCompression:
                f.create_dataset(key, data=value, compression='gzip')
            else:
                f.create_dataset(key, data=value)

def save_dict_as_json(
        save_file_dir: str, save_file_name: str,
        input_dict: dict):
    """
    保存dict为json文件
    :param save_file_dir: str
    :param save_file_name: str
    :param input_dict: dict
    :return: None
    """
    # 断言保证
    assertor.path_exist_assert(save_file_dir)

    with open(yy.io.join(save_file_dir, save_file_name), 'w') as f:
        f.write(json.dumps(input_dict, indent=4))

def get_hdf5_as_dict(*paths: tuple) -> dict:
    """
    通过hdf5文件读取,返回dict
    :param paths: tuple
    :return: data_dict: dict
    """
    # 断言保证
    assertor.tuple_type_assert(paths, str)

    file_path = yy.io.join(*paths)
    # 断言保证
    assertor.file_exist_assert(file_path)

    data_dict = {}
    with h5py.File(file_path, 'r') as f:
        for key,value in f.items():
            data_dict[key] = value.value
    return data_dict

def get_json_as_dict(file_path: str):
    """
    通过json文件读取,返回dict
    :param file_path: str
    :return: data_dict: dict
    """
    # 断言保证
    assertor.file_exist_assert(file_path)

    with open(file_path, 'r') as f:
        json_data = f.read()
    json_data = json.loads(json_data)
    data_dict = dict(json_data)

    return data_dict

def transfer_npy_to_hdf5(
        npy_file_path: str, save_file_dir: str,
        save_file_name: str, key_name: str) -> None:
    """
    读取npy文件, 转换为hdf5文件保存
    :param npy_file_path: str
    :param save_file_dir: str
    :param save_file_name: str
    :param key_name: str
    :return: None
    """
    # 断言保证
    assertor.file_exist_assert(npy_file_path)
    assertor.path_exist_assert(save_file_dir)
    # 读取npy数据
    npy_data = np.load(npy_file_path)
    # 变为dict
    rst_dict = {key_name : npy_data}
    # 存储为hdf5
    save_dict_as_hdf5(save_file_dir, save_file_name, rst_dict)

def save_list_to_str(input_list, save_dir, save_name):

    rst_str = '\n'.join(input_list)

    with open(yy.io.join(save_dir,save_name),'w') as f:
        f.write(rst_str)
