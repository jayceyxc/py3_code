#!/usr/bin/env python3
'''
@File    :   test_fast_fib.py
@Time    :   2020/04/20 22:06:01
@Author  :   Yu Xuecheng 
@Version :   1.0
@Contact :   yuxuecheng@xinluomed.com
@License :   (C)Copyright 2020-2022, yuxuecheng
@Desc    :   测试用cython生成的fast_fib库
'''

# here put the import lib
import time
from fast_fib import fib

start = time.time()
result = fib(40)
end = time.time()
print(f'斐波拉契数列第40项为：{result}，耗时：{end - start}秒')
