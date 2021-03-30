import multyThreadTest
import concurrent.futures

#craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(multyThreadTest.craw, multyThreadTest.urls)
    htmls = list(zip(multyThreadTest.urls,htmls))
    for url,html in htmls:
        print(url,len(html))

print("craw over")

#parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url,html in htmls:
        future = pool.submit(multyThreadTest.parse, html)
        futures[future] = url
        
    # for future,url in futures.items():
    #     print(url, future.result())

    #as_completed 不按顺序，任务执行完成即打印结果
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, future.result())