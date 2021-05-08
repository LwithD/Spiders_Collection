-创建基于CrawlSpider的爬虫文件  
-修改当前的爬虫文件：  
&emsp;&emsp;-导包:from scrapy_redis.spiders import RedisCrawlSpider  
&emsp;&emsp;-将start_urls和allowed_domains进行注释  
&emsp;&emsp;-添加新属性：redis_key , 表示可以被共享的调度器队列的名称  
&emsp;&emsp;-编写数据解析相关的操作  
&emsp;&emsp;-将当前爬虫类的父类修改成RedisCrawlSpider  
-修改settings  
&emsp;&emsp;-指定使用可共享的管道  
&emsp;&emsp;-指定redis服务器  
-redis相关操作配置：  
&emsp;&emsp;-配置redis的配置文件  
&emsp;&emsp;&emsp;&emsp;-bind 127.0.0.1注释掉    
&emsp;&emsp;&emsp;&emsp;-关闭保护模式:protect-mode no  
&emsp;&emsp;-开启redis服务:redis-server xxx\redis.windows.conf  
&emsp;&emsp;-启动客户端:redis-cli  
-执行工程：  
&emsp;&emsp;-scrapy runspider xxx.py(spider文件夹中运行)  
-向调度器的队列中放入起始的url：  
&emsp;&emsp;-lpush xxx www.xxx.com  
-爬取到的数据存储在redis的proName:items这个数据结构中

  
### 制式代码
#增加了一个去重容器类的配置，使用Redis的set集合来存储请求的指纹数据，从而实现请求去重的持久化  
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  
#使用scrapy-redis组建自己的调度器  
SCHEDULER = "scrapy_redis.scheduler.Scheduler"  
#配置调度器是否持久化（即爬虫结束后是否清空请求队列和set缓存  
SCHEDULER_PERSIST = True

