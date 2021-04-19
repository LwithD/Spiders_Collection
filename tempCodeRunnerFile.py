_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[4]/img')

# #裁剪截图
# location = code_img_ele.location
# print('location:' ,location)
# size = code_img_ele.size
# print('size:',size)
# rangle = (
#     location['x'],location['y'],location['x']+size['width'],location['y']+size['height'])
# i = Image.open('./10.screenshot.png')
# code_img_name = './10.CAPTCHA.png'
# #crop根据指定区域进行裁剪
# frame = i.crop(rangle)
# frame.save(code_img_name)