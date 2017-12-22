# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    offset = 0
    start_urls = ['https://movie.douban.com/top250?start=']
    url = [start_urls + offset]

    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath('//div[@class="info"]')

        for each in movies:
            # 标题：
            item['title'] = each.xpath('.// span[@ class ="title"][1] / text()').extract()[0]
            # 信息：
            item['bd'] = each.xpath('.// div[@ class ="bd"] / p / text()').extract()[0]
            # 评分：
            item['star'] = each.xpath('// div[@ class ="star"] / span[@ class ="rating_num"] / text()').extract()[0]
            # 简介：
            quote = each.xpath('// span[@ class ="inq"] / text()').extract()
            if len(quote) != 0:
                item['quote'] = quote[0]
            yield item

            if self.offset < 250:
                self.offset += 25
                yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
