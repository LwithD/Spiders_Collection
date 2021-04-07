import requests
import json,re


url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do"
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }

def get_ID(url):
    id_list = []
    for i in range(10):
        params = {
            "method" : 'getXkzsList',
            'page' : f'{i+1}',
            'pageSize' : '15'
        }
        json = requests.post(url, data=params, headers=headers).json()
        for dic in json['list']:
            id_list.append(dic['ID'])
        print(f"第{i+1}页ID爬取完成")
    return id_list

def get_data(id_list):
    dataurl = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do'
    with open("04.NMPA_Spider_Result.js", "w+") as f:
        for id in id_list:
            params = {
            "method" : 'getXkzsById',
            'id' : id
            }
            data_json = json.dumps(requests.post(dataurl,data=params,headers=headers).json())+'\n'
            f.write(data_json)
    print("数据存储完成")


def main():
    id_list = get_ID(url)
    # print(id_list)
    get_data(id_list)

if __name__ == '__main__':
    main()