# 动态文件web服务器
# 目的是让服务器运行python脚本，让运行结果返回
from socket import *
from multiprocessing import Process
import re
import sys

WSGI_PYTHON_DIR = "./wsgipython"

# 设置静态文件根目录
HTML_ROOT_DIR = './html'

class HttpServer():
    def __init__(self):
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

    def start_response(self, status, headers):
        response_header = 'HTTP/1.1' + status + '\r\n'
        for header in headers:
            response_header += '%s:%s\r\n' % header
        self.response_header = response_header

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

        if file_name.endswith('.py'):
            try:
                m = __import__(file_name[1:-3])
            except Exception:
                response_header = 'HTTP/1.1 404 Not found\r\n'
                response_body = 'not found'
            else:
                # env是在请求报文中的相关数据时产生的
                env = {}
                response_body = m.application(env, self.start_response)
            response = self.response_header + '\r\n' + response_body
        else:
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
    sys.path.insert(1, WSGI_PYTHON_DIR)
    httpserver = HttpServer()
    httpserver.bind(8000)
    httpserver.start()

if __name__ == '__main__':
    main()
