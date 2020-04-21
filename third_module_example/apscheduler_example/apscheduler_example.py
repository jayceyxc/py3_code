#!/usr/bin/env python3
'''
@File    :   apscheduler_example.py
@Time    :   2020/04/21 12:59:12
@Author  :   Yu Xuecheng 
@Version :   1.0
@Contact :   yuxuecheng@xinluomed.com
@License :   (C)Copyright 2020-2022, yuxuecheng
@Desc    :   APScheduler 框架使用
'''

# here put the import lib
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def job1():
    print('job1', datetime.datetime.now())


def job2(text):
    print('job2', datetime.datetime.now(), text)


# 选择调度器
scheduler = BlockingScheduler()

# 指定时间执行任务，只执行一次
scheduler.add_job(job2, 'date', run_date=datetime.datetime(
    2020, 4, 21, 13, 4, 6), args=['text'], id='job2')

# 间隔时间执行任务
scheduler.add_job(job1, 'interval', seconds=5, id='job1')

scheduler.start()
