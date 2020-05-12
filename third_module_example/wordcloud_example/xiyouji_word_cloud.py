#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 19:48
# @Author  : yuxuecheng
# @Contact : jayce123@163.com
# @Site    : 
# @File    : xiyouji_word_cloud.py
# @Software: PyCharm
# @Description: 西游记的词云图

import os
import codecs
from wordcloud import WordCloud
# 绘制图像的模块
import matplotlib.pyplot as plt
import jieba

from config import data_dir, picture_dir

file_path = os.path.join(data_dir, '红楼梦2.txt')

f = codecs.open(file_path, mode='r', encoding='utf-8').read()

# 结巴分词，生成字符串，wordcloud无法直接生成正确的中文词云
cut_text = ' '.join(jieba.cut(f))

wordcloud = WordCloud(
    # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
    font_path="/System/Library/fonts/PingFang.ttc",
    # 设置了背景，宽高
    background_color="white",
    width=1000,
    height=1000
).generate(cut_text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig(os.path.join(picture_dir, 'wordcloud', '红楼梦.png'))
plt.show()
