# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class DuplicatesPipeline(object):
    """
    去重
    """

    def __init__(self):
        self.name_set = set()

    def process_item(self, item, spider):
        name = item['name']

        if name in self.name_set:
            raise DropItem("Duplicate name found:%s" % item)

        self.name_set.add(name)
        return item
