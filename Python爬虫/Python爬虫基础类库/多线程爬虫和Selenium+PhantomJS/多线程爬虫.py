# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# from bs4 import BeautifulSoup
# import requests
# import time
#
# def captcha(captcha_data):
#     with open("captcha.jpg", "wb") as f:
#         f.write(captcha_data)
#     text = raw_input("请输入验证码：")
#     # 返回用户输入的验证码
#     return text
#
# def zhihuLogin():
#     # 构建一个Session对象，可以保存页面cookie
#     sess = requests.Session()
#
#     # 请求报头
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
#
#     # 首先获取登录页面，找到需要POST的数据(_xsrf),同时记录当前网页cookie值
#     html = sess.get('https://www.zhihu.com/#signin', headers=headers).text
#     # print html
#
#     # 调用lxml解析库
#     bs = BeautifulSoup(html, 'lxml')
#
#     # xsrf作用是防止CSRF攻击(跨站请求伪造)，通常叫跨域攻击，是一种利用网站对用户的一种信任来做坏事
#     # 跨域攻击通常会通过伪装成网站信任的用户的请求(利用cookie)，盗取用户信息、欺骗web服务器
#     # 所以网站会通过设置一个隐藏的字段来存放这个MD5字符串，这个字符串来校验用户cookie和服务器session的一种方式
#
#     # 找到name属性值为 _xsrf 的input标签，再取出value 的值
#     _xsrf = bs.find('input', attrs={'name': '_xsrf'}).get('value')
#
#     # 现在知乎已经不需要验证码输入了
#     # 根据UNIX 时间戳，匹配出验证码的url地址
#     captcha_url = "https://www.zhihu.com/captcha.gif?r=%d&type=login" % (time.time() * 1000)
#
#     # 发送图片的请求，获取图片数据流
#     captcha_data = sess.get(captcha_url, headers=headers).content
#
#     # 获取验证码里的文字，需要手动输入
#     text = captcha(captcha_data)
#
#     data = {
#         "_xsrf": _xsrf,
#         "email": "18788834071",
#         "password": "Tt2311472517",
#         "captcha": text
#     }
#
#     # 发送登录需要的POST数据，获取登陆后的Cookie(保存在session)
#     response = sess.post('https://www.zhihu.com/login/email', data=data, headers=headers)
#     print response.text
#
#     # 用已有的登录状态的cookie发送请求，获取目标页面源码
#     response = sess.get('https://www.zhihu.com/people/maozhaojun/activities', headers=headers)
#     with open('my.html', 'w') as f:
#         f.write(response.text.encode('utf-8'))
#
# if __name__ == '__main__':
#     zhihuLogin()

# !/usr/bin/env python
# -*- coding:utf-8 -*-

# from bs4 import BeautifulSoup
# import requests
# import time
#
# def captcha(captcha_data):
#     with open("captcha.jpg", "wb") as f:
#         f.write(captcha_data)
#     text = raw_input("请输入验证码：")
#     # 返回用户输入的验证码
#     return text
#
# def zhihuLogin():
#     # 构建一个Session对象，可以保存页面Cookie
#     sess = requests.Session()
#
#     # 请求报头
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
#
#     # 首先获取登录页面，找到需要POST的数据（_xsrf)，同时会记录当前网页的Cookie值
#     html = sess.get("https://www.zhihu.com/#signin", headers=headers).text
#     # 调用lxml解析库
#     bs = BeautifulSoup(html, "lxml")
#
#     # _xsrf 作用是防止CSRF攻击（跨站请求伪造)，通常叫跨域攻击，是一种利用网站对用户的一种信任机制来做坏事
#     # 跨域攻击通常通过伪装成网站信任的用户的请求(利用Cookie)，盗取用户信息、欺骗web服务器
#     # 所以网站会通过设置一个隐藏字段来存放这个MD5字符串，这个字符串用来校验用户Cookie和服务器Session的一种方式
#
#     # 找到name属性值为 _xsrf 的input标签，再取出value 的值
#     _xsrf = bs.find("input", attrs={"name": "_xsrf"}).get("value")
#
#     # 根据UNIX时间戳，匹配出验证码的URL地址
#     captcha_url = "https://www.zhihu.com/captcha.gif?r=%d&type=login" % (time.time() * 1000)
#     # 发送图片的请求，获取图片数据流，
#     captcha_data = sess.get(captcha_url, headers=headers).content
#     # 获取验证码里的文字，需要手动输入
#     text = captcha(captcha_data)
#
#     data = {
#         "_xsrf": _xsrf,
#         "email": "123636274@qq.com",
#         "password": "ALARMCHIME",
#         "captcha": text
#     }
#
#     # 发送登录需要的POST数据，获取登录后的Cookie(保存在sess里)
#     response = sess.post("https://www.zhihu.com/login/email", data=data, headers=headers)
#     print response.text
#
#     # 用已有登录状态的Cookie发送请求，获取目标页面源码
#     response = sess.get("https://www.zhihu.com/people/maozhaojun/activities", headers=headers)
#     with open("my.html", "w") as f:
#         f.write(response.text.encode("utf-8"))
#
# if __name__ == "__main__":
#     zhihuLogin()

