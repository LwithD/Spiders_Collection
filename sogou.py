#UA伪装

import requests
if __name__ == '__main__':
    url = 'https://www.sogou.com/web'
    header = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
    }
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    response = requests.get(url = url,params = param,headers= header)
    
    page_text = response.text

    fileName = r'.\sogouHtml\\'+kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功')
