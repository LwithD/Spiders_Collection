import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']


    #数据解析操作
    def parse(self, response):
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in div_list:
            #extract()方法提取selector对象的数据
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            content = div.xpath('./a[1]/div/span[1]//text()').extract()
            content = ''.join(content)

            print(author,content)
            
            break
