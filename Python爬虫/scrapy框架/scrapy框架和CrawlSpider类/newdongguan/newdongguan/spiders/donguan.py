# # -*- coding: utf-8 -*-
# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
# from newdongguan.items import NewdongguanItem
#
# class DonguanSpider(CrawlSpider):
#     name = 'dongguan'
#     allowed_domains = ['wz.sun0769.com']
#     start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
#
#     rules = (
#         # 本案例的url被web服务器篡改，需要调用process_links来处理提取出来的url
#         # follow：是一个布尔(boolean)值，指定了根据该规则从response提取的链接是否需要跟进。 如果callback为None，follow 默认设置为True ，否则默认为False。
#         Rule(LinkExtractor(allow=r'type=4'), process_links='deal_links'),
#         Rule(LinkExtractor(allow=r'/question/\d+/\d+'), callback='parse_item')
#     )
#
#     # links 是当前response里提取出来的链接列表
#     def deal_links(self, links):
#         for each in links:
#             each.url = each.url.replace("?", "&").replace("Type&", "Type?")
#         return links
#
#     def parse_item(self, response):
#         item = NewdongguanItem()
#
#         item['title'] = response.xpath('//div[@class="greyframe"]//strong').extract()[0]
#         item['number'] = item['title'].split(' ')[-1].split(':')[-1]
#         item['content'] = response.xpath('//div[@class="contentext"]/text()').extract()
#         item['url'] = response.url
#
#         yield item

# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newdongguan.items import NewdongguanItem


class DongdongSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    # 每一页的匹配规则
    pagelink = LinkExtractor(allow=("type=4"))
    # 每一页里的每个帖子的匹配规则
    contentlink = LinkExtractor(allow=(r"/html/question/\d+/\d+.shtml"))

    rules = (
        # 本案例的url被web服务器篡改，需要调用process_links来处理提取出来的url
        # 第一个是没有callback的，所以默认的是True，是继续深挖的，这是对的，因为本来就想取链接里面的内容
        # 而第二个在具体投诉的页面本身是不需要深挖的，只需要拿到页面上我们想要的信息，腾讯招聘那个案例，本身页面上有想要的信息，但是页面本身又要往下跑
        Rule(pagelink, process_links = "deal_links"),
        Rule(contentlink, callback = "parse_item")
    )

    # links 是当前response里提取出来的链接列表
    def deal_links(self, links):
        for each in links:
            each.url = each.url.replace("?","&").replace("Type&","Type?")
        return links

    def parse_item(self, response):
        item = NewdongguanItem()
        # 标题
        item['title'] = response.xpath('//div[contains(@class, "pagecenter p3")]//strong/text()').extract()[0]
        # 编号
        item['number'] = item['title'].split(' ')[-1].split(":")[-1]
        # 内容，先使用有图片情况下的匹配规则，如果有内容，返回所有内容的列表集合
        content = response.xpath('//div[@class="contentext"]/text()').extract()
        # 如果没有内容，则返回空列表，则使用无图片情况下的匹配规则
        if len(content) == 0:
            content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
            item['content'] = "".join(content).strip()
        else:
            item['content'] = "".join(content).strip()
        # 链接
        item['url'] = response.url

        yield item

