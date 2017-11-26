# from socket import *
# from time import sleep
#
# # 创建socket
# tcpSerSocket = socket(AF_INET, SOCK_STREAM)
#
# # 绑定本地信息
# address = ('', 7788)
# tcpSerSocket.bind(address)
#
# connNum = int(input('请输入要最大的连接数'))
#
# # 使用socket创建的套接字默认的属性是主动的，使用listen将其变成被动的，这样就可以接受别人的连接了
# tcpSerSocket.listen(connNum)
#
# # 如果有新的客户端来接连服务器，那么就创建一个新的套接字专门连接这个客户端
# # 在这个期间，如果有20个客户端调用了connect连接服务器，那么这个服务器的linux底层会自动维护2个队列（半连接和已连接），其中半连接和已连接
# # 的总数为listen中的值，如果这个值为5，那么意味着此时的服务器最多只有5个客户端能够连接成功，而剩余的15则会堵塞在connect函数
# for i in range(10):
#     print(i)
#     sleep(1)
#
# print('延时结束')
#
# while True:
#     # 如果服务器调用了accept，那么linux底层中的那个半连接和已连接中的客户端的个数就少1，此时那15个处于connect状态的客户机又会来争抢
#     # 这个空出来的位置
#     newSocket, clientAddr = tcpSerSocket.accept()
#     print(clientAddr)
#     sleep(1)

# # 使用进程来实现并发服务器
# # SerSocket是接收新的客户端，而newSocket是标记的在运行的客户端
# from socket import *
# from multiprocessing import Process
#
# def dealWithClinet(newSocket, destAddr):
#     while True:
#         recvData = newSocket.recv(1024)
#         if len(recvData) > 0:
#             print('接收数据')
#         else:
#             print('数据接收完毕，关闭客户端')
#
# SerSocket = socket(AF_INET, SOCK_STREAM)
#
# def main():
#     # 如果建立TCP连接中出现问题，服务器首先四次挥手，这句代码保证了服务器先发close()收到回复的正常
#     # 这句话保证了客户端在2MSL的时候才挂，不会先挂
#     SerSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#     localAddr = ('', 7788)
#     SerSocket.bind(localAddr)
#     SerSocket.listen(5)
#
#     try:
#         while True:
#             print('--主进程，等待新客户端的到来--')
#             newSocket, destAddr = SerSocket.accept()
#
#             print('--主进程，接下来创建子进程来实现多个客户端交互--')
#             client = Process(target=dealWithClinet, args=(newSocket, destAddr))
#             client.start()
#             # 在线程中不能关闭newSocket，因为线程是公用同一份资源，你关闭了，下一个线程就不能用了
#             newSocket.close()
#     finally:
#         # SerSocket可以被关闭，不影响里面的newSocket的运行，只是不能再接受新的客户端了
#         # 但是newSocket被关闭了，就不可以收发数据了
#         SerSocket.close()
#
# if __name__ == '__main__':
#     main()

# # 单线程费堵塞服务器
# from socket import *
#
# serSocket = socket(AF_INET, SOCK_STREAM)
#
# serSocket.setblocking(False)
# localAddr = ('', 7788)
# serSocket.bind(localAddr)
# serSocket.listen(10)
#
# # 用来保存所有已经连接的客户端的信息
# clientAddrList = []
#
# while True:
#     try:
#         clientSocket, clientAddr = serSocket.accept()
#     except:
#         pass
#     else:
#         print('一个新的客户端到来：%s' % (clientAddr))
#         clientSocket.setblocking(False)
#         clientAddrList.append((clientSocket, clientAddr))
#
#     for clientSocket, clientAddr in clientAddrList:
#         try:
#             recvData = clientSocket.recv(1024)
#         except:
#             pass
#         else:
#             if len(recvData) > 0:
#                 print('%s,%s' % (str(clientAddr), recvData))
#             else:
#                 clientSocket.close()
#                 clientAddrList.remove((clientSocket, clientAddr))
#                 print('%s 已经下线' % (str(clientAddr)))

