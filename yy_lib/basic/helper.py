#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: helper.py
@Time: 18-6-22 10:29
@Last_update: 18-6-22 10:29
@Desc: 辅助类,还不知道转到神码类下
"""
import numpy as np

def np_statics(data, name=''):

    print(name)
    print('min value is: %s'%str(np.min(data)))
    print('max value is: %s'%str(np.max(data)))
    print('mean value is: %s'%str(np.mean(data)))
    print()

    return None