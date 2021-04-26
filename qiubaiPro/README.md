### 基于终端指令：

scrapy crawl xxx -o filePath<br>

只可以为：'json','jsonline','jl','csv','xml'<br>

### 基于管道：
-数据解析<br>
-item类中定义相关属性<br>
-解析的数据封装到item类型的对象中<br>
-将item类中的对象提交到管道进行持久化存储的操作<br>
-在管道类的process_item中将接受的item对象中的数据进行持久化存储<br>
-在配置文件中开启管道


# 将爬取到的数据一份存储到本地一份存储到数据库  
-管道文件中的一个管道类对应的是将数据存储到一种载体<br>
-爬虫文件提交的item只会给管道类的第一个执行<br>
-process_item中的return item表示将item传递给下一个即将被执行的管道