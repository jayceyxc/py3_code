#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-06-24 19:44
# @Author  : yuxuecheng
# @Contact : yuxuecheng@xinluomed.com
# @Site    : 
# @File    : logger_toolkit.py
# @Software: PyCharm
# @Description 日志记录工具

import os
import sys
import logging

from logging.handlers import TimedRotatingFileHandler
from logging import Formatter, StreamHandler

from config import base_dir


def init_logging(logger, filename):
    """
    初始化日志
    :param logger: 日志记录对象
    :param filename: 日志文件名称
    :return:
    """
    logger.handlers = []
    logs_dir = os.path.join(base_dir, 'logs')
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    filename = os.path.join(logs_dir, filename)
    logger_formatter = '%(asctime)s %(threadName)s %(levelname)-8s ' \
                       '%(filename)s:%(lineno)-4d:%(funcName)-10s: %(message)s'

    assert isinstance(logger, logging.Logger)
    logger.setLevel(logging.DEBUG)
    # FileHandler Info
    file_handler = TimedRotatingFileHandler(filename=filename, when='H', interval=1, backupCount=20,
                                            encoding='utf-8')
    file_handler.setFormatter(Formatter(fmt=logger_formatter))
    file_handler.setLevel(logging.DEBUG)

    logger.addHandler(file_handler)

    # ConsoleHandler Debug
    console_handler = StreamHandler(stream=sys.stdout)
    console_handler.setFormatter(fmt=logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s'))
    console_handler.setLevel(logging.DEBUG)

    logger.addHandler(console_handler)

    return logger


def get_logger(file_name='test'):
    logger = logging.getLogger(file_name)
    if not logger.handlers:
        logger = init_logging(logger=logger, filename=file_name + '.log')

    return logger

