import requests
from lxml import etree


if __name__ == "__main__":
    baseurl = "https://hz.58.com/ershoufang/"
    headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }
    page_text = requests.get(baseurl,headers=headers).text
    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.HTML(page_text,parser=parser)
    title_list = tree.xpath('//div[@class="property"]//h3[@class="property-content-title-name"]/text()')
    with open('06._58ershou.txt','w') as fp:
        for title in title_list:
            fp.write(title+"\n")