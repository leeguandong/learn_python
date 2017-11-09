# # socket通信
# # 下面这段代码在linux中运行
# from socket import *
#
# # 使用udp协议
# udpSocket = socket(AF_INET, SOCK_DGRAM)
#
# # 信息绑定  第一个是你电脑主机的ip地址，不写表示哪一个ip地址都可以，因为你的主机可能存在多个ip地址，第二个是你自己主机的端口号
# udpSocket.bind(('', 7788))
#
# # 在Python3中，一定要加b，python2中不用加
# # 使用udp发送数据，每一次都要协商接收方的ip和port
# udpSocket == socket.sendto(b'haha', ('114.213.247.188', 8080))
#
# # 接收,1024表示一次只接受1024个字节
# recvData = udpSocket.recvfrom(1024)

# # 发送时编码
# from socket import *
#
# udpSocket = socket(AF_INET, SOCK_DGRAM)
# destIp = input('请输入内容')
# destPort = int(input('请输入目的port：'))
# sendData = input('请输入要发送的数据')
#
# udpSocket.sendto(sendData.encode('gb2312'), (destIp, destPort))

# # 接收时解码
# from socket import *
#
# udpSocket = socket(AF_INET, SOCK_DGRAM)
# udpSocket.bind(('', 7789))
# recvData = udpSocket.recvfrom(1024)
#
# # 这个操作相当于解包，第一个是存的内容，第二个是存的信息
# content, destInfo = recvData
#
# print('content is %s' % content)
# print('content is %s' % content.decode('gb2312'))

# 简单聊天室
from socket import *

def main():
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(('', 6678))

    # 收到 打印
    recvInfo = udpSocket.recvfrom(1024)
    print('[%s]:%s' % (str(recvInfo[1]), recvInfo[0].decode('gb2312')))

if __name__ == '__main__':
    main()