# # 拉勾网城市json提取
# import urllib2
# # json解析库，对应lxml
# import json
# # json解析与法，对应xpath
# import jsonpath
#
# url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
#
# request = urllib2.Request(url, headers=headers)
# response = urllib2.urlopen(request)
# # 取出json文件里的内容，返回的格式是字符串
# html = response.read()
#
# # 取出json形式的字符串转换成python形式的unicode字符串
# unicoder = json.loads(html)
#
# # python形式的列表
# city_list = jsonpath.jsonpath(unicoder, '$..name')
#
# for city in city_list:
#     print city
#
# # dumps()默认中文为ascii码，禁用ascii编码格式，返回unicode字符串，方便实用
# array = json.dumps(city_list, ensure_ascii=False)
#
# with open('city.json', 'w') as f:
#     f.write(array.encode('utf-8'))

# # 糗事百科案例
# import urllib2
# import json
# from lxml import etree
#
# url = "http://www.qiushibaike.com/8hr/page/2/"
# headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
#
# requst = urllib2.Request(url, headers=headers)
# html = urllib2.urlopen(requst).read()
#
# # 相应返回的是字符串，解析成HTML DOM模式
# text = etree.HTML(html)
#
# # 返回所有段子的节点位置，contains()模糊查询方法，第一个参数是要匹配的标签，第二个参数是标签名部分内容
# node_list = text.xpath('//div[contains(@id,"qiushi_tag")]')
#
# item = {}
# for node in node_list:
#     # 用户名
#     username = node.xpath('./div//h2')[0].text
#
#     # 图片链接，属性直接对应值就不用text
#     image = node.xpath('.//div[@class="thumb"]//@src')
#
#     # 取出标签中的段子内容，text就是取出标签中内容
#     content = node.xpath('.//div[@class="content"]/span')[0].text
#
#     # 点赞
#     zan = node.xpath('.//i')[0].text
#
#     # 评论
#     comments = node.xpath('.//i')[1].text
#
#     items = {
#         "username": username,
#         "image": image,
#         "content": content,
#         "zan": zan,
#         "comments": comments
#     }
#
#     with open('qiushi.json', 'a') as f:
#         f.write(json.dumps(items, ensure_ascii=False).encode("utf-8") + "\n")

