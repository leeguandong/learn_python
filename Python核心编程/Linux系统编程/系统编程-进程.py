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

# # 这是创建子进程的第二种方法，让子类继承父类Process父类
# from multiprocessing import Process
# import time
#
# class MyNewProcess(Process):
#     def run(self):
#         while True:
#             print('---1---')
#             time.sleep(1)
#
# if __name__=='__mian__':
#     p = MyNewProcess()
#     # 调用p.start()方法，p会先去父类中寻找start()，然后在Process的start方法中调用run方法
#     p.start()
#
#     while True:
#         print('---Main---')
#         time.sleep(1)

# # 进程池
# from multiprocessing import Pool
# import os
# import random
# import time
#
# def worker(num):
#     for i in range(5):
#         print('===pid=%d==num=%d='%(os.getpid(),num))
#         time.sleep(1)
#
# # 3表示进程池中最多有三个进程一起执行
# pool=Pool(3)
#
# for i in range(10):
#     print('---%d---'%i)
#     # 向进程中添加任务
#     # 注意：如果添加的任务数量超过了进程池中进程的个数的话，那么就不会接着往进程池中添加，如果还没有执行的话，他会等待前面的进程结束，然后在往
#     # 进程池中添加新进程
#     pool.apply_async(worker,(i,))
#
# pool.close() # 关闭进程池
# pool.join()  # 主进程在这里等待，只有子进程全部结束之后，在会开启主线程

# 案例 多进程拷贝文件
from multiprocessing import Pool, Manager
import os

def copyFileTask(name, oldFolderName, newFolderNmae, queue):
    "完成copy一个文件的功能"
    fr = open(oldFolderName + '/' + name)
    # name是放在目录后面，但一个name，找不到路径的
    fw = open(newFolderNmae + '/' + name, 'w')

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()

    queue.put(name)

def main():
    # 0.获取原来要copy的文件夹的名字
    oldFolderName = input('请输入文件夹的名字：')

    # 1.创建一个文件夹
    newFolderNmae = oldFolderName + '复件'
    os.mkdir(newFolderNmae)

    # 2.获取old文件夹中的所有的文件夹名
    fileNames = os.listdir(oldFolderName)

    # 3.使用多进程的方式copy，原文件中所有文件到新的文件夹中
    pool = Pool(5)
    queue = Manager().queue()

    # 不能把列表给子进程，如果给列表的话，相当于不是多任务执行，而是一个进程把所有的列表都在复制，所以这个用循环，每个文件给一个子进程
    for name in fileNames:
        pool.apply_async(copyFileTask, args=(name, oldFolderName, newFolderNmae, queue))

    num = 0
    allNum = len(fileNames)
    while True:
        queue.get()
        num += 1
        copyRate = num / allNum
        print('\rcopy的进度是：%.2f%%' % (copyRate * 100), end='')
        if num == allNum:
            break

        # 原本主进程在这里等着子进程完全结束，现在利用这段时间进行显示进度
        # pool.close()
        # pool.join()

if __name__ == '__main__':
    main()
