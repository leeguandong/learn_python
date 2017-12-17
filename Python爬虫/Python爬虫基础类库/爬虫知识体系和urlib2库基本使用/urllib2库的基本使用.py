# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# import urllib2
#
# ua_header = {
#     'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
# }
#
# # 通过urllib2.Request()方法构造一个请求对象
# request = urllib2.Request('http://www.baidu.com/', headers=ua_header)
#
# # 向指定的url地址发送请求，并返回服务器相应的类文件对象
# response = urllib2.urlopen(request)
#
# # 服务器返回的类文件对象支持python对象的操作方法
# # read()方法就是读取文件里的全部内容，返回字符串
# html = response.read()
#
# # 返回HTTP的响应码，成功返回200,4服务器页面出错，5服务器问题
# print response.getcode()
#
# # 返回实际数据的实际URL，防止重定向问题
# print response.geturl()
#
# # 返回服务器响应的HTTP报头
# print response.info()
#
# # 打印响应内容
# # print html


# # coding=utf-8
# # 为了防止反爬虫做的优化
# import urllib2
# import random
#
# # 可以是User-Agent列表，也可以是代理列表
# ua_list = [
#     ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
#     "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
#     "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11"
# ]
#
# # 在User-Agent列表里随机选择一个User-Agent
# user_agent = random.choice(ua_list)
#
# # 通过urllib2.Request()方法构造一个请求对象
# request = urllib2.Request('http://www.baidu.com/')
#
# # add_header()方法，添加/修改一个HTTP的报头
# request.add_header('User-Agent', user_agent)
#
# # get_header()获取一个已有的HTTP报头的值，注意只是第一个字母大写，其他均小写
# print request.get_header('User-agent')
#
# # 向指定的url地址发送请求，并返回服务器相应的类文件对象
# response = urllib2.urlopen(request)
#
# # 服务器返回的类文件对象支持python对象的操作方法
# # read()方法就是读取文件里的全部内容，返回字符串
# html = response.read()
#
# # 返回HTTP的响应码，成功返回200,4服务器页面出错，5服务器问题
# print response.getcode()
#
# # 返回实际数据的实际URL，防止重定向问题
# print response.geturl()
#
# # 返回服务器响应的HTTP报头
# print response.info()
#
# # 打印响应内容
# # print html

# # get方法组合url
# import urllib
# import urllib2
#
# url = 'http://www.baidu.com/s'
# headers = {'User-Agent': 'Mozilla...'}
#
# keyword = raw_input('请输入需要查询的关键字')
#
# # 组合中有汉字要解码，使用urlencode()方法，其参数是一个字典
# wd = {'wd': keyword}
# wd = urllib.urlencode(wd)
#
# # 组合url
# fullurl = url + '?' + wd
# print fullurl
#
# # 发送一个请求
# request = urllib2.Request(fullurl, headers=headers)
# response = urllib2.urlopen(request)
#
# print response.read()

# # 贴吧爬取案例
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf8')
#
# import urllib2
# import urllib
#
# # 一个page对应一个renturn
# def loadPage(url, filename):
#     """
#         作用：根据url发送请求，获取服务器响应文件
#         url: 需要爬取的url地址
#         filename : 处理的文件名
#     """
#     print '正在下载' + filename
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
#     request = urllib2.Request(url, headers=headers)
#     response = urllib2.urlopen(request)
#     return response.read()
#
# # 这边打开一个filename写出来
# def writePage(html, filename):
#     """
#         作用：将html内容写入到本地
#         html：服务器相应文件内容
#     """
#     print "正在保存 " + filename
#     # 文件写入
#     with open(filename, "w") as f:
#         f.write(html)
#     print "-" * 30
#
# def tiebaSpider(url, beginPage, endPage):
#     """
#         作用：贴吧爬虫调度器，负责组合处理每个页面的url
#         url : 贴吧url的前部分
#         beginPage : 起始页
#         endPage : 结束页
#     """
#     for page in range(beginPage, endPage + 1):
#         pn = (page - 1) * 50
#         filename = '第' + str(page) + '页.html'
#         filename = filename.decode('utf-8')
#         fullurl = url + '&pn=' + str(pn)
#         print fullurl
#
#         html = loadPage(fullurl, filename)
#         # print html
#         writePage(html, filename)
#
# if __name__ == '__main__':
#     kw = raw_input('请输入需要查询的关键字')
#     beginPage = int(raw_input('请输入开始页面'))
#     endPage = int(raw_input('请输入结束页面'))
#
#     key = urllib.urlencode({'kw': kw})
#     url = 'http://tieba.baidu.com/f?'
#     fullurl = url + key
#
#     tiebaSpider(fullurl, beginPage, endPage)