# # select 服务器
# # select的核心就在于多一个监听的socket，只要出现新的socket，即在下一次循环时就读出来，而原连接客户端在一个循环中不断读取
# import select
# import socket
# import sys
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(',7788')
# server.listen(5)
#
# inputs = [server, sys.stdin]
#
# running = True
#
# while True:
#     # 调用select函数，阻塞等待，select默认是阻塞的
#     readable, writeable, exceptional = select.select(inputs, [], [])
#
#     # 数据抵达 循环
#     for sock in readable:
#
#         # 监听新的连接
#         if socket == server:
#             conn, addr = server.accept()
#             # select 监听socket
#             inputs.append(conn)
#
#         # 监听键盘输入
#         elif sock == sys.stdin:
#             cmd = sys.stdin.readline()
#             running = False
#             break
#
#         # 有数据达到
#         else:
#             # 读取客户端发送的信息
#             recvData = sock.recv(1024)
#             if recvData:
#                 sock.send(recvData)
#             else:
#                 # 移除select监听的socket
#                 inputs.remove(sock)
#                 sock.close()

# # 和select是一致的，但是epoll是主动的事件通知机制，而不是被动的轮询
# # epoll
# # EPOLLIN 可读
# # EPOLLOUT 可写
# # EPOLLET ET模式  边缘触发 只通知一次，不处理就不通知了，效率高
# # EPOLLLT LT模式  水平触发 一直通知，直到完成处理
# import socket
# import select
#
# # 创建套接字
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 设置可以重复使用绑定的信息
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
# # 绑定本机信息
# localAddr = ('', 7788)
# s.bind(localAddr)
#
# # 变为被动
# s.listen(10)
#
# # 创建一个epoll对象
# epoll = select.epoll()
#
# # 测试，用来打印套接字对应的文件描述符
# # print(s.fileno())
#
# # 注册事件到epoll中
# # epoll.register(fd[ , eventmask])
# # 注意，如果fd已经注册，则会发生异常，将创建的套接字添加到epoll的时间监听中，注意注册是主动的事件通知，第一个参数就是文件描述符，而不是套接字
# epoll.register(s.fileno(), select.EPOLLIN | select.EPOLLEF)
#
# connections = {}
# addresses = {}
#
# # 循环等待客户端的到来或者对方发送数据
# while True:
#     # epoll进行fd扫描的地方
#     epoll_list = epoll.poll()
#
#     # 对事件进行判断
#     for fd, events in epoll_list:
#
#         # 如果是socket创建的套接字被激活
#         if fd == s.fileno():
#             conn, addr = s.accept()
#
#             print('有新的客户端')
#
#             # 将conn和addr信息分别保存起来，存在字典中是方便后续根据fd找套接字
#             connections[conn.fileno()] = conn
#             addresses[conn.fileno()] = addr
#
#             # 向epoll中注册链接的socket的可读事件
#             epoll.register(conn.fileno(), select.EPOLLIN | select.EPOLLEF)
#
#         elif events == select.EPOLLIN:
#             recvData = connections[fd].recv(1024)
#
#             if len(recvData) > 0:
#                 print('recv:%s' % recvData)
#             else:
#                 # 从epoll中移除连接fd
#                 epoll.unregister(fd)
#
#                 connections[fd].close()

# # 协程
# # 底层是用生成器做的，yield是生成器
# import time
# def A():
#     while True:
#         print('---A---')
#         yield
#         time.sleep(1)
#
# def B(c):
#     while True:
#         print('---B---')
#         c.next()
#         # next执行上一次执行到yield的地方，所以看起来先执行B，到next执行A，到yeild就停下来了，到B中执行，sleep之后再到next，到A中执行
#         # 下一次再到yield停止，依次循环
#         time.sleep(0.5)
#
# a= A()
# B(a)

# # greenlet实现协程
# from greenlet import greenlet
# import time
#
# def A():
#     while True:
#         print('--A--')
#         grl2.switch()
#         time.sleep(0.5)
#
# def B():
#     while True:
#         print('---B---')
#         grl1.switch()
#         time.sleep(1)
#
# grl1 = greenlet(A)
# grl2 = greenlet(B)
#
# grl1.switch()

# gevent协程
import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # 用来模拟耗时操作，gevent一遇到耗时操作时就会自动切换
        gevent.sleep(1)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)

g1.join()
g2.join()
g3.join()
