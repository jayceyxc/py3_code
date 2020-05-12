#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-28 21:00
# @Author  : yuxuecheng
# @Contact : yuxuecheng@xinluomed.com
# @Site    :
# @File    : server_conf.py
# @Software: PyCharm
# @Description

import os

base_dir = os.path.dirname(os.path.abspath(__file__))
print(base_dir)
data_dir = os.path.join(base_dir, 'data')
output_dir = os.path.join(base_dir, 'output')
picture_dir = os.path.join(output_dir, 'picture')

