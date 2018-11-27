#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: int_wrapper.py
@Time: 18-7-4 10:14
@Last_update: 18-7-4 10:14
@Desc: None
"""

__all__ = [
    'IntWrapper'
]

"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
现在这个IntWrapper有污染性,
所有经过的预算都会是IntWrapper实例化出的实例本身
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
class IntWrapper(object):

    def __init__(self, num):
        self.value = num

    def __iadd__(self, other):
        self.value += other
        self.value = int(self.value)
        return self

    def __add__(self, other):
        self.value += other
        self.value = int(self.value)
        return self

    def __isub__(self, other):
        self.value -= other
        self.value = int(self.value)
        return self

    def __sub__(self, other):
        self.value -= other
        self.value = int(self.value)
        return self

    def __imul__(self, other):
        self.value *= other
        self.value = int(self.value)
        return self

    def __mul__(self, other):
        self.value *= other
        self.value = int(self.value)
        return self

    def __itruediv__(self, other):
        self.value /= other
        self.value = int(self.value)
        return self

    def __truediv__(self, other):
        self.value /= other
        self.value = int(self.value)
        return self

    def __ifloordiv__(self, other):
        self.value //= other
        self.value = int(self.value)
        return self

    def __floordiv__(self, other):
        self.value //= other
        self.value = int(self.value)
        return self

    def __imod__(self, other):
        self.value %= other
        self.value = int(self.value)
        return self

    def __mod__(self, other):
        self.value %= other
        self.value = int(self.value)
        return self

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.value <= other

    def __eq__(self, other):
        return self.value == other

    def __gt__(self, other):
        return self.value > other

    def __ge__(self, other):
        return self.value >= other

    def __repr__(self):  # representation function.
        return str(int(self.value))

    def __str__(self):  # string function
        return str(int(self.value))

    def set_int(self, num):
        self.value = num
