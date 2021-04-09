import requests
from lxml import etree

if __name__ == '__main__':
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse('./sogouHtml/dnf.html',parser=parser)
    # r = tree.xpath('/html/head/title') #/从根节点开始定位
    # r = tree.xpath('/html/body/div')
    # r = tree.xpath('//div')   #//表示多层，可以从任意位置定位
    # r = tree.xpath('//div[@class="multiple-words-text"]') #属性定位
    # r = tree.xpath('//div[@class="multiple-words-text"]/p[1]')  #索引从1开始，非0 
    # r = tree.xpath('//div[@class="multiple-words-text"]/p/text()') #获取文本
    # r = tree.xpath('//div[@class="multiple-words-text"]//text()')
    r = tree.xpath('//div//a/@title')  #/@attrName
    print(r)