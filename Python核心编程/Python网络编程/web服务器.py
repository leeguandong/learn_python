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

# 使用进程来实现并发服务器
# SerSocket是接收新的客户端，而newSocket是标记的在运行的客户端
from socket import *
from multiprocessing import Process

def dealWithClinet(newSocket, destAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            print('接收数据')
        else:
            print('数据接收完毕，关闭客户端')
        newSocket.close()

SerSocket = socket(AF_INET, SOCK_STREAM)

def main():
    # 如果建立TCP连接中出现问题，服务器首先四次挥手，这句代码保证了服务器先发close()收到回复的正常
    SerSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddr = ('', 7788)
    SerSocket.bind(localAddr)
    SerSocket.listen(5)

    try:
        while True:
            print('--主进程，等待新客户端的到来--')
            newSocket, destAddr = SerSocket.accept()

            print('--主进程，接下来创建子进程来实现多个客户端交互--')
            client = Process(target=dealWithClinet, args=(newSocket, destAddr))
            client.start()
            # 在线程中不能关闭newSocket，因为线程是公用同一份资源，你关闭了，下一个线程就不能用了
            newSocket.close()
    finally:
        # SerSocket可以被关闭，不影响里面的newSocket的运行，只是不能再接受新的客户端了
        # 但是newSocket被关闭了，就不可以收发数据了
        SerSocket.close()

if __name__ == '__main__':
    main()
