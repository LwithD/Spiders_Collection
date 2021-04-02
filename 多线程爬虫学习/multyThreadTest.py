import time
import threading
import requests
from bs4 import BeautifulSoup

urls = [
    f"http://www.cnblogs.com/#p{page}"
    for page in range(1,50+1)
]

def craw(url):
    html = requests.get(url)
    return html.text

def single_process_spider(urls):
    for url in urls:
        craw(url)
        

def multy_process_spider(urls):
    threads = []
    for url in urls:
        th = threading.Thread(target=craw,args=(url,)) 
        threads.append(th)
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def parse(html):
    #class="post-item-title"
    soup  = BeautifulSoup(html,"html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]

def main():
    print("single process start")
    start = time.time()
    single_process_spider(urls)
    end = time.time()
    print("single process end, time = ", end-start," seconds")

    print("multy process start")
    start = time.time()
    multy_process_spider(urls)
    end = time.time()
    print("multy process end, time = ", end-start," seconds")


if __name__ == '__main__':
    main()
