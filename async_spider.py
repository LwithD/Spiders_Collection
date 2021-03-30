import asyncio
import aiohttp
import multyThreadTest
import time

sem = asyncio.Semaphore(10)

#定义协程
async def async_craw(url):
    print("craw url: ",url)
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                result = await resp.text()
                print(f"craw url: {url},{len(result)}")

#获取至尊循环
loop = asyncio.get_event_loop()


#创建task列表
tasks = [
    loop.create_task(async_craw(url))
    for url in multyThreadTest.urls]


start = time.time()
#执行爬虫事件列表
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print("use time= ",end-start,"seconds")
