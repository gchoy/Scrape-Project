import scrapy



class GuardianNews(scrapy.Spider):
    name = "theguardian"
    allowed_domains = ["theguardian.com"]
    start_urls = [
      "http://www.theguardian.com/environment/2016/may/11/canada-wildfire-environmental-impacts-fort-mcmurray"
    ]

    def parse(self, response):
        """Extracts data from the theguardian website"""
        date = response.xpath(".//*[@id='article']/div[2]/div/div[1]/div[2]/p[2]/time[1]/text()").extract()
        author = response.xpath(".//*[@id='article']/div[2]/div/div[1]/div[2]/p[1]/span/a/span/text()").extract()
        title = response.xpath(".//*[@id='article']/header/div[1]/div/div/h1/text()").extract()
        content = response.xpath(".//*[@id='article']/div[2]/div/div[1]/div[3]/p/text() |//*[@id='article']/div[2]/div/div[1]/div[3]/h2/text()").extract()
        #url = article['url']
        print date, author,title,content


