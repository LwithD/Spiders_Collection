import requests
import re
import os

baseurl = "https://www.qiushibaike.com/imgrank/page/"
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }

def get_url(num):
    url_list = []
    for i in range(num):
        url = baseurl+str(i+1)
        response = requests.get(url,headers=headers).text
        # print(response)
        ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
        img_src_list = re.findall(ex,response,re.S)
        for src in img_src_list:
            img_url = "https:"+src
            url_list.append(img_url)
    # print(url_list)
    return url_list
def get_image(url_list):
    #content：返回二进制数据
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    for url in url_list:
        img_data = requests.get(url=url, headers=headers).content
        name = re.findall('/medium/(.+).jpg',url)[0]
        with open(f'./qiutuLibs/{name}.jpg','wb') as fp:
            fp.write(img_data)

def main():
    num = int(input("请输入爬取的页数:\n"))
    url_list = get_url(num)
    get_image(url_list)
if __name__ == '__main__':
    main()