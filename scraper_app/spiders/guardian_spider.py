from scrapy.spider import BaseSpider
from scraper_app.items import GuardianNews


class GuardianSpider(BaseSpider):
   '''Spider for scraping theguardian.com site'''
   name = 'theguardian'
   allowed_domains = ['theguardian.com']
   start_urls = ['http://www.theguardian.com/environment/2016/may/11/canada-wildfire-environmental-impacts-fort-mcmurray']
   
   
   def parse(self, response):
        #for sel in response.xpath('//*'):
        date = response. xpath(".//*[@id='article']/div[2]/div/div[1]/div[2]/p[2]/time[1]").extract()
        author = response.xpath(".//*[@id='article']/div[2]/div/div[1]/div[2]/p[1]/span/a/span").extract()
        title = response.xpath(".//*[@id='article']/header/div[1]/div/div/h1").extract()
        content = response.xpath(".//*[@id='article']/div[2]/div/div[1]/div[3]").extract()
        url = response.xpath(".//*[@id='article']/html/body/div[6]/article/meta").extract()
        print date, author,title,url

