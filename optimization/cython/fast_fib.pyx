#!/usr/bin/env python3
'''
@File    :   fast_fib.pyx
@Time    :   2020/04/20 21:59:49
@Author  :   Yu Xuecheng 
@Version :   1.0
@Contact :   yuxuecheng@xinluomed.com
@License :   (C)Copyright 2020-2022, yuxuecheng
@Desc    :   利用Cython对Python代码进行加速
'''

'''
参考：https://mp.weixin.qq.com/s/NjjNmRwVJNwoA72FzTAaxA

官方文档：https://cython.readthedocs.io/
'''
# here put the import lib


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
