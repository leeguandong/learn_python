# 线程速度快
# 创建线程的第一种方法，使用Thread(Target=test)
# 主线程在末尾等待子线程全部执行完再执行
# from threading import Thread
# import time
#
# def test():
#     print('---时间快---')
#     time.sleep(1)
#
# for i in range(5):
#     t = Thread(target=test)
#     t.start()

# # 创建线程的第二种方法：
# import threading
# import time
#
# class MyThread(threading.Thread):
#     def run(self):
#         for i in range(3):
#             time.sleep(1)
#             msg = 'I m' + self.name + ' @ ' + str(i)
#             print(msg)
#
# if __name__ == '__main__':
#     t = MyThread()
#     t.start()

# # 线程调度顺序问题
# import threading
# import time
#
# class MyThread(threading.Thread):
#     def run(self):
#         for i in range(3):
#             time.sleep(1)
#             msg = 'I m' + self.name + ' @ ' + str(i)
#             print(msg)
#
# def test():
#     for i in range(5):
#         t = MyThread()
#         t.start()
#
# if __name__ == '__main__':
#     test()

# 线程要加死锁的原因，这个问题还是很重要的
# 在先后创建两个线程之后，test1()和test2()的执行就服从调度算法，test1()打印出来的结果并不是1000000，test2()打印出来的结果并不是2000000，
# 因为两个线程在CPU的调度权，有可能一个线程中对全局变量只执行了一半代码，而被踢出CPU，另一个接着执行，这就会产生问题。
# from threading import Thread
# g_num=0
#
# def test1():
#     global g_num
#     for i in range(1000000):
#         g_num += 1
#
#     print('--test1--g_num=%d' % g_num)
#
# def test2():
#     global g_num
#     for i in range(1000000):
#         g_num += 1
#
#     print('--test2--g_num=%d' % g_num)
#
# p1 = Thread(target=test1)
# p1.start()
#
# # time.sleep(3) # 取消屏蔽之后 再次运行程序，结果会不一样
#
# p2 = Thread(target=test2)
# p2.start()

# # 避免全局变量被修改的操作1   轮询
# from threading import Thread
#
# g_num = 0
# g_flag = 1
#
# def test1():
#     global g_num
#     # 在类中对全局变量进行修改就要加global
#     global g_flag
#     if g_flag == 1:
#         for i in range(1000000):
#             g_num += 1
#         g_flag = 0
#
#     print('--test1--g_num=%d' % g_num)
#
# def test2():
#     global g_num
#     # 轮询，线程在这里不断去执行，否则在上一个线程完成了加1000000的操作之后，下一个线程也执行完了，不会对条件进行判断
#     while True:
#         if g_flag != 1:
#             for i in range(1000000):
#                 g_num += 1
#             break
#
#     print('--test2--g_num=%d' % g_num)
#
# p1 = Thread(target=test1)
# p1.start()
#
# # time.sleep(3) # 取消屏蔽之后 再次运行程序，结果会不一样
#
# p2 = Thread(target=test2)
# p2.start()

# # 避免全局变量被修改的操作2  互斥锁 不占用资源，效率更高
# from threading import Thread, Lock
#
# g_num = 0
#
# def test1():
#     global g_num
#     # 上锁操作，一旦锁上，其他线程会被堵塞直到这个锁被解开为止
#     mutex.acquire()
#     for i in range(1000000):
#         # mutex.acquire()
#         # 放在里面也是可以的，但是第一个print就不是1000000，因为抢的次数并不是两者统一的，是两者的当时的总和
#         g_num += 1
#     # 开锁操作，一旦执行完毕即开锁，让其他线程抢锁
#     mutex.release()
#
#     print('--test1--g_num=%d' % g_num)
#
# def test2():
#     global g_num
#     mutex.acquire()
#     for i in range(1000000):
#         g_num += 1
#     mutex.release()
#
#     print('--test2--g_num=%d' % g_num)
#
# # 创建一把互斥锁，默认是没有上锁的
# mutex = Lock()
#
# p1 = Thread(target=test1)
# p1.start()
#
# p2 = Thread(target=test2)
# p2.start()

# # 线程中非全局变量是不共享的
# from threading import Thread
# import threading, time
#
# def test1():
#     g_num = 100
#     name = threading.current_thread().name
#     print('---线程的名字是%s' % name)
#     if name == 'Thread-1':
#         g_num += 1
#         print()
#     else:
#         time.sleep(2)
#     print('---线程的名字是%s--g_num=%d' % (name, g_num))
#
# p1 = Thread(target=test1)
# p1.start()
#
# p2 = Thread(target=test1)
# p2.start()

# # 生产者与消费者模式
# # 这个程序中有两个生产者和5个消费者，产生每次生产100个，只要缓冲池(queue)里面产品个数少于1000，即向里面添加数据
# # 消费者每个消费3个，只要缓冲池里面数据大于100，即向外取出数据
# import threading
# import time
# from queue import Queue
#
# class Produccer(threading.Thread):
#     def run(self):
#         global queue
#         count = 0
#         while True:
#             if queue.qsize() < 1000:
#                 for i in range(100):
#                     count = count + 1
#                     msg = '生成产品' + str(count)
#                     queue.put(msg)
#                     print(msg)
#             time.sleep(0.5)
#
#
# class Consumer(threading.Thread):
#     def run(self):
#         global queue
#         while True:
#             if queue.qsize() > 100:
#                 for i in range(3):
#                     msg = self.name + '消费了' + queue.get()
#                     print(msg)
#             time.sleep(1)
#
#
# if __name__ == '__main__':
#     queue = Queue()
#     for i in range(500):
#         queue.put('初始产品' + str(i))
#     for i in range(2):
#         p = Produccer()
#         p.start()
#     for i in range(5):
#         c = Consumer()
#         c.start()

# # 异步
# # 下面的代码就是主进程一直在循环，当子进程执行完毕时候，系统通知主进程去进行回调操作，并且能拿到子进程的返回值
# # 这个程序很好的阐述了异步，主进程一直在执行，他也不知道什么时候执行异步操作
# from multiprocessing import Pool
# import time
# import os
#
# def test():
#     print('--进程池中的进程--pid=%d,ppid=%d--' % (os.getpid(), os.getppid()))
#     for i in range(3):
#         print('---%d---' % i)
#         time.sleep(1)
#     return 'haha'
#
# def test2(args):
#     print('---callback func --pid=%d' % os.getpid())
#     print('---callback func --args=%s' % args)
#
# if __name__ == '__main__':
#     pool = Pool(3)
#     pool.apply_async(func=test, callback=test2)
#     while True:
#         time.sleep(1)
#         print('---主进程-pid=%d---' % os.getpid())

# 如何解决线程GIL的问题，关键代码用C写，C不存在GIL的问题







