#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: np_ops.py
@Time: 2020-01-20 10:55
@Last_update: 2020-01-20 10:55
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import numpy as np
import yy_lib.base.assertor as assertor


def judge_del_last_dim(input_array: np.ndarray, basic_dims=2):
    '''
    判别要显示的图像是否需要去除最后的维度
    :param input_array: ndarray,(x,y) or (x,y,1)
    :return: rst_array, ndarray
    '''
    # 断言保证
    assertor.array_x_dims_multi_assert(input_array, [basic_dims,basic_dims+1])

    rst_array = None
    if len(input_array.shape) == (basic_dims+1):
        # 断言保证
        assertor.array_length_assert(input_array,1,-1)

        array_shape = list(input_array.shape)
        array_shape.pop(-1)
        rst_array = np.reshape(input_array, array_shape)
    else:
        rst_array = input_array

    return rst_array


def save_npz(input_array, save_path, save_prefix='array'):
    """保存数据为npz格式"""
    data_dict = dict()
    for i in range(len(input_array)):
        data_dict['%s_%d' % (save_prefix, i)] = input_array[i:i + 1]

    np.savez(save_path, **data_dict)
