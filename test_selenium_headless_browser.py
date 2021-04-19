from time import sleep
from msedge.selenium_tools import Edge, EdgeOptions

#edge无头浏览器   phantomJs可用，已停止更新
options = EdgeOptions()
options.use_chromium = True
options.add_argument("headless")
options.add_argument("disable-gpu")
#防止打印无用信息   enable-automation规避检测
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])


#谷歌无头
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# webdriver1 = webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options)

wd = Edge(options = options)
wd.get('https://www.baidu.com')

print(wd.page_source)
sleep(2)
wd.quit()