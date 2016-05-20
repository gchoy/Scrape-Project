# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#pipelines.py connects with the MonogoDB database in compose.io
#and inserts the data once it's collected.
#MONGODB_URI, MONGODB_DB and MONGODB_COLLECTION were defined in the settings file.

import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem


class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings["MONGODB_URI"]
            
        )
        db = connection[settings["MONGODB_DB"]]
        self.collection = db[settings["MONGODB_COLLECTION"]]

    def process_item(self, item, spider):
        """Inserts the scraped data into the data base"""

        self.collection.insert(dict(item))
        return item
