# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem

class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        # 不写回调函数，默认follow为True，就是继续深挖链接里面的内容
        Rule(LinkExtractor(r'type=4&page=\d+')),
        # follow为False，可以不写了
        Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'), callback='parse_item'),
    )

    def parse_item(self, response):
        item = DongguanItem()
        item['title'] = response.xpath('//div[@class="greyframe"]//strong/text()').extract()[0]
        item['number'] = item['title'].split(' ')[-1].split(':')[-1]
        item['content'] = response.xpath('//div[@class="contentext"]/text()').extract()[0]
        item['url'] = response.url

        yield item
