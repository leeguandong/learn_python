# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']

    url = "http://hr.tencent.com/position.php?&start="
    offset = 0

    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            # 初始化模型对象
            item = TencentItem()
            # print item    是个 {}

            # 职位名称
            item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['positionLink'] = each.xpath('./td[1]/a/@href').extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()
            # 招聘人数
            item['peopleNum'] = each.xpath('./td[3]/text()').extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath('./td[4]/text()').extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            # yield很重要，他是爬虫和后端管道数据处理的桥梁，每处理就返回信息
            yield item
        if self.offset < 2623:
            self.offset += 10

        # 每处理完一页数据之后，重新发送下一页页面请求
        # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
