# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import re
from scrapy.exceptions import DropItem
from w3lib.html import remove_tags


class ScrapyTemplePipeline(object):

    # 移除标签和空格等字符
    def del_special_char(self, target_str, tags=True, rnts=True):
        if isinstance(target_str, str):
            result = remove_tags(target_str)
            if rnts:
                result_1 = re.subn("[\r\n\t\s]", "", result)
                return result_1[0]
            else:
                return result
        else:
            return target_str


    def process_item(self, item, spider):

        return item


class SaveData(object):

    def __init__(self, mongodb_uri, mongodb_db):
        self.mongodb_uri = mongodb_uri
        self.mongodb_db = mongodb_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_uri=crawler.settings.get('MONGODB_URL'),
            mongodb_db=crawler.settings.get('MONGODB_DB')
        )

    def open_spider(self, spider):
        self.collection_name = spider.mongodb_db_name
        spider.client = pymongo.MongoClient(self.mongodb_uri)
        spider.db = spider.client[self.mongodb_db]
        spider.collection = spider.db[self.collection_name]

    def process_item(self, item, spider):
        dict_data = dict(item)
        try:
            spider.collection.insert_one(dict_data)
            spider.logger.info(dict_data['name'] + 'is ok')
        except Exception as e:
            spider.logger.worning('mongodb_db save exception !!!')
            raise DropItem
        else:
            return item

    def close_spider(self, spider):
        spider.client.close()
