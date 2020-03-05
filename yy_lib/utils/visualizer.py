#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: visualizer.py
@Time: 2020-01-20 10:53
@Last_update: 2020-01-20 10:53
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import matplotlib.pyplot as plt
import yy_lib.base.assertor as assertor
import yy_lib as yy


def show_np(input_array, x_label='"x_label"', y_label='y_label'):
    """
    显示numpy的图
    :param input_array: ndarray
    :return: None
    """
    # 断言保证
    assertor.array_x_dims_multi_assert(input_array, [2,3])

    input_array = yy.io.judge_del_last_dim(input_array)

    plt.imshow(input_array)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
    plt.close()


def show_2np(input_array1, input_array2, title1='image1', title2='image2'):

    input_array1 = yy.io.judge_del_last_dim(input_array1)
    input_array2 = yy.io.judge_del_last_dim(input_array2)

    plt.figure()
    plt.subplot(121)
    plt.imshow(input_array1)
    plt.title(title1)
    plt.subplot(122)
    plt.imshow(input_array2)
    plt.title(title2)
    plt.show()
    plt.close()
