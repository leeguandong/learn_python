from socket import *
from multiprocessing import Process
import re
import sys

# 设置静态文件根目录
HTML_ROOT_DIR = './html'

class HttpServer():
    def __init__(self, application):
        self.app = application
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
        method = re.match(r"(\w+) +/[^ ]* ", request_start_line.decode("utf-8")).group(1)

        env = {
            "PATH_INFO": file_name,
            "METHOD": method
        }
        response_body = self.app(env, self.start_response)

        response = self.response_headers + "\r\n" + response_body

        cli_socket.send(bytes(response, 'utf-8'))
        cli_socket.close()

def main():
    sys.path.insert(1,'/web服务器框架')
    if len(sys.argv) < 2:
        sys.exit("python MyWebServer.py Module:app")
    # python Mywebserver.py Mywebframework:app
    moudle_name, app_name = sys.argv[1].split(':')
    m = __import__(moudle_name)
    app = getattr(m, app_name)
    httpserver = HttpServer(app)
    httpserver.bind(8000)
    httpserver.start()

if __name__ == '__main__':
    main()
