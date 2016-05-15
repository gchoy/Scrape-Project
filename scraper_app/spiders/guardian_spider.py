import scrapy
from scraper_app.items import GuardianNews


class DmozSpider(scrapy.Spider):
    name = "theguardian"
    allowed_domains = ["theguardian.com"]
    start_urls = [
      "http://www.theguardian.com/environment/2016/may/11/canada-wildfire-environmental-impacts-fort-mcmurray",
      "http://www.theguardian.com/environment/2016/may/14/scientists-people-power-find-disease-ash-resistant-trees"
    ]

    def parse(self, response):
        """Extracts data from the theguardian website"""
        
        item = GuardianNews()
        for sel1 in response.xpath(".//*[@id='article']"):

            item['date'] = sel1.xpath("////p[2]/time[1]/text()").extract()
            item['author'] = sel1.xpath("////p[1]/span/a/span/text()").extract()
            item['title'] = sel1.xpath("header/div[1]/div/div/h1/text()").extract()
            item['content'] = sel1.xpath('////p/text() | ////h2/text()').extract()

        for sel2 in response.xpath('//html'):

            item['url'] = sel2.xpath(".//link[18]/@href").extract()
            yield item

