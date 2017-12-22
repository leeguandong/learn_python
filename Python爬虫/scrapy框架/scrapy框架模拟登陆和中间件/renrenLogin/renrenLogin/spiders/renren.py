# -*- coding: utf-8 -*-
import scrapy

# 正统模拟登陆方法：
# 首先发送登录页面的get的请求，获取到页面里的登录必须的参数，比如说zhihu的——xsrf
# 然后和账号密码一起post到服务器，登录成功

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    # 这个url是个列表，如果你写元组的话，就别忘了加个逗号
    start_urls = ["http://www.renren.com/PLogin.do"]

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formdata={'email': '18788834071', 'password': '123456'},
            callback=self.parse_page
        )

    def parse_page(self, response):
        print '=====1=====' + response.url
        url = 'http://www.renren.com/422167102/profile'
        yield scrapy.Request(url, callback=self.parse_newpage)

    def parse_newpage(self, response):
        print '=======2=====' + response.url
        with open('newuser.html', 'w') as filename:
            filename.write(response.body)
