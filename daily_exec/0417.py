# coding=utf-8
"""
    n k     数字个数n，数字差值k
    n个正整数
    输出 差值位k的数字对去重后的个数

def foo1(shuru,arr):
    if len(arr)!=shuru[0] or len(arr)<=0 or len(shuru)<2:
        return -1
    arr1=[]
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]-arr[j]==shuru[1]or arr[j]-arr[i]==shuru[1]:
                arr1.append((arr[i],arr[j]))
    return len(set(arr1))

if __name__ == '__main__':
    shuru=map(int,raw_input("数字个数和差值：").split(' '))
    arr=map(int,raw_input("输入正整数：").split(' '))
    print foo1(shuru,arr)
"""
#APScheduler
"""
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('interval', seconds=3)
def timed_job():
    print('This job is run every three minutes.')


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='0-9', minute='30-59', second='*/3')
def scheduled_job():
    print('This job is run every weekday at 5pm.')


print('before the start funciton')
sched.start()
print("let us figure out the situation")
"""

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

import datetime
import time
import logging


def job_function():
    print
    "Hello World" + " " + str(datetime.datetime.now())


if __name__ == '__main__':
    log = logging.getLogger('apscheduler.executors.default')
    log.setLevel(logging.INFO)  # DEBUG

    fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    h = logging.StreamHandler()
    h.setFormatter(fmt)
    log.addHandler(h)

    print('start to do it')

    sched = BlockingScheduler()

    # Schedules job_function to be run on the third Friday
    #  of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
    sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour='0-9', minute="*", second="*/4")

    sched.start()