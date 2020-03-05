#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: assertor.py
@Time: 2019-11-12 14:58
@Last_update: 2019-11-12 14:58
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
import inspect
import numpy as np

__all__ = [
    'get_varname',
    'type_assert',
    'type_multi_assert',
    'condition_not_happen_assert',
    'equal_assert',
    'equal_multi_assert',
    'not_equal_assert',
    'greater_or_equal_assert',
    'smaller_or_equal_assert',
    'array_x_dims_assert',
    'array_x_dims_multi_assert',
    'array_dtype_assert',
    'array_length_assert',
    'array_shape_assert',
    'file_exist_assert',
    'xyzc_seq_array_assert',
    'xyz_seq_array_assert',
    'list_type_assert',
    'tuple_type_assert',
    'zyx_seq_array_assert',
    'byxz_seq_array_assert',
    'yx_seq_array_assert',
    'tuple_length_assert',
    'list_length_assert',
    'xyc_seq_array_assert',
    'path_exist_assert',
    'zyx_seq_image_assert',
    'zyx_seq_space_assert',
    'zyx_seq_mask_assert',
    'not_None_assert',
    'in_list_assert',
    'method_not_override_assert',
    'instance_of_assert',
    'dict_has_key_assert',
    'file_not_exist_assert'
]

# TODO 风险: 如果b=a,然后传入b为传参,会显示最开始的变量名也就是a
def get_varname(var: object) -> str:
    """
    获取变量名
    :param var:
    :return:
    """
    for fi in reversed(inspect.stack()):
        names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
        if len(names) > 0:
            return names[0]

# 待测试
def type_assert(input_: object, type_: type) -> None:
    """
    断言输入的类型
    :param input_: object为需要保证的输入
    :param type_: type
    :return: None
    """
    input_type = type(input_)
    assert type(input_) == type_, \
        'The %s not meet the required, \nexpect type:%s, input type:%s' \
        % (get_varname(input_), str(type_), str(input_type))

# 待测试
def type_multi_assert(input_: object, type_list: list) -> None:
    """
    断言输入类型为type list内的类型
    :param input_: object
    :param type_list: list(type)
    :return: None
    """
    # 断言保证
    list_type_assert(type_list, type)
    input_type = type(input_)
    assert input_type in type_list, \
        'The %s not meet the required, \nexpect type:%s, input type:%s' \
        % (get_varname(input_), str(type_list), str(input_type))

def instance_of_assert(input_: object, type_: type) -> None:
    """
    断言输入的类型是子类
    :param input_: object为需要保证的输入
    :param type_: type
    :return: None
    """
    assert isinstance(input_, type_), \
        'The %s not meet the required, \nexpect type:%s, input type:%s' \
        % (get_varname(input_), str(type_), str(type(input_)))

def method_not_override_assert() -> None:
    """
    没有重写的错误
    :return:
    """
    assert False, 'The method meet problem, this method should be override!'

def condition_not_happen_assert(info='') -> None:
    """
    条件不应该存在的断言
    :return:
    """
    print(info)
    assert False, 'The condition meet problem, this condition should not happen!'

def equal_assert(input_1: object, input_2: object) -> None:
    """
    保证input_1 等于 input_2
    :param input_1: object
    :param input_2: object
    :return: None
    """
    assert input_1 == input_2, \
        'The %s, %s not meet the required, \n' \
        'expect %s equal to %s, \n%s:%s, %s:%s' \
        % (get_varname(input_1), get_varname(input_2),
           get_varname(input_1), get_varname(input_2),
           get_varname(input_1), str(input_1),
           get_varname(input_2), str(input_2))

def equal_multi_assert(input_1: object, input_2_list: list) -> None:
    """
    保证input_1 等于 input_2_list中的值
    :param input_1: object
    :param input_2: list
    :return: None
    """
    type_assert(input_2_list, list)
    rst_bool = False
    for input_2 in input_2_list:
        temp_bool = (input_1 == input_2)
        rst_bool = rst_bool or temp_bool
    assert rst_bool, \
        'The %s, %s not meet the required, \n' \
        'expect %s equal to %s, \n%s:%s, %s:%s' \
        % (get_varname(input_1), get_varname(input_2),
           get_varname(input_1), get_varname(input_2),
           get_varname(input_1), str(input_1),
           get_varname(input_2), str(input_2))

