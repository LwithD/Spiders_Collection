from bs4 import BeautifulSoup
import requests

html = requests.get('https://book.qidian.com/info/1025649259#Catalog').text

soup = BeautifulSoup(html,'lxml')

a = soup.find('ul',class_='cf')

for l in a.find_all('li'):
    print(l.text)

# print(a)

#soup.find_all()
#soup.find('div',class_/id/attr='song')
#soup.select('.tang > ul > li > a')  >表示单个层级
#soup.select('.tang > ul a') 空格表示多个层级
#soup.a.text/string/get_text()   #string获取直系子标签的文本，其他获取所有子标签的文本