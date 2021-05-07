# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class No11SunproPipeline:
    fp = None
    def open_spider(self, spider):
        self.fp = open('sun.txt','w')
    def process_item(self, item, spider):
        if item.__class__.__name__ =='No11SunproItem':
            self.fp.write(item['title']+'\n')
        else:
            self.fp.write(item['new_id']+item['content']+'\n')
        return item
    def close_spider(self, spider):
        self.fp.close()