def not_equal_assert(input_1: object, input_2: object) -> None:
    """
    保证input_1 不等于 input_2
    :param input_1: object
    :param input_2: object
    :return: None
    """
    assert input_1 != input_2, \
        'The %s, %s not meet the required, \n' \
        'expect %s not equal to %s, \n%s:%s, %s:%s' \
        % (get_varname(input_1), get_varname(input_2),
           get_varname(input_1), get_varname(input_2),
           get_varname(input_1), str(input_1),
           get_varname(input_2), str(input_2))

def not_None_assert(input_1: object) -> None:
    """
    保证input_1 不等于 None
    :param input_1: object
    :return: None
    """
    assert input_1 != None, \
        'The %s not meet the required, \n' \
        'expect %s not equal to None, \n%s:%s' \
        % (get_varname(input_1), get_varname(input_1),
           get_varname(input_1), str(input_1))

def greater_or_equal_assert(input_1: object, input_2: object) -> None:
    """
    保证input_1 大于等于input_2
    :param input_1: object
    :param input_2: object
    :return: None
    """
    assert input_1 >= input_2, \
        'The %s, %s not meet the required, \n' \
        'expect %s greater or equal than %s, \n%s:%s, %s:%s' \
        % (get_varname(input_1), get_varname(input_2),
           get_varname(input_1), get_varname(input_2),
           get_varname(input_1), str(input_1),
           get_varname(input_2), str(input_2))

def smaller_or_equal_assert(input_1: object, input_2: object) -> None:
    """
    保证input_1 小于等于input_2
    :param input_1: object
    :param input_2: object
    :return: None
    """
    assert input_1 <= input_2, \
        'The %s, %s not meet the required, \n' \
        'expect %s smaller or equal than %s, \n%s:%s, %s:%s' \
        % (get_varname(input_1), get_varname(input_2),
           get_varname(input_1), get_varname(input_2),
           get_varname(input_1), str(input_1),
           get_varname(input_2), str(input_2))

# 待测试
def array_x_dims_assert(input_array: np.ndarray, dims: int) -> None:
    """
    保证输入矩阵为x维矩阵
    :param input_array: ndarray
    :param dims: int
    :return: None
    """
    # 断言输入保证
    type_assert(input_array, np.ndarray)
    type_assert(dims, int)

    array_dim = len(input_array.shape)
    assert array_dim == dims, \
        'The %s not meet the required, \nexpect dims:%s, input dims:%s' \
        % (get_varname(input_array), str(dims), str(array_dim))

# 待测试
def array_x_dims_multi_assert(input_array: np.ndarray, dims_list: list) -> None:
    """
    保证输入矩阵为x维矩阵,x为在dims_list中的数据
    :param input_array: ndarray
    :param dims_list: list
    :return: None
    """
    # 断言输入保证
    type_assert(input_array, np.ndarray)
    type_assert(dims_list, list)

    array_dim = len(input_array.shape)
    assert array_dim in dims_list, \
        'The %s not meet the required, \nexpect dims:%s, input dims:%s' \
        % (get_varname(input_array), str(dims_list), str(array_dim))

def byxz_seq_array_assert(input_: np.ndarray) -> None:
    """
    保证输入矩阵为按照byxz顺序排列,
    当前的断言方法是判断y,x轴大小相同
    :param input_: ndarray
    :return:
    """
    # 断言输入保证
    type_assert(input_, np.ndarray)
    array_x_dims_assert(input_, 4)

    axis_y, axis_x = input_.shape[1:3]
    assert axis_y == axis_x, \
        'The %s not meet the required, \nexpect axis seq is byxz and y=x,' \
        ' input shape:%s' \
        % (get_varname(input_), str(input_.shape))

def zyx_seq_array_assert(input_: np.ndarray) -> None:
    """
    保证输入矩阵为按照zyx顺序排列,
    当前的断言方法是判断y,x轴大小相同
    :param input_: ndarray
    :return:
    """
    # 断言输入保证
    type_assert(input_, np.ndarray)
    array_x_dims_assert(input_, 3)

    axis_y, axis_x = input_.shape[1:]
    assert axis_y == axis_x, \
        'The %s not meet the required, \nexpect axis seq is zyx and y=x,' \
        ' input shape:%s' \
        % (get_varname(input_), str(input_.shape))

