#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: label_to_bbox.py
@Time: 2020-03-05 13:46
@Last_update: 2020-03-05 13:46
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
from skimage.measure import label


def label_yx_to_bbox(label_array, bbox_name_list=['xmin','ymin','xmax','ymax']):
    """
    把分割的单层二值图像转换为bbox
    :param label_array: 为二维单张二值图
    :param bbox_name_list: 为输出的值的顺序列表，
    共有以下几个值：xmin,xmax,ymin,ymax,xcenter,ycenter,w,h
    :return: 根据bbox_name_list得到的值的list
    整体流程：
    1. 把区域label化
    2. 根据label后的数值遍历
    3. 找到bbox的数值
    4. 按照bbox_name_list存入列表返回
    """
    assert len(np.unique(label_array)) == 2, \
        'The label array should be only two values, now %d' % len(np.unique(label_array))

    # 1. 把区域label化
    labeled_array = label(label_array)

    # 2. 根据label后的数值遍历
    rst_list = []
    for i in np.unique(labeled_array):
        # 跳过背景
        if i == 0:
            continue

        # 3. 找到bbox的数值
        y_pos, x_pos = np.where(labeled_array == i)
        xmin = x_pos.min()
        xmax = x_pos.max()
        ymin = y_pos.min()
        ymax = y_pos.max()
        xcenter = xmin + (xmax - xmin) // 2
        ycenter = ymin + (ymax - ymin) // 2
        w = xmax - xmin
        h = ymax - ymin
        bbox_dict = {
            'xmin': xmin, 'xmax': xmax, 'ymin': ymin, 'ymax': ymax,
            'xcenter': xcenter, 'ycenter': ycenter, 'w': w, 'h': h
        }

        # 4. 按照bbox_name_list存入列表返回
        rst_list.append(tuple(bbox_dict[name] for name in bbox_name_list))

    return rst_list


if __name__ == '__main__':
    from yy_lib.utils.visualizer import show_np
    a = np.zeros((128, 128))
    a[20:50,20:60] = 1
    a[45:55,55:65] = 1
    a[70:80,70:80] = 1

    bbox = label_yx_to_bbox(a)
    print(bbox)