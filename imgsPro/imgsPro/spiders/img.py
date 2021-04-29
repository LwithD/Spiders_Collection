import scrapy
from imgsPro.items import ImgsproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            #src2伪属性
            src = div.xpath('./div/a/img/@src2').extract_first().split('_')[0]
            src = 'https:'+ src + '.jpg'
            print(src)
            item = ImgsproItem()
            item['src'] = src

            yield item
