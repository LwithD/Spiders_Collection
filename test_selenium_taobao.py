from selenium import webdriver
from lxml import etree
#导入动作链
from selenium.webdriver import ActionChains
import time

wd = webdriver.Edge()
# wd.get("https://www.taobao.com")

# #标签定位
# search_input = wd.find_element_by_id('q')
# #标签交互
# search_input.send_keys('iphone')

# #execute js
# wd.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# time.sleep(2)

# #button交互
# btn = wd.find_element_by_class_name('btn-search')
# btn.click()

# wd.get('https://www.baidu.com')
# time.sleep(2)

# #回退
# wd.back()

# #前进
# wd.forward()

#iframe
wd.get('https://www.runoob.com/try/try.php?filename=jqueryui-example-droppable')
wd.switch_to.frame('iframeResult')  #iframe_id
div = wd.find_element_by_id('draggable')

#动作链
action = ActionChains(wd)
action.click_and_hold(div)

for i in range(5):
    #perform()立即执行
    action.move_by_offset(17,2).perform()
    time.sleep(0.3)

#release ActionChains
action.release()



time.sleep(5)
wd.quit()