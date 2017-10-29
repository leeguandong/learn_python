'''
fork()部分代码均在ubuntu中运行
'''

# # 多任务执行--fork()
# import os
# import time
#
# # 生成一个子进程，此时函数就有两个进程，一个父(主)进程，一个子进程，系统为了区分子进程和父进程，会给父进程返回一个大于0的值，而子进程则是等于0的值
# ret = os.fork()
# if ret == 0:
#     while True:
#         print('---1---')
#         time.sleep(1)
# else:
#     while True:
#         print('---2---')
#         time.sleep(1)

# # 创建父子进程
# import os
# import time
#
# ret = os.fork()
# if ret == 0:
#     print('---子进程1---')
#     time.sleep(5)
#     print('---子进程over---')
# else:
#     print('---父进程---')
#     time.sleep(3)
# print('---进程完毕---')

# # 进程与进程不进行数据交换，即便是全局变量，在不同的进程也是不同的
# # 这个程序让主进程暂停3s，然后子进程执行，其实展示了进程和主进程中的全局变量的不用，更进一步说明两个进程之间是互不通信的，主进程是100，子进程是101
# import os
# import time
#
# g_num = 100
# ret = os.fork()
# if ret == 0:
#     print('---processing---')
#     g_num += 1
#     print('---processing-1 g_num%s---' % g_num)
# else:
#     time.sleep(3)
#     print('---processing1---')
#     print('---prcessing1 g_nuum%s' % g_num)

# # 多次fork()问题
# # 注意第二个fork与第一个fork平齐，那么第一个fork产生的父子进程会在下一个fork中同时在产生父子进程，也就是此时会增加两个进程
# # 但是如果把第二个fork放到第一个fork后面，此时自会增加一个子进程，它的else后面的仍然是之前的父进程在执行
# import  os
#
# ret=os.fork()
# if ret==0:
#     print('---1---')
# else:
#     print('---2---')
#
# ret=os.fork()
# if ret==0:
#     print('---1---')
# else:
#     print('---2---')
#
#     ret = os.fork()
#     if ret == 0:
#         print('---1---')
#     else:
#         print('---2---')

# # frok()只能在linux中使用，不具有跨平台性，现在使用一个跨平台的创建子进程的类
# from multiprocessing import Process
# import time
#
# def test():
#     while True:
#         print('---test---')
#         time.sleep(1)
#
# # 下面这段代码就是测试时使用，调用的时候不使用
# if __name__ == '__main__':
#     p=Process(target=test)
#     p.start()
#     while True:
#         print('---main---')
#         time.sleep(1)

# 这是创建子进程的第二种方法，让子类继承父类Process父类
from multiprocessing import Process
import time

class MyNewProcess(Process):
    def run(self):
        while True:
            print('---1---')
            time.sleep(1)

if __name__=='__mian__':
    p = MyNewProcess()
    # 调用p.start()方法，p会先去父类中寻找start()，然后在Process的start方法中调用run方法
    p.start()

    while True:
        print('---Main---')
        time.sleep(1)
