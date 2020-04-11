#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 12:43
# @Author  : yuxuecheng
# @Contact : yuxuecheng@xinluomed.com
# @Site    : 
# @File    : kwargs_test.py
# @Software: PyCharm
# @Description


def test(*, a, b):
    print(f'a={a}, b={b}')


# test("value for a", "value for b")  # TypeError: test() takes 0 positional arguments...
test(a="value", b="value 2")  # Works...
