# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QiubaiproPipeline:
    fp = None
    #覆写父类的方法:该方法只在开始爬虫的时候被调用一次
    def open_spider(self,spider):
        print('开始爬虫......')
        self.fp = open('./qiubai.txt','w',encoding='utf-8')

    #用来接受和处理item类型对象
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        
        self.fp.write(author+":"+content+"\n")

        return item

    #爬虫结束时调用：只被调用一次
    def close_spider(self,spider):
        print('结束爬虫！')
        self.fp.close()