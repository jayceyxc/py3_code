#!/usr/bin/env python3
'''
@File    :   apscheduler_decorator.py
@Time    :   2020/04/21 14:51:30
@Author  :   Yu Xuecheng 
@Version :   1.0
@Contact :   yuxuecheng@xinluomed.com
@License :   (C)Copyright 2020-2022, yuxuecheng
@Desc    :   使用APScheduler的装饰器来进行任务调度
'''

# here put the import lib
import os
import sys
import time
import codecs
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

sc = BlockingScheduler()

# 每天凌晨1点30分50秒执行
# @sc.scheduled_job('cron', day_of_week='*', hour=1, minute='30', second='50')
@sc.scheduled_job('interval', seconds=5)
def check_db():
    print('aaa')


def main():
    with codecs.open('1.txt', mode='a', encoding='UTF-8') as f:
        try:
            sc.start()
            time.sleep(30)
            print('定时任务成功执行')
            f.write('定时任务成功执行')
            sc.shutdown()
        except Exception as e:
            sc.shutdown()
            print('定时任务执行失败')
            f.write('定时任务执行失败')
        finally:
            f.close()


if __name__ == "__main__":
    main()
