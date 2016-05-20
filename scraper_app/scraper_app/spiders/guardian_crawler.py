# -*- coding: utf-8 -*-
#guardian_crawler.py crawls and scrapes information from
#theguardian.com following rules and start page specified 
#in rules list and star_urls respectively.

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scraper_app.items import ScraperAppItem


class GuardianCrawlerSpider(CrawlSpider):
    name = "guardian_crawler"
    allowed_domains = ["theguardian.com"]
    start_urls = ["http://www.theguardian.com/environment"]

    rules = [
        Rule(LinkExtractor(), callback="parse_item", follow=True)
        
   ]

    def parse_item(self, response):
        """Scrapes information from pages of theguardian.com website"""
        
        for sel1 in response.xpath(".//*[@id='article']"):
       
            item = ScraperAppItem()
            item["date"] = map(unicode.strip, sel1.xpath("////p[2]/time[1]/text()").extract())
            item["author"] = map(unicode.strip, sel1.xpath("////p[1]/span/a/span/text()").extract())
            item["title"] = map(unicode.strip, sel1.xpath("header/div[1]/div/div/h1/text()").extract())
            item["content"] = map(unicode.strip, sel1.xpath("////p/text() | ////h2/text()").extract())
            item["url"] = map(unicode.strip, response.xpath("/html/head/link[26]/@href").extract())

            
            yield item
