from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#设置chromeoption
options = ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
options.add_experimental_option("excludeSwitches", ["enable-automation",'enable-logging'])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option('useAutomationExtension', False)



#get直接返回，不再等待界面加载完成
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"

#创建webdriver
wd = Chrome(options=options)

# wd.implicitly_wait(10)
wd.set_page_load_timeout(3)
wd.set_script_timeout(3)

try:
    wd.get('https://vip.anjuke.com/portal/login/')
except:
    wd.find_element_by_xpath('//*[@id="login-mod-container"]/div/div[1]/ul/li[1]').click()
    wd.find_element_by_xpath('//*[@id="loginAccount"]').send_keys('17826738050')
    wd.find_element_by_xpath('//*[@id="loginPwd"]').send_keys('Aa6277741230')
    wd.find_element_by_xpath('//*[@id="loginSubmit"]').click()
    sleep(2)
    cookie = wd.get_cookies()
    print(cookie)
    wd.get('https://vip.anjuke.com/logout/')
    sleep(3)


    # wd.find_element_by_xpath('//*[@id="login-mod-container"]/div/div[1]/ul/li[1]').click()
    # wd.find_element_by_xpath('//*[@id="loginAccount"]').send_keys('awdubnaiwu')
    # wd.find_element_by_xpath('//*[@id="loginPwd"]').send_keys('asoinoncz')
    # wd.find_element_by_xpath('//*[@id="loginSubmit"]').click()
    # sleep(2)
    # for i in range(15):
    #     wd.find_element_by_xpath('//*[@id="loginAccount"]').send_keys('awdubnaiwu')
    #     wd.find_element_by_xpath('//*[@id="loginPwd"]').send_keys('asoinoncz')
    #     wd.find_element_by_xpath('//*[@id="loginSubmit"]').click()
    #     sleep(2)