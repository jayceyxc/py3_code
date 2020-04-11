#!/usr/bin/env python3
'''
@File    :   loguru_example.py
@Time    :   2020/03/25 17:29:45
@Author  :   Yu Xuecheng 
@Version :   1.0
@Contact :   yuxuecheng@xinluomed.com
@License :   (C)Copyright 2020-2022, yuxuecheng
@Desc    :   None
'''

# here put the import lib
from loguru import logger


@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)


def bind_test():
    logger.add("logs/file.log", format="{extra[ip]} {extra[user]} {message}")

    logger_ctx = logger.bind(ip="192.168.0.1", user="someone")
    logger_ctx.info("Contextualize your logger easily")
    logger_ctx.bind(user="someoneelse").info(
        "Inline binding of extra attribute")


def log_to_file():
    logger.add('logs/file_{time}.log', rotation='1 hour',
               retention='10 hour', compression='zip', level='INFO')
    logger.info('test logger to file')
    logger.error('error logger to file')
    logger.debug('hello')


def main():
    logger.debug("That's it, beautiful and simple logging!")


if __name__ == "__main__":
    # main()
    # my_function(0, 0, 0)
    # bind_test()
    log_to_file()
