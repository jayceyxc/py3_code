#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 12:44
# @Author  : yuxuecheng
# @Contact : yuxuecheng@xinluomed.com
# @Site    : 
# @File    : class_support_with_example.py
# @Software: PyCharm
# @Description 创建支持「with」语句的对象


class Connection(object):
    def __init__(self, name='default'):
        print('__init__')
        self.name = name

    def __enter__(self):
        # Initialize connection...
        print('__enter__')

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close connection...
        print('__exit__')

    def __repr__(self):
        print('__repr__')
        return f'name: {self.name}'

    def __str__(self):
        print('__str__')
        return f'name: {self.name}'


with Connection() as c:
    # __enter__() executes
    print(type(c))
    # conn.__exit__() executes
