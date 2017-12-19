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


# # re模块正则表达式的函数用法
# import re
#
# str = 'abc123'
# re.match(str, 3, 5)
#
# # re.I忽略大小写，re.S全本匹配
# patten = re.compile(r'([a-z]+)([a-z]+)', re.I)
#
# m = patten.match('Hello world hello python')
# m.span()


# # 案例
# # 使用正则表达式爬内涵段子
# import urllib2
# import re
#
# class Spider():
#     def __init__(self):
#         '''下载页面'''
#         # 初始化起始位置
#         self.page = 2
#         # 爬取开关
#         self.switch = True
#
#     def loadPage(self):
#         '''处理每页的段子'''
#         print '正在下载'
#         url = 'http://www.neihan8.com/article/index_' + str(self.page) + '.html'
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
#         request = urllib2.Request(url, headers=headers)
#         response = urllib2.urlopen(request)
#
#         # 获取每页的HTML源码字符串
#         html = response.read()
#
#         # 创建正则表达式规则对象，匹配每页里的段子
#         patten = re.compile('<div\sclass="desc">(.*?)</div>', re.S)
#
#         # 将正则匹配对象应用到html源码字符串中，返回列表
#         content_list = patten.findall(html)
#
#         # 调用dealPage()处理段子中的不规则符号
#         self.dealPage(content_list)
#
#     def dealPage(self, content_list):
#         '''处理每页的段子'''
#         for item in content_list:
#             # item = item.replace(' ', '')
#             print item
#             self.writePage(item)
#
#     def writePage(self, item):
#         '''把每页的段子写入文件里'''
#         print '正在写入'
#         # a 表示在一个文档里面可以多次输入
#         with open('duanzi.txt', 'a') as f:
#             f.write(item)
#
#     def startWork(self):
#         '''控制爬虫的进度'''
#         # 循环执行，直到self.swith ==False
#         while self.switch:
#             self.loadPage()
#             command = raw_input('继续输入请按回车，结束输入请按quit')
#             if command == 'quit':
#                 self.switch = False
#             self.page += 1
#         print '谢谢使用'
#
# if __name__ == '__main__':
#     spider = Spider()
#     spider.startWork()


# 案例
# 贴吧图片下载案例
# 首先找贴吧网页，其次处理贴吧的页面，紧接着处理每一页贴吧，每一页贴吧上面有一条一条的信息，最后对每条信息进入其页面对其页面中的图片进行处理
import urllib
import urllib2
from lxml import etree

def loadPage(url):
    request = urllib2.Request(url)
    html = urllib2.urlopen(request).read()
    # 解析HTML文档为HTML DOM模型
    content = etree.HTML(html)
    # 返回所有匹配成功的列表集合
    link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')

    for link in link_list:
        fullurl = "http://tieba.baidu.com" + link
        # 组合为每个帖子的连接
        loadImage(fullurl)

# 取出每个帖子里的每个图片链接
def loadImage(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
    request = urllib2.Request(url, headers=headers)
    html = urllib2.urlopen(request).read()
    # 解析
    content = etree.HTML(html)
    # 取出帖子里每层主发送的图片连接集合
    link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    # 取出每个图片的连接
    for link in link_list:
        # print link
        wirteImage(link)

def wirteImage(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
    request = urllib2.Request(url, headers=headers)
    image = urllib2.urlopen(request).read()
    # 取出连接后10为为文件名
    filename = link[-10:]
    # 写入到本地磁盘文件内
    with open(filename, 'wb') as f:
        f.write(image)
    print "已经成功下载 " + filename

def tiebaSpider(url, beginPage, endPage):
    '''贴吧爬虫调度器，负责组合处理每个网页的url'''
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        # filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        # print fullurl
        loadPage(fullurl)
        print "谢谢使用"

if __name__ == '__main__':
    kw = raw_input("请输入需要爬取的贴吧名:")
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)
