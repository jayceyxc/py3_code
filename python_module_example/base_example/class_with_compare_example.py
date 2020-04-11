#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 12:55
# @Author  : yuxuecheng
# @Contact : yuxuecheng@xinluomed.com
# @Site    : 
# @File    : class_with_compare_example.py
# @Software: PyCharm
# @Description 实现比较运算符的简单方法

from functools import total_ordering


@total_ordering
class Number(object):
    """
    我们用「total_ordering」装饰器简化实现对类实例排序的过程。我们只需要定义「__lt__」和「__eq__」就可以了，
    它们是实现其余操作所需要的最小的操作集合
    """
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


if __name__ == '__main__':
    print(Number(20) > Number(3))
    print(Number(1) < Number(5))
    print(Number(15) >= Number(15))
    print(Number(10) <= Number(2))
