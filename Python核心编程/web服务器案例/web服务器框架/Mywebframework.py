# 框架
import time
# from Mywebserver import Httpserver

HTML_ROOT_DIR = './html'

class Application():
    def __init__(self, urls):
        # 设置路由信息
        self.urls = urls

    def __call__(self, env, start_response):
        # get方式如果不存在，'/'默认直接去主页，[]形式去找，如果出错，则返回错误
        path = env.get('PATH_INFO', '/')
        # 静态网页  都是以/static开始的
        if path.startwith('/static'):
            # 要访问的静态文件
            file_name = path[7:]
            try:
                file = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                # 代表未找到路由信息，404错误
                status = "404 Not Found"
                headers = []
                start_response(status, headers)
                return "not found"
            else:
                file_data = file.read()
                file.close()

                status = "200 OK"
                headers = []
                start_response(status, headers)
                return file_data.decode("utf-8")

        for url, handler in self.urls:
            if path == url:
                return handler(env, start_response)

        # 未找到路由，返回404
        status = '404 Not Found'
        header = []
        start_response(status, header)
        return 'not found'

def show_ctime(env, start_response):
    status = '200 ok'
    headers = {
        ('Content-Type', 'text/html')
    }
    start_response(status, headers)
    return time.ctime()

def sayhello(env, start_response):
    status = '200 ok'
    headers = {
        ('Content-Type', 'text/html')
    }
    start_response(status, headers)
    return 'hello world'

# 此处存储路由信息，对于开发者而言，他不需要知道Application的实现细节，他只需要知道自己需要添加什么信息即可
urls = {
    ('/ctime', show_ctime),
    ('/sayhello', sayhello)
}

app = Application(urls)

# def main():
#     App = Application(urls)
#     httpserver = Httpserver(App)
#     httpserver.bind(8000)
#     httpserver.start()
#
# if __name__ == '__main__':
#     main()
