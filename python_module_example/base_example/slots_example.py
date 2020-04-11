#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 12:53
# @Author  : yuxuecheng
# @Contact : yuxuecheng@xinluomed.com
# @Site    : 
# @File    : slots_example.py
# @Software: PyCharm
# @Description 用__slots__节省内存


class Person:
    """
    当我们定义了「__slots__」属性时，Python 没有使用字典来表示属性，而是使用小的固定大小的数组，这大大减少了每个实例所需的内存。
    使用「__slots__」也有一些缺点：我们不能声明任何新的属性，我们只能使用「__slots__」上现有的属性。而且，带有「__slots__」
    的类不能使用多重继承。
    """
    __slots__ = ["first_name", "last_name", "phone"]

    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone