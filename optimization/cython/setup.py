#!/usr/bin/env python3
'''
@File    :   setup.py
@Time    :   2020/04/20 22:01:51
@Author  :   Yu Xuecheng 
@Version :   1.0
@Contact :   yuxuecheng@xinluomed.com
@License :   (C)Copyright 2020-2022, yuxuecheng
@Desc    :   None
'''

# here put the import lib
from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('fast_fib.pyx'))
