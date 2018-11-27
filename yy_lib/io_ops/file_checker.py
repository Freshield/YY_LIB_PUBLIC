#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: file_checker.py
@Time: 18-6-20 20:18
@Last_update: 18-6-20 20:18
@Desc: 检查dcm file的相关数据文件
"""
import re
import os
import pydicom as dicom

import yy_lib.assert_ops.assertor as assertor

class DcmFileChecker(object):

    @classmethod
    def _check_label_exist(cls, rule: str, filename: str) -> int:
        """
        通过正则表达式来判断文件名和rule一致
        :param rule: str,正则的规则
        :param filename: str,文件的名字
        :return: int, 表达是否正确, 方便下一步计算匹配个数
        """
        # 断言保证输入
        assertor.type_assert(rule, str)
        assertor.type_assert(filename, str)

        # 进行正则匹配
        res = re.match(rule, filename, re.IGNORECASE)
        if res:
            print('----Find %s' % res.group())
            return 1
        else:
            return 0

    @classmethod
    def _get_match_num(cls, dir_path: str, rules: list) -> int:
        """
        得到匹配的数量
        :param dir_path: str,文件夹的路径
        :param rules: list,匹配的规则
        :return: match_num: int,匹配的数量
        """
        # 断言保证
        assertor.path_exist_assert(dir_path)
        assertor.list_type_assert(rules, str)

        match_num = 0
        for file in os.listdir(dir_path):
            for rule in rules:
                res = cls._check_label_exist(rule, file)
                match_num += res
        return match_num

    @classmethod
    def check_labels_exists(cls, dir_path: str, rules: list, label_dirname='1') -> None:
        """
        检查labels是否存在且是否齐全
        :param dir_path: str,文件夹的路径
        :param rules: list,匹配的规则
        :param label_dirname: str,label文件夹的名字
        :return: None
        """
        # 断言保证
        assertor.path_exist_assert(dir_path)
        assertor.list_type_assert(rules, str)
        assertor.type_assert(label_dirname, str)

        dir_end = dir_path.split(os.sep)[-1]
        for (root, dirs, files) in os.walk(dir_path):
            if label_dirname in dirs:
                path_list = root.split(os.sep)
                for i in range(len(path_list)):
                    if dir_end == path_list[i]:
                        print('Dir %s' % path_list[i + 1])
                        break
                sub_path = os.path.join(root, label_dirname)
                print(os.path.join(root, sub_path).split('/')[-2])
                match_num = cls._get_match_num(sub_path, rules)
                if match_num != len(rules):
                    print('---------------------------------------------------------------------')
                    print('---------------------------------------------------------------------')
                    print('Warning: dir %s Not have all of the mask' % str(dir_path))
                    print('---------------------------------------------------------------------')
                    print('---------------------------------------------------------------------')

    @classmethod
    def check_spacings(cls, path: str, image_dirname='CT', show_all=False) -> None:
        """
        检查所有图片的spacing大小
        :param path: str,文件夹路径
        :param label_dirname: str,image的文件夹名字
        :param show_all: bool,是否要单独显示所有的spacing序列
        :return: None
        """
        spacing_list = []
        for (root, dirs, files) in os.walk(path):
            if image_dirname in dirs:
                dir = os.path.join(root, image_dirname)
                file_dir_num = os.path.join(root, dir).split('/')[-3]
                print(file_dir_num)
                for file in os.listdir(dir):
                    if os.path.isfile(os.path.join(dir, file)) and file.split('.')[-1] == 'dcm':
                        filename = os.path.join(dir, file)
                        file_value = dicom.read_file(filename)
                        spacing_list.append(file_value.PixelSpacing[0])
                        print('%.3f' % file_value.PixelSpacing[0])
                        break

                print()

        if show_all:
            for i in spacing_list:
                print('%.3f' % i)
