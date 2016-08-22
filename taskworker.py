# -*- coding: utf-8 -*-

import Queue
import time
from multiprocessing.managers import BaseManager


# 创建类似QueueManager
class QueueManage(BaseManager):
    pass

# 由于只从网络上获取Queue，所以注册时只提供名字:
QueueManage.register('get_task_queue')
QueueManage.register('get_result_queue')

# 连接到服务器端，即task_master.py
server_addr = '127.0.0.1'
print('Connection to server: %s' % server_addr)

# 处理端口信息与认证信息
m = QueueManage(address=(server_addr, 50000), authkey=b'sun')

# 从网络连接
m.connect()

# 获取Queue对象
task = m.get_task_queue()
result = m.get_result_queue()

# 从task队列获取任务，并把结果写入result
for _ in xrange(10):
    try:
        n = task.get(timeout = 2)
        print('run task: %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, (n*n))
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')

# 处理结束
print('worker exit.')