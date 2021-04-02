import requests
import re,json

baseurl = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"

params = {
    'cname': '温州',
    'pageIndex': 1,
    'pageSize': 80
}

header = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
}

def main():
    response = requests.post(url = baseurl, data=params, headers=header)
    data = response.text
    j = re.findall('"storeName":"([\u4e00-\u9fa5]+)","addressDetail"',data)
    for i in j:
        print(i)
    # print(j)
if __name__ == '__main__':
    main()