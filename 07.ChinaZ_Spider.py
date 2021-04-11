import requests
from lxml import etree
import os

if __name__ == "__main__":
    if not os.path.exists('./07.ChinaZ_Jianli'):
        os.mkdir('./07.ChinaZ_Jianli')
    baseurl = "https://sc.chinaz.com/jianli/free"
    headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }
    # parser = etree.HTMLParser(encoding=etree.apparent_encoding)
    for i in range(2,15):
        url = baseurl+f"_{i}.html"
        response = requests.get(url,headers = headers)
        response.encoding = response.apparent_encoding   #解决编码问题
        tree = etree.HTML(response.text)
        p_list = tree.xpath('//div[@id="main"]//p')
        for p in p_list:
            resume_name = p.xpath('./a/text()')[0]
            if '互联网' in resume_name or '程序' in resume_name or '应届生' in resume_name:
                resume_url = 'https:'+p.xpath('./a/@href')[0]
                text2 = requests.get(resume_url,headers=headers).text
                tree2 = etree.HTML(text2)
                download_url = tree2.xpath('//ul[@class="clearfix"]/li/a/@href')[0]
                with open(f'./07.ChinaZ_Jianli/{resume_name}.rar','wb') as fp:
                    fp.write(requests.get(download_url,headers=headers).content)
        print("第",i,"页爬取完毕")
        # print(name_list)
    #     content = requests.get(baseurl,headers=headers).content
    