#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 12:31
# @Author  : yuxuecheng
# @Contact : yuxuecheng@xinluomed.com
# @Site    : 
# @File    : clean_string.py
# @Software: PyCharm
# @Description 整理字符串输入

user_input = "This\nstring has\tsome whitespaces...\r\n"

character_map = {
    ord('\n'): ' ',
    ord('\t'): ' ',
    ord('\r'): None
}

# This string has some whitespaces...
print(user_input.translate(character_map))
