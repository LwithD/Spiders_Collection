# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from time import sleep

class News163SpiderDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    #拦截五大板块相应对象，进行修改
    def process_response(self, request, response, spider):
        bro = spider.bro        #获取爬虫类中定义的浏览器对象

        #挑选出指定的响应对象进行篡改
        #通过url指定request
        #通过request指定response

        if request.url in spider.models_urls:
            #基于selenium获取动态加载的数据
            bro.get(request.url)
            sleep(5)
            page_text = bro.page_source #包含动态加载的数据
            # print(page_text)
            #实例化新的响应对象（包含动态加载）
            new_response = HtmlResponse(url = request.url,body=page_text,encoding='utf-8',request=request)
            return new_response
        else:
            return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
