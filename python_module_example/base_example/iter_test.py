#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 12:34
# @Author  : yuxuecheng
# @Contact : yuxuecheng@xinluomed.com
# @Site    :
# @File    : iter_test.py
# @Software: PyCharm
# @Description 迭代器切片

import itertools

s = itertools.islice(range(50), 10, 20)
for val in s:
    print(val)

string_from_file = '''// Author: ...
// License: ...
//
// Date: ...
Actual content...
'''
for line in itertools.dropwhile(lambda line: line.startswith('//'), string_from_file.split('\n')):
    print(line)
