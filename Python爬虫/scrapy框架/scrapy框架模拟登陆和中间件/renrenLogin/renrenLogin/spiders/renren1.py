# -*- coding: utf-8 -*-
import scrapy

# 只要是需要提供post数据的，就可以用这种方法，
# 下面示例: post数据是账号密码

class RenrenSpider(scrapy.Spider):
    name = 'renren1'
    allowed_domains = ['renren.com']

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        yield scrapy.FormRequest(
            url=url,
            formdata={'email': '18788834071', 'password': '123456'},
            callback=self.parse_page
        )

    def parse_page(self, response):
        with open('uu.html', 'w') as filename:
            filename.write(response.body)
