# -*- coding: utf-8 -*-
import scrapy

# 实在没办法了，可以用这种方法模拟登陆，麻烦一点，但是成功率很高

class RenrenSpider(scrapy.Spider):
    name = 'renren2'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/xxxxx',
                  'http://www.renren.com/11111',
                  'http://www.renren.com/xx', ]

    cookies = {
        "anonymid": "ixrna3fysufnwv",
        "_r01_": "1",
        "ap": "327550029",
        "JSESSIONID": "abciwg61A_RvtaRS3GjOv",
        "depovince": "GW",
        "springskin": "set",
        "jebe_key": "f6fb270b-d06d-42e6-8b53-e67c3156aa7e%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1484060607478%7C1%7C1486198628950",
        "jebe_key": "f6fb270b-d06d-42e6-8b53-e67c3156aa7e%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1484060607478%7C1%7C1486198619601",
        "ver": "7.0",
        "XNESSESSIONID": "e703b11f8809",
        "jebecookies": "98c7c881-779f-4da8-a57c-7464175cd469|||||",
        "ick_login": "4b4a254a-9f25-4d4a-b686-a41fda73e173",
        "_de": "BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5",
        "p": "ea5541736f993365a23d04c0946c10e29",
        "first_login_flag": "1",
        "ln_uact": "mr_mao_hacker@163.com",
        "ln_hurl": "http://hdn.xnimg.cn/photos/hdn521/20140529/1055/h_main_9A3Z_e0c300019f6a195a.jpg",
        "t": "691808127750a83d33704a565d8340ae9",
        "societyguester": "691808127750a83d33704a565d8340ae9",
        "id": "327550029",
        "xnsid": "f42b25cf",
        "loginfrom": "syshome"
    }

    def start_requests(self):
        for url in self.start_urls:
            # yield scrapy.Request(url, callback = self.parse)
            # url = "http://www.renren.com/410043129/profile"
            yield scrapy.FormRequest(url, cookies=self.cookies, callback=self.parse_page)

    def parse_page(self, response):
        print "===========" + response.url
        with open("deng.html", "w") as filename:
            filename.write(response.body)
