import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
