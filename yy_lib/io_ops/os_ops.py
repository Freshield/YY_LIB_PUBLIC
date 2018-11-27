#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: os_ops.py
@Time: 18-6-19 16:06
@Last_update: 18-6-19 16:06
@Desc: 对于系统的操作
"""
import os
import shutil
import zipfile
import subprocess
from pyunpack import Archive

import yy_lib as yy
import yy_lib.assert_ops.assertor as assertor

__all__ = [
    'join',
    'mkdir',
    'judge_mkdir',
    'del_file',
    'rename_file',
    'del_dir',
    'copy_file',
    'get_files_path',
    'judge_del_file',
    'zip_file',
    'zip_dir',
    'move_dir_or_file',
    'get_dir_list_under_root_dir',
    'compress_dir_by_7z',
    'judge_del_dir',
    'judge_del_copy_dir',
    'judge_del_copy_all_to_target_dir',
    'un_compression',
    'get_all_file_ending_under_dir',
    'del_all_ending_files_under_dir',
    'un_compression_all_ending_files_under_dir',
    'get_all_ending_files_under_dir',
    'get_list_from_list_file',
    'judge_add_os_sep',
    'compress_dir_by_shutil',
    'compression_ending',
    'del_empty_ending_files',
    'make_same_empty_sub_dirs',
    'run_command',
    'get_all_target_name_files_list_under_dir',
    'is_ending_with',
    'copy_dir',
    'get_target_name_dir_path_list_under_dir',
    'get_all_include_name_files_list_under_dir',
    'is_file_name_in_file_path_list',
    'get_file_path_in_file_path_list_by_file_name'
]

compression_ending = ['.7z', '.tar', '.zip', '.rar', '.gz', '.bz2']

def join(*path_tuple: tuple) -> str:
    """
    连接路径,接受多个输入
    :param path_tuple: tuple
    :return: path: str
    """
    # 断言保证
    assertor.tuple_type_assert(path_tuple, str)

    path = ''
    for i in range(len(path_tuple)):
        path = os.path.join(path, path_tuple[i])

    return path

def mkdir(path:str) -> None:
    """
    创建文件夹
    :param path: str
    :return: None
    """
    # 断言保证
    assertor.type_assert(path, str)
    assertor.not_equal_assert(path, '')

    # 去除首空格
    path = path.strip()
    os.makedirs(path)


def judge_mkdir(path: str) -> None:
    """
    判别位置,如果不存在则创建文件夹
    :param path: str
    :return: None
    """
    # 断言保证
    assertor.type_assert(path, str)
    assertor.not_equal_assert(path, '')

    # 去除首空格
    path = path.strip()
    # 判别是否存在路径,如果不存在则创建
    if not os.path.exists(path):
        mkdir(path)


def del_file(file_dir: str, file_name: str) -> None:
    """
    删除目标文件
    :param file_dir: str
    :param file_name: str
    :return: None
    """
    # 断言保证
    assertor.type_assert(file_dir, str)
    assertor.type_assert(file_name, str)

    file_path = join(file_dir, file_name)
    # 断言保证
    assertor.file_exist_assert(file_path)

    os.remove(file_path)

def judge_del_file(file_dir: str, file_name: str) -> None:

    if os.path.exists(join(file_dir,file_name)):
        del_file(file_dir,file_name)

def del_dir(file_dir):
    # 断言保证
    assertor.path_exist_assert(file_dir)

    shutil.rmtree(file_dir)

def judge_del_dir(file_dir: str) -> None:

    if os.path.exists(file_dir):
        del_dir(file_dir)


def rename_file(file_dir, file_name, new_file_name):
    old_path = join(file_dir, file_name)
    # 断言保证
    assertor.file_exist_assert(old_path)

    new_path = join(file_dir, new_file_name)
    os.rename(old_path, new_path)

def copy_file(old_dir, old_name, new_dir, new_name):
    old_path = join(old_dir, old_name)
    # 断言保证
    assertor.file_exist_assert(old_path)
    assertor.path_exist_assert(new_dir)

    new_path = join(new_dir, new_name)
    shutil.copyfile(old_path, new_path)

def copy_dir(old_dir, old_dir_name, new_dir, new_dir_name):
    old_path = join(old_dir, old_dir_name)
    # 断言保证
    assertor.file_exist_assert(old_path)

    if not os.path.exists(new_dir):
        new_path = join(new_dir, new_dir_name)
        shutil.copytree(old_path, new_path)
    else:
        print("================================================")
        print("WARNING the new dir exist, not running copy dir")
        print("THIS WARNING FROM FUNCTION -> copy_dir")
        print("================================================")

def get_files_path(root_dir):
    assertor.path_exist_assert(root_dir)

    path_set = set()
    for root, dirs, files in os.walk(root_dir, topdown=False):
        if len(files) != 0:
            for file in files:
                path_set.add(join(root, file))

    return list(path_set)

def zip_file(file_dir:str, file_name:str,
             target_dir:str, target_name:str):
    file_path = join(file_dir, file_name)
    assertor.file_exist_assert(file_path)

    judge_mkdir(target_dir)

    with zipfile.ZipFile(
            join(target_dir, target_name),
            'w', zipfile.ZIP_DEFLATED) as f:
        print('begin to zip file')
        f.write(file_path)

    print('done')

def zip_dir(dir_path:str, target_dir:str, target_name):
    assertor.path_exist_assert(dir_path)

    judge_mkdir(target_dir)

    files = get_files_path(dir_path)

    with zipfile.ZipFile(
            join(target_dir, target_name),
            'w', zipfile.ZIP_DEFLATED) as f:
        print('begin to zip file')
        for file in files:
            f.write(file)

    print('done')


def move_dir_or_file(ori_dir, ori_name,
                     tar_dir, tar_name):
    ori_path = join(ori_dir, ori_name)
    assertor.path_exist_assert(ori_path)

    judge_mkdir(tar_dir)

    tar_path = join(tar_dir, tar_name)

    shutil.move(ori_path, tar_path)

def get_dir_list_under_root_dir(root_dir:str, anti_list=[]):
    assertor.path_exist_assert(root_dir)

    dir_list = []

    for file in os.listdir(root_dir):
        file_path = join(root_dir, file)
        if os.path.isdir(file_path):
            res = True
            for anti_word in anti_list:
                if anti_word in file_path:
                    res = False
            if res:
                dir_list.append(file_path)

    return dir_list

def compress_dir_by_7z(
        cmp_dir:str, target_path:str, password='', print_msg=True):
    """
    压缩文件夹到目标位置
    :param cmp_dir: 要压缩的文件夹
    :param target_path: 要存储的路径
    :param password: 密码
    :param print_msg: 是否打印细节
    :return:
    """
    # 断言保证
    assertor.path_exist_assert(cmp_dir)

    if password != '':
        cmd = '7za a -t7z -p%s -r %s %s' % (target_path, password, cmp_dir)
    else:
        cmd = '7za a -t7z -r %s %s' % (target_path, cmp_dir)

    log = run_command(cmd, print_msg=print_msg)

    return log

def compress_dir_by_shutil(
        ori_dir: str, tar_dir: str, tar_name: str, display=True):
    assertor.path_exist_assert(ori_dir)

    judge_mkdir(tar_dir)

    tar_path = join(tar_dir, tar_name)
    tar_path = os.path.splitext(tar_path)[0]

    shutil.make_archive(tar_path, 'zip', ori_dir)

    if display:
        print('Done compression: %s to %s'%(ori_dir, tar_path))


def judge_del_copy_dir(old_dir, new_dir):
    # 断言保证
    assertor.file_exist_assert(old_dir)
    judge_del_dir(new_dir)

    shutil.copytree(old_dir, new_dir)

def judge_del_copy_all_to_target_dir(
        ori_dir:str, tar_dir:str):
    assertor.path_exist_assert(ori_dir)

    judge_mkdir(tar_dir)

    for file in os.listdir(ori_dir):
        file_path = join(ori_dir, file)

        if os.path.isfile(file_path):
            copy_file(ori_dir, file, tar_dir, file)

        if os.path.isdir(file_path):
            tar_path = join(tar_dir, file)
            judge_del_copy_dir(file_path, tar_path)

def un_compression(filename):
    assertor.file_exist_assert(filename)

    file_root = os.path.splitext(filename)[0]
    judge_mkdir(file_root)
    un_comp_file = Archive(filename)
    un_comp_file.extractall(file_root)

def get_all_file_ending_under_dir(file_dir: str):
    assertor.path_exist_assert(file_dir)

    file_ending = set()

    for root, dirs, files in os.walk(file_dir, topdown=False):

        if len(files) != 0:
            for file in files:
                ending = os.path.splitext(file)[-1]
                file_ending.add(ending)

    return file_ending

def get_all_ending_files_under_dir(
        file_dir: str, ending_list: list, display=False):
    assertor.path_exist_assert(file_dir)
    assertor.list_type_assert(ending_list, str)

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
                    file_path = join(root, file)
                    path_set.add(file_path)
                    count += 1
                    if display:
                        print(count)
                        print(file_path)

    if display:
        print('Done get all ending files under dir')
    return list(path_set)

def get_all_include_name_files_list_under_dir(
        file_dir: str, name_list: list, ignore_capital=True, display=False):
    """
    获得所有名字列表中的路径列表
    :param file_dir:
    :param name_list:
    :param display:
    :return:
    """
    assertor.path_exist_assert(file_dir)
    assertor.list_type_assert(name_list, str)

    if display:
        print('Begin get all include name files under dir')
    file_dir = judge_add_os_sep(file_dir)
    path_set = set()
    count = 0
    # 遍历所有的数据
    for root, dirs, files in os.walk(file_dir, topdown=False):
        # 如果文件列表不是空
        if len(files) != 0:
            # 遍历所有文件名
            for file_name in files:
                # 遍历所有包含名的部分
                for include_name in name_list:
                    #  是否忽略大小写
                    if ignore_capital:
                        temp_include_name = include_name.lower()
                        temp_file_name = file_name.lower()
                    else:
                        temp_include_name = include_name
                        temp_file_name = file_name
                    # 如果include name在文件名中
                    if temp_include_name in temp_file_name:
                        file_path = join(root, file_name)
                        path_set.add(file_path)
                        count += 1
                        if display:
                            print(count)
                            print(file_path)

    if display:
        print('Done get all include name files under dir')
    return list(path_set)

def get_all_target_name_files_list_under_dir(
        file_dir: str, name_list: list, display=False):
    """
    获得所有名字列表中的路径列表
    :param file_dir:
    :param name_list:
    :param display:
    :return:
    """
    assertor.path_exist_assert(file_dir)
    assertor.list_type_assert(name_list, str)

    if display:
        print('Begin get all target name files under dir')
    file_dir = judge_add_os_sep(file_dir)
    path_set = set()
    count = 0
    for root, dirs, files in os.walk(file_dir, topdown=False):
        if len(files) != 0:
            for file_name in files:
                if file_name in name_list:
                    file_path = join(root, file_name)
                    path_set.add(file_path)
                    count += 1
                    if display:
                        print(count)
                        print(file_path)

    if display:
        print('Done get all target name files under dir')
    return list(path_set)

def get_target_name_dir_path_list_under_dir(
        file_dir: str, name_list: list, display=False):
    """
    获得所有名字列表中的路径列表
    :param file_dir:
    :param name_list:
    :param display:
    :return:
    """
    assertor.path_exist_assert(file_dir)
    assertor.list_type_assert(name_list, str)

    if display:
        print('Begin get all target name dir under dir')
    file_dir = judge_add_os_sep(file_dir)
    path_set = set()
    count = 0
    for root, dirs, files in os.walk(file_dir, topdown=False):

        if len(dirs) != 0:
            for dir_name in dirs:
                if dir_name in name_list:
                    dir_path = join(root, dir_name)
                    path_set.add(dir_path)
                    count += 1
                    if display:
                        print(count)
                        print(dir_path)

    if display:
        print('Done get all target name dir under dir')
    return list(path_set)

def del_all_ending_files_under_dir(
        file_dir: str, ending_list: str, display=False):
    assertor.path_exist_assert(file_dir)
    assertor.list_type_assert(ending_list, str)

    file_dir = judge_add_os_sep(file_dir)
    if display:
        print("Begin to get all ending files")
    file_list = get_all_ending_files_under_dir(file_dir, ending_list, display)
    if display:
        print("Done get all ending files")

    if display:
        print("Total %d files need del\n" % len(file_list))

    for i in range(len(file_list)):
        if display:
            print('%d/%d: %s deleting' % (i + 1, len(file_list), file_list[i]))
        del_file('', file_list[i])

def del_empty_ending_files(root_dir:str, ending:str, display=False):
    assertor.path_exist_assert(root_dir)

    if display:
        print('Begin to get ending file path list')
    ending_file_path_list = yy.io.get_all_ending_files_under_dir(root_dir, [ending], display=display)
    if display:
        print('Done get ending file path list')

    empty_count = 0
    total_count = 0
    for file_path in ending_file_path_list:
        if display:
            print('processing %d/%d ...'%(total_count, len(ending_file_path_list)))
        total_count += 1
        size = os.path.getsize(file_path)
        if size == 0:
            yy.io.del_file('',file_path)
            if display:
                print('Done del empty file %s'%(file_path))
            empty_count += 1
    if display:
        print('Total delete %d empty files'%(empty_count))

def un_compression_all_ending_files_under_dir(
        file_dir: str, ending_list: list):
    assertor.path_exist_assert(file_dir)
    assertor.list_type_assert(ending_list, str)

    file_dir = judge_add_os_sep(file_dir)
    file_list = get_all_ending_files_under_dir(file_dir, ending_list)

    print("Total %d files need uncompression\n" % len(file_list))

    for i in range(len(file_list)):
        print('%d/%d: %s un_compression'%(i+1,len(file_list),file_list[i]))
        un_compression(file_list[i])

def save_list_to_list_file(input_list:list, save_path:str):
    assertor.type_assert(input_list, list)
    assertor.file_exist_assert(file_path)

    with open(file_path, 'w') as f:
        f.write(str(input_list))

    return rst_list

def get_list_from_list_file(file_path: str):
    assertor.file_exist_assert(file_path)

    with open(file_path, 'r') as f:
        data = f.read()
        rst_list = eval(data)

    return rst_list

def judge_add_os_sep(file_path: str):
    if file_path[-1] != os.sep:
        file_path = file_path + os.sep

    return file_path

def make_same_empty_sub_dirs(root_dir, save_dir, anti_list=['lost+found', '.Trash']):
    assertor.path_exist_assert(root_dir)

    yy.io.judge_mkdir(save_dir)

    sub_dir_list = yy.io.get_dir_list_under_root_dir(root_dir, anti_list)

    for sub_dir in sub_dir_list:
        sub_dir_name = sub_dir.split(os.sep)[-1]
        save_path = yy.io.join(save_dir, sub_dir_name)
        yy.io.judge_mkdir(save_path)

def run_command(command, print_msg=True):
    """
    运行命令行命令且实时显示命令输出，最后返回log列表
    :param command:
    :param print_msg:
    :return:
    """
    lines = []
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in iter(p.stdout.readline, b''):
        line = line.rstrip().decode('utf8')
        if print_msg:
            print(">>>", line)
        lines.append(line)
    return lines

def is_ending_with(file_path, ending=''):
    """
    判别是否以目标名结尾
    :param file_path:
    :param ending:
    :return:
    """
    assertor.not_equal_assert(ending, '')

    file_ending = os.path.splitext(file_path)[-1]

    return file_ending == ending


def is_file_name_in_file_path_list(file_name: str, file_path_list: list):
    """
    判别文件名是否在文件路径列表中
    :param target_name:
    :param path_list:
    :return:
    """
    rst_bool = False
    for file_path in file_path_list:
        if file_name in file_path:
            rst_bool = True
            break

    return rst_bool


def get_file_path_in_file_path_list_by_file_name(file_name: str, file_path_list: list):
    """
    判别文件名是否在文件路径列表中
    :param target_name:
    :param path_list:
    :return:
    """
    for file_path in file_path_list:
        if file_name in file_path:
            return file_path


if __name__ == '__main__':
    test = join('','lol','data')
    print(test)