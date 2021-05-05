from time import sleep
from msedge.selenium_tools import Edge, EdgeOptions

#edge无头浏览器   phantomJs可用，已停止更新
options = EdgeOptions()
options.use_chromium = True
options.add_argument("headless")
options.add_argument("disable-gpu")
#防止打印无用信息   enable-automation规避检测 #最新版浏览器已无用
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])


#谷歌无头  #谷歌88.0版本可用
# from selenium.webdriver import Chrome
# from selenium.webdriver import ChromeOptions
# options = ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# options.add_experimental_option("excludeSwitches", ["enable-automation",'enable-logging'])
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_experimental_option('useAutomationExtension', False)
# wd = Chrome(options=options)

wd = Edge(options = options)
wd.get('https://www.baidu.com')

print(wd.page_source)
sleep(2)
wd.quit()