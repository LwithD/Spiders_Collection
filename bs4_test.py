from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.baidu.com').text

soup = BeautifulSoup(html,'lxml')

a = soup.find('img',hidefocus='true')

print(a)