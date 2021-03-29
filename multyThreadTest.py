import time
import threading
import requests

urls = [
    f"http://www.cnblogs.com/#p{page}"
    for page in range(1,50+1)
]

def craw(url):
    html = requests.get(url)
    print(url,len(html.text))

def main():
    print("single process start")
    start = time.time()
    for url in urls:
        craw(url)
    end = time.time()
    print("single process end, time = ", end-start," seconds")

    print("multy process start")
    start = time.time()
    threads = []
    for url in urls:
        th = threading.Thread(target=craw,args=(url,)) 
        threads.append(th)
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    end = time.time()
    print("multy process end, time = ", end-start," seconds")


if __name__ == '__main__':
    main()
