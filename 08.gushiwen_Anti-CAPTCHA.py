import requests
from lxml import etree
from PIL import Image
import json
import base64
import urllib.parse

#baidu-ai
APP_ID = '23974174'
API_KEY ='iHYt2Bymf10vYZ4rHHkFljmh'
SECRECT_KEY = 'fEzEZTgzviQj7HMlknIK59OGFkFSqMZf'
body = {'grant_type': 'client_credentials',
        'client_id': API_KEY,
        'client_secret': SECRECT_KEY
}
host = 'https://aip.baidubce.com/oauth/2.0/token'

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }

def get_img(url,header):
    page_text = requests.get(url,headers = header).text
    tree = etree.HTML(page_text)
    img_src = 'https://so.gushiwen.cn/'+tree.xpath('//*[@id="imgCode"]/@src')[0]
    img_data = requests.get(img_src,headers=headers).content
    with open('./08.CAPTCHA.jpg','wb') as fp:
        fp.write(img_data)

def get_codeText():
    image = Image.open('08.CAPTCHA.jpg')
    image = binarizing(image)
    image = Noise_reduction(image)
    image.save('./08.CAPTCHA.jpg')
    text = ocr()

#二值化
def binarizing(img,threshold=127):
    img = img.convert("L")
    pixdata = img.load()
    w,h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x,y] <threshold:
                pixdata[x,y] = 0
            else:
                pixdata[x,y] = 255
    return img

#降噪
def Noise_reduction(img):
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count >= 4:
                pixdata[x,y] = 255
    return img


def get_token():
    req = requests.post(url=host, data=body)
    token = json.loads(req.content)['access_token']
    return token

#识别
def ocr():
    token = get_token()
    ocr_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=%s'%token
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    body = base64.b64encode(open('./08.CAPTCHA.jpg' ,'rb').read())
    
    # 进行urlencode
    data = urllib.parse.urlencode({'image': body})

    # post请求
    r = requests.post(url=ocr_url, headers=headers, data=data)

    # 输出请求结果
    print('请求码为: %s' %r.status_code)
    res_words = json.loads(r.content)['words_result'][0]['words']
    print('识别结果为: %s' %res_words) 



if __name__ == '__main__':
    get_img(url,headers)
    get_codeText()
