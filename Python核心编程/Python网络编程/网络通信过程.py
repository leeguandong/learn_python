# # 广播
# import socket, sys
#
# dest = ('<broadcast>', 7788)
#
# # 创建udp套接字
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # 对需要发送广播的套接字进行修改设置，否则不能发送广播数据
# s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#
# # 以广播的形式发送数据到本网络的所有电脑中
# s.sendto('HI', dest)
#
# while True:
#     (buf, address) = s.recvfrom(2048)
#     print('Received from %s: %s' % (address, buf))

# # TCP服务器端代码
# from socket import *
#
# serverSocket = socket(AF_INET, SOCK_STREAM)
# serverSocket.bind('', 8899)
#
# # 一次最多接受5个连接
# serverSocket.listen(5)
#
# # 返回值是两个元组，第一个是回复的端口，第二个是回复客户的信息
# clientSocket, clientInfo = serverSocket.accept()
#
# recvData = clientSocket.recv(1024)
#
# print('%s:%s' % (str(clientInfo), recvData))
#
# clientSocket.close()
# serverSocket.close()

# TCP客户端代码
from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect('192.168.155.1', 8989)

clientSocket.send('haha'.encode('gb2312'))

recvData = clientSocket.recv(1024)

print('recvData %s' % recvData)
clientSocket.close()
