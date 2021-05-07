### CrawlSpider: Spider的一个子类

-全站数据爬取<br>
&emsp;-基于Spider：手动请求<br>
&emsp;-基于CrawlSpider<br>

-CrawlSpider的使用：<br>
&emsp;-创建工程<br>
&emsp;-cd XXX<br>
&emsp;-创建爬虫文件（CrawlSpider）：  
&emsp;&emsp;-scrapy genspider -t crawl xxx www.xxx.com  
&emsp;&emsp;-链接提取器：  
&emsp;&emsp;&emsp;&emsp;-作用：根据指定规则（allow)进行链接提取  
&emsp;&emsp;-规则解析器：  
&emsp;&emsp;&emsp;&emsp;-将链接提取器提取到的链接进行指定规则（callback）的解析
