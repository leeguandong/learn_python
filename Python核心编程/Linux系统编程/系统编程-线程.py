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

# 避免全局变量被修改的操作2  互斥锁 不占用资源，效率更高
from threading import Thread, Lock

g_num = 0

def test1():
    global g_num
    # 上锁操作，一旦锁上，其他线程会被堵塞直到这个锁被解开为止
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    # 开锁操作，一旦执行完毕即开锁，让其他线程抢锁
    mutex.release()

    print('--test1--g_num=%d' % g_num)

def test2():
    global g_num
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()

    print('--test2--g_num=%d' % g_num)

# 创建一把互斥锁，默认是没有上锁的
mutex = Lock()

p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test2)
p2.start()
