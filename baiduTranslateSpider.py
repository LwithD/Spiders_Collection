import requests
import json
import execjs
import re

# baseurl = r"https://fanyi.baidu.com/sug"
# baseurl = "https://fanyi.baidu.com/basetrans"
baseurl = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45",
    "cookie":"BAIDUID=8E852C33192F422CCA5FDE9BD97E6831:FG=1; __yjs_duid=1_e88d9b33050b623e41bbe851752bb2461614565407669; BDUSS=klmUlp0YWtnRlhhUW9DY2c1R0cxODZ2YmdydXVDVUd4d0c2SWZ1dG04ZFdiMjFnSVFBQUFBJCQAAAAAAAAAAAEAAADaiMkKYTkwNDkxOTg2MwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFbiRWBW4kVge; BDUSS_BFESS=klmUlp0YWtnRlhhUW9DY2c1R0cxODZ2YmdydXVDVUd4d0c2SWZ1dG04ZFdiMjFnSVFBQUFBJCQAAAAAAAAAAAEAAADaiMkKYTkwNDkxOTg2MwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFbiRWBW4kVge; BIDUPSID=8E852C33192F422CCA5FDE9BD97E6831; PSTM=1615279069; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=8E852C33192F422CCA5FDE9BD97E6831:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1615343243; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1615344585; ab_sr=1.0.0_ZjVlZmYyN2U5ZDEwMzI4MTYwZWIyMGNlMjdkMjAxMWQ0NjE3Y2EyODFhNjRlYmIzODcwNDdlMDQ0MDhjMzQ1M2VkYzk2MGIzNGQ3N2M5YmQ2ZGZjODUwNTk4OTExYWJh; __yjsv5_shitong=1.0_7_c325d0d023e64c3f9c780060ed9ecb51303c_300_1615344583743_112.17.238.250_8d0e5138"
}

ctx = 0

def get_Json():
    query = input("请输入需要翻译的词:\n")
    sign = ctx.call('e',query)
    # print(sign)
    param = {
        "from": 'en',
        'to': 'zh',
        'query':query,
        # 'kw':query,
        # 'transtype': 'realtime',
        # 'simple_means_flag': 3,
        # 'sign': '783622.988727',
        'sign': sign,
        'token': '2102d5d09008eeadcdcc418cbafda612'
        # 'domain': 'common'
    }
    response = requests.post(url = baseurl,headers = headers,data=param)
    Json = response.json()
    # print(json.detect_encoding())
    return json.dumps(Json,ensure_ascii=False)
    # return Json
    # js = response.text
    # with open('./json.js','w',encoding="utf-8") as f:
    #     f.write(js)

def get_sign():
    f = open("./baiduTranslateSignJson.js",'r')
    global ctx
    signJson = f.read()
    ctx = execjs.compile(signJson)
    f.close()
    
def get_translation(Json):
    j = re.findall(r'"dst": "(.+?)", "prefixWrap"',Json)
    # print(Json)
    print(j[0])

def main():
    get_sign()
    Json = get_Json()
    get_translation(Json)

    # print(ctx)

if __name__ == '__main__':
    main()