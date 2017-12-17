# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 简单的Handler构建urlopen()方法
# import urllib2
#
# # 在HTTPHandler增加参数'debuglevel=1'将会自动打开Debug log模式
# # 程序在执行的时候会打印收发包的信息
# http_handler = urllib2.HTTPHandler(debuglevel=1)
#
# # # 构建一个HTTPHandler处理器对象，支持处理HTTP的请求
# # http_handler = urllib2.HTTPHandler()
#
# # 调用build_opener()方法构建一个自定义的opener对象，参数就是构建的处理器对象
# opener = urllib2.build_opener(http_handler)
#
# request = urllib2.Request('HTTP://www.baidu.com/')
#
# response = opener.open(request)
#
# print response.read()

# # 代理
# # 不过在西刺上的免费代理好像不能用,很多人用，不稳定
#
# import urllib2
#
# # 代理开关,表示是否启用代理
# proxyswitch = False
#
# # 构建一个Handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器IP+PROT
# httpproxy_handler = urllib2.ProxyHandler({'http': '119.39.68.73:808	'})
#
# # # 如果不是免费的代理，而是私密代理的话，就要加上账号和密码
# # uthproxy_handler = urllib2.ProxyHandler({"http" : "mr_mao_hacker:sffqry9r@114.215.104.49:16816"})
#
# # 构建了一个没有代理的处理器对象,也要传一个空字典类型
# nullproxy_handler = urllib2.ProxyHandler({})
#
# if proxyswitch:
#     opener = urllib2.build_opener(httpproxy_handler)
# else:
#     opener = urllib2.build_opener(nullproxy_handler)
#
# # 构建一个全局的opener，之后所有的请求都可以用urlopen()方法去发送，也附带Handler的功能
# # 如果这个opener只是用一次，那就不需要用全局的opener，反复用就创建一个opener
# urllib2.install_opener(opener)
#
# request = urllib2.Request('http://www.baidu.com/')
# response = urllib2.urlopen(request)
#
# # 使用代理的话要接一下码，不使用就不用解码了
# # print response.read().decode('gbk')
#
# print response.read()

# # 授权代理处理器和验证web客户端的授权处理器
# import urllib2
#
# test = 'test'
# password = '123456'
# webserver = '192.168.21.52'
#
# # 构建一个密码管理对象，可以用来保存和HTTP请求相关的授权账户信息
# passwordMgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
#
# # 添加授权账户信息，第一个采纳数realm(域)如果没有指定就写None，后三个参数分别是站点IP，账户和密码
# passwordMgr.add_password(None, webserver, test, password)
#
# # HTTPBasicAuthHandler() HTTP基础验证处理器类  验证web客户端的授权处理器
# httpauth_handler = urllib2.HTTPBasicAuthHandler(passwordMgr)
#
# # 处理授权代理服务器
# proxyauth_handler = urllib2.ProxyBasicAuthHandler(passwordMgr)
#
# # 构建自定义的opener
# opener = urllib2.build_opener(httpauth_handler, proxyauth_handler)
# urllib2.install_opener(opener)
#
# request = urllib2.Request('http://' + webserver + '/')
#
# # 用来授权验证信息
# response = opener.open(request)
#
# # # 没有授权验证信息
# # response = urllib2.urlopen(request)

# # 模拟登陆
# # post方式，初次登录记录cookie，然后通过其他链接获取数据
# import urllib2
# import cookielib
# import urllib
#
# # 通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
# cookie = cookielib.CookieJar()
#
# # 通过HTTPCookieProcessor()处理器构建一个处理器对象，用来处理cookie
# # 参数就是构建CookieJar()对象
# cookie_handler = urllib2.HTTPCookieProcessor(cookie)
#
# # 构建一个自定义的opener
# opener = urllib2.build_opener(cookie_handler)
#
# # 通过自定义opener的addheaders的参数，可以添加HTTP报头参数
# opener.addheaders = [('User-Agent',
#                       'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')]
#
# # renren网站的登录接口
# url = 'http://www.renren.com/PLogin.do'
#
# # 需要登录的账户密码
# data = {'email': '18788834071', 'password': '123456'}
#
# # 通过urlencode()编码转换
# data = urllib.urlencode(data)
#
# request = urllib2.Request(url, data=data)
# response = opener.open(request)
# # print response.read()
#
# # 通过cookie去获取其他链接
# response_peng = opener.open('http://www.renren.com/880151247/profile')
#
# print response_peng.read()

# re模块正则表达式的函数用法
import re

str = 'abc123'
re.match(str, 3, 5)

# re.I忽略大小写，re.S全本匹配
patten = re.compile(r'([a-z]+)([a-z]+)', re.I)

patten.match('Hello world hello python')
