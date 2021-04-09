import re

s = '{"rownum":79,"storeName":"瞿溪新天地","addressDetail":"瞿溪街道河头村瞿溪新天地广场一层","pro":"Wi-Fi,店内参观","provinceName":"浙江省","cityName":"温州市"},{"rownum":80,"storeName":"瞿溪新天地","addressDetail":"瞿溪街道河头村瞿溪新天地广场一层","pro":"Wi-Fi,店内参观","provinceName":"浙江省","cityName":"温州市"}]}'
j = re.findall(r'"storeName":"(.+)","addressDetail"',s)
    # print(Json)
print(j[0])
# '[\u4e00-\u9fa5]+'