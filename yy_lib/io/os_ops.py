#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: os_ops.py
@Time: 2019-11-12 15:04
@Last_update: 2019-11-12 15:04
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
import shutil
import subprocess
import yy_lib.base.assertor as assertor


def mkdir(path: str):
    """
    创建文件夹
    """
    # 断言保证
    assertor.type_assert(path, str)
    assertor.not_equal_assert(path, '')

    # 去除首空格
    path = path.strip()
    os.makedirs(path)


def del_dir(file_dir):
    # 断言保证
    assertor.path_exist_assert(file_dir)

    shutil.rmtree(file_dir)


def copy_dir(old_path, new_path, old_dir_name=None, new_dir_name=None, force=False):
    """
    复制文件夹
    如果force为True则如果目标文件夹存在则会先删除再复制
    """
    old_path = os.path.join(old_path, old_dir_name) if old_dir_name is not None else old_path
    # 断言保证
    assertor.file_exist_assert(old_path)

    new_path = os.path.join(new_path, new_dir_name) if new_dir_name is not None else new_path

    if force and os.path.exists(new_path):
        del_dir(new_path)

    if not os.path.exists(new_path):
        shutil.copytree(old_path, new_path)
    else:
        print("================================================")
        print("WARNING the new dir exist, not running copy dir")
        print("THIS WARNING FROM FUNCTION -> copy_dir")
        print("================================================")


def judge_add_os_sep(file_path: str):
    """
    判别在尾部添加sep
    """
    # 断言保证
    assertor.type_assert(file_path, str)
    assertor.not_equal_assert(file_path, '')

    if file_path[-1] != os.sep:
        file_path = file_path + os.sep

    return file_path


def judge_del_os_sep(file_path: str):
    """
    判别在尾部添加sep
    """
    # 断言保证
    assertor.type_assert(file_path, str)
    assertor.not_equal_assert(file_path, '')

    if file_path[-1] == os.sep:
        file_path = file_path[:-1]

    return file_path


def judge_mkdir(path: str):
    """
    判别位置,如果不存在则创建文件夹
    """
    # 断言保证
    assertor.type_assert(path, str)
    assertor.not_equal_assert(path, '')

    # 去除首空格
    path = path.strip()
    # 判别是否存在路径,如果不存在则创建
    if not os.path.exists(path):
        mkdir(path)


def copy_file(old_path, new_path, old_name=None, new_name=None):
    old_path = os.path.join(old_path, old_name) if old_name is not None else old_path
    new_path = os.path.join(new_path, new_name) if new_name is not None else new_path
    # 断言保证
    assertor.file_exist_assert(old_path)

    shutil.copyfile(old_path, new_path)


def del_file(file_path: str, file_name=None):
    """
    删除目标文件
    """

    file_path = os.path.join(file_path, file_name) if file_name is not None else file_path
    # 断言保证
    assertor.file_exist_assert(file_path)

    os.remove(file_path)


def get_all_ending_files_under_dir(
        file_dir: str, ending_list: list, display=False):
    assertor.path_exist_assert(data_root)
    if display:
        print('Begin get all ending files under dir')
    file_dir = judge_add_os_sep(file_dir)
    path_set = set()
    count = 0
    for root, dirs, files in os.walk(file_dir, topdown=False):

        if len(files) != 0:
            for file in files:
                ending = os.path.splitext(file)[-1]
                if ending in ending_list:
                    file_path = os.path.join(root, file)
                    path_set.add(file_path)
                    count += 1

                    if display:
                        if count % 500 == 0:
                            print('processing %d... %s' % (count, file_path))

    if display:
        print('Done get all ending files under dir')
    return list(path_set)

