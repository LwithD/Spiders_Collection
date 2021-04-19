import scrapy


class TestSpiderSpider(scrapy.Spider):
    name = 'test_Spider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
