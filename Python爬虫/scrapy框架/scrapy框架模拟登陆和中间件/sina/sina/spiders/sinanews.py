# -*- coding: utf-8 -*-
from sina.items import SinaItem
import scrapy
import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

class SinanewsSpider(scrapy.Spider):
    name = 'sinanews'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        items = []

        # 所有大类的url和标题
        parentUrls = response.xpath('//div[@class="clearfix"]/h3/a/@href').extract()
        parentTitle = response.xpath('//div[@class="clearfix"]/h3/a/text()').extract()

        # 所有小类的url和标题
        subUrls = response.xpath('//div[@class="clearfix"]/ul/li/a/@href').extract()
        subTitle = response.xpath('//div[@class="clearfix"]/ul/li/a/text()').extract()

        # 爬取所有大类
        for i in range(0, len(parentTitle)):
            # 指定大类目录的路径和目录名
            parentFilename = './Data/' + parentTitle[i]

            # 如果目录不存在，则创建目录
            if (not os.path.exists(parentFilename)):
                os.makedirs(parentFilename)

            # 爬取所有小类
            for j in range(0, len(subUrls)):
                item = SinaItem()

                # 保存大类的title和urls
                item['parentTitle'] = parentTitle[i]
                item['parentUrls'] = parentUrls[i]

                # 检查小类的url是否以同类别大类url开头，如果是返回True (sports.sina.com.cn 和 sports.sina.com.cn/nba)
                if_belong = subUrls[j].startswith(item['parentUrls'])

                # 如果是属于本大类，将存储目录放到本大类目录下
                if (if_belong):
                    subFilename = parentFilename + '/' + subTitle[j]
                    # 如果目录不存在，则创建目录
                    if (not os.path.exists(subFilename)):
                        os.makedirs(subFilename)

                    # 存储小类url、title和filename字段数据
                    item['subUrls'] = subUrls[j]
                    item['subTitle'] = subTitle[j]
                    item['subFilename'] = subFilename

                    items.append(item)

        # 发送每个小类url的Request请求，得到Response连同包含meta数据一同交给回调函数second_parse方法处理
        for item in items:
            yield scrapy.Request(url=item['subUrls'], meta={'meta_1': item}, callback=self.second_parse)

    # 对于返回的小类的url，在进行递归请求
    def second_parse(self, response):
        # 提取每次的Response的meta数据
        meta_1 = response.meta['meta_1']

        # 取出小类里所有的子链接
        sonUrls = response.xpath('//div[@class="blk12"]//a/@href').extract()
        sonUrls1 = response.xpath('//div[@class="blk2"]//a/@href').extract()
        sonUrls = sonUrls + sonUrls1

        items = []
        for i in range(0, len(sonUrls)):
            # 检查每个链接是否以大类url开头，以shtml结尾，如果是赶回True
            if_belong = sonUrls[i].endswith('.shtml') and sonUrls[i].startswith(meta_1['parentUrls'])

            # 如果属于本大类，获取字段值放在同一个item下便于传输
            if (if_belong):
                item = SinaItem()
                item['parentTitle'] = meta_1['parentTitle']
                item['parentUrls'] = meta_1['parentUrls']
                item['subUrls'] = meta_1['subUrls']
                item['subTitle'] = meta_1['subTitle']
                item['subFilename'] = meta_1['subFilename']
                item['sonUrls'] = sonUrls[i]
                items.append(item)

        # 发送每个小类下子链接url的Request请求，得到Response后连同包含meta数据一同交给回调函数detail_parse方法处理
        for item in items:
            yield scrapy.Request(url=item['sonUrls'], meta={'meta_2': item}, callback=self.detail_parse)

    # 数据解析方法，获取文章标题和内容
    def detail_parse(self, response):
        item = response.meta['meta_2']
        content = ''
        head = response.xpath('//h1[@class="main-title"]/text()')
        content = response.xpath('//div[@class="article"]/p/text()').extract()
        if len(content) != 0:
            content = content[0]
        else:
            content = content

        # 将p标签里的文本内容合并在一起
        for content_one in content:
            content += content_one

        item['head'] = head
        item['content'] = content

        yield item
