# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import sys

reload(sys)
sys.setdefaultencoding("utf-8")

class SinaPipeline(object):
    def process_item(self, item, spider):
        sonUrls = item['sonUrls']

        # 文件名为子链接url中间部分，并将 / 替换为 _,保存为 .txt格式,防止转义字符
        filename = sonUrls[7:-6].replace('/', '-')
        filename += '.txt'

        fp = open(item['subFilename'] + '/' + filename, 'w')
        fp.write(item['content'])
        fp.close()

        return item