# # 使用多线程去爬取糗事百科
# # 使用线程库
# import threading
# # 队列
# from Queue import Queue
# # 解析库
# from lxml import etree
# # 请求处理
# import requests
# # json文件处理
# import json
# import time
#
# class ThreadCrawl(threading.Thread):
#     def __init__(self, threadName, pageQueue, dataQueue):
#         # 调用父类初始化方法,下面两种都可以，但第二种更好，在多参数时，不需要更改
#         # threading.Thread.__init__(self)
#         super(ThreadCrawl, self).__init__()
#         # 线程名
#         self.threadName = threadName
#         # 页码队列
#         self.pageQueue = pageQueue
#         # 数据队列
#         self.dataQueue = dataQueue
#         # 请求报头
#         self.headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
#
#     def run(self):
#         print '启动' + self.threadName
#         while not CRAWL_EXIT:
#             try:
#                 # 取出一个数字，先进先出
#                 # 可选参数block，默认值为True
#                 # 1. 如果对列为空，block为True的话，不会结束，会进入阻塞状态，直到队列有新的数据
#                 # 2. 如果队列为空，block为False的话，就弹出一个Queue.empty()异常，
#                 page = self.pageQueue.get(False)
#                 url = "http://www.qiushibaike.com/8hr/page/" + str(page) + "/"
#                 content = requests.get(url, headers=self.headers).text
#                 time.sleep(1)
#                 self.dataQueue.put(content)
#             except:
#                 pass
#         print '结束' + self.threadName
#
# class ThreadParse(threading.Thread):
#     def __init__(self,threadName,dataQueue,filename,lock):
#         super(ThreadParse,self).__init__()
#         # 线程名
#         self.threadName = threadName
#         # 数据队列
#         self.dataQueue = dataQueue
#         # 保存解析后的文件名
#         self.filename =filename
#         # 锁
#         self.lock = lock
#
#     def run(self):
#         print "启动" + self.threadName
#         while not PARSE_EXIT:
#             try:
#                html = self.dataQueue.get(False)
#                self.parse(html)
#             except:
#                 pass
#         print '退出' + self.threadName
#
#     def parse(self,html):
#         # 解析为HTML DOM
#         html = etree.HTML(html)
#
#         node_list = html.xpath('//div[contains(@id, "qiushi_tag")]')
#
#         for node in node_list:
#             # xpath返回的列表，这个列表就这一个参数，用索引方式取出来，用户名
#             username = node.xpath('./div/a/@title')[0]
#             # 图片连接
#             image = node.xpath('.//div[@class="thumb"]//@src')  # [0]
#             # 取出标签下的内容,段子内容
#             content = node.xpath('.//div[@class="content"]/span')[0].text
#             # 取出标签里包含的内容，点赞
#             zan = node.xpath('.//i')[0].text
#             # 评论
#             comments = node.xpath('.//i')[1].text
#
#             items = {
#                 "username": username,
#                 "image": image,
#                 "content": content,
#                 "zan": zan,
#                 "comments": comments
#             }
#
#             # with 后面有两个必须执行的操作：__enter__ 和 _exit__
#             # 不管里面的操作结果如何，都会执行打开、关闭
#             # 打开锁、处理内容、释放锁
#             with self.lock:
#                 # 写入存储的解析后的数据
#                 self.filename.write(json.dumps(items, ensure_ascii=False).encode("utf-8") + "\n")
#
#
# CRAWL_EXIT = False
# PARSE_EXIT = False
#
# def main():
#     # 页码的队列，表示10个页面
#     pageQueue = Queue(10)
#
#     # 放入1-10的数字，先进先出
#     for i in range(1, 11):
#         pageQueue.put(i)
#
#     # 采集结果(每页的HTML源码)的数据队列，参数为空表示不限制
#     dataQueue = Queue()
#
#     filename = open('duanzi.json', 'a')
#     # 创建锁
#     lock = threading.Lock()
#
#     # 三个采集线程的名字
#     crawlList = ['采集线程1号', '采集线程2号', '采集线程3号']
#
#     # 储存三个采集线程的列表集合
#     threadcrawl = []
#     for threadName in crawlList:
#         thread = ThreadCrawl(threadName, pageQueue, dataQueue)
#         thread.start()
#         threadcrawl.append(thread)
#
#     # 三个解析线程名字
#     parseList = ['解析线程1号', '解析线程2号', '解析线程3号']
#
#     # 存储三个采集线程
#     threadparse = []
#     for threadName in threadparse:
#         thread = ThreadParse(threadName, dataQueue, filename, lock)
#         thread.start()
#         threadparse.append(thread)
#
#     # 等待pageQueue队列为空，也就是等待之前的操作完毕,程序在这里不断运行的，不会结束
#     # 在确定页面队列为空后，会进入全局变量CRAWL_EXIT,然后终止循环
#     while not pageQueue.empty():
#         pass
#
#     # 守护线程，主线程结束，子线程就结束了
#     # 此处是非守护线程，主进程此处阻塞，等待子线程执行结束在结束
#     # 如果pageQueue队列为空，采集线程退出循环
#     global CRAWL_EXIT
#     CRAWL_EXIT = True
#
#     print 'pageQueue为空'
#
#     # 此处为阻塞
#     for thread in threadcrawl:
#         thread.join()
#         print '1'
#
#     # 判断数据队列
#     while not dataQueue.empty():
#         pass
#
#     global PARSE_EXIT
#     PARSE_EXIT = True
#
#     for thread in threadparse:
#         thread.join()
#         print '2'
#
#     with lock:
#         # 关闭文件
#         filename.close()
#     print '谢谢使用！'
#
# if __name__ == '__main__':
#     main()

# # 模拟登陆豆瓣网
# # 采用selenium  web自动化测试工具
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
# driver = webdriver.PhantomJS()
# driver.get('http://www/douban.com')
#
# # 输入账号密码
# driver.find_element_by_name('form_email').send_keys(' ')
# driver.find_element_by_name('from_password').send_keys(' ')
#
# # 模拟点击登录
# driver.find_element_by_xpath('//input[@class="bn-submit"]').click()
#
# # 等待3秒
# time.sleep(3)
#
# # 生成登录后快照
# driver.save_screenshot('douban.png')
#
# with open('douban.html', 'w') as file:
#     file.write(driver.page_source)
#
# driver.quit()

