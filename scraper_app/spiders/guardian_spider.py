from scrapy.spider import BaseSpider
from scraper_app.items import GuardianNews
from readability import ParserClient


class GuardianSpider(BaseSpider):
   '''Spider for scraping theguardian.com site'''
   name = 'theguardian'
   allowed_domains = ['theguardian.com']
   start_urls = ['http://www.theguardian.com/environment/2016/may/11/canada-wildfire-environmental-impacts-fort-mcmurray']
   
   content_list_xpath='//*[@id="article"]'
   item_fields = {
       'articletext' = './/p | .//h2'
   } 
   parser_response = parser_client.get_article('http://www.theguardian.com/environment/2016/may/11/canada-wildfire-environmental-impacts-fort-mcmurray')
   news_items = parser_response.json()
   item_fields['date'] = news_items['date_published']
   item_fields['author'] = news_items['author']
   item_fields['title'] = news_items['title']
   item_fields['url'] = news_items['url']
