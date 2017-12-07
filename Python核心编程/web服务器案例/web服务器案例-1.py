# # 静态web服务器
# from socket import *
# from multiprocessing import Process
#
# def main():
#     # tcp sever
#     tcpsocker = socket(AF_INET, SOCK_STREAM)
#     tcpsocker.bind(('', 8001))
#     tcpsocker.listen(128)
#
#     while True:
#         cli_socket, cli_address = tcpsocker.accept()
#         print('%s %s:' % cli_address)
#         p = Process(target=handle, args=(cli_socket,))
#         p.start()
#         cli_socket.close()
#
# def handle(cli_socket):
#     recvdata = cli_socket.recv(1024)
#     print('recvdata:', recvdata)
#     # 解析HTTP报文数据
#     # 提取请求方式
#     # 提取请求路径
#     # 返回指定报文
#     response_start_line = 'HTTP/1.1 200 OK\r\n'
#     response_header = 'Server:My server\r\n'
#     response_body = 'hello leeguandong'
#     response = response_start_line + response_header + '\r\n' + response_body
#     print('response data:', response)
#     cli_socket.send(bytes(response, 'utf-8'))
#     cli_socket.close()
#
# if __name__ == '__main__':
#     main()

# # 静态文件web服务器
# # 在服务器中维护了对于请求的应答文件
# from socket import *
# from multiprocessing import Process
# import re
#
# # 设置静态文件根目录
# HTML_ROOT_DIR = './html'
#
# def main():
#     # tcp sever
#     tcpsocker = socket(AF_INET, SOCK_STREAM)
#     tcpsocker.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#     tcpsocker.bind(('', 8000))
#     tcpsocker.listen(128)
#
#     while True:
#         cli_socket, cli_address = tcpsocker.accept()
#         print('%s %s:' % cli_address)
#         p = Process(target=handle, args=(cli_socket,))
#         p.start()
#         cli_socket.close()
#
# def handle(cli_socket):
#     recvdata = cli_socket.recv(1024)
#     print('recvdata:', recvdata)
#     # 解析HTTP报文数据
#     request_lines = recvdata.splitlines()
#     for line in request_lines:
#         print(line)
#
#     # 提取请求方式
#     request_start_line = request_lines[0]
#     file_name = re.match(r'\w+ +(/[^ ]*)', request_start_line.decode('utf-8')).group(1)
#     print('*******')
#     print(file_name)
#
#     if '/' == file_name:
#         file_name = '/index.html'
#
#     # 提取请求路径
#     try:
#         file = open(HTML_ROOT_DIR + file_name, 'rb')
#         print('--------------------')
#         print(file)
#     except IOError:
#         response_start_line = 'HTTP/1.1 404 not found\r\n'
#         response_header = 'Server:My server\r\n'
#         response_body = 'not found'
#     else:
#         file_data = file.read()
#         print(file_data)
#         file.close()
#
#         # 返回指定报文
#         response_start_line = 'HTTP/1.1 200 OK\r\n'
#         response_header = 'Server:My server\r\n'
#         response_body = file_data.decode('utf-8')
#     response = response_start_line + response_header + '\r\n' + response_body
#     print('response data:', response)
#     cli_socket.send(bytes(response, 'utf-8'))
#     cli_socket.close()
#
# if __name__ == '__main__':
#     main()

# 面向对象编程
# 静态文件web服务器
# 在服务器中维护了对于请求的应答文件
from socket import *
from multiprocessing import Process
import re

# 设置静态文件根目录
HTML_ROOT_DIR = './html'

class HttpServer():
    def __init__(self):
        # 为什么要加self?  如果不添加self，那么一离开__init__方法，这个属性就丢了，所以要存到self对象里面去
        self.tcpsocker = socket(AF_INET, SOCK_STREAM)
        self.tcpsocker.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self, port):
        self.tcpsocker.bind(('', port))

    def start(self):
        self.tcpsocker.listen(128)
        while True:
            cli_socket, cli_address = self.tcpsocker.accept()
            print('%s %s:' % cli_address)
            p = Process(target=self.handle, args=(cli_socket,))
            p.start()
            cli_socket.close()

    def handle(self, cli_socket):
        recvdata = cli_socket.recv(1024)
        print('recvdata:', recvdata)
        # 解析HTTP报文数据
        request_lines = recvdata.splitlines()
        for line in request_lines:
            print(line)

        # 提取请求方式
        request_start_line = request_lines[0]
        file_name = re.match(r'\w+ +(/[^ ]*)', request_start_line.decode('utf-8')).group(1)
        print('*******')
        print(file_name)

        if '/' == file_name:
            file_name = '/index.html'

        # 提取请求路径
        try:
            file = open(HTML_ROOT_DIR + file_name, 'rb')
            print('--------------------')
            print(file)
        except IOError:
            response_start_line = 'HTTP/1.1 404 not found\r\n'
            response_header = 'Server:My server\r\n'
            response_body = 'not found'
        else:
            file_data = file.read()
            print(file_data)
            file.close()

            # 返回指定报文
            response_start_line = 'HTTP/1.1 200 OK\r\n'
            response_header = 'Server:My server\r\n'
            response_body = file_data.decode('utf-8')
        response = response_start_line + response_header + '\r\n' + response_body
        print('response data:', response)
        cli_socket.send(bytes(response, 'utf-8'))
        cli_socket.close()

def main():
    httpserver = HttpServer()
    httpserver.bind(8000)
    httpserver.start()

if __name__ == '__main__':
    main()
