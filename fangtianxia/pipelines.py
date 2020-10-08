# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import pymongo
import codecs
import csv


class FangtianxiaPipeline(object):
    def process_item(self, item, spider):
        return item


# 保存到CSV文件中
class CsvPipeline(object):

    def __init__(self):
        self.file = codecs.open('data.csv', 'w', encoding='utf_8_sig')

    def process_item(self, item, spider):
        fieldnames = ['_id', 'province', 'city', 'name', 'price', 'house_type',
                      'area', 'address', 'district', 'sale', 'origin_url', 'jzmj', 'lpyh', 'kpsj', 'xszt', 'jfsj',
                      'xmts', 'zxdh', 'tcw', 'ldzs', 'rjl', 'zxzk', 'lczk', 'wylb', 'hxwz', 'zdmj', 'jzlb', 'cqnx',
                      'zlhx', 'ysxkz', 'wyf', 'kfs', 'wygs', 'wyfms', 'lhl', 'zhs']
        w = csv.DictWriter(self.file, fieldnames=fieldnames, quotechar='"', quoting=csv.QUOTE_ALL)
        # w.writeheader()
        w.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()


'''
class MongoPipeline(object):
    """MongoDB管道"""
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item.__class__.__name__
        data = dict(item)
        self.db[name].update_one({"_id": data['_id']}, {"$set": data}, upsert=True)
        return item

    def close_spider(self, spider):
        self.client.close()

'''
