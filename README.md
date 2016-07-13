##Scrape-Project
####Creating a news site web crawler that stores content on MONGODB

The scraper was built using the scrapy framework and consists of two different spiders (which must run independently):

- ```guardian_spider.py```: which scrapes data of specific websites placed in the start_url's list.
- ```guardian_crawler.py```: which starts crawling from link to link throughout a website. Starting at the page indicated in the start_url list.

When running, these spiders are aided by:

- ```pipelines.py```: which connects to the database and inserts the scraped information.
- ```settings.py```: which contains working parameters (i.e. download delay) for the spiders and database specifications.


The results are available through the testapi.py file ,which is in the news_api folder. This API runs in the command line
by running: ```python testapi.py``` . And is searchable by keyword, if the keyword matches the title, the content, or author, a record will be included in the results. A short video of the API in use can be seen here: [youtube] (https://www.youtube.com/watch?v=93mL9nE66tc )


It is not necessary to run the spiders before the API, as there is some data already available in the database.
However, before running the API the following modules must be installed:

- ```sudo pip install pymongo```
- ```sudo pip install bottle```


Then place the spider, the crawler, the settings and the pipelines and items files in the corresponding folders in the project tree. 
To run the spider or the crawler go to the first scraper_app folder (the folder before the one that has the helper files) and enter in the command line:

- For the spider: ```scrapy crawl theguardian```
- For the crawler: ```scrapy crawl guardian_crawler```
 
 
 

 
