import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']


    #终端指令存储
    # def parse(self, response):
    #     div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
    #     all_data = []
    #     for div in div_list:
    #         #extract()方法提取selector对象的数据
    #         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         content = div.xpath('./a[1]/div/span[1]//text()').extract()
    #         content = ''.join(content)

    #         dic = {
    #             'author' : author,
    #             'content' : content
    #         }

    #         all_data.append(dic)

    #         # print(author,content)
    #     return all_data

    #基于管道存储
    def parse(self, response):
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        all_data = []
        for div in div_list:
            #extract()方法提取selector对象的数据
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            content = div.xpath('./a[1]/div/span[1]//text()').extract()
            content = ''.join(content)
            item = QiubaiproItem()
            #item.Field()方法基本上继承了字典，所以用字典的访问方式
            item['author'] = author
            item['content'] = content

            yield item