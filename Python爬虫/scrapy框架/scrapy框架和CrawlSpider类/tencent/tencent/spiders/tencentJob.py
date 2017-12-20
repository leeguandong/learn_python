# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent.items import TencentItem

class TencentSpider(CrawlSpider):
    name = 'tencent'
    # 指定爬虫爬取范围，不需要写http，这个是域
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    # Response里连接的提取规则，返回的符合匹配规则的连接匹配对象链表
    pagelink = LinkExtractor(allow=('start=\d+'))
    print pagelink

    rules = (
        # 获取这个列表里的连接，一次发送请求，并且继续跟进，调用指定回调函数处理
        # 可以写多个rule进行连接提取，follow这个参数表示是否深度提取，就是点击进入链接之后爬取，这个由于不断点击下一页中去获取该页item，所以
        # 是需要深度提取的
        Rule(pagelink, callback='parseTencent', follow=True),
    )

    # 这种方法不需要再给url手动进行赋值，而是设定一定的规则，在提取的连接中匹配对象，凡是满足规则的，就加入到Resquest队列里面，在调度器中
    # 有自动的去重等操作，所以不需要担心队列里面url的重复问题
    def parseTencent(self, response):
        # evenlist = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        # oddlist = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        # fulllist = evenlist + oddlist
        # for each in fulllist:
        for each in response.xpath('//tr[@class="even"]|//tr[@class="odd"]'):
            item = TencentItem()
            # 职位名称
            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item
