from scrapy.item import Item, Field

class GuardianNews(Item):
    """News container (dictionary like object) scraped data"""

    date = Field()
    author = Field()
    title = Field()
    content = Field()
    url = Field()
