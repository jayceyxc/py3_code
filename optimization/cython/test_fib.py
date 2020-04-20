#!/usr/bin/env python3
'''
@File    :   test_fib.py
@Time    :   2020/04/20 22:10:28
@Author  :   Yu Xuecheng 
@Version :   1.0
@Contact :   yuxuecheng@xinluomed.com
@License :   (C)Copyright 2020-2022, yuxuecheng
@Desc    :   测试python版本的斐波那契数列
'''

# here put the import lib
import time


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    start = time.time()
    result = fib(40)
    end = time.time()
    print(f'斐波拉契数列第40项为：{result}，耗时：{end - start}秒')