def zyx_seq_image_assert(input_image: np.ndarray) -> None:
    """
    保证输入图像为按照zyx顺序排列,
    当前的断言方法是判断y,x轴大小相同
    同时dtype为float32
    :param input_image: ndarray(np.float32)
    :return:
    """
    # 断言输入保证
    array_dtype_assert(input_image, np.float32)
    zyx_seq_array_assert(input_image)

def zyx_seq_mask_assert(input_mask: np.ndarray) -> None:
    """
    保证输入图像为按照zyx顺序排列,
    当前的断言方法是判断y,x轴大小相同
    同时dtype为int8
    :param input_image: ndarray(np.int8)
    :return:
    """
    # 断言输入保证
    array_dtype_assert(input_mask, np.int8)
    zyx_seq_array_assert(input_mask)

def xyz_seq_array_assert(input_: np.ndarray) -> None:
    """
    保证输入矩阵为按照xyz顺序排列,
    当前的断言方法是判断y,x轴大小相同
    :param input_: ndarray
    :return:
    """
    # 断言输入保证
    type_assert(input_, np.ndarray)
    array_x_dims_assert(input_, 3)

    axis_y, axis_x = input_.shape[:2]
    assert axis_y == axis_x, \
        'The %s not meet the required, \nexpect axis seq is xyz and y=x,' \
        ' input shape:%s' \
        % (get_varname(input_), str(input_.shape))

# 待测试
def xyc_seq_array_assert(input_: np.ndarray) -> None:
    """
    保证输入矩阵为按照xyc顺序排列,
    当前的断言方法是判断y,x轴大小相同
    :param input_: ndarray
    :return: None
    """
    # 断言输入保证
    type_assert(input_, np.ndarray)
    array_x_dims_assert(input_, 3)

    axis_y, axis_x = input_.shape[:2]
    assert axis_y == axis_x, \
        'The %s not meet the required, \nexpect axis seq is xyc and y=x,' \
        ' input shape:%s' \
        % (get_varname(input_), str(input_.shape))

# 待测试
def xyzc_seq_array_assert(input_: np.ndarray) -> None:
    """
    保证输入矩阵为按照xyzc顺序排列,
    当前的断言方法是判断y,x轴大小相同
    :param input_: ndarray
    :return: None
    """
    # 断言输入保证
    type_assert(input_, np.ndarray)
    array_x_dims_assert(input_, 4)

    axis_y, axis_x = input_.shape[:2]
    assert axis_y == axis_x, \
        'The %s not meet the required, \nexpect axis seq is xyzc and y=x,' \
        ' input shape:%s' \
        % (get_varname(input_), str(input_.shape))

def yx_seq_array_assert(input_array: np.ndarray) -> None:
    """
    保证输入矩阵为按照yx顺序排列,
    当前的断言方法是判断y,x轴大小相同
    :param input_array: ndarray
    :return:
    """
    # 断言输入保证
    type_assert(input_array, np.ndarray)
    array_x_dims_assert(input_array, 2)

    axis_y, axis_x = input_array.shape[:]
    assert axis_y == axis_x, \
        'The %s not meet the required, \nexpect axis seq is yx and y=x,' \
        ' input shape:%s' \
        % (get_varname(input_array), str(input_array.shape))

def list_length_assert(input_: list, length: int) -> None:
    """
    保证输入矩阵为x维矩阵
    :param input_: list
    :param length: int
    :return: None
    """
    # 断言输入保证
    type_assert(input_, list)

    list_length = len(input_)
    assert list_length == length, \
        'The %s not meet the required, \n' \
        'expect list length:%s, input list length:%s' \
        % (get_varname(input_), str(length), str(list_length))

def list_type_assert(input_list: list, type_: type) -> None:
    """
    保证输入list为type的list类型
    :param input_list: list(type)
    :param type_: type
    :return:
    """
    # 断言保证
    type_assert(input_list, list)

    for item in input_list:
        type_assert(item, type_)

def in_list_assert(item: object, input_list: list) -> None:
    """
    保证item在input list中
    :param item: object
    :param input_list: list
    :return:
    """
    # 断言保证
    type_assert(input_list, list)

    assert item in input_list, \
        'The %s,%s not meet the required, \n' \
        'expect item in input list,\n' \
        'item :%s, input_list: %s' % (
        get_varname(item), get_varname(input_list),
        str(item), str(input_list))

