#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: label_channel_layer_to_bbox.py
@Time: 2020-03-05 14:48
@Last_update: 2020-03-05 14:48
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
from yy_lib.process.label_yx_to_bbox import label_yx_to_bbox


def label_yxc_to_bbox(label_array, object_name_list,
                      bbox_name_list=['xmin','ymin','xmax','ymax'],
                      have_background=True):
    """
    把单张多通道的二值二维label转换为bbox
    如果有背景则默认认为背景在第零维
    :param label_array: 单张二值label矩阵
    :param object_name_list: 每个通道代表的object名称
    :param bbox_name_list: bbox的表示列表
    :return: 本张图片的物体字典列表
    整体流程：
    1. 把通道分开
    2. 分别得到单通道的bbox
    3. 放入list返回
    """
    if have_background:
        label_array = label_array[...,1:]
    assert len(object_name_list) == label_array.shape[-1], \
        'The object name list, label array channel length not equal,' \
        'object name list: %d, label array: %s' % (len(object_name_list), str(label_array.shape))

    object_list = []
    # 1. 把通道分开
    for c in range(label_array.shape[-1]):
        # 2. 分别得到单通道的bbox
        tmp_bbox_list = label_yx_to_bbox(label_array[...,c], bbox_name_list)
        for tmp_bbox in tmp_bbox_list:
            tmp_dict = {'name': object_name_list[c]}
            for num, bbox_name in enumerate(bbox_name_list):
                tmp_dict[bbox_name] = tmp_bbox[num]
            # 3. 放入list返回
            object_list.append(tmp_dict)

    return object_list


if __name__ == '__main__':
    from yy_lib.utils.visualizer import show_np

    a = np.zeros((128, 128, 3))
    a[20:50, 20:60, 1] = 1
    a[45:55, 55:65, 1] = 1
    a[70:80, 70:80, 2] = 1

    bbox_list = label_yxc_to_bbox(a, ['lung_l', 'lung_r'])

    list(map(print, bbox_list))