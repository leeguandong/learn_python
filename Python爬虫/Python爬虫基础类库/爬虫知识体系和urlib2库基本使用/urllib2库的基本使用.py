# coding=utf-8

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


