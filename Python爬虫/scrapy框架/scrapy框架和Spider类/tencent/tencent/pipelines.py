# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentPipeline(object):
    def __init__(self):
        self.filename = open('tencent.json', 'w')

    def process_item(self, item, spider):
        # ensure_ascii=False 传输数据中有中文，要禁用这个，因为该模式默认数据被转成ascii码，转成unicode更具有通用性，python3就是unicode编码
        text = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.filename.write(text.encode('utf-8'))
        return item

    def close_spider(self, spider):
        self.filename.close()