# # 斗鱼
# # 动态网页模拟点击
# # 测试化工具，就是用无界面浏览器，模拟其点击下一面不断获取页面上的信息并做一点处理，前提是网站是js形式的，就不需要抓包分析了，就直接模拟点击下一页就可以
# # 这里是有问题的，因为爬取每页上面都有四个页面是没有人数，这里一个房间号对应一个人数是不对的
# import unittest
# from selenium import webdriver
# from bs4 import BeautifulSoup as bs
#
# class douyu(unittest.TestCase):
#     # 初始化方法,必须是Setup()
#     def setUp(self):
#         self.driver = webdriver.PhantomJS()
#         self.num = 0
#         self.count = 0
#
#     # 测试化方法必须有test字样开头
#     def testDouyu(self):
#         self.driver.get('https://www.douyu.com/directory/all')
#
#         while True:
#             # bs中第一个参数拿到所有网页源码，第二参数解析库是lxml
#             soup = bs(self.driver.page_source, 'lxml')
#             # 房间名，返回列表
#             names = soup.find_all('h3', {'class': 'ellipsis'})
#             # 观众人数，返回列表
#             numbers = soup.find_all('span', {'class': 'dy-num fr'})
#             print type(numbers)
#
#             # zip(names,numners) 将name和number这两个列表组合起来
#             for name, number in zip(names, numbers):
#                 print u"观众人数：" + number.get_text().strip() + u'\t房间号：' + name.get_text().strip()
#                 self.num += 1
#
#             # 如果在页面源码里找到'下一页'为隐藏的标签，就退出标签,找不到会返回-1，不等于-1，说明找到了，直接跳出
#             if self.driver.page_source.find("shark-pager-disable-next") != -1:
#                 break
#
#             # 一直点击下一页
#             self.driver.find_element_by_class_name("shark-pager-next").click()
#
#     # 测试结束执行的方法
#     def tearDown(self):
#         # 退出PhantomJS()浏览器
#         print "当前网站直播人数" + str(self.num)
#         print "当前网站观众人数" + str(self.count)
#         self.driver.quit()
#
# if __name__ == '__main__':
#     # 启动测试模块
#     unittest.main()

# 利用机器学习库来进行验证码识别，准确率不高
# 这个pytesseract库是要自己安装的，我并没有安装这个库，所以下面这段代码不能运行的
from bs4 import BeautifulSoup
import requests
import time

from pytesseract import *
from PIL import Image

def captcha(captcha_data):
    with open("captcha.jpg", "wb") as f:
        f.write(captcha_data)
    image = Image.open('captcha.jpg')
    text = image_to_string(image)
    print '机器学习识别后的验证码为：' + text
    command = raw_input('输入Y表示验证正确，同意使用(输入键自行输入)')
    if (command == 'Y' or command == 'y'):
        return text
    else:
        return raw_input('请输入验证码')

def zhihuLogin():
    # 构建一个Session对象，可以保存页面Cookie
    sess = requests.Session()

    # 请求报头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    # 首先获取登录页面，找到需要POST的数据（_xsrf)，同时会记录当前网页的Cookie值
    html = sess.get("https://www.zhihu.com/#signin", headers=headers).text
    # 调用lxml解析库
    bs = BeautifulSoup(html, "lxml")

    # _xsrf 作用是防止CSRF攻击（跨站请求伪造)，通常叫跨域攻击，是一种利用网站对用户的一种信任机制来做坏事
    # 跨域攻击通常通过伪装成网站信任的用户的请求(利用Cookie)，盗取用户信息、欺骗web服务器
    # 所以网站会通过设置一个隐藏字段来存放这个MD5字符串，这个字符串用来校验用户Cookie和服务器Session的一种方式

    # 找到name属性值为 _xsrf 的input标签，再取出value 的值
    _xsrf = bs.find("input", attrs={"name": "_xsrf"}).get("value")

    # 根据UNIX时间戳，匹配出验证码的URL地址
    captcha_url = "https://www.zhihu.com/captcha.gif?r=%d&type=login" % (time.time() * 1000)
    # 发送图片的请求，获取图片数据流，
    captcha_data = sess.get(captcha_url, headers=headers).content
    # 获取验证码里的文字，需要手动输入
    text = captcha(captcha_data)

    data = {
        "_xsrf": _xsrf,
        "email": "123636274@qq.com",
        "password": "ALARMCHIME",
        "captcha": text
    }

    # 发送登录需要的POST数据，获取登录后的Cookie(保存在sess里)
    response = sess.post("https://www.zhihu.com/login/email", data=data, headers=headers)
    # print response.text

    # 用已有登录状态的Cookie发送请求，获取目标页面源码
    response = sess.get("https://www.zhihu.com/people/maozhaojun/activities", headers=headers)
    with open("my.html", "w") as f:
        f.write(response.text.encode("utf-8"))

if __name__ == "__main__":
    zhihuLogin()