# # 有道词典的api调用  使用post方式
# import urllib2
# import urllib
#
# # 通过抓包的方式获取的url，并不是浏览上显示的url
# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
#
# # 完整的headers
# headers = {
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'X-Requested-With': 'XMLHttpRequest',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Accept-Language': 'zh-CN,zh;q=0.8'
# }
#
# # 用户接口输入
# key = raw_input('请输入需要查询的词')
#
# # 发送到web服务器的表单数据
# formdata = {
#     'i': key,
#     'from': 'AUTO',
#     'to': 'AUTO',
#     'doctype': 'json',
#     'version': '2.1',
#     'keyfrom': 'fanyi.web',
#     'action': 'FY_BY_REALTIME',
#     'typoResult': 'true',
# }
#
# # 经过urlencode转码
# data = urllib.urlencode(formdata)
#
# # 如果Request()方法里的data参数有值，那么这个请求就是POST
# # 如果没有，就是Get
# request = urllib2.Request(url, data, headers=headers)
# print urllib2.urlopen(request).read()

# # 动态Ajax下载豆瓣页面
# import urllib
# import urllib2
#
# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"
#
# headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
#
# formdata = {
#         "start":"0",
#         "limit":"20"
#     }
#
# data = urllib.urlencode(formdata)
#
# request = urllib2.Request(url, data = data, headers = headers)
#
# print urllib2.urlopen(request).read()

# 利用已有的cookie数据模拟登陆
# import urllib2
#
# url = 'https://weibo.com/u/2903702617/home?wvr=5'
#
# headers = {
#     'Host': 'www.weibo.com',
#     'Connection': 'keep-alive',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#     'Accept': '*/*',
#     'Referer': 'https://weibo.com/2903702617/profile?rightmod=1&wvr=6&mod=personinfo&is_all=1',
#     'Accept-Language': 'zh-CN,zh;q=0.8',
#     'Cookie': 'SINAGLOBAL=4898999002003.896.1493286473499; Hm_lvt_407473d433e871de861cf818aa1405a1=1493550953,1495866525; UM_distinctid=15d017deeca38-076aabc60e760d-4e47052e-144000-15d017deecb397; UOR=lbsyun.baidu.com,widget.weibo.com,news.ifeng.com; _s_tentry=-; Apache=3355183685824.4053.1513331274441; ULV=1513331274515:66:3:2:3355183685824.4053.1513331274441:1513329778911; SCF=AhAEX2Jt7tcq0ziiWH71lsmp4HdJhmqoRAnyfF1jmp1mWbtMl0HXCXrSu6nYVHhYtQCfX16l_mnyg-5XT-BDe6c.; SUB=_2A253N-wmDeRhGeRH61EW8CzKyjuIHXVURVrurDV8PUNbmtBeLUn2kW9NTa16RY4c17jPIe-Zh5NABcmBPABEczIo; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W51sIyEX2_8CMB9OkYILWgJ5JpX5K2hUgL.Foz4eheNehzceKM2dJLoIEBLxKqL1--L1-eLxKBLBonL12BLxKnLBKnL1h5LxKBLBonLB-Bt; SUHB=04Wugvvs45jLJz; ALF=1513936738; SSOLoginState=1513331830; un=18788834071',
# }
#
# request = urllib2.Request(url,headers=headers)
# print urllib2.urlopen(request).read()

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2

url = "http://www.renren.com/410043129/profile"

headers = {
    "Host" : "www.renren.com",
    "Connection" : "keep-alive",
    #"Upgrade-Insecure-Requests" : "1",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer" : "http://www.renren.com/SysHome.do",
    #"Accept-Encoding" : "gzip, deflate, sdch",
    "Cookie" : "anonymid=ixrna3fysufnwv; _r01_=1; depovince=GW; jebe_key=f6fb270b-d06d-42e6-8b53-e67c3156aa7e%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1484060607478%7C1%7C1484400895379; jebe_key=f6fb270b-d06d-42e6-8b53-e67c3156aa7e%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1484060607478%7C1%7C1484400890914; JSESSIONID=abcX8s_OqSGsYeRg5vHMv; jebecookies=0c5f9b0d-03d8-4e6a-b7a9-3845d04a9870|||||; ick_login=8a429d6c-78b4-4e79-8fd5-33323cd9e2bc; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=0cedb18d0982741d12ffc9a0d93670e09; ap=327550029; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20140529/1055/h_main_9A3Z_e0c300019f6a195a.jpg; t=56c0c522b5b068fdee708aeb1056ee819; societyguester=56c0c522b5b068fdee708aeb1056ee819; id=327550029; xnsid=5ea75bd6; loginfrom=syshome",
    "Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6",
}

request = urllib2.Request(url, headers = headers)

response = urllib2.urlopen(request)

print response.read()