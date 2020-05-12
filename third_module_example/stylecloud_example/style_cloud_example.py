#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 20:04
# @Author  : yuxuecheng
# @Contact : jayce123@163.com
# @Site    : 
# @File    : style_cloud_example.py
# @Software: PyCharm
# @Description: stylecloud绘制词云

import os
from jieba.analyse import extract_tags

from config import data_dir, picture_dir
from stylecloud import gen_stylecloud


def jieba_cloud(file_name):
    with open(file_name, 'r', encoding='utf8') as f:
        word_list = extract_tags(f.read(), topK=100)
        result = " ".join(word_list)  # 分词用 隔开
        # 制作中文云词
        base_file_name = os.path.basename(file_name)
        png_name = base_file_name.split('.')[0]
        png_name = png_name + '.png'
        gen_stylecloud(text=result,
                       font_path="/System/Library/fonts/PingFang.ttc",
                       output_name=os.path.join(picture_dir, 'stylecloud', png_name))  # 必须加中文字体，否则格式错误


if __name__ == "__main__":
    file_name = os.path.join(data_dir, '红楼梦2.txt')
    jieba_cloud(file_name)
