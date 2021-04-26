# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

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

        #传递给下一个优先级低的管道类
        return item

    #爬虫结束时调用：只被调用一次
    def close_spider(self,spider):
        print('结束爬虫！')
        self.fp.close()


#管道文件中的一个管道类对应一组数据存储到一个载体
class mysqlPileLine:
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password = 'password',db ='qiubai')
    
    def process_item(self,item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(f'insert into qiutubaike values("{item["author"]}","{item["content"]}")')
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            self.conn.commit()

        return item
    
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()