def dict_has_key_assert(key: object, input_dict: dict) -> None:
    """
    保证key在input dict的key中
    :param key: object
    :param input_dict: list
    :return:
    """
    # 断言保证
    type_assert(input_dict, dict)

    assert key in input_dict.keys(), \
        'The %s,%s not meet the required, \n' \
        'expect key in input dict,\n' \
        'key :%s, input_dict: %s' % (
        get_varname(key), get_varname(input_dict),
        str(key), str(input_dict))


def array_length_assert(input_: np.ndarray, length: int, axis=0) -> None:
    """
    保证输入矩阵的axis维长度为length
    :param input_: list
    :param length: int
    :return: None
    """
    # 断言输入保证
    type_assert(input_, np.ndarray)
    greater_or_equal_assert(len(input_.shape), axis)

    list_length = input_.shape[axis]
    assert list_length == length, \
        'The %s not meet the required, \n' \
        'expect array length:%s, input array length:%s' \
        % (get_varname(input_), str(length), str(list_length))

def array_shape_assert(input_array: np.ndarray, shape: tuple) -> None:
    """
    保证输入矩阵的shape
    :param input_array: ndarray
    :param shape: tuple
    :return:
    """
    # 断言保证
    type_assert(input_array, np.ndarray)
    tuple_type_assert(shape, int)
    tuple_length_assert(shape, len(input_array.shape))

    array_shape = input_array.shape
    assert array_shape == shape, \
        'The %s not meet the required, \n' \
        'expect array shape:%s, input array shape:%s' \
        % (get_varname(input_array), str(shape), str(array_shape))

def array_dtype_assert(input_array: np.ndarray, dtype_: type) -> None:
    """
    保证输入矩阵的dtype
    :param input_array: ndarray
    :param dtype_: type
    :return:
    """
    # 断言保证
    type_assert(input_array, np.ndarray)
    type_assert(dtype_, type)

    array_dtype = input_array.dtype
    assert array_dtype == dtype_, \
        'The %s not meet the required, \n' \
        'expect array dtype:%s, input array dtype:%s' \
        % (get_varname(input_array), str(dtype_), str(array_dtype))

def zyx_seq_space_assert(input_space: np.ndarray) -> None:
    """
    保证输入space为按照zyx顺序排列,
    当前的断言方法是判断y,x轴大小相同
    并且dtype是np.float32
    :param input_space: ndarray
    :return:
    """
    # 断言输入保证
    array_length_assert(input_space, 3)
    array_dtype_assert(input_space, np.float32)

    axis_y, axis_x = input_space[1:]
    assert axis_y == axis_x, \
        'The %s not meet the required, \nexpect axis seq is zyx and y=x,' \
        ' input :%s' \
        % (get_varname(input_space), str(input_space))

def path_exist_assert(input_path: str) -> None:
    """
    保证输入路径存在
    :param input_path: str
    :return:
    """
    is_exist = os.path.exists(input_path)
    assert is_exist, \
        'The %s is not exist, path: %s' \
        % (get_varname(input_path), str(input_path))

def file_exist_assert(input_file: str) -> None:
    """
    保证输入路径存在
    :param input_file: str
    :return:
    """
    is_exist = os.path.exists(input_file)
    assert is_exist, \
        'The %s is not exist, file: %s' \
        % (get_varname(input_file), str(input_file))

def file_not_exist_assert(input_file: str) -> None:
    """
    保证输入路径存在
    :param input_file: str
    :return:
    """
    is_exist = not os.path.exists(input_file)
    assert is_exist, \
        'The %s is exist, file: %s' \
        % (get_varname(input_file), str(input_file))

def tuple_type_assert(input_tuple: tuple, type_: type) -> None:
    """
    保证输入tuple为type的tuple类型
    :param input_tuple: tuple(type)
    :param type_: type
    :return:
    """
    # 断言保证
    type_assert(input_tuple, tuple)

    for item in input_tuple:
        type_assert(item, type_)

def tuple_length_assert(input_tuple: tuple, length: int):
    """
    保证输入tuple的长度为length
    :param input_tuple: tuple
    :param length: int
    :return:
    """
    # 断言保证
    type_assert(input_tuple, tuple)
    type_assert(length, int)

    tuple_length = len(input_tuple)
    assert tuple_length == length, \
        'The %s not meet the required, \n' \
        'expect tuple length:%s, input tuple length:%s' \
        % (get_varname(input_tuple), str(length), str(tuple_length))

if __name__ == "__main__":
    a = 1
    b = [2,3,4,5]
    in_list_assert(a, b)