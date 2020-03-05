#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: nii_ops.py
@Time: 2020-01-20 10:09
@Last_update: 2020-01-20 10:09
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
import nibabel as nb


def get_nii_data(file_path, file_dir=None, swap_data_axes=True):
    """
    从路径上读取nii数据并返回图像矩阵以及spacing
    """
    if file_dir is not None:
        file_path = os.path.join(file_dir, file_path)
        
    nii_loader = nb.load(file_path)
    affine = nii_loader.affine
    header = nii_loader.header

    spacing_list = []
    for i in range(2, -1, -1):
        spacing_list.append(abs(nii_loader.affine[i][i]))

    image_array = nii_loader.get_data()
    if swap_data_axes:
        image_array = image_array.swapaxes(0, 2)

    return image_array, spacing_list, affine, header


def to_nii_file(file_path, np_array, affine, header, file_dir=None):
    """
    将模型的预测结果存储为nii数据
    """
    if file_dir is not None:
        file_path = os.path.join(file_dir, file_path)

    # 调用 nib.Nifti1Image() 将 numpy 存储成 nii.
    mask_3d = mask_3d.swapaxes(0, 2)
    img = nb.Nifti1Image(mask_3d, affine=affine, header=header)
    nb.save(img, file_path)

