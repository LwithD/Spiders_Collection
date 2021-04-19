import time
from msedge.selenium_tools import Edge, EdgeOptions
from PIL import Image
from selenium.webdriver import ActionChains


options = EdgeOptions()
# options.add_argument("headless")
# options.add_argument("disable-gpu")
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
# options.add_argument('-kiosk') #全屏打开

wd = Edge(options = options)
wd.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(1)
#全屏
wd.maximize_window()

#点击账户登录
wd.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()

time.sleep(1)
#screenshot
wd.save_screenshot('./10.screenshot.png')

code_img_ele = wd.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[4]/img')

#裁剪截图
location = code_img_ele.location
print('location:' ,location)
size = code_img_ele.size
print('size:',size)
rangle = (
    location['x'],location['y'],location['x']+size['width'],location['y']+size['height'])
i = Image.open('./10.screenshot.png')
code_img_name = './10.CAPTCHA.png'
#crop根据指定区域进行裁剪
frame = i.crop(rangle)
frame.save(code_img_name)

#使用打码平台识别验证码图片获得坐标（略）
example_location = '253,83|253,153' #示例坐标


#滑动点击
all_list = [] #存储坐标
if '|' in example_location:
    list_1 = example_location.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(example_location.split(',')[0])
    y = int(example_location.split(',')[1])
    all_list.append([x,y])

for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(wd).move_to_element_with_offset(code_img_ele,x,y).click().perform()
    time.sleep(1)

#输入账号密码
wd.find_element_by_xpath('//*[@id="J-userName"]').send_keys('xxxxxx')
time.sleep(2)
wd.find_element_by_xpath('//*[@id="J-password"]').send_keys('xxxxxx')
time.sleep(2)
# wd.find_element_by_xpath('//*[@id="J-login"]').click()
time.sleep(10)
wd.quit()