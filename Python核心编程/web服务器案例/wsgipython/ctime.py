# 这个程序与用户的需求有关，改程序在服务器中被调用
# 这个程序必须有一个返回值，作为响应体返回给请求方，如果是time.ctime，那么在浏览器中就显示当时的时间
# 但是这个程序是与用户的需求相关的，既然是动态页面，那么用户是可以在请求中添加请求信息的，这些请求信息被env收录在dict中，我们可以通过env
# 来获取这些特定的请求信息，然后执行相关请求操作。
# 在获取数据，执行请求之后，程序要得到响应头，通过传进来的第二个参数start_response，实际上是一个函数在服务器中执行，拼接了返回的报文，仅仅是执行
# 报文的拼接这一任务。有了响应头，和返回的响应体，这部分就完整了。
import time

def application(env, start_response):
    # 通过env获取请求数据

    # 执行相应请求

    # 响应头
    status = '200 ok'
    headers = {
        ('Content-Type', 'text/html')
    }

    start_response(status, headers)
    return time.ctime()
