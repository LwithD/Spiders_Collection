import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from No_11_sunPro.items import No11SunproItem,DetailItem

class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=2']

    #链接提取器：根据规则（allow="正则"）提取指定链接

    # def process(self,value):
    #     return 'wz.sun0769.com'+value

    link = LinkExtractor(allow=r'&page=\d+')
    # link_detail = LinkExtractor(restrict_xpaths='//ul[@class="title-state-ul"]/li/span[3]/a/@href',process_value=process)
    
    #/political/politics/index?id=500045
    #/political/politics/index?id=500042
    rules = (
        #规则解析器
        Rule(link, callback='parse_item', follow=False),
        # Rule(link_detail,callback='parse_detail'),#rocess_request='splash_request',
    )
    

    # def splash_request(self, request):
    #     request = request.replace(url='wz.sun0769.com' + request.url)
    #     print(request.url)
    #     return request

    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        # print(response)
        #xpath不可以出现tbody
        li_list = response.xpath('//ul[@class="title-state-ul"]/li')
        for li in li_list:
            new_num = li.xpath('./span[1]/text()').extract_first()
            new_title = li.xpath('./span[3]//text()').extract_first()
            item = No11SunproItem()
            item['title'] = new_title
            item['new_num'] = new_num

            yield item
            # url = li.xpath('./span[3]/a/@href').ex



        url_list = response.xpath('//ul[@class="title-state-ul"]/li/span[3]/a/@href').extract()
        for url in url_list:
            url  = "http://wz.sun0769.com"+url
            yield scrapy.Request(url,callback=self.parse_detail)

    def parse_detail(self,response):
        # print(response)
        new_id = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[4]/text()').extract_first()
        new_content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract_first()
        # new_content = ''.join(new_content)
        # print(new_id,new_content)
        item = DetailItem()
        item['new_id']= new_id
        item['content'] = new_content
        yield item