import scrapy
from bossPro.items import BossproItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/c101210100-p100122/?page=1&ka=page-1']

    url = 'https://www.zhipin.com/c101210100-p100122/?page=1%d&ka=page-%d'
    page_num = 2
    def parse_detail(self,response):
        item = response.meta['item']
        
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]//text()').extract()
        job_desc = ''.join(job_desc)
        # print(job_desc)
        item['job_desc'] = job_desc
        
        yield  item



    # def parse(self, TextResponse):
    def parse(self, response):
        # print(TextResponse.text)
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        print(li_list)
        for li in li_list:
            item = BossproItem()
            primary_box = li.xpath('./div/div[1]/div[1]/div')
            job_name = primary_box.xpath('./div[1]/span[1]/a/text()').extract_first()
            item['jobname'] = job_name
            detail_url =  'https://www.zhipin.com/'+primary_box.xpath('./div[1]/span/a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 3:
            new_url = format(self.url%self.page_num)
            self.page_num += 1

            yield scrapy.Request(new_url,callback=self.parse)