import requests

url = 'http://ip.293.net/'
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
}
proxy = {
    'http':'210.48.204.134:46669'
}
page_text = requests.get(url = url,headers=headers,proxies = proxy)

page_text.encoding = page_text.apparent_encoding

page_text = page_text.text

with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(page_text)