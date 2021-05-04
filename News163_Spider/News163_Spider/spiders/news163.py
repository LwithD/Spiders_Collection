import scrapy
from msedge.selenium_tools import Edge,EdgeOptions
from News163_Spider.items import News163SpiderItem

class News163Spider(scrapy.Spider):
    name = 'news163'
    # allowed_domains = ['news.163.com']
    start_urls = ['http://news.163.com/']
    models_urls = []

    
    def __init__(self):
        options = EdgeOptions()
        options.use_chromium = True
        # options.add_argument("headless")
        # options.add_argument("disable-gpu")
        #防止打印无用信息   enable-automation规避检测
        options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        self.bro = Edge(options = options)


    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [3,4,6,7]
        for index in alist:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)
        for url in self.models_urls:
            yield scrapy.Request(url,callback=self.parse_model)

    def parse_model(self,response):
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:        
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            news_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            item = News163SpiderItem()
            item['title'] = title
            #新闻详情页请求
            yield scrapy.Request(url = news_detail_url,callback=self.parse_detail,meta={'item':item})

    def parse_detail(self,response):
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content)
        item = response.meta['item']
        print(item)
        item['content'] = content
        yield item


    def closed(self,spider):
        self.bro.quit()