# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperAppItem(scrapy.Item):
       
     """Dictionary like object that holds scraped data"""

     date = scrapy.Field()
     author = scrapy.Field()
     title = scrapy.Field()
     content = scrapy.Field()
     url = scrapy.Field()