def get_all_target_name_path_list_under_dir(
        file_dir: str, name_list: list, only_file=False, only_dir=False,
        ignore_capital=True, ignore_ending=False, display=False):
    """
    获得所有目标名称的文件路径
    :param file_dir: 根目录
    :param name_list: 目标名称列表，如果为空代表所有文件
    :param only_file: 是否只搜索文件
    :param only_dir: 是否只搜索文件夹
    :param ignore_capital: 是否忽略大小写
    :param ignore_ending: 是否忽略文件类型
    :param display: 是否显示
    :return: list
    """
    assertor.path_exist_assert(file_dir)
    assertor.list_type_assert(name_list, str)

    if ignore_capital:
        name_list = [name.lower() for name in name_list]
    if display:
        print('Begin get all target name files under dir')
    file_dir = judge_add_os_sep(file_dir)
    path_set = set()
    count = 0
    # 遍历所有路径
    for root, dirs, files in os.walk(file_dir, topdown=True):
        # 判断文件是否有和是否只搜索文件夹
        if (len(files) != 0) and (only_dir is not True):
            for file_name in files:
                filename_compare = file_name
                # 是否忽略大小写
                if ignore_capital:
                    filename_compare = filename_compare.lower()
                # 是否忽略文件类型
                if ignore_ending:
                    filename_compare = os.path.splitext(filename_compare)[0]
                # 如果name_list不为空且file_name不再name_list中则继续
                if (len(name_list) != 0) and (filename_compare not in name_list):
                    continue
                # 否则任意情况都添加，也就是name_list为空，或者file_name在name_list中
                else:
                    file_path = os.path.join(root, file_name)
                    path_set.add(file_path)
                    count += 1
                    if display:
                        print(count)
                        print(file_path)

        # 判断文件夹是否有和是否只搜索文件
        if (len(dirs) != 0) and (only_file is not True):
            for dir_name in dirs:
                dirname_compare = dir_name
                # 是否忽略大小写
                if ignore_capital:
                    dirname_compare = dirname_compare.lower()
                # 如果name_list不为空且file_name不再name_list中则继续
                if (len(name_list) != 0) and (dirname_compare not in name_list):
                    continue
                # 否则任意情况都添加，也就是name_list为空，或者file_name在name_list中
                else:
                    file_path = os.path.join(root, dir_name)
                    path_set.add(file_path)
                    count += 1
                    if display:
                        print(count)
                        print(file_path)

    if display:
        print('Done get all target name files under dir')
    return list(path_set)


def run_command(command, print_msg=True):
    """
    运行命令行命令且实时显示命令输出，最后返回log列表
    """
    lines = []
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    for line in iter(p.stdout.readline, b''):
        line = line.rstrip().decode('utf8')
        if print_msg:
            print(">>>", line)
        lines.append(line)

    p.wait()
    return lines, p.returncode


def get_strable_file(file_path: str, file_name=None):
    """
    按照str类型来读取文件
    """
    if file_name is not None:
        file_path = os.path.join(file_path, file_name)

    with open(file_path, 'r') as f:
        str_data = f.read()

    return str_data


def save_strable_file(save_file_path: str, save_item, save_file_name=None):
    """
    保存可以直接str化的对象
    """
    if save_file_name is not None:
        save_file_path = os.path.join(save_file_path, save_file_name)

    with open(save_file_path, 'w') as f:
        f.write(str(save_item))


class HiddenPrints:
    @classmethod
    def hidden(cls):
        cls._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    @classmethod
    def back(cls):
        sys.stdout.close()
        sys.stdout = cls._original_stdout


def get_subdeep_dirpath_iter(data_path_list, num_sub_deep, return_list=False):
    """
    得到第i层的所有dir的路径迭代器
    """
    if type(data_path_list) is str:
        data_path_list = [data_path_list]

    for i in range(num_sub_deep):
        data_path_list = (os.path.join(path, sub_path) for path in data_path_list for sub_path in os.listdir(path) if os.path.isdir(os.path.join(path, sub_path)) )

    if return_list:
        data_path_list = list(data_path_list)

    return data_path_list


def get_all_ending_files_path_iter(data_root, ending_list, return_list=False):
    """
    得到所有目标结尾的文件的生成器
    整体流程：
    1. 把所有ending_list变为.开头
    2. 得到生成器
    """
    assertor.path_exist_assert(data_root)
    if type(ending_list) is str:
        ending_list = [ending_list]

    # 1. 把所有ending_list变为.开头
    ending_list = ['.%s' % ending if ending[0] != '.' else ending for ending in ending_list]

    # 2. 得到生成器
    def _ending_searcher_iter(data_root, ending_list):
        for root, dirs, files in os.walk(data_root):
            for file in files:
                ending = os.path.splitext(file)[-1]
                if ending in ending_list:
                    yield os.path.join(root, file)

    ending_path_iter = _ending_searcher_iter(data_root, ending_list)

    if return_list:
        ending_path_iter = list(ending_path_iter)

    return ending_path_iter


def get_all_exclude_ending_files_path_iter(data_root, exclude_ending_list, return_list=False):
    """
    得到所有目标结尾的文件的生成器
    整体流程：
    1. 把所有ending_list变为.开头
    2. 得到生成器
    """
    assert os.path.exists(data_root), 'The data path not exist, %s' % data_root
    if type(exclude_ending_list) is str:
        exclude_ending_list = [exclude_ending_list]

    # 1. 把所有ending_list变为.开头
    exclude_ending_list = ['.%s' % ending if ending[0] != '.' else ending for ending in exclude_ending_list]

    # 2. 得到生成器
    def _exclude_ending_searcher_iter(data_root, exclude_ending_list):
        for root, dirs, files in os.walk(data_root):
            for file in files:
                ending = os.path.splitext(file)[-1]
                if ending not in exclude_ending_list:
                    yield os.path.join(root, file)

    exclude_ending_path_iter = _exclude_ending_searcher_iter(data_root, exclude_ending_list)

    if return_list:
        exclude_ending_path_iter = list(exclude_ending_path_iter)

    return exclude_ending_path_iter

