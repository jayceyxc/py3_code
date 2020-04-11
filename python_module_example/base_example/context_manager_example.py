#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 12:50
# @Author  : yuxuecheng
# @Contact : yuxuecheng@xinluomed.com
# @Site    : 
# @File    : context_manager_example.py
# @Software: PyCharm
# @Description 使用contextmanager来管理上下文

from contextlib import contextmanager

'''
使用 contextmanager 的 manager 装饰器实现了内容管理协议。在进入 with 块时 tag 函数的第一部分（在 yield 之前的部分）就已经执行了，
然后 with 块才被执行，最后执行 tag 函数的其余部分。
'''
@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")


with tag("h1"):
    print("This is Title.")


