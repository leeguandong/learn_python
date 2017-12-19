# coding=utf-8

import scrapy
from myspider.items import ItcastItem
import sys

sys.path.insert(1, 'F:\Github\learn_python\Python爬虫\scrapy框架\scrapy框架和Spider类\myspider')

# 创建一个爬虫类
class ItcastSpider(scrapy.Spider):
    # 爬虫名
    name = 'itcast'
    # 允许爬虫作用的范围
    allowed_domains = ['http://www.itcast.cn/']
    # 爬虫起始的url
    start_urls = [
        "http://www.itcast.cn/channel/teacher.shtml#aandroid",
        "http://www.itcast.cn/channel/teacher.shtml#ac",
        "http://www.itcast.cn/channel/teacher.shtml#acloud",
        "http://www.itcast.cn/channel/teacher.shtml#aios",
        "http://www.itcast.cn/channel/teacher.shtml#ajavaee",
        "http://www.itcast.cn/channel/teacher.shtml#anetmarket",
        "http://www.itcast.cn/channel/teacher.shtml#aphp",
        "http://www.itcast.cn/channel/teacher.shtml#apython",
        "http://www.itcast.cn/channel/teacher.shtml#astack",
        "http://www.itcast.cn/channel/teacher.shtml#aui",
        "http://www.itcast.cn/channel/teacher.shtml#aweb"]

    def parse(self, response):
        # with open('teacher.html', 'w') as f:
        #     f.write(response.body)
        # 通过scrapy自带的xpath匹配出所有老师的根节点列表集合
        teacher_list = response.xpath('.//div[@class="li_text"]')

        # 所有老师信息的列表集合
        # teacherItem = []
        # 遍历根节点集合
        for each in teacher_list:
            # Item对象用来保存数据的
            item = ItcastItem()
            # name,extract() 将匹配出来的结果转换成unnicode字符串
            # 不加extract() 结果为xpath匹配对象
            name = each.xpath('./h3/text()').extract()
            # title
            title = each.xpath('./h4/text()').extract()
            # info
            info = each.xpath('./p/text()').extract()

            # item['name'] = name[0].encode("gbk")
            # item['title'] = title[0].encode("gbk")
            # item['info'] = info[0].encode("gbk")

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            # 每次运行到这里，就yeild一次数据出去给pipline处理
            yield item

            # teacherItem.append(item)

        # return teacherItem
