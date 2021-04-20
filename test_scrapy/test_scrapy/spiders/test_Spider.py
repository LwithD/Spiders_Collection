import scrapy


class TestSpiderSpider(scrapy.Spider):
    name = 'test_Spider'
    #允许的域名：限定start_urls列表中哪些url可以进行请求发送
    # allowed_domains = ['www.baidu.com']
    #起始url列表,列表中的urlscrapy会自动进行请求的发送
    start_urls = ['http://www.baidu.com/']

    #数据解析:respose表示请求成功后的响应对象
    def parse(self, response):
        print(response)
