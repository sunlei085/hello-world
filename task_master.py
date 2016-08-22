# -*- coding: utf-8 -*-

import Queue
import random
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = Queue.Queue()

# 接收任务的队列
result_queue = Queue.Queue()

class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda :task_queue)
QueueManager.register('get_result_queue', callable=lambda :result_queue)

# 绑定端口50000，设置验证码‘sun’
manager = QueueManager(address=('', 50000), authkey=b'sun')

# 启动queue
manager.start()

# 获得网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放任务进入
for i in xrange(10):
    n = random.randint(0, 1000)
    print('Put task %d' % n)
    task.put(n)

# 获取任务结果
print('Try get result ....')
for _ in xrange(10):
    r = result.get(timeout = 10)
    print ('Result: %s' % r)

# 关闭
manager.shutdown()


