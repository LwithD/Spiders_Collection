import re

s = ' "dst":"这是一个触发器","prefixWrap":0,'
j = re.findall(r'"dst":"(.+?)", "prefixWrap"',s)
    # print(Json)
print(j[0])