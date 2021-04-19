from selenium import webdriver
from lxml import etree
import time
bro = webdriver.Edge()
bro.get('http://scxk.nmpa.gov.cn:81/xk/')

page_text = bro.page_source
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    print(li.xpath('./dl/a/text()')[0])
time.sleep(5)
bro.quit()