# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy

# class ImgsproPipeline:
#     def process_item(self, item, spider):
#         return item

class ImgsproPipeline(ImagesPipeline):

    #根据图片地址进行图片数据的请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src'])
        # return super().get_media_requests(item, info)

    def file_path(self, request, response=None, info=None):
        imgName = request.url.split('/')[-1]
        return imgName
        # return super().file_path(request, response=response, info=info, *, item=item)

    def item_completed(self, results, item, info):
        return item
        #返回给下一个管道类
        # return super().item_completed(results, item, info)